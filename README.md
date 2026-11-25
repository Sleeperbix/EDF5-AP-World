# Earth Defense Force 5 Archipelago

This is a work in progress Archipelago implementation for Earth Defense Force 5 (also known as EDF5).
Version 0.1.0.

## Requirements

- Windows (Linux is not currently supported)
- An installation of EDF5 (Steam)
- The latest version of Archipelago
- The EDF5 APWorld file
- A spare save slot in EDF5 (preferably not slot 4)
- An existing save file that has unlocked Hardest and Inferno **(if you want to play with Hardest and Inferno checks)**

## Setup

- Download the latest version of Archipelago (https://github.com/ArchipelagoMW/Archipelago/releases).
- Install edf5.apworld (either by double-clicking the APWorld file, or through the Archipelago Launcher).
- Generate a YAML file through the Options Creator in the Archipelago Launcher, or open Generate Template Options also within the Archipelago Launcher (and edit that template in an editor of your choice).
- Provide the generated YAML file to whoever is generating your APWorld, or save it inside the players folder.
- If you are generating the world, press Generate in the Archipelago Launcher (with your YAML file in the players folder).
- Either press Host in the Archipelago Launcher and select the generated game (zipped folder) in outputs if you want to host the game locally, or upload the generated game to Archipelago’s website.

## Joining and playing a game

- Launch EDF5, create a new save and name it EDF5-AP. The name must be EDF5-AP for the client to work, and preferably not in slot 4.
- Select Offline Mission Mode, then Offline Mission Mode again (do not select Online, 2 Player Split-Screen or any of the DLCs)
- Launch the EDF5 Client from the Archipelago Launcher. It will say “Found EDF5!” if it has found EDF5. It will also say “Lost connection to EDF5!” if it loses connection to EDF5.
- Connect to the host with the server address (use localhost if you are hosting locally), the player name you set in the YAML file, and the server password if one is set.
- The game should now be ready to play. To confirm everything is working, select Start Mission, and you should see every mission up to Mission 110 is titled “???”, apart from the missions you set in your options file to start with.
- If you want to switch save files at any point, return to the menu while the EDF5 Client is still running. If you have already closed the client, restart the game before opening another save file.

## What gets randomised?

All 110 base game missions, along with level appropriate maxed weapons and accessories for your selected classes, are items you can receive from checks. You can't enter a mission without the appropriate mission item; for example, you need the AP item 'Mission 50' to be able to play Mission 50.

You also gain Armor Boosts as items, with Big Armor Boosts as an item if you play with Inferno and/or Hardest enabled.
Armor boosts aren’t directly applied, and instead just increase your maximum armor value (which can be set by going to Adjust Armor in your selected classes’ equipment menu).

## What are the checks?

Checks are awarded for completing missions on each difficulty that you set in your YAML file, as each class you set in your YAML file, as well as for clearing each mission on any difficulty and any class.

So to summarise:
- One general completion check.
- One check for each enabled difficulty and selected class.

The amount of checks depends on what difficulties and classes you have selected. The formula, if you will, is **110 + ((110 x D) x C)**, with D being difficulties and C being classes.
For example:
- Playing as Ranger and Air Raider with Hardest difficulty: 110 + ((110 x 4) x 2) = 990 checks.
- Playing as Fencer with Hard difficulty: 110 + ((110 x 3) x 1) = 440 checks.
- Playing as Ranger, Wing Diver, Air Raider and Fencer, with Inferno difficulty: 110 + ((110 x 5) x 4) = 2310 checks.

**I would recommend not selecting all four classes and all difficulties (unless your host knows you are doing this), as this will very likely be a LONG game.**

The only victory condition at the moment is to clear Mission 110 on any difficulty. Mission 110 is unlocked by clearing Mission 109 on any difficulty.
Victory is achieved after the credits, as you return to the Headquarters menu.

## Does this work with other mods?

If the mod adds weapons and missions it won’t work, but if it replaces them it would probably work (although the names won’t match those in the apworld). The only mod I have tried this with is the Lootmaster mod, which appears to be fine. Otherwise, try to play as vanilla as possible (or don't, I can't stop you!).

## Does this work on multiplayer?

I have not tried this implementation in multiplayer, nor do I currently intend for this to work in multiplayer. Use in multiplayer is entirely at your own risk, and I cannot guarantee that it will function correctly.

## Why shouldn’t I use slot 4 as my AP save file?

As the game transitions from the title screen to the screen where you select a save, it briefly loads each save file’s name into memory as the active save. However, it never unloads save 4, which means while you are on the 'select a save screen', the game thinks you are actually in save 4.
This isn’t usually an issue, but the way I have coded this implementation has the client check which file is the active save file and only making changes to the game’s memory if the active save file is “EDF5-AP”, as a means of protecting other save files from being messed around with.
I haven’t noticed any major issues as a result of this from testing, but I find it better to err on the side of caution. It’s up to you if you use save slot 4 ultimately, but remember my warning.

## Known Issues

    - Certain missions as Air Raider might be difficult, as the logic doesn’t currently give you 'required' items to beat specific missions (e.g. a weapon/vehicle to shoot Teleportation Ships from underneath, weapons that are suitable for underground missions).
    - Fencer can currently receive weapons that require Air Raider’s targeting tools as randomised items. I will remove these by default in an update in the future, but give the option to re-enable them for players using mods that remove the targeting tool requirement (e.g. Class Addons - Fencer No Beacon Addon).
    - If you close the EDF5 Client and then open another save file, the game will likely crash on opening the mission menu. The game will return to normal after restarting though.
    - If you try to go into Mission Pack 1 or 2 on your EDF5-AP save and open the mission menu, the game will crash (if the client is open). Although this is expected as Mission Packs 1 and 2 aren’t supported.

## Future Plans

I intend to add a number of features to this AP implementation in the future, such as:

- Checks for killing quantities of enemies (e.g. 100 Ants, 1,000 Bees, 2,500 Spiders etc.)
- Quicker missions (likely modding each mission to reduce the amount of time waiting for dialogue to finish, if possible)
- Additional mission/weapon logic (Air Raider and Fencer need some attention for certain weapons and missions)
- Add an option to remove underground missions from the item pool (mostly for Air Raider players who really love air strikes)
- An option to remove armor and weapon drops (or ignore them)
- Progressive weapons (as opposed to specific weapons as items)
- Classes as items (for games with more than one class enabled, you have to unlock them)
- Other victory conditions (e.g. collecting X ‘EDF Emblems’ to win)
- Deathlink
- Traps and other useful items (e.g. fully restore armor in mission)

## AI Disclosure

I used AI assistance primarily for parts of the client implementation, and for some troubleshooting whenever I broke something. The project, its code, and underlying logic were written and developed by me.

## Credits

Idlehands88 – Author of the Cheat Engine Table I used to find memory addresses for various things
EDF5 Japanese Wiki – Mission and weapon information
NewSoupVi - AP Quest developer (the base I used to get started)
The Archipelago Team and community – For creating and maintaining Archipelago!

## Disclaimer

Earth Defense Force 5 and all associated game assets, trademarks and intellectual property belong to their respective owners. This is an unofficial, fan-made Archipelago implementation and is not affiliated with, endorsed by, or supported by D3 Publisher, Sandlot, or any other rights holder.

This project does not include or distribute any original EDF5 game files or assets. A legitimate installation of Earth Defense Force 5 is required.

This software is provided “as is”, without any guarantees that it will function correctly or be compatible with every system, game version, save file, or mod. Use it at your own risk. I recommend backing up your save files before playing.

I do not accept any responsibility for lost or corrupted save data, game crashes or other issues arising from its use.
