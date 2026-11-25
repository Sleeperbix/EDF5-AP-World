from collections.abc import Mapping
from typing import Any

# Imports of base Archipelago modules must be absolute.
from worlds.AutoWorld import World

# Imports of your world's files must be relative.
from . import items, locations, regions, rules, web_world
from . import options as edf5_options  # rename due to a name conflict with World.options
from .weapon_logic import get_logic_anchors
from .items import ITEM_DATA

# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/world%20api.md

class EDF5World(World):
    """
    Stand and fight for humanity.
    This arcade shooter takes place in the year 2022, as the Earth Defense Force fends off an all-out attack by unknown life forms.
    Become an EDF soldier, battle against endless hordes of immense enemies, and restore peace to the earth.
    """

    game = "Earth Defense Force 5"

    # The WebWorld is a definition class that governs how this world will be displayed on the website.
    web = web_world.EDF5WebWorld()
    options_dataclass = edf5_options.EDF5Options
    options: edf5_options.EDF5Options

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    # There is always one region that the generator starts from & assumes you can always go back to.
    origin_region_name = "EDF5"

    # Called during generation to create every region in the world
    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)
        locations.create_events(self)

    # Called during generation to define which locations require which items
    def set_rules(self) -> None:
        rules.set_all_rules(self)

    # Called during generation to populate the item pool
    def create_items(self) -> None:
        items.create_all_items(self)
        
    # Called early in generation to determine the anchor weapons, and give the player their starting missions
    def generate_early(self) -> None:
        self.weapon_anchors, self.utility_anchors = get_logic_anchors(self, items.ITEM_DATA)
        
        # Should I move this to items.py? Maybe...
        for mission in range (1, self.options.starting_missions.value + 1):
            self.multiworld.push_precollected(self.create_item(f"Mission {mission}"))

    # Creates a single EDF5 item
    def create_item(self, name: str) -> items.EDF5Item:
        return items.create_item_with_correct_classification(self, name)

    # Gives the generator a filler item whenever one is required
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)
    
    # This is where the players options are sent to the client (as long as they are defined)
    # These values are available in client.py using "self.ctx.slot_data"
    def fill_slot_data(self) -> Mapping[str, Any]:
        return {
            "armor_boost_value": self.options.armor_boost_value.value,
            "player_classes": list(self.options.player_classes.value),
            "higher_difficulty_clears_lower": self.options.higher_difficulty_clears_lower.value,
        }