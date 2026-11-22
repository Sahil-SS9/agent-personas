---
name: "scale-to-complexity-and-cost-before-fanout"
description: "Estimate task complexity and token cost before spawning workers; fan out only when the task pays for it."
license: "MIT"
---
# Scale to Complexity and Cost Before Fan-out

## Use when
- Deciding how many workers a task actually needs.
- Anyone proposes parallel agents for a task that might be one agent's job.
- A run's token spend needs a ceiling written before dispatch, not after.

## Instructions

1. Estimate first, spawn second: simple tasks → one worker with a handful of
   tool calls; medium → a few workers; broad or research-heavy → many. The
   lead estimates; the requester should never have to.
2. Multi-agent costs a large multiple of single-agent tokens. Fan out only
   when at least one of three holds:
   - a single context window would be polluted by the task's breadth;
   - the subtasks genuinely run in parallel;
   - specialisation improves tool choice or focus.
   If none holds, run single-agent and say so.
3. Write the budget line before the first dispatch: expected workers,
   expected steps each, expected token ceiling, and what you will do when the
   ceiling is hit (shrink width, drop depth, or stop and report).
4. Match worker count to the estimate, then hold it: widening mid-run needs a
   new budget line and a reason, not momentum.
5. Report spend against the estimate in the final status; variance explained,
   not discovered.

## Stop conditions
- Never fan out without a written budget estimate and a complexity reason.
- Never spawn ten workers on a simple case, and never compress a complex case
  to one worker to save tokens without recording the trade-off.

## Escalation
- When the budget ceiling is reached, stop starting new nodes and escalate:
   partial results, remaining graph, and the recommended cut — the owner
   decides whether the overrun is worth it.
