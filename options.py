from dataclasses import dataclass

from Options import Choice, PerGameCommonOptions, Range, Toggle, OptionSet
from Options import OptionGroup
    
class PlayerClasses(OptionSet):
    """
    Which classes the player will be playing as.
    (Ranger | Wing Diver | Air Raider | Fencer.)
    """
    
    display_name = "Player Classes"
    
    valid_keys = {"Ranger", "Wing Diver", "Air Raider", "Fencer"}
    
    default = {"Ranger"}
    
class ArmorBoostValue(Range):
    """
    How much armor an Armor Boost item will give your classes.
    The actual armor you receive is multiplied based on the class you are playing.
    (e.g. 1 armor = 0.8 Fencer, 0.64 Ranger/Air Raider, 0.4 Wing Diver)
    """
    
    display_name = "Armor Boost Value"
    
    range_start = 50
    range_end = 500    
    default = 100
    
# class GoalCondition(Choice):
#     """
#     Which condition should the goal for your
#     game be?
    
#     'Mission 109 Then Mission 110'
#     Clear Mission 109 to unlock Mission 110,
#     then clear Mission 110 to win.
#     Mission 109 will be shuffled somewhere, but it
#     will always give Mission 110 on clearing it.
    
#     'Mission 110 Only'
#     Clear Mission 110 to win.
#     Mission 110 will be shuffled somewhere.
#     """
    
#     display_name = "Goal Condition"
    
#     option_mission_109_then_mission_110 = 0
#     option_mission_110_only = 1
    
#     default = option_mission_109_then_mission_110
    
class Difficulties(Choice):
    """
    Set the difficulties for checks to be in.
    This also controls which weapons will be able to spawn.
    (e.g. Weapons up to lv. 52 will be avaiable on Easy Normal Hard)
    
    !!! WARNING !!!
    Only select anything other than Easy, Medium and Hard if you already have unlocked
    Hardest and Inferno (e.g. you have cleared Mission 110 on another save).
    """

    display_name = "Difficulties"
    
    option_easy_medium_hard = 0
    option_easy_medium_hard_hardest = 1
    option_easy_medium_hard_hardest_inferno = 2
    
    default = option_easy_medium_hard
    
class StartingMissions(Range):
    """
    Set how many missions you have available from the start of the game.
    """
    
    display_name = "Number of Starting Missions"
    
    range_start = 1
    range_end = 10
    default = 5
    
class HigherDifficultyClearsLower(Toggle):
    """
    Higher difficulties also count as checks for lower difficulty locations.
    This only applies to clearing checks on Inferno and Hardest.
    (e.g. Clearing a check on Hardest also checks it on Hard, Normal and Easy)
    """
    
    display_name = "Higher Difficulty Clears Lower Difficulties"
    
    default = True
    
class LogicWeaponLevel(Toggle):
    """
    For a mission and it's difficulty to be in logic, a randomly selected level appropriate weapon is required.
    These levels are based on the multiplayer weapon limits.
    If you're playing a game with Hardest or Inferno enabled, you'll probably want this setting enabled.
    """
    
    display_name = "Weapon Levels in Logic"
    
    default = True

class LogicArmorAmount(Toggle):
    """
    For a mission and it's difficulty to be in logic, appropriate armor amounts are required.
    These amounts are based on the multiplayer armor limits.
    If you're playing a game with Hardest or Inferno enabled, you'll probably want this setting enabled.
    """
    
    display_name = "Armor Amount in Logic"
    
    default = True

# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class EDF5Options(PerGameCommonOptions):
    player_classes: PlayerClasses
    armor_boost_value: ArmorBoostValue
    difficulties: Difficulties
    starting_missions: StartingMissions
    higher_difficulty_clears_lower: HigherDifficultyClearsLower
    weapon_levels_in_logic: LogicWeaponLevel
    armor_amount_in_logic: LogicArmorAmount


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "Gameplay Options",
        [PlayerClasses, ArmorBoostValue, Difficulties],
    ),
    OptionGroup(
        "Mission Options",
        [StartingMissions, HigherDifficultyClearsLower],
    ),
    OptionGroup(
        "Logic",
        [LogicWeaponLevel, LogicArmorAmount]
    )
]
