---
name: "perf-regression-monitoring"
description: "Guard performance with CI budgets, RUM alerting and perf-reviewed diffs."
license: "MIT"
---

# Performance regression monitoring

## When to use
Ongoing, for any live property.

## Procedure
1. CI budgets: per-route lab checks fail the build on budget breach (bundle size, LCP simulation, CLS).
2. Field monitoring: RUM collects CWV per page/class; alert on p75 drift beyond threshold; segment by device and geography.
3. Perf diffs: changes with performance impact reviewed like correctness diffs; every regression has a named cause and a fix or accepted trade-off.
4. Before/after records: every optimisation logged with field evidence; wins and failures both recorded.
5. Quarterly review: budget recalibration against real-user device mix and business priority.

## Decision rules
- Regressions are treated like bugs: found, attributed, fixed or consciously accepted.
- Silent metric drift is a monitoring defect, not a mystery.

## Pitfalls
- Alerting on lab metrics only.
- Budgets set once and never recalibrated.

## Done
Enforced CI budgets, live field alerting, and a complete before/after optimisation log.