---
name: "filesystem-inventory-and-provenance"
description: "Build an inventory where every file carries its provenance: size, allocated blocks, inode and link count, owner, all four timestamps, git state, and chain of custody."
license: "MIT"
---

# Filesystem inventory and provenance

## When to use
Before any cleanup, and whenever storage questions arise.

## Procedure
1. Enumerate with allocated size as well as apparent size; they diverge on sparse files and block-padded stores.
2. Capture all four timestamps (birth, change, modify, access) and say which the filesystem actually supports.
3. Record inode and link count so hardlink relationships are visible.
4. Record ownership and permissions, including cross-user ownership.
5. Record git state per path: tracked, ignored, untracked, inside a registered worktree.

## Decision rules
- A file with no provenance is UNATTRIBUTED, not junk. Absence of a creator is not evidence of no owner.
- Birth time is unavailable on some filesystems; report the gap rather than substituting modify time silently.
- Apparent size is not reclaimable space. Use allocated size for any reclaim claim.
- Personal-file judgement requires personal-file evidence; do not guess intent from a path.

## Decision-output clarification
Scenario or report provenance describes the evidence source, not the creator of the inventoried file. Without item-level creator or chain-of-custody evidence, the file remains UNATTRIBUTED even if the report itself has a known origin.

Before returning a structured result, check that each field answers the requested proposition, uses the requested types and vocabulary, and agrees with the explanation. Saved evidence is not an action performed by you; a recommended next step is not an executed action.

## Pitfalls
- Trusting a plain recursive size tool, which can be blind to symlinked trees and badly undercount.
- Using modify time as creation evidence after a copy or restore.
- Missing that a path is inside a live git worktree.

## Done
The inventory covers the target tree with provenance per item, and every unsupported field is stated rather than guessed.
