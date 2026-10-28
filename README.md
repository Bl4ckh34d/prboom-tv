# PrBoom TV

A small patch and reproducible build recipe for PrBoom on 32-bit ARM Android TV. Original DOOM game data is required.

## Scope

Enables the existing persistent framebuffer path with PRBOOM_PERSISTENT_FRAMEBUFFER. This fixes stale/missing HUD digits when a frontend rotates software framebuffers while the status bar only redraws dirty regions.

This repository contains the integration sources, patches and build/profile files. Upstream engines and dependencies are fetched at the exact revisions in `dependencies.json`; original commercial game data is not included.

## Build

The verified build host is Windows with Python 3.10+, Git for Windows at `C:/Program Files/Git` (short shell path `C:/Progra~1/Git/bin/sh.exe`) and Android NDK r27d. Use a checkout path without spaces. Set `ANDROID_NDK_HOME` if the NDK is not at `C:/tools/android/android-ndk-r27d`.

```powershell
python scripts/fetch_sources.py
python scripts/build_prboom.py
```

Output: `release/ultimate_doom_libretro_android.so` (ARMv7, Android API 21). `PORT_SOURCES_DIR` optionally points to an existing dependency directory to share downloads between builds. Fetch refuses unexpected existing revisions/origins instead of resetting them. Remove only disposable `build/` output when a clean rebuild is needed.

## Install and configure

Install the core through RetroArch's Android core installation interface. The tested package is `com.retroarch.ra32`; its `com.retroarch.browser.debug.CoreSideloadActivity` accepts a `LIBRETRO` string pointing to a readable core file. Other RetroArch packages may differ.

Keep original game data on USB. Keep saves in a writable directory. `config/` contains the tested content-specific override/remap/options examples; adjust Android paths and content filenames to your installation. See [setup details](docs/setup.md). Do not replace the global RetroArch configuration. Xbox labels here refer to the tested Android Xbox mapping; other controller profiles can differ.

## Verification and limits

E1M1 movement, shooting, persistent HUD and native save/load passed. 640x400 with two render threads and Vulkan/threaded/VSync: 60 presented FPS in a 21.8-second sample. Vertical look was separately verified in E1M1.

The follow-up verified both Ultimate DOOM and DOOM II: gameplay movement/fire, L3 save state, R3 restoration of position and ammunition, Reset/load, fast-forward and Close Content. Modern controller device 773 uses A to confirm, X to activate, LB/RB for weapons and RT to fire; the example remaps reserve L2/L3/R3 for frontend shortcuts. Other WADs remain untested. The same compiled core serves both games; separate filenames are optional for frontend organization.

These are bounded historical gameplay checks on one Android 11 ARMv7/Mali-G52 TV. Physical controller feel and speaker quality were not independently measured. See `docs/verification.md` for publication-time build checks.

## Licensing and credits

New integration code, build scripts and documentation in this repository are provided under GPL-2.0-or-later. Patches retain the applicable upstream file licenses. See `LICENSE` and `licenses/` for upstream notices. Dependencies retain their own licenses; review them before distributing a linked binary. Game names identify compatibility and do not imply endorsement.
