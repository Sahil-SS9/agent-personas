---
name: "lakehouse-architecture-selection"
description: "Choose storage/lakehouse architecture from workload needs, not fashion."
license: "MIT"
---

# Lakehouse architecture selection

## When to use
Designing the data platform or adding a workload class.

## Procedure
1. Characterise the workload: BI/analytics (SQL, concurrent scans), ML (raw scale, schema-light), real-time (seconds), archival (cheap, rare).
2. Match architecture: warehouse for governed BI; lake/table formats (iceberg-style) for flexible scale with ACID; streaming only when latency genuinely demands; object storage for raw/archive with lifecycle rules.
3. Layer medallion-style: raw (immutable, cheap) → cleaned (validated, deduplicated) → modelled (dimensional, served). Contracts between layers; cost tracked per layer.
4. Design for the failure modes: small files (compaction), schema drift (evolution policy), late data (watermarks), deletion (GDPR-ready design).
5. Reassess when workloads change; architectures follow requirements, not conferences.

## Decision rules
- Streaming is not a status symbol: batch is correct until latency demands otherwise.
- Every layer has a cost owner and a retention policy.
- One governance layer (catalogue, permissions, lineage) across storage choices.

## Pitfalls
- Ingesting everything "in case" without retention policy.
- Real-time pipelines nobody consumes.

## Done
Workload-matched architecture with layered zones, contracts, cost tracking, and designed-for failure modes.