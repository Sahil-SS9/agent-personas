---
name: "guard-model-selection-and-calibration"
description: "Choose and calibrate the model that powers a rail, and prove the operating point on your own data rather than trusting a leaderboard."
license: "MIT"
---

# Guard model selection and calibration

## When to use
A rail is model-backed: moderation, injection detection, PII, policy classification.

## Procedure
1. Define the decision the model must make and the cost of each error direction.
2. Assemble a labelled set from your own traffic, including hard negatives.
3. Calibrate thresholds to the operating point your error budget requires.
4. Measure at the operating point: false positives, false negatives, latency, cost per decision.
5. Record model version, threshold and dataset hash together; re-measure when any changes.

## Decision rules
- Public safety benchmarks do not transfer to your traffic. Measure on yours.
- Intent manipulation drives moderation classifiers to near-total bypass in published tests; do not treat a moderation model as an adversarial control.
- A threshold without its dataset hash is not reproducible.
- Calibration drift is silent; schedule re-measurement.

## Pitfalls
- Selecting on leaderboard rank.
- Publishing a single accuracy figure with no operating point.
- Assuming a bigger guard model is strictly safer.

## Done
The chosen model has a stated operating point, measured error rates in both directions, and a re-measurement trigger.
