---
name: "pre-deletion-backup-and-retention-proof"
description: "Prove an item is genuinely recoverable before removing it: backup exists, is consistent, and is restorable — not merely present."
license: "MIT"
---

# Pre deletion backup and retention proof

## When to use
Before any irreversible removal, and when auditing whether a backup claim is real.

## Procedure
1. Identify the backup that covers the item, its destination and its age.
2. Verify the backup is restorable, not just that a file exists: spot-check an integrity check or a test restore.
3. Confirm the retention window covers your audit horizon.
4. Confirm the backup is not superseded by a newer one that omitted the item.
5. Record the restore reference on the register row.

## Decision rules
- A backup you have never restored from is a hypothesis.
- Superseded backups that no longer contain the item do not protect it.
- If restore is untested, treat the item as unrecoverable and raise the confidence bar.
- Retention windows shorter than your horizon do not count.

## Decision-output clarification
Separate investigation candidates, proven restore references and removal authority. You may mention a snapshot as an unverified candidate for investigation; relevance, coverage, suitability, integrity and a test restore remain requirements before relying on it for removal. Saved complete proof can support a proposed register entry within that evidence scope without claiming you performed a live restore or wrote the register. Return the requested structured decision rather than a reasoning transcript.

Before returning a structured result, check that each field answers the requested proposition, uses the requested types and vocabulary, and agrees with the explanation. Saved evidence is not an action performed by you; a recommended next step is not an executed action.

## Pitfalls
- Counting snapshots as restorable without a test.
- Assuming a backup covers a path it was configured to exclude.
- Forgetting that a deleted-but-hardlinked file may still be reachable.

## Done
The register row carries a restore reference whose coverage, age and retention have been verified.
