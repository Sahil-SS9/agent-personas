---
name: "ux-flow-and-heuristics"
description: "Design flows that never make users think; apply usability heuristics systematically."
license: "MIT"
---

# UX flow and heuristics

## When to use
Designing any user flow or reviewing existing UX.

## Procedure
1. Map the flow: entry → steps → success; every step earns its place; remove steps that serve the system, not the user.
2. Apply core heuristics per screen: obvious labels, recognisable affordances, immediate feedback on every action, error messages that say what happened and how to fix it (not just error codes).
3. Reduce cognitive load: Hick's law (fewer choices), progressive disclosure (complexity on demand), recognition over recall (visible options, not remembered).
4. Consistency: same action = same control = same place, across the product (Jakob's law: users spend most time elsewhere).
5. Handle the edges: empty states (teach), loading (progress), errors (recovery), empty states (first-run). Destructive actions are separated, labelled, and confirmed.

## Decision rules
- If the design needs a manual, redesign it: clarity over cleverness.
- Defaults serve the majority; the power path never punishes the simple case.
- Every form field earns its place; every optional field is visibly optional.

## Pitfalls
- Clever icons without labels.
- Error messages that blame the user.

## Done
A flow map with heuristics-checked states for every step.