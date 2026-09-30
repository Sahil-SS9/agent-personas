---
name: "storage-pressure-and-reclaim-forensics"
description: "Find where space actually went when usage is unexplained — with a 100% certainty bar, not an estimate."
license: "MIT"
---

# Storage pressure and reclaim forensics

## When to use
Reported usage exceeds the sum of visible files, or a reclaim claim must be provable.

## Procedure
1. Compare apparent against allocated size across the tree; account for sparse files and block padding.
2. Audit deleted-but-open files, which hold space invisibly.
3. Audit symlink-blind traversal, which can hide a large tree entirely.
4. Audit snapshots, container layers, and filesystem-level reservations.
5. Iterate until the accounting closes, then state the residual if it does not.

## Decision rules
- Unaccounted space is a finding, not an error margin. Chase it.
- Claim only what you can attribute; a percentage estimate is not an audit.
- Independent verification of a large reclaim claim is mandatory before reporting it.
- If the accounting does not close, report the gap and its size rather than rounding it away.

## Decision-output clarification
Build a non-overlapping accounting ledger before summing. A sparse file within the visible tree is already represented by visible allocated size; its individual allocation is diagnostic, not another disjoint top-level category. If containment is unknown, report that uncertainty rather than assuming either inclusion or independence. Never add apparent size to allocated usage.

Before returning a structured result, check that each field answers the requested proposition, uses the requested types and vocabulary, and agrees with the explanation. Saved evidence is not an action performed by you; a recommended next step is not an executed action.

## Pitfalls
- Concluding that a size difference is a reporting bug.
- Missing a subtree hidden behind a symlink, which can conceal hundreds of gigabytes.
- Reporting a reclaim figure from an estimate instead of an audited total.

## Done
Usage is reconciled against attributable items to the extent possible, with any residual gap stated and its cause hypothesised.
