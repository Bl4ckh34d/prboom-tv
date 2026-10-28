# Follow-up verification — 2026-10-29

The repository's build script completed on Windows with NDK r27d using the pinned shared sources. Python scripts parse, and source patches pass both a forward check against a temporary pristine upstream index and a reverse check against the working source. Original game data, saves, screenshots and binaries are excluded from publication.

Build: `ultimate_doom_libretro_android.so`, 2,104,792 bytes, SHA-256 `d24971b605fa67565bec6f2bc0f081fabf7bf65a9df353287f9908308774c1d0`.

The byte-identical installed build passed Ultimate DOOM and DOOM II gameplay, save-state restoration of position/ammunition, reset/load, fast-forward, vertical look and Close Content. Modern device 773 and the included remaps reserve L2/L3/R3 for frontend hotkeys. DOOM II profiles are included under config/Doom2.

These are bounded checks on Android 11 ARMv7. They do not establish whole-campaign performance or subjective physical-controller feel. Earlier records below describe their own historical builds.

---

# Publication verification � 2026-10-28

The checked-in build recipe passed on Windows with Python/Git and NDK r27d, targeting ARMv7 API 21. Python scripts parse successfully. All patches pass forward checks against the pinned upstream index and reverse checks against the patched working tree.

Build: `ultimate_doom_libretro_android.so`, 2104824 bytes, SHA256 `190c6c691165c64d0dc46f3054daae04115f5b079f07d3051c180b9150e6e3fb`. This identifies this verification build; paths and timestamps can affect rebuild hashes. Original game files, player saves and generated output are not included in Git.

Rebuilt hash is identical to the previously installed, gameplay-tested binary recorded in project evidence. Production core unchanged.
