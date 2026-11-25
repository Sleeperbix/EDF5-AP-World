from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification
import math

from .item_tables.items_general import GENERAL_ITEMS
from .item_tables.items_ranger import RANGER_ITEMS
from .item_tables.items_wingdiver import WINGDIVER_ITEMS
from .item_tables.items_fencer import FENCER_ITEMS
from .item_tables.items_airraider import AIRRAIDER_ITEMS

if TYPE_CHECKING:
    from .world import EDF5World
    
ITEM_DATA = {     
    **GENERAL_ITEMS,
    **RANGER_ITEMS,
    **WINGDIVER_ITEMS,
    **FENCER_ITEMS,
    **AIRRAIDER_ITEMS,
}

# Find each items name, and their ID.
ITEM_NAME_TO_ID = {    
    name: data.id
    for name, data in ITEM_DATA.items()
}

# Find each items name, and their classification.
DEFAULT_ITEM_CLASSIFICATIONS = {    
    name: data.classification
    for name, data in ITEM_DATA.items()
}

# Each Item instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Item class and override the "game" field.
class EDF5Item(Item):
    game = "Earth Defense Force 5"

# Ontop of our regular itempool, our world must be able to create arbitrary amounts of filler as requested by core.
# To do this, it must define a function called world.get_filler_item_name(), which we will define in world.py later.
# For now, let's make a function that returns the name of a random filler item here in items.py.
def get_random_filler_item_name(world: EDF5World) -> str:
    return "Armor Boost"

def create_item_with_correct_classification(world: EDF5World, name: str) -> EDF5Item:
    item = ITEM_DATA[name]    
    classification = item.classification
    
    weapon_anchors = getattr(world, "weapon_anchors", {})
    utility_anchors = getattr(world, "utility_anchors", {})
    
    if any(name in anchors for anchors in weapon_anchors.values()):
        classification = ItemClassification.progression
        
    if any(name in anchors for anchors in utility_anchors.values()):
        classification = ItemClassification.progression
    
    return EDF5Item(name, classification, item.id, world.player)    

