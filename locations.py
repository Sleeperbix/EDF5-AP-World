from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Location

if TYPE_CHECKING:
    from .world import EDF5World

# This is the master lookup table for the missions    
LOCATION_NAME_TO_ID = {}

# The next unused AP location ID. Counter is incremented each time a new location is assigned an ID
idCounter = 1

# Define all classes, and difficulties.
classes = ["Ranger", "Wing Diver", "Air Raider", "Fencer"]
difficulties = ["Easy", "Normal", "Hard", "Hardest", "Inferno"]

# Generate the ids for all missions and difficulties. These won't all necessarily exist in the seed.
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

class EDF5Location(Location):
    game = "Earth Defense Force 5"
    
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: EDF5World) -> None:
    create_regular_locations(world)

def create_regular_locations(world: EDF5World) -> None:
    edf5 = world.get_region("EDF5")
    
    # Get classes the player selected to play as
    selected_classes = world.options.player_classes.value
    
    # Get the difficulties the player selected to play on (0 = Hard, 1 = Hardest, 2 = Inferno)
    selected_difficulties = world.options.difficulties.value
    if selected_difficulties == 0:
        allowed_difficulties = ["Easy", "Normal", "Hard"]
    elif selected_difficulties == 1:
        allowed_difficulties = ["Easy", "Normal", "Hard", "Hardest"]
    elif selected_difficulties == 2:
        allowed_difficulties = ["Easy", "Normal", "Hard", "Hardest", "Inferno"]
    else:
        raise ValueError(f"Unknown difficulty option: {selected_difficulties!r}")
    # Create the location list. It will start empty, and have locations added to it
    enabled_locations = {}
    
    # Check all locations
    for location_name, location_id in LOCATION_NAME_TO_ID.items():

        # If cleared is in the name, add it to the location list. "Mission X - Cleared" must always be in the location list (for now)
        if "Cleared" in location_name:
            enabled_locations[location_name] = location_id
            continue
        
        # Each class the player has selected to play as has their locations added to the location list.
        for playerClass in classes:
            if (playerClass in selected_classes and f"({playerClass})" in location_name):
                for difficulty in allowed_difficulties:
                    if (f" - {difficulty} (" in location_name):
                        enabled_locations[location_name] = location_id
                        break
    
    # Finally, add the locations to Archipelago            
    edf5.add_locations(enabled_locations, EDF5Location)    
    
def create_events(world: EDF5World) -> None:
    edf5 = world.get_region("EDF5")    
    