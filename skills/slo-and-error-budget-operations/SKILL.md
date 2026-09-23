---
name: "slo-and-error-budget-operations"
description: "Define user-side SLOs, operate error budgets, alert on symptoms and burn rates."
license: "MIT"
---

# SLO and error-budget operations

## When to use
For every user-visible service, before feature pressure arrives.

## Procedure
1. Define SLIs from the user side (availability, latency, freshness, correctness); internal green dashboards lie.
2. Set SLOs per service with the product owner; error budget = 1 − SLO. The budget converts reliability into a decision rule.
3. Alert on symptoms and burn rates (fast-burn pages, slow-burn tickets), not on every error. Every alert actionable and unique.
4. Enforce the budget policy: budget exhausted → feature work pauses in favour of reliability work, jointly agreed in advance.
5. Review SLOs quarterly against reality; targets drift, so must the numbers.

## Decision rules
- No SLO, no deployment gate for that service.
- A 100% SLO is a non-SLO: it makes change impossible and incidents inevitable.
- Capacity and headroom are part of the SLO story: forecast, load-test, keep failover room.

## Pitfalls
- Alerting on causes instead of symptoms.
- Treating the error budget as an accounting nicety rather than a hard gate.

## Done
SLOs with agreed budgets, symptom-based alerting wired to burn rates, and an enforced budget policy.