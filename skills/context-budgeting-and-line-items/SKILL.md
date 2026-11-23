---
name: "context-budgeting-and-line-items"
description: "Budget context from measured task needs."
license: "MIT"
---
# Context Budgeting and Line Items

## Use when
- Designing or reviewing an agent's context strategy.
- A new tool, retrieval source or instruction block is about to be added.
- The agent "knows less" at the end of sessions than at the start.

## Instructions

1. Name the line items: instructions, tool schemas, examples, message
   history, retrieved material, scratchpads. A window without a budget is
   a bucket that fills with whatever arrived last.
2. Budget below the ceiling: rated window sizes are not working sizes —
   quality can degrade well before the rated limit, and the point varies by
   model and task, so there is no universal threshold. Reserve output and tool-growth
   headroom, then measure task accuracy at several context lengths.
3. Every addition re-prices the budget: a new tool or retrieval source
   usually costs more than its line item suggests. Re-measure the whole
   budget when the surface grows, and record the delta.
4. Cache-aware economics: the prefix the cache depends on is a line item
   too. Check the provider's actual cache behaviour: clearing or rewriting earlier
   messages can invalidate reuse. Record cached tokens and re-fetch cost.
5. Pin the invariants: the task statement, the authorisation context and
   the decision record stay pinned in the window; everything else is
   budgeted, cleared or externalised.
6. Review the budget from evidence: token counts per line item per turn,
   cache hit rate, and where quality first degrades. A budget nobody
   measures is a guess with a number on it.

## Stop conditions
- Never operate at the window ceiling and hope.
- Never add a tool or retrieval source without re-measuring the budget.
- Never leave the task statement or authorisation context to compaction.

## Escalation
- When the honest budget cannot fit the required work, escalate the
  architecture decision: isolate into separate windows or externalise state
  — do not quietly exceed the budget.
