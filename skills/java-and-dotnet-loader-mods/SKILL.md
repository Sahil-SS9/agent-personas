---
name: java-and-dotnet-loader-mods
description: "Build mods on established loaders: Minecraft Fabric/NeoForge, tModLoader, SMAPI, Everest, Godot, Geode, REFramework."
version: 0.1.0
author: Hermes
license: MIT
---

# Java and .NET loader mods

These ecosystems have mature loaders with real APIs and dev clients. Use the API before any patching.

## Minecraft Java
- **Fabric** (light, fast to update; Mixin for bytecode patches) or **NeoForge** (larger API: capabilities, events). Match game version, loader version and API version exactly.
- Scaffold from the official template; build with `./gradlew build`; the jar goes in `mods/`.
- `./gradlew runClient` starts a dev client with your mod: the best oracle (log in `run/logs/latest.log`). GameTests on the test server give automated checks.
- Register items, blocks, entities and sounds through registries. Assets under `assets/<modid>/` (16x16 PNG textures, JSON models, lang, `sounds.json` + ogg); data (recipes, loot tables, tags) under `data/<modid>/`.
- Server-side plugins (Paper) plus resource packs change a lot without any client mod.
- Bedrock: behaviour packs (JSON plus the Script API) and resource packs, with the content log on.

## Terraria (tModLoader)
- tModLoader is a free Steam app; it must be in the user's library. Never patch that check.
- Mods are C# in `ModSources/<Mod>/`: `ModItem`, `ModProjectile`, `ModNPC`, `ModPlayer`, `ModSystem`, `GlobalItem`/`GlobalNPC`, and `ModCommand` for test commands.
- Art is PNG beside the class; NPC sheets are vertical strips (frame height = texture height / frame count).
- Isolate test saves with `-tmlsavedirectory`; logs in `tModLoader-Logs/client.log`.

## Stardew Valley (SMAPI)
- Content changes (sprites, dialogue, maps, data): Content Patcher JSON packs. Code: SMAPI C# mods (`ModEntry`, game-loop events, content API) with Harmony where needed. The ModBuildConfig NuGet package finds the game and deploys.

## Celeste (Everest), Godot, Geometry Dash, RE Engine
- Celeste: Everest via Olympus; MonoMod hooks; maps in Lönn.
- Godot games: godot-mod-loader for GDScript games; check whether the export is GDScript or C# first.
- Geometry Dash: Geode SDK mods (C++), distributed through Geode's index.
- RE Engine (Resident Evil, Monster Hunter, Dragon's Dogma 2): REFramework Lua scripts and plugins.

## Common practice
- Read the game before patching: ILSpy/ilspycmd for .NET, Loom `genSources` or Vineflower for Java. Keep decompiled output outside the repo and never ship it.
- Make tunables configurable. Keep multiplayer sync in mind: on tModLoader, `side = Both` mods sync; elsewhere assume single-player unless every client runs the mod.

## Proof
Dev client or game log shows the mod loading; a test command or GameTest exercises the feature; the game runs cleanly with the mod removed.
