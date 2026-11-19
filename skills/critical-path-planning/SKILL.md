---
name: "critical-path-planning"
description: "From task durations and dependencies, find which delays actually move the finish date and how far other tasks can slip."
license: "MIT"
---

# Critical Path Planning

`writing-plans` and `workstream-orchestration` identify what blocks what. This skill answers
a narrower question: **which delay would actually move the finish date, and which tasks have
room to slip?** It is a calculation over supplied estimates, not a scheduling tool and not a
promise of a delivery date.

## 1. Require the inputs, state the model
You need, for each task: a duration (with units) and its finish-to-start predecessors (the
tasks that must finish before it starts). State the assumptions explicitly:
- finish-to-start dependencies only;
- one consistent time unit;
- no resource levelling, no calendar/holiday effects, no parallelism limits beyond the
  dependency graph.
If the real problem has resource contention, calendars or lag/lead times outside this model,
say so and name what is missing — do not silently produce a date the model cannot support.

## 2. Refuse to invent missing data
- A task with no duration estimate: return `missing estimate for <task>` and stop the
  calculation for the affected path. Do not guess a number.
- A dependency cycle: report the cycle explicitly; a cyclic graph has no finite critical path.
- An ambiguous predecessor: ask for the specific clarification rather than assuming.

## 3. Compute forward and backward passes
- **Forward pass:** earliest start (ES) and earliest finish (EF) for each task. ES = max EF
  of predecessors (0 for a start task); EF = ES + duration. The project's earliest completion
  is the max EF across all end tasks.
- **Backward pass:** latest finish (LF) and latest start (LS) from the project completion
  time. LF = min LS of successors (project completion for an end task); LS = LF − duration.
- **Total float** = LS − ES (equivalently LF − EF). It is how long a task may slip without
  moving the project completion.

## 4. Report the controlling paths and the float
- The **critical path** is the chain(s) of tasks with zero total float. There may be more
  than one tied critical path — list all of them, not just the first you find.
- Give a table: task → duration → ES → EF → total float → critical (yes/no).
- State the earliest completion time with its unit, and which tasks control it.
- A correct table is a complete answer. A diagram is optional; a correct-looking chart with
  the wrong finish time is a failure.

## 5. Sanity-check the arithmetic
Re-derive the completion time by summing durations along each reported critical path and
confirm it equals the forward-pass result. If two tied paths give different sums, the
calculation is wrong — fix it before reporting.

## Voice
Show the float, name every tied critical path, and state the units. Refuse to invent a
duration or a date the inputs cannot support; return the specific missing information
instead.
