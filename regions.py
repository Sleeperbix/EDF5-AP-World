from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import EDF5World

# EDF5 doesn't really have any regions (for now), apart from perhaps the menu and the game itself.
def create_and_connect_regions(world: EDF5World) -> None:
    menu = Region("Menu", world.player, world.multiworld)
    edf5 = Region("EDF5", world.player, world.multiworld)
    
    world.multiworld.regions += [menu, edf5]
    menu.connect(edf5, "Start Game")
    