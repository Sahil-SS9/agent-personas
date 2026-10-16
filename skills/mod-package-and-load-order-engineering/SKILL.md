---
name: mod-package-and-load-order-engineering
description: "Build reproducible mods with dependencies and load order."
version: 0.1.0
author: Hermes
license: MIT
---

# Mod package and load-order engineering

Package a mod so its files, dependencies, load order and conflicts are explicit. This skill does not distribute copyrighted game assets or conceal incompatible changes.

## Procedure
1. Keep source, generated output, metadata and user configuration separate.
2. Declare game/engine/loader versions, dependencies, load order, conflicts, permissions and install/uninstall paths.
3. Prefer patching or extension points over replacing original assets. Never overwrite a user file without a backup and a manifest.
4. Build deterministic archives from a clean tree; record hashes and generated-file inputs.
5. Test absent dependencies, reordered dependencies, duplicate files, uninstall and upgrade paths.
6. Document provenance and licence obligations for every bundled asset or library.

## Verification
A package passes only if clean install, upgrade, uninstall and conflict checks reproduce from the manifest.
