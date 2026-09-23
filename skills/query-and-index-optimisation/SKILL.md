---
name: "query-and-index-optimisation"
description: "Optimise queries from measured plans; index by selectivity and cost."
license: "MIT"
---

# Query and index optimisation

## When to use
Slow queries, high load, or before shipping new access patterns.

## Procedure
1. Measure first: EXPLAIN the slow query; find the actual plan (sequential scans, bad joins, sorts spilling to disk).
2. Index by evidence: selectivity/cardinality of filter columns, covering indexes for hot paths; justify every index against its write cost.
3. Fix query shape: avoid SELECT *, N+1 patterns, functions on indexed columns; sargable predicates only.
4. Partition large tables on the access axis (usually time); prune partitions in queries.
5. Cache only measured hotspots with deliberate invalidation; a cache without an invalidation story is a future bug report.

## Decision rules
- No index without a query that needs it; no query shipped without a plan check.
- Optimise the measured slow query, not the imagined one.
- Data volume grows: designs must survive 10× rows.

## Pitfalls
- Indexes added for one report that tax every write.
- ORMs emitting accidental cross joins.

## Done
Measured plans showing the improvement, indexes justified, and the change documented.