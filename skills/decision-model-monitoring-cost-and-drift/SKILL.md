---
name: "decision-model-monitoring-cost-and-drift"
description: "Watch a deployed decision model for drift, latency and unit economics, and treat silent quality decay as the primary failure."
license: "MIT"
---

# Decision model monitoring cost and drift

## When to use
Continuously after deployment.

## Procedure
1. Track the verdict mix, band distribution and rejection rate over time.
2. Track input distribution shift, since drift in inputs precedes drift in outcomes.
3. Track latency percentiles and cost per decision.
4. Where ground truth arrives late, estimate performance without labels rather than waiting.
5. Re-run the frozen exam on a schedule and after any model, threshold or upstream change.

## Decision rules
- A stable rejection rate is not health; a filter that stops rejecting looks identical to one that works.
- Outcome-based monitoring is unavailable for the horizon where labels are delayed; use label-free estimation in the interval.
- Thresholds are versioned artefacts. Record them with the model version.
- Cost per decision belongs in the same dashboard as latency, or the economics drift unnoticed.

## Pitfalls
- Monitoring accuracy only, which is unavailable exactly when drift is happening.
- Treating a throughput drop as infrastructure noise when the model has degraded.
- Changing a threshold without recording it, making the historical series meaningless.

## Done
The dashboard covers verdict mix, input drift, latency, cost and label-free performance, and thresholds are versioned with the model.
