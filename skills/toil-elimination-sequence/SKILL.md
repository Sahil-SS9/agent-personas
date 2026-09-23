---
name: "toil-elimination-sequence"
description: "Measure toil, then eliminate, simplify, and only then automate — with evidence at each step."
license: "MIT"
---

# Toil elimination sequence

## When to use
Any request to "automate this" or any recurring manual workflow.

## Procedure
1. Measure the toil first: frequency, time per run, error rate, whether it scales with growth. Toil = manual, repetitive, automatable, tactical, no enduring value. Quantify before acting — target the biggest source, not the most annoying.
2. Ask the elimination question: should this step exist at all? Remove it if not.
3. Simplify what remains: fewer hand-offs, fewer decisions, fewer moving parts. Every component must earn its complexity.
4. Only then automate — and prefer the stabilised path: linear, churning processes are better left manual until they stop changing.
5. Record the sequence: what was eliminated, what was simplified, what was automated, with the before/after toil numbers.

## Decision rules
- Automating waste produces faster waste — the elimination gate always comes first.
- No automation without a measured toil baseline; "it feels slow" is not a baseline.
- An automation that costs more to maintain than the toil it removed gets deleted.

## Pitfalls
- Scripting a workaround for a broken upstream process.
- Automating the visible symptom while the real toil lives one step earlier.

## Done
Measured baseline, elimination/simplification record, automation scoped only to what remains, and after-measurement proving the win.