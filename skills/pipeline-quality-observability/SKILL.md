---
name: "pipeline-quality-observability"
description: "Build rerunnable, observable pipelines with data-quality gates and lineage."
license: "MIT"
---

# Pipeline quality and observability

## When to use
Building or operating any data pipeline.

## Procedure
1. Design reruns in: idempotent tasks, deterministic inputs, incremental where volume demands, tested backfill procedure.
2. Emit observability per run: rows in/out, freshness lag, null/duplicate checks, runtime, cost. A pipeline that cannot report its own health is unfinished.
3. Data-quality gates: schema contracts, null/uniqueness/range checks, freshness SLAs; failed checks stop downstream consumption (quarantine, don't publish garbage).
4. Document lineage: source → transformations → consumers; contracts with producers on schema and delivery.
5. Orchestrate explicitly: DAG of dependencies, retries with backoff, alerts on failure and freshness breach.

## Decision rules
- Silent data corruption is worse than loud failure: gates stop publication.
- Late/duplicate source data is a designed-for case, not an exception.
- Ownership explicit: every dataset has an owner and consumers know who to call.

## Pitfalls
- Backfills that double-count or poison downstream models.
- Quality checks that alert but don't block.

## Done
Rerunnable, observable pipelines with enforced quality gates and documented lineage.
