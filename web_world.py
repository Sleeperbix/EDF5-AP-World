from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups as EDF5_OPTION_GROUPS

# Keeping this file for the future, and it currently keeps the option groups working (in the launcher)
class EDF5WebWorld(WebWorld):
    game = "Earth Defense Force 5"
    theme = "partyTime"

    # A WebWorld can have any number of tutorials, but should always have at least an English setup guide.
    # Many WebWorlds just have one setup guide, but some have multiple, e.g. for different languages.
    # We need to create a Tutorial object for every setup guide.
    # In order, we need to provide a title, a description, a language, a filepath, a link, and authors.
    # The filepath is relative to a "/docs/" directory in the root folder of your apworld.
    # The "link" parameter is unused, but we still need to provide it.
    # setup_en = Tutorial(
    #     "Multiworld Setup Guide",
    #     "A guide to setting up APQuest for MultiWorld.",
    #     "English",
    #     "setup_en.md",
    #     "setup/en",
    #     ["NewSoupVi"],
    # )

    # We add these tutorials to our WebWorld by overriding the "tutorials" field.
    # tutorials = [setup_en]

    # If we have option groups and/or option presets, we need to specify these here as well.
    option_groups = EDF5_OPTION_GROUPS
