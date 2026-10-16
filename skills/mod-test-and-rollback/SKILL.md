---
name: mod-test-and-rollback
description: "Test mods with controls and reversible rollback."
version: 0.2.0
author: Hermes
license: MIT
---

# Mod test and rollback

Qualify a mod with isolated fixtures, regression checks and a proven rollback. A launch is not sufficient validation.

## Procedure
1. Freeze a clean baseline, save/config backup and no-op control. Hash each artefact.
2. Test install, first launch, target behaviour, unrelated control behaviour, reload, upgrade, disable and uninstall.
3. Exercise missing dependency, wrong version, load-order conflict, corrupted config and crash recovery in a disposable copy.
4. Capture logs and exit status; distinguish mod errors, loader errors, game errors and environmental failures.
5. Execute rollback from the documented manifest, restore saves/config and verify hashes plus a clean launch.
6. Repeat rollback once from a fresh fixture. Record data loss, residual files and unsupported cases.

## Acceptance
Normal and negative controls produce expected outcomes; no save is modified outside scope; uninstall leaves the baseline; rollback restores the pre-test hash set; known failures are documented with repro fixtures.
