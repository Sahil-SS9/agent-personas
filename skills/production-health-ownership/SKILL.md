---
name: "production-health-ownership"
description: "Own production health: capacity, incident command, blameless postmortems."
license: "MIT"
---

# Production health ownership

## When to use
Ongoing operation of any production service.

## Procedure
1. Capacity: forecast growth against current headroom; load-test before the cliff; document the scaling plan (what happens at 2×, 10×).
2. Incident command: on-call rotation with escalation path; IC role during incidents; the 3Cs — coordinate, communicate, control; declare early, update on cadence, keep a timestamped working record.
3. Recovery: rehearsed failure modes; recovery procedures documented and actually executed in drills, not just written.
4. Postmortems: blameless, within days, each producing at least one concrete action item with an owner and a deadline.
5. Toil budget: track ops toil; hand repetitive repairs to the automation-engineer persona rather than absorbing them.

## Decision rules
- Production access follows least privilege with audit; break-glass is logged and reviewed.
- Reliability decisions are made on SLO data, not on the loudest recent outage.

## Pitfalls
- Heroics as a system: unmanaged on-call leads to burnout and missed alerts.
- Postmortems that assign blame instead of fixes.

## Done
Owned production with rehearsed incident command, capacity forecasts, and a closed postmortem loop.