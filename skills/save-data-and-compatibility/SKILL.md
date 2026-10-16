---
name: save-data-and-compatibility
description: "Protect saves and manage mod compatibility."
version: 0.2.0
author: Hermes
license: MIT
---

# Save data and compatibility

Design mod changes around save safety, migration and rollback. Do not recover or modify saves without owner authority.

## Procedure
1. Locate saves through documented paths, copy to a disposable fixture set and record hashes; never operate on the only copy.
2. Identify schema/version markers, references, compression and external dependencies without guessing undocumented fields.
3. Define a versioned migration with preconditions, idempotence, bounded resource use, backup and failure restore. Prefer copy-on-write.
4. Test clean save, old save, current save, missing/extra fields, corrupt/truncated save and wrong-game/version fixtures.
5. Verify load, save, reload and downgrade/disable behaviour. Record whether a mod is save-breaking, save-affecting or save-neutral.
6. Rehearse restore from backup and verify the original hash. Document residual files and manual recovery steps.

## Verification
Migration passes only when successful output reloads, a second run is idempotent, malformed input fails closed, failure restores the original and rollback leaves the baseline usable. Never promise cross-version safety without a fixture.
