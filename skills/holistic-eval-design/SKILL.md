---
name: "holistic-eval-design"
description: "Design multi-dimensional model evaluations with task-valid metrics and stated conditions."
license: "MIT"
---

# Holistic eval design

## When to use
Before judging any model, prompt, or pipeline change.

## Procedure
1. Pick scenarios that mirror the actual deployment distribution — the benchmark-vs-production gap is where models disappoint. If you cannot name the production task, you cannot design the eval.
2. Select multiple dimensions (accuracy, robustness, fairness, calibration, efficiency, safety) and report per-dimension: aggregate scores hide failures.
3. Choose task-valid metrics: state how each metric maps to user-visible quality. If you cannot, the metric is decoration.
4. State conditions with every number: dataset version, prompt/template, decoding params, seeds, date. Reproducibility is part of the result.
5. Report variance where cheap (multiple samples/seeds): a single run is a data point, not a measurement.
6. For subjective dimensions, define a rubric with anchored examples first; collect judgments; report agreement. Rubric-free vibes are not evaluation.

## Decision rules
- No single benchmark is a verdict.
- Unverifiable claims are reported as unverifiable — never auto-passed.
- Prefer a conservative number with provenance over an exciting number without.

## Pitfalls
- Leaderboard-chasing metrics that do not map to the task.
- Reporting a headline score with no conditions attached.

## Done
A multi-dimensional, condition-stated, reproducible eval design tied to real task requirements.