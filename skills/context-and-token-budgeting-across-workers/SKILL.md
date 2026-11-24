---
name: "context-and-token-budgeting-across-workers"
description: "Use when planning what each sub-agent or worker receives: context and token budgets per worker, size caps, and hand-offs as files or artefact references instead of copied chat history."
license: "MIT"
---

# Context and token budgeting across workers

Step 3. A worker that sees too little guesses; one that sees too much drowns or overflows. Budget both, per worker.

## Use when
- Writing briefs and inputs for any multi-worker plan; when a worker overruns its context or token budget.

## DO NOT use when
- Single-agent work that fits comfortably in one context.

Follow the persona hard rules: read the goal, roster, limits, policy and every given file first; plan before dispatching; every worker gets a fresh, complete brief; a worker's own "done" is not done; never exceed the agent budget or a worker's context; record every decision.

## Procedure
1. **Per worker, list what it must see:** its brief, the input artefacts it consumes, the tools it needs. Nothing else.
2. **Size it:** tokens for its tasks plus every input's output size. Keep it under the context limit with room for the work itself.
3. **Pass references, not copies:** workers write outputs to files and hand back a path and a short summary; the coordinator does not relay full outputs (each relay loses information and costs tokens).
4. **Set a budget per dispatch:** time and tokens, written in the brief, so overruns are visible (failure-replanning-and-escalation acts on them).
5. **Persist the plan to a file** so the coordinator can recover it when its own context is compacted.
6. **Record a budget ledger:** planned vs spent per worker; report totals with the result.

## Worked example
Three researchers each return 12k-token reports; the writer's context is 32k. Passing all three in full (36k) overflows. Each researcher also writes a 1.5k-token findings summary with source paths; the writer gets the three summaries (4.5k) plus the paths, and opens a full report only to check a specific claim.

## Checklist
- [ ] Each worker sees only its brief, inputs and tools
- [ ] Per-worker size under the context limit
- [ ] Outputs passed as files plus summaries
- [ ] Time and token budget in every brief
- [ ] Plan persisted to a file
- [ ] Budget ledger kept

## Output
Per-worker context list and the budget ledger.

## Avoid
- Copying whole outputs through the coordinator.
- Briefs with no budget, so overruns go unnoticed.
