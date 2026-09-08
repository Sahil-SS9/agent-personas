---
name: "simplify-swarm"
description: "Use after writing or modifying code to simplify it with three parallel read-only agents (Hygiene, Clarity, Correctness) applied in SAFE→CAREFUL→RISKY order."
license: "MIT"
---
# Simplify Swarm

## When to use
Use after writing or modifying code to simplify it with three parallel read-only agents (Hygiene, Clarity, Correctness) applied in SAFE→CAREFUL→RISKY order.

## Method
1. Establish the changed scope and behavioural baseline before reviewing for simplification. Preserve public contracts and user-approved behaviour.
2. Inspect reuse, correctness, clarity and unnecessary complexity as separate lenses. Parallel review is optional and requires permission; direct review remains valid.
3. Prove each proposed simplification against concrete callers and edge cases. Retain guards that look redundant but protect untrusted inputs or failure boundaries.
4. Apply small behaviour-preserving changes with witnessed regression tests where a defect exists. Run relevant wider checks after refactoring.
5. Do not trade safety or semantics for fewer lines. Report rejected simplifications and distinguish independent review from the author’s own inspection.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
