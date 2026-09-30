---
name: "policy-to-control-decomposition"
description: "Turn a written policy into enforceable controls, marking each one decidable and machine-checkable or explicitly human-only."
license: "MIT"
---

# Policy to control decomposition

## When to use
A policy, standard or regulatory requirement must become something the system actually does.

## Procedure
1. Extract each obligation from the source text as a single sentence.
2. For each, ask what observable state would violate it.
3. Classify: deterministically decidable, statistically detectable, or human-judgement only.
4. Convert decidable obligations into gates; statistically detectable ones into monitors with a stated error budget.
5. Label the rest human-only and schedule the review that will exercise them.

## Decision rules
- An obligation with no observable violating state is not enforceable and must be labelled as such.
- Do not launder a statistical detector into a compliance gate; they have different failure semantics.
- Human-only controls need a named human and a cadence, or they are aspirations.
- Prefer the fewest controls that cover the obligation.

## Pitfalls
- Producing a policy-to-control matrix where every cell says enforced.
- Treating a model judgement as a deterministic gate.
- Forgetting that some obligations apply to the operator, not the system.

## Done
Every obligation carries a decidability class, and every decidable one has a named control with a test.
