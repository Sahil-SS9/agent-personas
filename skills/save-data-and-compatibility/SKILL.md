---
name: save-data-and-compatibility
description: "Protect saves and manage mod compatibility."
version: 0.1.0
author: Hermes
license: MIT
---

# Save data and compatibility

Design mod changes around save safety, migration and rollback. This skill does not recover or modify saves without owner authority.

## Procedure
1. Locate saves through documented paths, copy them to a disposable fixture set and record hashes.
2. Define schema/version changes, stable identifiers, defaults, migration order and failure handling.
3. Test new save, old save, missing mod, disabled mod, downgrade and interrupted migration.
4. Preserve unknown fields where the format permits; never silently discard data.
5. Make migrations idempotent and write a new file before replacing the original.
6. Document incompatible versions and the exact recovery path.

## Verification
The matrix must show load/save results for every supported transition and prove the original fixture remains unchanged.
