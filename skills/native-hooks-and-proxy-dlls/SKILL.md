---
name: native-hooks-and-proxy-dlls
description: "Mod native C/C++ games with no loader: proxy DLLs, signature scans, function hooks and in-game overlays."
version: 0.1.0
author: Hermes
license: MIT
---

# Native hooks and proxy DLLs

The most work, and only for single-player, offline or user-run servers. Never on anti-cheat-protected games, and never past DRM or ownership checks.

## 1. Get code into the process
- **Proxy DLL:** a DLL named like one the game loads from its own folder (`version.dll`, `dinput8.dll`, `winmm.dll`, `dxgi.dll`, `xinput1_3.dll`). Check the game's imports first (dumpbin or PE-bear). Forward every real export; in `DllMain` only start a thread, because the loader lock is held.
- **Ultimate ASI Loader** loads `*.asi` plugins and is already used by many older games.
- Prefer an existing script extender or community framework when one exists.
- Linux/Proton: `WINEDLLOVERRIDES="dinput8=n,b" %command%`.
- Tell the user exactly which files were added and how to remove them.

## 2. Find what to hook
- **Static:** Ghidra or IDA (an agent can drive them over a localhost-only MCP bridge). Start from strings, log messages and imports, follow cross-references to the function you need, and record names in MODLOG.md.
- **Dynamic:** Cheat Engine value scans to find what writes health, ammo or position, then walk back to the struct; x64dbg for breakpoints; ReClass.NET for live struct layout. Close protected games first.
- **Signatures, not addresses:** find functions by byte-pattern scan with wildcards at startup so the mod survives updates; log clearly when a pattern is missing and disable the feature instead of crashing.

## 3. Hook
- MinHook, SafetyHook or Detours; call the original through the trampoline. Match the calling convention exactly (x86 needs `__thiscall`/`__stdcall` care).
- Mid-function hooks change registers at one instruction.
- Keep hooks tiny; do heavy work on your own thread, and queue anything that touches game state onto the game's main thread from a per-frame hook.

## 4. Draw and interact
- Overlays: hook `Present` (D3D11/12) or `vkQueuePresentKHR` and render Dear ImGui, or use the ReShade addon API.
- Drawing inside the game's 3D pass: take the view-projection matrix and depth buffer the game already uses (find them with RenderDoc).

## 5. Stability
- Compute addresses from the module base at runtime (ASLR).
- Log to a flushed file; install a crash handler that writes a minidump.
- Pin and document the supported game build.

## 6. Proof
The hook's log line, the changed behaviour in a repeatable scene, a clean run after removing the proxy, and no crash over a defined play session.
