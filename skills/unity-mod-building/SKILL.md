---
name: unity-mod-building
description: "Build Unity game mods with BepInEx or MelonLoader, Harmony patches and IL2CPP interop."
version: 0.1.0
author: Hermes
license: MIT
---

# Unity mod building

## 1. Identify the backend (it decides everything)
- **Mono:** `<Game>_Data/Managed/Assembly-CSharp.dll` exists. Game logic is .NET IL, readable and patchable.
- **IL2CPP:** `GameAssembly.dll` plus `<Game>_Data/il2cpp_data/Metadata/global-metadata.dat`. Logic is native; mods go through generated interop.
- Record the Unity version (from `globalgamemanagers` or the player log) and the loader build that the game's community recommends for it.
- Saves, config and `Player.log` live in `%USERPROFILE%\AppData\LocalLow\<company>\<product>\`. Read `Player.log` first when anything fails.

## 2. Prefer the game's own API or community library
Many Unity games already have one (R2API, Jotunn, a game-specific Modding API on Thunderstore or Nexus). Build on it before raw patching.

## 3. Loader setup
- **BepInEx 5** for Mono: unzip into the game folder (adds the `winhttp.dll` Doorstop proxy), run once to generate `BepInEx/config`, plugins go in `BepInEx/plugins/`, log in `BepInEx/LogOutput.log`.
- **BepInEx 6** for IL2CPP: generates interop assemblies on first run (slow once).
- **MelonLoader:** alternative for Mono and IL2CPP; uses `version.dll` and a `Mods/` folder.
- Linux/Proton: `WINEDLLOVERRIDES="winhttp=n,b" %command%` (BepInEx) or `version=n,b` (MelonLoader).
- Tell the user which files were added to the game folder and how to remove them, or use a separate game copy or mod-manager profile.

## 4. Plugin skeleton (BepInEx 5, Mono)
```csharp
[BepInPlugin("author.mymod", "My Mod", "0.1.0")]
public class Plugin : BaseUnityPlugin {
    void Awake() { new Harmony("author.mymod").PatchAll(); Logger.LogInfo("My Mod loaded"); }
}
[HarmonyPatch(typeof(PlayerController), "Update")]
static class PlayerUpdatePatch {
    static void Postfix(PlayerController __instance) { /* change behaviour here */ }
}
```
- Reference `Assembly-CSharp.dll` and `UnityEngine*.dll` from `_Data/Managed` with `<Private>false</Private>`; target the game's framework (often `netstandard2.0` or `net472`).
- Make values configurable with `Config.Bind` so players can tune without rebuilding.

## 5. Harmony patch choice
- **Prefix:** runs before; returning `false` skips the original. Use sparingly; it breaks other mods patching the same method.
- **Postfix:** runs after; can change `__result`. The safest default.
- **Transpiler:** edits IL for surgical changes; pin the game build, and fail loudly if the expected IL pattern is missing.
- `AccessTools` reaches private members. Use a unique Harmony ID per mod.

## 6. IL2CPP specifics
- Read types with Cpp2IL or Il2CppDumper (`GameAssembly.dll` + `global-metadata.dat`), then browse dummy DLLs in ILSpy. Method bodies are native: name them in Ghidra with the generated scripts.
- Patch through the generated `Il2Cpp*` interop types. Register managed MonoBehaviours with `ClassInjector.RegisterTypeInIl2Cpp<T>()`.
- Expect stripping: unused methods and generic instantiations may not exist in the build.

## 7. Find the right object fast
UnityExplorer (a loader plugin) gives an in-game hierarchy, inspector and C# console. Use it to locate the GameObject, component and field, then write the patch.

## 8. Content
- New items or characters: clone an existing prefab with `Object.Instantiate`, swap mesh, material and stats.
- Own assets: AssetBundles built with the same Unity major version, or PNGs via `Texture2D.LoadImage`.
- Re-apply state on scene loads (`SceneManager.sceneLoaded`).

## 9. Proof
The plugin's load line in the loader log, the patched behaviour in a scripted scene, and a clean launch with the plugin removed. Multiplayer Unity games with EAC/BattlEye: no client mods.
