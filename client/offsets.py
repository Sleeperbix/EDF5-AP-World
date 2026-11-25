PLAYER_DATA_POINTER = 0x125AB30
# MISSION_TABLE_POINTER = 0x0125B188
AP_SAVE_NAME = "EDF5-AP"

# Armor Offsets
RANGER_ARMOR = 0x6D24
WINGDIVER_ARMOR = 0x6D28
AIRRAIDER_ARMOR = 0x6D2C
FENCER_ARMOR = 0x6D30

ARMOR_OFFSETS = [RANGER_ARMOR, WINGDIVER_ARMOR, AIRRAIDER_ARMOR, FENCER_ARMOR]

# Mission Completion Offsets
MISSION_OFFSETS = {    
    "Ranger":       0x566C,
    "Wing Diver":   0x586C,
    "Air Raider":   0x5A6C,
    "Fencer":       0x5C6C
}

# The game finished building the mission state table at EDF5.exe.text+526F1D. The text section starts 0x1000 into the module, which is why it's 0x527F1D
MISSION_MENU_HOOK = 0x527F1D

# The original instructions at 0x527F1D. In case we need to restore the original bytes (like when we load a different save file that isn't EDF5-AP)
MISSION_MENU_HOOK_DEFAULT = bytes([0x41, 0x8B, 0xD4, 0x45, 0x33, 0xC0])

MISSION_COUNT = 110

WEAPON_UNLOCK_DATA = bytes([
    0x01, 0x00, 0x00, 0x00,
    0x0A, 0X0A, 0X0A, 0X0A,
    0X0A, 0X0A, 0X0A, 0X0A
])

# Weapon Table Information
WEAPON_TABLES = {
    "Ranger":       {"start_id": 120,  "end_id": 446,  "start_offset": 0xEA0C},
    "Wing Diver":   {"start_id": 500,  "end_id": 760,  "start_offset": 0xF960},
    "Fencer":       {"start_id": 800,  "end_id": 1008, "start_offset": 0x1059C},
    "Air Raider":   {"start_id": 1100, "end_id": 1414, "start_offset": 0x10F80}
}

WEAPON_ID_MIN = min(table["start_id"] for table in WEAPON_TABLES.values())
WEAPON_ID_MAX = max(table["end_id"] for table in WEAPON_TABLES.values())

WEAPON_SIZE = 0xC

DIFFICULTY_FLAGS = {
    1: "Easy",
    2: "Normal",
    4: "Hard",
    8: "Hardest",
    16: "Inferno"
}