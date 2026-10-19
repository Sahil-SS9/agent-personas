---
name: mod-idea-to-route
description: "Turn a game-mod idea into a recon-backed build plan and the cheapest route that delivers it."
version: 0.1.0
author: Hermes
license: MIT
---

# Mod idea to route

Start every mod here. The goal is a written plan that names the game build, the route, what "done" means and how it will be proved, before any code.

## 1. Intake (five answers, one sentence each)
- Game, store and platform; who owns it.
- The idea, e.g. "a homing missile launcher and a nuke that craters the world".
- Online or offline. Online, competitive or anti-cheat-protected clients are out of scope: offer official tools, an offline mode or a server the user runs.
- What "done" means: working in the real game, plus the proof (a log line, a scripted scene, a screenshot, a short clip).
- The user's asset preference (local tools, paid services, or both) if the idea needs new art, models or sound.

Start a `MODLOG.md` journal now: versions, paths, IDs, routes tried, failures and why. Anything not written down is lost when context is compacted.

## 2. Recon before choosing anything
- Identify engine and runtime from install files without modifying them: `UnityPlayer.dll` plus `GameAssembly.dll` (IL2CPP) or `Managed/Assembly-CSharp.dll` (Mono); `*-Win64-Shipping.exe` plus `Content/Paks` (Unreal); `Data/*.esm` with BSA/BA2 (Bethesda); a managed .NET exe with XNA/FNA/MonoGame (Terraria, Stardew, Celeste); `.pck` (Godot); Java jars (Minecraft).
- Record exact game build, engine version and any installed loader. Loaders are version-locked.
- Find anti-cheat (EAC, BattlEye, Vanguard, Ricochet, ACE, VAC on official servers) and the save and config folders.
- Search the community as it is today: the game's modding wiki, Nexus, Thunderstore, mod.io, Workshop, GitHub. If a community loader or API exists, use it. Install from the official release page only; look-alike repos with download buttons are a known malware channel.

## 3. Pick the cheapest route that reaches the idea
| Route | Use when | Examples |
|---|---|---|
| Data or assets only | the idea fits the game's data files | Bethesda ESP/ESL records, Paradox scripts, JSON content packs, pak overrides |
| Loader API | a loader exposes the hook you need | tModLoader, SMAPI, BepInEx, MelonLoader, UE4SS Lua, REFramework Lua, SKSE, Fabric/NeoForge, Geode, godot-mod-loader |
| Managed-code patching | .NET/Mono/IL2CPP/Java with no API for the idea | Harmony/HarmonyX prefix, postfix, transpiler; MonoMod; Mixin |
| Native hooks | C/C++ engine with no loader | proxy DLL plus MinHook/SafetyHook and signature scans |
| Reimplementation, decomp or recomp | total control or retro targets | matching decomps, static recompilations that read the user's own files |
| Mashup | two games at once | see `mashup-and-cross-game-bridges` |

Write the chosen route and the reason into MODLOG.md. Name the next-cheapest route as the fallback.

## 4. Plan the first vertical slice
One item, unit or mechanic, end to end, with placeholder art. Name its oracle up front (see `mod-oracles-and-in-game-verification`). Widen only after the slice is proved in the real game.

## 5. Stop and ask when
- the route needs DRM, ownership-check or anti-cheat bypass (stop; it is out of scope);
- the build fingerprint is ambiguous;
- installing a loader into the game folder, changing the registry or spending money is next (ask first).

## Done
A MODLOG entry with game build, engine/runtime, loader and versions, anti-cheat status, save paths, route plus fallback, slice definition, its oracle and the user's asset preference.
