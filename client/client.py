import asyncio
import struct

from CommonClient import logger, server_loop
from CommonClient import CommonContext as SuperContext

from NetUtils import ClientStatus
from .memory import EDF5Memory
from .offsets import *

LOCATION_NAME_TO_ID = {}

idCounter = 1
classes = ["Ranger", "Wing Diver", "Air Raider", "Fencer"]
difficulties = ["Easy", "Normal", "Hard", "Hardest", "Inferno"]

# Generate the ids for all missions and difficulties.
for mission in range(1, 111):
    # Location for clearing the mission on any difficulty and any class
    LOCATION_NAME_TO_ID[f"Mission {mission} - Cleared"] = idCounter
    idCounter += 1
    for playerClass in classes:
        
        # Location for clearing the mission on a specific difficulty and specific class
        for difficulty in difficulties:            
            name = (f"Mission {mission} - {difficulty} ({playerClass})") 
            LOCATION_NAME_TO_ID[name] = idCounter
            idCounter += 1

class EDF5Context(SuperContext):
    game = "Earth Defense Force 5"
    items_handling = 0b111
    
    def __init__(self, server_address = None, password = None):
        super().__init__(server_address, password)
        
        self.slot_data = {}
        self.ap_connected = False        
    
    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            self.slot_data = args.get("slot_data", {})
            self.ap_connected = True

        super().on_package(cmd, args)        
        
    def make_gui(self):
        from kvui import GameManager
        
        class EDF5Manager(GameManager):
            base_title = "Earth Defense Force 5 Client"
            
        return EDF5Manager
        
    async def disconnect(self, allow_autoreconnect: bool = False):
        self.ap_connected = False
        await super().disconnect(allow_autoreconnect)
       
    async def server_auth(self, password_requested=False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
            
        if not self.auth:
            await self.get_username()

        await self.send_connect(
            game=self.game,
            name=self.auth,
            password=self.password
            )

async def main(args):
    ctx = EDF5Context(
        args.connect,
        args.password
    )
    
    ctx.auth = args.name if args.name else None   
      

    ctx.server_task = asyncio.create_task(
        server_loop(ctx),
        name="server loop"
    )

    ctx.run_gui()
    ctx.run_cli()
    
    edf5_client = EDF5Client(ctx)
    asyncio.create_task(edf5_client.run(), name = "EDF5 Monitor")

    await ctx.exit_event.wait()
    edf5_client.remove_mission_menu_hook()
    await ctx.shutdown()
    
class EDF5Client:
    def __init__(self, ctx):
        self.memory = EDF5Memory()
        self.just_connected = False
        self.ctx = ctx
        self.connected = False
        self.found_locations = set()    
        self.unlocked_missions = set()
        self.unlocked_weapons = set()
        self.has_achieved_victory = False
        self.ap_active = False        
        self.hook_cave = None
        self.hook_installed = False        
            
    # ----------------------------- #
    #           Main Loop           #
    # ----------------------------- #    
    
    # The main loop, for checking locations and unlocking items
    async def run(self):
        while True:
            proc = self.memory.find_edf5()

            if proc and not self.connected:
                self.memory.connect()
                self.connected = True
                logger.info("Found EDF5!")
                self.just_connected = True

            elif not proc and self.connected:
                self.disconnect_from_edf5()

            self.ap_active = (
                self.get_active_save_name() is True if self.connected else False
            )

            if self.connected and self.ctx.ap_connected and self.ap_active:
                try:
                    if self.just_connected:
                        await asyncio.sleep(1)
                        self.just_connected = False
                    self.write_mission(111, 17)

                    await self.check_for_new_completions()
                    await self.check_victory()

                    self.refresh_unlocked_sets()
                    self.install_mission_menu_hook()
                    self.update_mission_hook()
                    
                    if self.memory.is_safe_to_write():
                        self.synchronise_armor()
                        self.enforce_weapon_states()

                except Exception as e:
                    logger.info(f"Error: {e}")
                    self.disconnect_from_edf5()
            else:
                self.remove_mission_menu_hook()

            await asyncio.sleep(0.25)            
    
    def disconnect_from_edf5(self):
        if self.connected:
            logger.info("Lost connection to EDF5!")
            
        self.remove_mission_menu_hook()
        self.hook_cave = None        
        self.connected = False
        self.memory.disconnect()
        self.just_connected = False        
        self.unlocked_missions.clear()
        self.unlocked_weapons.clear()
        self.ap_active = False
    
    # ---------------------------- #
    #           Missions           #
    # ---------------------------- #    
    
    # Machine code the game runs at the hook. Copies our list of mission states (the items) over EDF5's versions (vanilla)
    # 'cave' is the memory we allocated, 'hook' is the address of the hook in the game
    def build_mission_menu_code(self, cave, hook):
        code_start = cave + 0x200
        
        # Our instructions to put into memory. Little breakdown on each line to help me remember what does what
        code = b"".join([
            b"\x56\x57\x51",                                # push rsi / rdi / rcx (save the registers we're about to use)
            b"\x49\x8B\x3E",                                # mov rdi,[r14]        (rdi = the game's mission table)
            b"\x48\xBE" + struct.pack("<Q", cave),          # mov rsi,<cave>       (rsi = our list of states)
            b"\xB9" + struct.pack("<I", MISSION_COUNT),     # mov ecx,110          (how many entries to copy)
            b"\xF3\xA5",                                    # rep movsd            (copy them, 4 bytes at a time)
            b"\x59\x5F\x5E",                                # pop rcx / rdi / rsi  (put the registers back)
            MISSION_MENU_HOOK_DEFAULT,                      # the two instructions we replaced
        ])
        
        # Return into the game, just after the bytes we replaced
        jump_back = (hook + len(MISSION_MENU_HOOK_DEFAULT)) - (code_start + len(code) + 5)
        code += b"\xE9" + struct.pack("<i", jump_back)
        
        return code
    
    def update_mission_hook(self):
        states = [1 if mission in self.unlocked_missions else 2 for mission in range(1, MISSION_COUNT + 1)]
        self.memory.write_bytes(self.hook_cave, struct.pack(f"<{MISSION_COUNT}i", *states))
        
    # Patch the hook into EDF5
    def install_mission_menu_hook(self):
        if self.hook_installed:
            return
        
        hook = self.memory.get_module_base() + MISSION_MENU_HOOK
        
        # Only patch if the game's code is what we expect to see
        current = self.memory.read_bytes(hook, len(MISSION_MENU_HOOK_DEFAULT))
        if current != MISSION_MENU_HOOK_DEFAULT and current[0] != 0xE9:
            raise RuntimeError("Unexpected code at mission menu hook! (Different version?)")
        
        if self.hook_cave is None:
            self.hook_cave = self.memory.allocate_near(hook)
            if self.hook_cave is None:
                raise RuntimeError("Couldn't find memory near EDF5 for mission menu hook!")
            
        code_start = self.hook_cave + 0x200
        self.memory.write_bytes(code_start, self.build_mission_menu_code(self.hook_cave, hook))
        
        # Fill our mission list before patching, by default it will be 0s (all missions cleared/accessible)
        self.update_mission_hook()
        
        # A 5 byte jump into our code, plus a nop to fill the 6th byte we're replacing
        jump = b"\xE9" + struct.pack("<i", code_start - (hook + 5)) + b"\x90"
        self.memory.write_bytes(hook, jump)
        self.hook_installed = True
        #logger.info("Mission menu hook installed!")
        
    # Put the game's original instructions back
    def remove_mission_menu_hook(self):
        if not self.hook_installed:
            return
    
        try:
            hook = self.memory.get_module_base() + MISSION_MENU_HOOK
            self.memory.write_bytes(hook, MISSION_MENU_HOOK_DEFAULT)
        except Exception:
            pass # EDF5 has probably closed, so there is nothing to restore
        
        self.hook_installed = False
    
    # Used for reading a single mission.        
    def read_mission(self, mission_number, player_class):
        if not self.memory.is_connected():
            return None
        
        module_base = self.memory.get_module_base()     
        try:
            r11 = self.memory.read_u64(module_base + PLAYER_DATA_POINTER)
            if r11 == 0:
                return
        except Exception as e:
            #logger.error(f"Failed reading mission pointer: {e}")
            return None        
        
        # Make sure the game doesn't crash, by checking the player has entered a correct class name
        if player_class not in MISSION_OFFSETS:
            return None
        
        mission_base = r11 + MISSION_OFFSETS[player_class]
        
        try:
            # return self.pm.read_uchar(mission_base + (mission_number - 1))
            return self.memory.read_u8(mission_base + (mission_number - 1))
        except Exception as e:
            #logger.error(f"Failed reading mission {mission_number} {player_class}: {e}")
            return None
        
    # Write mission completion state. Currently only used to write mission 111 as 17 (Unlocking all missions in the mission menu)
    # (17 (EASY & INFERO) isn't important, it's just a number I picked)
    def write_mission(self, mission_number, value):
        if not self.memory.is_connected():
            return None
        
        module_base = self.memory.get_module_base()
        
        r11 = self.memory.read_u64(module_base + PLAYER_DATA_POINTER)
        mission_base = r11 + 0x566C
        
        address = mission_base + (mission_number - 1)
        self.memory.write_u8(address, value)
        
    # ------------------------------------- #
    #           Location Checking           #
    # ------------------------------------- # 
    
    # Check for new completions.
    async def check_for_new_completions(self):
        current_locations = self.get_cleared_locations()
        
        # Check if there are any new locations since last check
        new_locations = current_locations - self.found_locations
        
        if new_locations:                
            await self.ctx.check_locations(new_locations)    
            self.found_locations.update(new_locations)
    
    # Read all locations in the game (Each mission on each difficulty on each class)    
    def get_cleared_locations(self):
        locations = set()
        # Get the selected classes from the slot data (What the player picked). Ranger is the default/fallback in case something goes wrong
        selected_classes = self.ctx.slot_data.get("player_classes", ["Ranger"])
        higher_clears_lower = self.ctx.slot_data.get("higher_difficulty_clears_lower", True)        
        
        # Loop through all missions
        for mission in range(1, 111):
            
            mission_cleared = False
            
            for player_class in selected_classes:
                value = self.read_mission(mission, player_class)
                
                if value is None:
                    continue
                
                # Check if any class has cleared this mission
                if value:
                    mission_cleared = True              
                    
                if higher_clears_lower:
                    if value & 16:
                        given_bits = [1, 2, 4, 8, 16]
                    elif value & 8:
                        given_bits = [1, 2, 4, 8]
                    elif value & 4:
                        given_bits = [1, 2, 4]
                    elif value & 2:
                        given_bits = [1, 2]
                    elif value & 1:
                        given_bits = [1]
                    else:
                        given_bits = []
                        
                else:
                    given_bits = [
                        bit for bit in DIFFICULTY_FLAGS
                        if value & bit
                    ]                
                
                for bit in given_bits:
                    difficulty = DIFFICULTY_FLAGS[bit]
                    
                    location_name = (f"Mission {mission} - {difficulty} ({player_class})")
                    locations.add(LOCATION_NAME_TO_ID[location_name])
                    
            if mission_cleared:
                locations.add(LOCATION_NAME_TO_ID[f"Mission {mission} - Cleared"])
                                
        return locations
        
    # ----------------------------------- #        
    #           Item Processing           #
    # ----------------------------------- #
    
    def get_logical_armor_bonus(self):
        armor_value = self.ctx.slot_data.get("armor_boost_value", 200)
        small = sum(1 for item in self.ctx.items_received if item.item == 111)
        big = sum(1 for item in self.ctx.items_received if item.item == 112)
        return small * armor_value + big * 1000
    
    def synchronise_armor(self):
        target = self.get_logical_armor_bonus()
        cap = int(target * 1.2)
        
        base = self.memory.get_player_data_base()
        actual = self.memory.read_i32(base + RANGER_ARMOR)
        
        if target <= actual <= cap:
            return
        
        delta = target - actual
        for offset in ARMOR_OFFSETS:
            addr = base + offset
            current = self.memory.read_i32(addr)
            self.memory.write_i32(addr, max(0, current +delta))
            
    async def check_victory(self):
        if self.has_achieved_victory:
            return
        if any(item.item == 116 for item in self.ctx.items_received):
            await self.ctx.send_msgs([{
                "cmd": "StatusUpdate",
                "status": ClientStatus.CLIENT_GOAL
            }])
            self.has_achieved_victory = True
            
    def refresh_unlocked_sets(self):
        received = {item.item for item in self.ctx.items_received}
        self.unlocked_missions = {i for i in received if 1 <= i <= 110}
        self.unlocked_weapons = {i for i in received if WEAPON_ID_MIN <= i <= WEAPON_ID_MAX}    
        
    # ------------------------------------ #
    #           Weapon Unlocking           #
    # ------------------------------------ # 
    
    def enforce_weapon_states(self):
        base = self.memory.get_player_data_base()
        
        for item_id in self.unlocked_weapons:
            offset = self.get_weapon_offset(item_id)
            
            if offset is None:
                continue
            
            address = base + offset
            current = self.memory.read_bytes(address, len(WEAPON_UNLOCK_DATA))
            if current != WEAPON_UNLOCK_DATA:
                self.memory.write_bytes(address, WEAPON_UNLOCK_DATA)            
    
    def get_weapon_offset(self, item_id):
        for table in WEAPON_TABLES.values():
            start = table["start_id"]
            end = table["end_id"]
            
            if start <= item_id <= end:
                return table["start_offset"] + ((item_id - start) * WEAPON_SIZE)
            
        return None    
    
    # ----------------------------- #
    #             Other             #
    # ----------------------------- #     

    def get_active_save_name(self):
        if not self.memory.is_connected():
            return None
        
        try:
            module_base = self.memory.get_module_base()
            base_addr = module_base + PLAYER_DATA_POINTER
            
            pointer = self.memory.read_u64(base_addr)
            filename_address = pointer + 0x51D8
            
            active_save_name = self.memory.read_utf16(filename_address)
            
            return active_save_name == AP_SAVE_NAME
            
        except Exception as e:
            return None