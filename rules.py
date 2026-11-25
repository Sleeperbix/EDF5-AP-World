from __future__ import annotations

import math
from typing import TYPE_CHECKING
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasFromListUnique
from .mission_table import MISSION_TABLE
from .items import ITEM_DATA
from .weapon_logic import get_required_big_armor_boosts

if TYPE_CHECKING:
    from .world import EDF5World

# Define the requirements needed to access every EDF5 location. 
def set_all_rules(world: EDF5World) -> None:
        
    # Obtain the classes the player has selected to play as
    selected_classes = world.options.player_classes.value
    selected_difficulties = world.options.difficulties.value

    if selected_difficulties == 0:
        allowed_difficulties = ["Easy", "Normal", "Hard"]
    elif selected_difficulties == 1:
        allowed_difficulties = ["Easy", "Normal", "Hard", "Hardest"]
    elif selected_difficulties == 2:
        allowed_difficulties = ["Easy", "Normal", "Hard", "Hardest", "Inferno"]
    
    # Go through missions 1 to 110, set each location (class/difficulty) to require the respective mission item
    for mission in range(1, 111):              
        
        # Generic mission cleared location
        mission_rule = Has(f"Mission {mission}")        
        location_clear = world.get_location(f"Mission {mission} - Cleared")
        world.set_rule(location_clear, mission_rule)
        
        # Difficulty specific locations
        for player_class in selected_classes:
            for difficulty in allowed_difficulties:
                
                location_difficulty = world.get_location(f"Mission {mission} - {difficulty} ({player_class})")                           
                rule = mission_rule
                
                if difficulty in ["Hardest", "Inferno"]:
                    weapon_requirement = MISSION_TABLE[mission][f"w-{difficulty.lower()}"]
                    armor_requirement = MISSION_TABLE[mission][f"a-{difficulty.lower()}"]
                    
                    # Find the anchors that are good enough
                    if world.options.weapon_levels_in_logic:
                        suitable_weapons = [weapon for weapon in world.weapon_anchors[player_class] if ITEM_DATA[weapon].level is not None and ITEM_DATA[weapon].level >= math.ceil (weapon_requirement * 0.75)]
                        suitable_utilities = [utility for utility in world.utility_anchors[player_class] if ITEM_DATA[utility].level is not None and ITEM_DATA[utility].level >= math.ceil (weapon_requirement * 0.75)]
                                       
                        weapon_rule = HasFromListUnique(*suitable_weapons, count=1)
                        utility_rule = HasFromListUnique(*suitable_utilities, count=1)
                        
                        rule = rule & weapon_rule  & utility_rule
                    
                    if world.options.armor_amount_in_logic:
                        armor_amount_required = get_required_big_armor_boosts(armor_requirement)
                        armor_rule = Has("Big Armor Boost", armor_amount_required)
                        
                        rule = rule & armor_rule
                
                world.set_rule(location_difficulty, rule)                
                
    set_completion_condition(world)            
    
# The current completion condition for EDF5 is completing mission 110, which gives the item "Victory" on "Mission 110 - Cleared"
def set_completion_condition(world: EDF5World) -> None:
    world.set_completion_rule(Has("Victory"))
    
