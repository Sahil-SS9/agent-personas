---
name: game-target-and-toolchain-routing
description: "Route game targets by engine and platform."
version: 0.1.0
author: Hermes
license: MIT
---

# Game target and toolchain routing

Identify a game’s engine, version, platform and supported extension model before selecting a modding method. This skill does not enable cheating, piracy or unauthorised tampering with live services.

## Procedure
1. Confirm ownership/permission, offline or private test scope and backup/rollback conditions.
2. Fingerprint engine and build using install metadata and read-only inspection: Unity/IL2CPP, Unreal, Bethesda-style data archives, Source-like mounts or a documented SDK.
3. Prefer official SDKs, documented plugin APIs and community tools with compatible licences.
4. Select the least invasive route: data mod, scripting/API mod, plugin, source build or controlled local instrumentation.
5. Record game version, platform, loader/runtime versions and dependencies; reject mismatched toolchains.
6. Build a minimal hello-world or no-op mod before changing gameplay behaviour.

## Verification
Return a routing matrix with target markers, selected route, version constraints, prohibited routes and rollback plan.