# With those two helper functions defined, let's now get to actually creating and submitting our itempool.
def create_all_items(world: EDF5World) -> None:
    # Create itempool      
    itempool:list[Item] = []
    
    selected_classes = world.options.player_classes.value
    selected_difficulties = world.options.difficulties.value + 1 # Add 1 to bring it inline with the difficulty values on the item tables
    
    # Import in the missions the player has selected to start with, from the options file
    starter_missions_no = world.options.starting_missions.value
    total_missions_no = 109 # Change this if for whatever reason the total missions changes (e.g. adding dlc missions)
    # This is also 109 because we don't want 110 to randomly appear in the itempool (for now)
    
    for x in range (starter_missions_no + 1, total_missions_no + 1):
        itempool.append(world.create_item(f"Mission {x}"))
    
    # Create 20 Big Armor Boosts, which should be enough to clear all missions on inferno
    # These should only be created if hardest and inferno are in the logic
    if selected_difficulties >= 2:
        for x in range(20):
            itempool.append(world.create_item("Big Armor Boost"))
    
    # Then check for the classes the player has selected to play as, starting with Ranger    
    
    if "Ranger" in selected_classes:
        for item_name, item_data in ITEM_DATA.items():
            if item_data.player_class == "Ranger":
                # Check if the items under Ranger have "bonus" as dlc_type. Bonus refers to DLC weapons (not mission pack DLC)
                if item_data.dlc_type not in ["bonus"]:
                    # Check if the item is unobtainable. Unobtainable items are usually items you can't get normally (such as 'Empty', for the bike slot)
                    if item_data.unobtainable != 1:
                        # Check if the item should be obtainable on the selected difficulties. E.g. difficulty 2 items are obtainable on Easy, Normal, Hard, and Hardest (Not Inferno)
                        if item_data.difficulty <= selected_difficulties:
                            itempool.append(world.create_item(item_name))
    
    if "Wing Diver" in selected_classes:
        for item_name, item_data in ITEM_DATA.items():
            if item_data.player_class == "Wing Diver":
                if item_data.dlc_type not in ["bonus"]:
                    if item_data.unobtainable != 1:
                        if item_data.difficulty <= selected_difficulties:
                            itempool.append(world.create_item(item_name))
                        
    if "Fencer" in selected_classes:
        for item_name, item_data in ITEM_DATA.items():
            if item_data.player_class == "Fencer":                
                if item_data.dlc_type not in ["bonus"]:
                    # Unobtainable for Fencer includes items he starts with, but don't actually have a star rating to them (his cells/boosters), so receiving them as an item would be pointless
                    if item_data.unobtainable != 1:
                        if item_data.difficulty <= selected_difficulties:
                            itempool.append(world.create_item(item_name))
                            
    if "Air Raider" in selected_classes:
        for item_name, item_data in ITEM_DATA.items():
            if item_data.player_class == "Air Raider":
                if item_data.dlc_type not in ["bonus"]:
                    if item_data.unobtainable != 1:
                        if item_data.other_type not in ["Targeting Tool"]: # This currently removes the Air Raiders targeting tools from item generation
                            if item_data.difficulty <= selected_difficulties:
                                itempool.append(world.create_item(item_name))

    # Set "Mission 110" and "Victory" to be given upon clearing Mission 109 and Mission 110
    # This will become conditional at some point, based on what victory condition the player picks
    world.get_location("Mission 109 - Cleared").place_locked_item(world.create_item("Mission 110"))
    world.get_location("Mission 110 - Cleared").place_locked_item(world.create_item("Victory"))
    # Then stop progression items from being placed in Mission 109 & 110 (This seems to stop very short games where Mission 109 is placed in sphere 1 or 2)
    for player_class in selected_classes:
        world.get_location(f"Mission 109 - Easy ({player_class})").item_rule = lambda item: not item.advancement
        world.get_location(f"Mission 110 - Easy ({player_class})").item_rule = lambda item: not item.advancement
        world.get_location(f"Mission 109 - Normal ({player_class})").item_rule = lambda item: not item.advancement
        world.get_location(f"Mission 110 - Normal ({player_class})").item_rule = lambda item: not item.advancement
        world.get_location(f"Mission 109 - Hard ({player_class})").item_rule = lambda item: not item.advancement
        world.get_location(f"Mission 110 - Hard ({player_class})").item_rule = lambda item: not item.advancement
        if world.options.difficulties.value >= 1:
            world.get_location(f"Mission 109 - Hardest ({player_class})").item_rule = lambda item: not item.advancement
            world.get_location(f"Mission 110 - Hardest ({player_class})").item_rule = lambda item: not item.advancement
        if world.options.difficulties.value >= 2:
            world.get_location(f"Mission 109 - Inferno ({player_class})").item_rule = lambda item: not item.advancement
            world.get_location(f"Mission 110 - Inferno ({player_class})").item_rule = lambda item: not item.advancement

    # The length of our itempool is easy to determine, since we have it as a list.
    number_of_items = len(itempool)

    # The number of locations is also easy to determine, but we have to be careful.
    # Just calling len(world.get_locations()) would report an incorrect number, because of our *event locations*.
    # What we actually want is the number of *unfilled* locations. Luckily, there is a helper method for this:
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    # Now, we just subtract the number of items from the number of locations to get the number of empty item slots.
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    # Finally, we create that many filler items and add them to the itempool.
    # To create our filler, we could just use world.create_item("Confetti Cannon").
    # But there is an alternative that works even better for most worlds, including APQuest.
    # As discussed above, our world must have a get_filler_item_name() function defined,
    # which must return the name of an infinitely repeatable filler item.
    # Defining this function enables the use of a helper function called world.create_filler().
    # You can just use this function directly to create as many filler items as you need to complete your itempool.
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool