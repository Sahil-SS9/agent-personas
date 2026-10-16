---
name: mod-test-and-rollback
description: "Test mods with controls and reversible rollback."
version: 0.1.0
author: Hermes
license: MIT
---

# Mod test and rollback

Qualify a mod with isolated fixtures, regression checks and a proven rollback. This skill does not treat “the game launched” as sufficient validation.

## Procedure
1. Freeze a clean baseline and capture a no-op control with the same loader.
2. Test install, first launch, target behaviour, unrelated gameplay, performance, logs, save lifecycle and uninstall.
3. Exercise missing dependencies, conflicts, version mismatch, malformed configuration and interrupted install.
4. Compare deterministic outputs where possible; record flaky observations separately.
5. Restore the baseline snapshot and prove the game launches without the mod and without residual files.
6. Publish a concise compatibility report with known risks and reproduction steps.

## Verification
Rollback passes only when the baseline hash/manifest and clean launch are restored after both successful and failed installation paths.
