---
name: "workstream-orchestration"
description: "Plan and steer multiple agent workstreams with WIP limits and review gates."
license: "MIT"
---
# Workstream Orchestration

## Use when
- Coordinating several agents/streams toward one outcome
- Work keeps colliding (same files, conflicting assumptions)
- Progress reporting has become guesswork

## Instructions

1. Decompose by INTERFACES, not by job title: each stream owns files/paths/
   contracts nobody else touches; shared seams get an owner before work
   starts.
2. Sequence with a dependency line, not a gantt: what blocks what, minimum
   parallel width, and the integration checkpoint where streams reconcile.
3. Split streams only on evidence: start with one; add a stream when a
   clear modularity or safety boundary exists (premature parallelism buys
   coordination cost without throughput). Design each seam (tool/model/
   prompt/brief boundary) as a substitution point.
4. Run review gates between phases: output of each stream is verified
   against its brief before dependent streams consume it (two-stage pattern).
5. Steer drift, kill overrun: when a stream drifts while still running at
   normal speed, course-correct mid-run with a specific message; full
   re-dispatch is the last resort. A worker past roughly twice its siblings'
   median runtime is overrunning, not drifting — the kill rule in
   failure-replanning-and-escalation governs it, not steering.
6. Status = evidence: report per stream as done/in-progress/blocked WITH the
   artifact or blocker attached; no vibe-based percentages.

## Stop conditions
- Never let two unowned streams write to the same seam.
- Never report a stream complete without its verification artifact.

## Escalation
- Cross-stream conflicts escalate to the human owner with both briefs and
  the collision evidence — not resolved silently by either agent.

## Wrap-up reserve
- Before starting another task, reserve enough of the remaining time/turn budget to
  collect evidence and hand the work over. The reserve is part of the budget, not spare.
- With a constrained budget, decline the extra task and return: completed work with its
  evidence, unfinished work, the blocker, and the next owner who can pick it up.
- With ample budget, do not stop early; the reserve is a floor for handover, not a reason
  to idle. This is an operating rule for steering, not a scheduler to build.
