---
name: "unused-orphan-and-load-bearing-confirmation"
description: "Classify a candidate as unused or orphan only after proving nothing load-bearing depends on it — the reverse burden of proof."
license: "MIT"
---

# Unused orphan and load bearing confirmation

## When to use
A file or directory looks abandoned and is being considered for removal.

## Procedure
1. Search for references: imports, config includes, cron and systemd units, scripts, lockfiles, CI definitions, and sibling repositories.
2. Check whether it is held open by a running process, mounted, or inside a registered worktree.
3. Check whether a service reads config from it at start.
4. Check the reference is not dynamic (path assembled at runtime, glob, environment-derived).
5. Only then classify ORPHAN or UNUSED, with the negative search recorded.

## Decision rules
- Absence of a reference in the obvious places is not absence of a reference. Record where you looked.
- A zero-reference verdict on a live system is a claim requiring a second method before it counts.
- Anything reachable from an ExecStart, cron entry, or import path is LIVE regardless of appearance.
- If you cannot search exhaustively, downgrade the confidence, not the file.

## Pitfalls
- Declaring a directory unused because nothing in its own tree references it.
- Missing a dependency from a sibling repository or a container build context.
- Overlooking an open file descriptor holding deleted-but-live data.

## Done
Each classification carries the searches performed and the method, and anything unsearchable is downgraded rather than deleted.
