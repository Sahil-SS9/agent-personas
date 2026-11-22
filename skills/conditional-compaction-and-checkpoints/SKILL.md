---
name: "conditional-compaction-and-checkpoints"
description: "Compact against constraints and verify checkpoints."
license: "MIT"
---
# Conditional Compaction and Checkpoints

## Use when
- A session is approaching the working budget or the model is degrading.
- Someone proposes "summarise the conversation" by default.
- A long-horizon task needs to survive beyond one window.

## Instructions

1. Name the constraint before compacting. Compaction is justified by one of
   three measured constraints, not habit: the context does not fit the
   working budget; cached-input economics stop favouring resending; or
   quality measurably degrades. No named constraint, no compaction.
2. Diagnose the failure first, because compaction is not one fix:
   - distraction (too much irrelevant material) — compaction helps;
   - poisoning (bad instructions or wrong facts riding along) — compaction
     can launder or amplify the instructions; quarantine or correct first and
     verify authority boundaries after summarisation;
   - overflow — clear, externalise, or isolate before you summarise.
3. Checkpoint into a verified artifact: at a fixed point, compress the
   working state into a written artifact (progress, decisions, open items,
   pointers), verify it carries what matters, and restart from it in a
   fresh window. The artifact is auditable; a summary nobody checked is
   a guess.
4. Probe what survives: after any compaction, test that the load-bearing
   facts survived — task statement, constraints, decisions, open items.
   What the summary dropped is a defect list, not a mystery.
5. Restart from the artifact, not from the truncated tail: a session that
   limps to the window limit has spent its most important turns in the
   low-recall zone; the checkpoint pattern fails smaller and earlier.
6. Replace the default prompt when your needs differ: what the compactor
   preserves should be specified per workload — the default preserves the
   average task's priorities, not yours.

## Stop conditions
- Never compact without a named constraint.
- Never accept a compaction whose survival you did not probe.
- Never let poisoned content ride through compaction unflagged.

## Escalation
- Sessions that need repeated compaction escalate as an architecture
  finding: the durable state belongs outside the window (memory tiers), not
  in an ever-shortening summary.
