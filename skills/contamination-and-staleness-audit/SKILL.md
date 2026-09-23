---
name: "contamination-and-staleness-audit"
description: "Check evals for train/test leakage and saturation before trusting scores."
license: "MIT"
---

# Contamination and staleness audit

## When to use
Before trusting any headline benchmark score or comparing models across time.

## Procedure
1. Check the dates: does the model's training data cut precede the benchmark's release? Models released after a public benchmark may have seen it. A contaminated score is marketing, not evidence.
2. Look for memorisation signals: implausibly high scores on hard items, verbatim answer overlap, near-perfect performance with brittle rephrasings.
3. Test with perturbations: rephrase, re-order, or swap surface details; a contaminated/overfit model degrades sharply when the surface changes, a genuinely-capable one does not.
4. Check saturation: scores clustered at ceiling mean the benchmark no longer discriminates — rotate or extend the set.
5. Prefer refreshed/adversarial eval sets over frozen leaderboards; keep eval data distinct from training data and document collection dates.

## Decision rules
- Assume benchmarks leak until checked; absence of a contamination statement is itself a red flag.
- A benchmark at ceiling is retired from decision-making, whatever its prestige.

## Pitfalls
- Comparing model A (evaluated on a clean set) with model B (trained into the set).
- Trusting a single frozen leaderboard across model generations.

## Done
A written audit: contamination risk per benchmark, perturbation evidence, saturation status, and a trust verdict for each score cited.