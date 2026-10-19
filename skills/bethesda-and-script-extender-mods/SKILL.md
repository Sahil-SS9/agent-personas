---
name: bethesda-and-script-extender-mods
description: "Build Bethesda Creation Engine mods: ESP/ESL plugins, Papyrus, script-extender plugins and load order."
version: 0.1.0
author: Hermes
license: MIT
---

# Bethesda and script-extender mods

Covers Skyrim SE/AE, Fallout 3/NV/4, Oblivion and Starfield. Fallout 76 is online-only: no client mods.

## 1. Identify and isolate
- `Data/*.esm` plus `.bsa`/`.ba2` archives beside the game exe. Saves and INIs live in `Documents/My Games/<Game>/`.
- Record the exact runtime (for Skyrim: SE 1.5.97 versus AE 1.6.x/1.7.x). Script-extender plugins are runtime-specific.
- Use Mod Organizer 2 with a dedicated instance and a profile per experiment. Its virtual file system leaves `Data/` untouched. Download mod managers only from official pages.

## 2. Pick the lightest layer
1. **Plugin records (ESP/ESM/ESL):** weapons, armour, NPCs, leveled lists, quests, cells. Edit in xEdit (scriptable) or the Creation Kit. Plugins are structured records, so generating them from scripts is reliable and reviewable. ESL-flag small plugins to save load-order slots.
2. **Papyrus scripts** (`.psc` compiled to `.pex`): event-driven logic attached to records. Compile with the Creation Kit's compiler.
3. **Script-extender native plugin** when Papyrus cannot do it: new functions, hooks, UI, physics, rendering.
   - SKSE64 / F4SE / xNVSE / OBSE / SFSE, built in C++ with CommonLibSSE-NG (Skyrim) or CommonLibF4.
   - Use Address Library IDs instead of raw addresses so the plugin survives patches.
   - Plugins go in `Data/SKSE/Plugins/*.dll`; logs in `Documents/My Games/<Game>/SKSE/`.
4. **Assets:** NIF meshes (NifSkope, Blender with PyNifly), DDS textures (BC1/BC3/BC7), BSA/BA2 packing (BSArch, Archive2). Reuse existing Havok behaviours rather than authoring new ones.

## 3. Load order and conflicts
- Sort with LOOT, then check conflicts in xEdit (overridden records shown in red). Decide winners deliberately and write a small patch plugin for the merge instead of relying on "whatever loads last".
- Know the master list, including Creation Club and Anniversary content, before declaring masters.

## 4. Out-of-process pattern
A thin script-extender plugin that captures game events and calls a heavier process over localhost (file drop, HTTP or shared memory) is how AI-NPC mods and cross-game mashups are built here. Keep the in-game side small and crash-safe.

## 5. Proof
- Plugin: the record visible in game (spawn command or test cell), xEdit showing no unintended overrides.
- Script extender: its log line and the hooked effect, on the recorded runtime.
- Removal: test on a throwaway save; removing scripted mods mid-save can corrupt it, so document safe removal.

## 6. Hard stops
No redistribution of game files or Creation Club content; no edits to the game exe; no mods for online-only titles.
