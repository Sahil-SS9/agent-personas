# System design: <name>

Status: Draft v0.1 | Owner: <team> | Date: <DD/MM/YYYY> | Reviewers: <names or roles>

## Context and goals
What problem, for whom, why now. Goals and explicit non-goals.

## Requirements
Functional:
- <what the system must do>

Non-functional (SLOs; measured where users feel them):

| SLI | Target | Window | Measured at |
|---|---|---|---|
| <operation> latency | p99 < <n> ms | 28 days | <where> |
| <operation> availability | <99.9>% | 28 days | <where> |

Other constraints: data residency, compliance, budget, deadlines, team skills, existing platforms.

## Assumptions and estimates
Assumptions (each labelled, with source or "to confirm"): users, actions per user per day, peak factor, object sizes, retention, replicas.
Derived figures from `scripts/capacity_estimate.py` (with units): average and peak QPS per operation, storage per day and over retention, bandwidth, nodes, token throughput and cost for AI parts.
Binding constraint: which resource decides the design.

## High-level design

| Component | Responsibility | Technology choice | State |
|---|---|---|---|
| <name> | <one line> | <choice and why> | Stateless / Durable |

Diagram: C4 context and container views (Mermaid or tool of choice). Request flow for the main use cases.

## Data design

| Data | Store | Access pattern | Partition key | Consistency | Retention |
|---|---|---|---|---|---|

## Interfaces
Key APIs and events; idempotency keys; versioning.

## Deep dives
The two or three components where this design is hard.

## Failure modes and resilience

| Component | Failure | Detection | Impact | Mitigation |
|---|---|---|---|---|

Static stability, failure domains, capacity after losing one zone.

## Overload and traffic management
Timeouts per call (from downstream percentiles), retries (one layer, backoff with jitter, budget, idempotent only), rate limits and fairness, load shedding priorities, backlog metrics.

## Security and privacy
Trust boundaries, identities, authorisation, secrets, encryption, tenant isolation, personal data handling.

## Operations and rollout
SLIs and alerts, dashboards, rollout stages and rollback, migrations, runbooks.

## Cost
Unit cost (per request, user or tenant), dominant drivers, first levers.

## AI and LLM components
(Delete if none.) Why a model is needed and the simplest pattern that works; model access (gateway, quotas, outage behaviour); context and retrieval; budgets (tokens, steps, time, spend); untrusted inputs and prompt injection controls; write actions and their approval gates; evaluation before launch and in operation.

## Alternatives considered

| Option | Why rejected |
|---|---|

## Risks and open questions
1. <question, owner, by when>
