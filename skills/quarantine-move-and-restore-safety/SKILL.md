---
name: "quarantine-move-and-restore-safety"
description: "Move suspect items to quarantine reversibly, and prove the restore path works before anything is finally removed."
license: "MIT"
---

# Quarantine move and restore safety

## When to use
Executing a cleanup that must stay reversible.

## Procedure
1. Move to a quarantine location on the same filesystem, so the move is atomic and cheap.
2. Preserve relative structure so restoration is mechanical.
3. Record a manifest: original path, quarantine path, hash, timestamp, reason.
4. Prove one restore end to end before trusting the mechanism.
5. Keep quarantine for a defined period; only then release space, with a second approval.

## Decision rules
- Cross-device moves are copies plus deletes; they are not reversible in one step. Say which you are doing.
- Restore must be testable without a disaster; test it on a sample first.
- Quarantine is not a bin: nothing leaves it automatically.
- Chain the quarantine location to its final target so the move cannot land somewhere unexpected.

## Pitfalls
- Moving across filesystems and assuming the operation is atomic.
- Quarantine on the same path being cleaned, so it is swept in the next pass.
- No manifest, so restoration depends on memory.

## Done
Quarantine holds the items with a manifest, a restore has been demonstrated, and the release is gated on a second approval.
