---
name: "operability-and-rollout-design"
description: "Design for running the system: SLIs and alerts, the four golden signals, dashboards, logs and traces, safe staged rollout and rollback, migrations and runbooks."
license: "MIT"
---

# Operability and rollout design

A design is not finished until someone can run it at 3 a.m.

## 1. Observability built in
- SLIs from the requirements, measured where users feel them, with error budgets and burn-rate alerts.
- Four golden signals per service: latency (successes and failures separately, as percentiles), traffic, errors, saturation.
- Per-dependency metrics: call latency, error rate, timeouts, retries, circuit or shedding events.
- Asynchronous work: age of oldest message, throughput, dead letters.
- Structured logs with request and trace ids; distributed tracing across services; no secrets or personal data in logs.
- Alert on symptoms users feel; route cause metrics to dashboards.

## 2. Safe change
- Every change (code, config, schema, feature flag, model or prompt) goes out in stages: shadow or dark launch where possible, canary (one cell or a small percentage), then wider, with automatic rollback on SLO regression.
- Deploy one failure domain at a time; keep versions backward and forward compatible during rollout.
- Config is versioned, validated and rolled out like code.
- Schema migrations: expand, migrate, contract; never a breaking change in one step.

## 3. Operational simplicity
Automate everything repetitive (provisioning, failover, scaling, backups and restore tests). Prefer managed services where the team lacks depth. Keep one version in production where possible.

## 4. Runbooks and ownership
Each alert links to a runbook: what it means, how to confirm, how to mitigate, how to escalate. Name the owning team for every component.

## 5. Capacity operations
Load tests to the estimate's peak and beyond; capacity reviews against growth; quotas and limits tracked before they bite (provider limits, connection pools, IPs).

## Output
Operations section: SLIs and alerts, dashboards list, tracing and logging plan, rollout stages and rollback trigger, migration plan, runbooks, owners.

## Pitfalls
- Average-only dashboards.
- Rollback that needs a data migration reversal nobody tested.
- Alert floods on causes rather than symptoms.
