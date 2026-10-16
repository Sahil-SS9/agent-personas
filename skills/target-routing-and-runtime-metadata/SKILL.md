---
name: target-routing-and-runtime-metadata
description: "Route targets by runtime metadata before decompilation."
version: 0.1.0
author: Hermes
license: MIT
---

# Target routing and runtime metadata

Identify the target family before choosing an analysis tool. This skill does not claim that metadata proves behaviour; it uses metadata to select the next evidence-producing method.

## Procedure
1. Preserve the original and record hash, architecture, format, runtime and build identifiers.
2. Fingerprint without execution: PE/ELF/Mach-O, APK/AAB, WebAssembly, .NET/Mono, Electron/asar, Unity/IL2CPP, Unreal, Go or Rust metadata.
3. Record what metadata is authoritative enough to guide analysis: exports, debug symbols, source maps, manifests, reflection data, generated registration tables and version information.
4. Choose the narrowest compatible toolchain. Record tool and version; do not silently substitute a decompiler that changes the evidence class.
5. Feed recovered names and boundaries back into the static model, then verify one sample against bytes or controlled runtime behaviour.
6. Stop and report unknowns when the target is packed, encrypted, managed by an unsupported runtime, or outside authorised scope.

## Boundaries
Metadata is a routing signal, not proof of intent, safety or source equivalence. Do not bypass licensing, access controls, anti-cheat or platform protections without explicit authority.

## Verification
Return a target matrix: target family, observed markers, selected method, rejected methods and the evidence ceiling.
