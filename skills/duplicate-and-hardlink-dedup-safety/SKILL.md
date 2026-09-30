---
name: "duplicate-and-hardlink-dedup-safety"
description: "Resolve duplicates and content-addressed stores by picking a canonical copy without breaking links, mounts or ownership boundaries."
license: "MIT"
---

# Duplicate and hardlink dedup safety

## When to use
Duplicate files are consuming space, or a dedup or hardlink-dedup tool is being considered.

## Procedure
1. Group candidates by content hash, and separately by similarity where the tool supports near-duplicates.
2. Inspect link counts before touching anything; a dedup tool that ignores hardlinks can corrupt data.
3. Choose the canonical copy by rule: tracked over untracked, primary tree over copy, older over newer only when identical.
4. Verify with a byte comparison, not a size comparison.
5. Execute via move or link, never in-place truncation.

## Decision rules
- Size equality is not content equality. Compare bytes.
- Hardlinked files are one object wearing several names; deleting a name is safe, editing is not.
- A duplicate on a store with no remote is not a duplicate you can delete freely.
- Never dedup across ownership boundaries without the owner's decision.

## Pitfalls
- Running an aggressive dedup tool on a live tree with hardlinks and symlinks.
- Deleting the copy that a backup job reads.
- Assuming a package cache is disposable while a pin depends on it.

## Done
Duplicates are grouped by verified content, canonical copies are chosen by a stated rule, and link counts are unchanged or intentionally reduced.
