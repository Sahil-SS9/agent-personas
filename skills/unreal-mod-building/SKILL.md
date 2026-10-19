---
name: unreal-mod-building
description: "Build Unreal Engine 4/5 mods with UE4SS Lua or C++, pak/IoStore packaging and blueprint mods."
version: 0.1.0
author: Hermes
license: MIT
---

# Unreal mod building

## 1. Identify
- `<Project>/Binaries/Win64/<Project>-Win64-Shipping.exe` and `<Project>/Content/Paks/`.
- UE 4.26+ and UE5 usually store assets in IoStore `.utoc`/`.ucas` beside a small `.pak`.
- Record the exact engine version (the exe contains a `++UE4+Release-4.x` or `++UE5+Release-5.x` string). Paks cooked for the wrong version crash on mount.
- Saves: `%LOCALAPPDATA%\<Project>\Saved\SaveGames`. Many tweaks are config-only (`Saved\Config\Windows\Engine.ini`, `[SystemSettings]`): try that first.

## 2. Route A: UE4SS scripting (no engine rebuild)
- Install RE-UE4SS from its official releases next to the shipping exe (a proxy DLL plus the `ue4ss/` folder). Check the game's compatibility notes; some forks need config overrides.
- **Lua mods:** `ue4ss/Mods/<Mod>/Scripts/main.lua`, enabled in `mods.txt`.
  - `RegisterHook("/Script/Engine.PlayerController:ClientRestart", fn)` to run on engine events.
  - `NotifyOnNewObject`, `FindFirstOf("PlayerCharacter")`, read/write UProperties, call UFunctions.
  - Use `ExecuteInGameThread` for anything that touches the world.
- **C++ mods** for heavy work, from the UE4SS C++ template.
- **Live View** and the SDK/header dump find the class, property and function names you need. Read the bundled example mods first.

## 3. Route B: pak mods (assets and blueprints)
- Browse with FModel (needs the right engine version, and the AES key when paks are encrypted; use keys the community already publishes for single-player games you own, and never for online anti-tamper).
- Edit `.uasset` with UAssetGUI/UAssetAPI (JSON round trip), or cook replacements in an editor of the same engine version with matching project name and `/Game/...` paths.
- Pack with repak (pak) or retoc (IoStore). Name the file `*_P.pak` so it overrides originals and place it in `Content/Paks/~mods/`.
- New meshes, materials or blueprints: cook in the matching editor and pak only your cooked files.
- **Blueprint logic mods:** UE4SS loads `LogicMods` paks from `Content/Paks/LogicMods`.

## 4. Route C: VR, camera and engine tweaks
UEVR adds stereo VR to many UE4/UE5 games with per-game profiles. Console unlockers or UE4SS enable `r.*` cvars, freecam and slow motion for showcase shots.

## 5. Reading the game
UE4SS dump or Dumper-7 for class/property/function names and offsets; Ghidra on the shipping exe for native gameplay code, naming engine functions against Unreal source.

## 6. Proof
- UE4SS: the mod's log line in `UE4SS.log` and the hooked effect in a scripted scene.
- Pak: the asset visibly replaced in game, mount messages clean, and the game launching cleanly once the pak is removed.
- Note which game build was tested; blueprint and AOB-based mods break on updates.

## 7. Hard stops
EAC/BattlEye titles and online play: no client mods. Pak signature checks that protect online play: never bypass. If a mod only works by defeating a protection, drop the route.
