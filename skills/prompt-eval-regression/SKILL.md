---
name: "prompt-eval-regression"
description: "Gate prompt/agent changes behind fixed eval sets with measured before/after."
license: "MIT"
---

# Prompt eval regression

## When to use
Every prompt or agent-behaviour change.

## Procedure
1. Maintain a fixed eval set per prompt/agent: representative real inputs with expected-behaviour rubrics. Frozen, versioned, extended deliberately.
2. Before/after: run the eval set on the current and the changed version; compare per-case, not just aggregate.
3. Regression gate: changes that fail previously-passing cases are reverted or reworked — a new win does not pay for an old break.
4. Extend the eval set with every bug found: real failures become permanent test cases.
5. Record evidence in the changelog: which eval version, which results, what decision.

## Decision rules
- No eval set, no change to production prompts.
- Anecdotes are hypotheses; evals are evidence.
- A passing eval on one model says nothing about another model; state the model.

## Pitfalls
- Tuning the prompt to the eval set until it only does those cases.
- Eval sets that never grow with real failures.

## Done
Every prompt change measured against a fixed, growing eval set with recorded evidence.