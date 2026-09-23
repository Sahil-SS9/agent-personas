---
name: "architecture-decision-records"
description: "Capture each irreversible decision as a superseding ADR."
license: "MIT"
---

# Architecture decision records (ADRs)

Make the costly, hard-to-reverse decisions durable and reviewable.

## When to use
Whenever a decision is costly or irreversible to change, or forms shared understanding the team will rely on.

## ADR shape (one decision per record)
- Title + status (proposed / accepted / superseded).
- Context: the forces, constraints and driving characteristics at play.
- Options considered: at least the two strongest, with their trade.
- Decision: what was chosen.
- Consequences: what becomes easier and what becomes harder.

## Decision rules
- One decision per record; never edit an accepted ADR — write a new one that supersedes it.
- Only record architectural decisions (costly/irreversible/shared). Cheap-to-reverse choices stay in code, not in the ADR log.
- Link each ADR to the driving characteristic(s) it serves so future readers see why.

## Pitfalls
- ADRs written after the fact as decoration, with no real options weighed.
- Editing history instead of superseding, so the reasoning trail is lost.

## Done
Every irreversible decision has an ADR with context, weighed options, decision and consequences; superseded ones retained.
