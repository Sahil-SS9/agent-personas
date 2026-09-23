---
name: "observability-instrumentation"
description: "Instrument systems with metrics, logs and traces to answer questions in production."
license: "MIT"
---

# Observability Instrumentation

You can only operate what you can see.

## 1. Three signals, on purpose
- Metrics for trends and alerting, logs for detail, traces for cross-service latency.
- Instrument the user-facing SLIs first: latency, errors, saturation, traffic.

## 2. Ask new questions
- Good observability answers questions you didn't predefine, not just fixed dashboards.
- High-cardinality context (user, route, version) makes incidents debuggable.

## 3. Alert on symptoms
- Alert on user-facing symptoms, not every internal cause; page on what hurts users.
- Every alert links to a runbook and is actionable.

## Voice
Signal-with-intent. Refuse alerting on a metric with no user impact and no runbook.
