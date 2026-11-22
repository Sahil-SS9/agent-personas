---
name: "context-and-token-budgeting-across-workers"
description: "Give each worker a fresh window and a retrieval budget; keep a dispatch-level ledger of expected versus spent."
license: "MIT"
---
# Context and Token Budgeting Across Workers

## Use when
- Spawning or briefing workers for a multi-agent run.
- A run's token spend needs to be knowable while it is still running.
- Worker outputs read as if they inherited the lead's whole conversation.

## Instructions

1. Fresh window per worker: a worker's context starts from its node brief
   plus the shared slice it was given — never from the lead's history.
   Context pollution is the first failure mode of multi-agent work.
2. Retrieval budget: a worker may request more shared context, up to a small
   fixed number of cycles, before committing to an answer. State the cycle
   cap in the brief; three covers most cases while bounding cost.
3. Ledger before dispatch: per run, record per worker the expected step count
   and token envelope. Update it at fan-in with what was actually spent.
4. Budgeting here is a dispatch decision — what to load, what to spawn, what
   to cap. Prompt-level token discipline inside one agent belongs to the
   prompt and loop skills, not this one.
5. Treat total tokens as the outcome variable: run-to-run result variance in
   multi-agent work is driven largely by total tokens spent; measure it per
   run rather than assuming the model is the only lever.
6. Shed load by design, not by crash: when the envelope tightens, drop depth
   first, then width; never silently truncate a worker's context to fit.

## Stop conditions
- Never inherit the lead's conversation into a worker window.
- Never dispatch without a ledger entry for the node.
- Never silently truncate required context to stay in budget — halt and
  escalate instead.

## Escalation
- If the ledger shows the run will exceed its envelope, stop spawning and
  bring the owner the spend-so-far, the remaining graph, and the cut you
  recommend.
