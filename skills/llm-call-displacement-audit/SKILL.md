---
name: "llm-call-displacement-audit"
description: "Audit a live system for calls that should not be LLM calls — where a cheap classifier answers the same question faster and deterministically."
license: "MIT"
---

# Llm call displacement audit

## When to use
Cost, latency or nondeterminism is driven by an LLM making yes/no or pick-one-among-N decisions.

## Procedure
1. Inventory LLM calls and classify each by job: generation, extraction, classification, routing, scoring, formatting.
2. Flag every call whose output is drawn from a small closed set.
3. For each flagged call, estimate volume, current cost and current latency.
4. Judge feasibility: is the decision separable, and is there a supply of labels?
5. Rank by value: volume times saving, penalised by the cost of building the frozen exam.

## Decision rules
- Generation cannot be displaced. Decisions over a closed label set can be.
- Determinism is a win independent of cost where reproducibility is required.
- Do not displace a call whose output is merely mostly a label; if it sometimes returns prose, it is not a classification.
- A displacement needs the same fail-open contract as any other pre-filter.

## Decision-output clarification
The selected displacement candidate must be eligible, not merely the name of the call being assessed. If the only call also supplies downstream-used free text, select no displacement candidate. A separately extracted closed-set component requires an explicit design preserving the useful generation and its own approval.

Before returning a structured result, check that each field answers the requested proposition, uses the requested types and vocabulary, and agrees with the explanation. Saved evidence is not an action performed by you; a recommended next step is not an executed action.

## Pitfalls
- Displacing a call that also does useful extraction on the side.
- Counting token savings without counting the cost of labelling and benchmarking.
- Ignoring the latency budget: a locally served 4B model can be slower than the API it replaces.

## Done
Each LLM call is classified by job, every closed-set call carries a value estimate, and the recommendation names the benchmark required before displacement.
