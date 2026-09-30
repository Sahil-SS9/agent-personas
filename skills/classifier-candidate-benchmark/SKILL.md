---
name: "classifier-candidate-benchmark"
description: "Run candidates through the frozen exam and report each verdict with its gates, utility, calibration, determinism and latency — including the candidates that fail."
license: "MIT"
---

# Classifier candidate benchmark

## When to use
Evaluating models for a decision, including reproductions of commercial ones.

## Procedure
1. Run each candidate through the identical harness and save raw answers, not just scores.
2. Report per candidate: gates passed or failed, utility at the operating point, calibration, determinism across repeats, latency, and marginal cost.
3. Adopt the canonical serving path the author specifies before judging a candidate; an adapted path is a different model.
4. Record byte-identical determinism checks across runs.
5. Publish the rejects with their reason. A benchmark that only reports a winner is not a benchmark.

## Decision rules
- Non-determinism disqualifies a candidate where reproducible routing is required.
- Latency is a gate, not a footnote. A qualifying model at eight seconds per input against a 100-millisecond budget is a design problem, not a pass.
- Hosted commercial references are useful as calibration and unacceptable as a hard dependency when spend or retention is a constraint.
- Re-run after any upstream correction, and report whether the verdict moved.

## Pitfalls
- Judging a model on a non-canonical serving path and blaming the model.
- Reporting only the winner.
- Ignoring marginal cost per call in a high-volume pre-filter.

## Done
Every candidate has a dated verdict with gates, utility, calibration, determinism, latency and cost — and the rejects are documented as thoroughly as the winner.
