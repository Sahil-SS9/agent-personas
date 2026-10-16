---
name: game-target-and-toolchain-routing
description: "Route game targets by engine and platform."
version: 0.2.0
author: Hermes
license: MIT
---

# Game target and toolchain routing

Identify engine, version, platform and supported extension model before selecting a modding method. No cheating, piracy, DRM/anti-cheat bypass or unauthorised live-service tampering.

## Procedure
1. Confirm ownership/permission, offline or private test scope, data backup and rollback authority.
2. Fingerprint from read-only install metadata and documented files: Unity Mono/IL2CPP, Unreal, Bethesda/archive, Source-like mounts, or a documented SDK. Record build and loader versions.
3. Prefer official APIs/SDKs and community tools with compatible licences. Reject mismatched or unmaintained toolchains.
4. Choose the least invasive route: data patch, documented script/API, plugin, source build or bounded local instrumentation.
5. Declare dependencies, supported versions, platform differences, prohibited routes and expected failure modes.
6. Build a no-op/hello-world mod and prove load/unload before changing behaviour.

## Routing matrix
Target markers; engine/runtime; loader; selected route and why; tool/version/licence; fixture; authority; compatibility risk; rollback command; escalation. Stop if fingerprint is ambiguous or the route requires bypassing a protection.
