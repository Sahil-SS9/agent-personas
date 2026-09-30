---
name: "guardrail-change-control-and-drift-monitoring"
description: "Gate changes to the rail estate and watch for quiet decay once they ship: traffic drift, adaptive attackers, provider changes and silent non-compliance."
license: "MIT"
---

# Guardrail change control and drift monitoring

## When to use
Modifying any rail, and on a recurring cadence for the live estate.

## Procedure
1. Before a change: state what it is for, what it could break, and how it will be validated.
2. Re-run the rail's benchmark before and after; a change with no before/after is not controlled.
3. After the change: watch the drift signals — trigger rate, verdict mix, latency, cost, input distribution shift.
4. Track upstream dependencies: model deprecation, provider terms, quota changes.
5. Look specifically for silent non-compliance, where the rail is nominally on but no longer acting.

## Decision rules
- A rail that has never fired is either unnecessary or broken; determine which.
- An all-green report is a failure signal. Somewhere in any estate, something has decayed.
- Adaptive attackers change the input distribution; static thresholds age.
- Provider-side changes are your incident, not theirs.

## Pitfalls
- Monitoring detection counts and missing that the rail stopped acting.
- Treating the vendor's uptime as your guardrail's uptime.
- No owner, so drift is discovered by a user.

## Done
Every rail has a before/after record for its last change and a drift signal someone is accountable for watching.
