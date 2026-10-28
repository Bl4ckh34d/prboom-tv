# Setup details

The content example is an Ultimate Doom.m3u file containing one absolute path to the original DOOM.WAD. Use Modern controller device 773. For right-stick vertical look, edit the game's saved prboom.cfg while content is closed: movement_mouselook 1. Leave movement_mouseinvert 0 and movement_maxviewpitch 32 unless you prefer other settings. This is a game configuration setting, not a new engine patch.

Modern Xbox controls use A to confirm, B to toggle autorun or cancel menus, X to activate, Y to turn 180 degrees, LB/RB to select weapons and RT to fire. View opens the map; Start opens the game menu. The included remap disables L2/L3/R3 game actions so frontend fast-forward and save-state hotkeys do not collide. Doom II uses the same core with its own original WAD and content-specific profile. Reset returns to the title sequence; a saved state can be loaded afterward.

`config/Doom2` contains the tested DOOM II override, remap, core options and native settings. Adjust the example paths. The optional `doom2_libretro_android.so` name is a copy of the same build; it needs no independent engine repository. The tested content hook `DOOM II (Native).m3u` contains the absolute path to the user's original `DOOM2.WAD`.
