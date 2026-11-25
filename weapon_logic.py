from __future__ import annotations

import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import EDF5World
    
def get_required_big_armor_boosts (armor_requirement: int) -> int:
    starting_armor = 200 # Ranger's starting armor. We will use Ranger's armor values to determine armor related logic
    armor_per_boost = 1000 # The value of the big armor boosts
    
    # Give the player some leeway for meeting the requirements. They'll also have a decent amount of small boosts anyway
    target_armor = armor_requirement * 0.75
    
    if target_armor <= starting_armor:
        return 0
    
    return math.ceil(target_armor / armor_per_boost)    


def get_logic_suitable_weapons(ITEM_DATA: dict, player_class: str, required_level:int) -> list[str]:
    suitable_weapons = []
    level_requirement = math.ceil(required_level * 0.75) # Take 25% off of the required level
    
    for item_name, item_data in ITEM_DATA.items():
        # Check the item being looked at actually is a weapon for the class in question
        if item_data.player_class != player_class:
            continue
        
        # These are item types to ignore, that are specific to each class
        if player_class == "Ranger" and item_data.weapon_type in ["Special", "Support Equipment", "Bike", "Tank", "Helicopter"]:
            continue
        
        if player_class == "Wing Diver" and item_data.weapon_type in ["Special", "Plasma Core"]:
            continue
        
        if player_class == "Fencer" and item_data.weapon_type in ["Shield", "Enhanced Booster", "Enhanced Shield", "Enhanced Cannon", "Enhanced Exoskeleton"]:
            continue
                
        if player_class == "Air Raider" and item_data.weapon_type in ["Stationary Weapon", "Support Equipment", "Special", "Tank", "Powered Exoskeleton", "Special Weapon", "Helicopter", "Ground Vehicle"]:
             continue
        
        # Ignore any bonus DLC and unobtainable weapons. Bonus DLC could be added at some point in the future.
        if item_data.dlc_type in ["bonus", "n/a"]:
            continue
        
        # If for some reason the weapon doesn't have a level, we ignore it (mostly as a failsafe)
        if item_data.level is None:
            continue
        
        # Add the item as a suitable weapon
        if item_data.level >= level_requirement:
            suitable_weapons.append(item_name)
            
    return suitable_weapons


def get_logic_suitable_utilities(ITEM_DATA: dict, player_class: str, required_level:int) -> list[str]:
    suitable_utilities = []
    level_requirement = math.ceil(required_level * 0.75) # Take 25% off of the required level
    
    for item_name, item_data in ITEM_DATA.items():
        if item_data.player_class != player_class:
            continue
        
        if player_class == "Ranger" and item_data.weapon_type != "Support Equipment":
            continue
        
        if player_class == "Wing Diver" and item_data.weapon_type != "Plasma Core":
            continue
            
        if player_class == "Fencer" and item_data.weapon_type not in ["Enhanced Booster", "Enhanced Cannon", "Enhanced Exoskeleton"]:
            continue

        if player_class == "Air Raider" and item_data.weapon_type not in ["Tank", "Powered Exoskeleton", "Ground Vehicle"]:
            continue        
        
        if item_data.dlc_type in ["bonus", "n/a"]:
            continue
        
        if item_data.level is None:
            continue
        
        if item_data.level >= level_requirement:
            suitable_utilities.append(item_name)
            
    return suitable_utilities
    

def get_logic_anchors(world: EDF5World, ITEM_DATA: dict):
    # Anchors are the weapons we choose to be the 'progression' weapons, which ensure the player should always have a suitable weapon for hardest and inferno at some point
    # Milestones are the weapon level brackets for the missions, so a mission with a 50 weapon requirement can be fulfilled by a lvl 50 weapon (or something within 25% of it)
    selected_classes = world.options.player_classes.value
    anchors_weapons = {}
    anchors_utilities = {}
    milestones = [50, 60, 70, 80, 90, 100]
    
    for player_class in selected_classes:
        anchors_weapons[player_class] = []
        anchors_utilities[player_class] = []
        milestone_index = 0
        
        while milestone_index < len(milestones):
            milestone = milestones[milestone_index]
            
            suitable_weapons = get_logic_suitable_weapons(ITEM_DATA, player_class, milestone)
            suitable_utilities = get_logic_suitable_utilities(ITEM_DATA, player_class, milestone)
            
            if not suitable_weapons or not suitable_utilities:
                milestone_index += 1
                continue
            
            # The first anchor must be restricted, so AP doesn't just pick a high level weapon and be done with it
            if not anchors_weapons[player_class]:
                suitable_weapons = [item_name for item_name in suitable_weapons if ITEM_DATA[item_name].level < 60]
                suitable_utilities = [item_name for item_name in suitable_utilities if ITEM_DATA[item_name].level < 60]
                
            if not suitable_weapons or not suitable_utilities:
                milestone_index += 1
                continue
            
            # Pick a suitable weapon and utility
            weapon_anchor = world.random.choice(suitable_weapons)
            utility_anchor = world.random.choice(suitable_utilities)
            
            anchors_weapons[player_class].append(weapon_anchor)
            anchors_utilities[player_class].append(utility_anchor)
            
            # Use the lower level of the two items to determine how many milestones they cover
            weapon_level = ITEM_DATA[weapon_anchor].level
            utility_level = ITEM_DATA[utility_anchor].level
            anchor_level = min(weapon_level, utility_level)
            
            while (milestone_index < len(milestones) and anchor_level is not None and anchor_level >= math.ceil(milestones[milestone_index] * 0.75)):
                milestone_index += 1
                
    return anchors_weapons, anchors_utilities




