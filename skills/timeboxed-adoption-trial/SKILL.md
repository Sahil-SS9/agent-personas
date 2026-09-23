---
name: "timeboxed-adoption-trial"
description: "Design and run the smallest reversible experiment that produces keep/kill evidence."
license: "MIT"
---

# Time-boxed adoption trial

## When to use
Between Assess and Adopt: proving a candidate tool in our real context.

## Procedure
1. Pre-commit the evidence: define BEFORE the trial what result keeps the tool and what kills it. Un-decidable trials are waste.
2. Pick the smallest reversible experiment: one real (but low-blast-radius) workload, real constraints, real data-handling rules — never vendor demo settings.
3. Time-box it (calendar deadline, not scope deadline). Record: setup friction, operating cost, failure modes encountered, exact commands/config used.
4. Measure both benefit and cognitive cost: did it close the gap, and can the team understand/maintain what it produced? Codebase cognitive debt is a real trial output.
5. Verdict to ring: convert evidence into an Adopt/Trial/Assess/Caution recommendation with expiry and re-assessment triggers; record the decision trail.

## Decision rules
- Kill on pre-committed failure evidence even if sunk cost is high; the trial exists to produce the kill signal cheaply.
- Do not extend a trial repeatedly without a new pre-commitment — that is a decision avoided, not a trial.
- Two trials of the same question = an experiment design problem; fix the design, not the calendar.

## Pitfalls
- Trials run on ideal data with no failure injection.
- Success criteria so vague any outcome can be argued either way.

## Done
Time-boxed trial with pre-committed evidence, honest setup record, ringed verdict, and a durable decision record.