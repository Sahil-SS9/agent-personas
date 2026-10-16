---
name: mod-package-and-load-order-engineering
description: "Build reproducible mods with dependencies and load order."
version: 0.2.0
author: Hermes
license: MIT
---

# Mod package and load-order engineering

Package a mod so files, dependencies, load order and conflicts are explicit. Do not redistribute copyrighted game assets or conceal incompatible changes.

## Manifest
Declare game/engine/loader versions, dependency IDs and ranges, conflicts, load-after/load-before rules, permissions, install/uninstall paths, generated files and licence/provenance for every bundled item. Separate source, generated output and user config.

## Procedure
1. Prefer extension points or patches over replacing original files; back up any user file and emit a manifest.
2. Build deterministic archives from a clean tree; record tool versions, inputs and output hashes.
3. Validate missing dependency, incompatible version, cycle, duplicate path, case collision, load-order conflict, upgrade and uninstall fixtures.
4. Test both a clean install and an existing installation with an explicit conflict resolution.
5. Verify the package contains no credentials, unapproved assets or build-machine paths.
6. Document how to disable, remove and restore the mod without deleting saves.

## Verification
A package passes only when clean install, upgrade, uninstall, conflict resolution and reproducible rebuild agree with the manifest. “The loader accepted it” is insufficient.
