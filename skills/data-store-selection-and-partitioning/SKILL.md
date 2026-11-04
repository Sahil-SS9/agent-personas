---
name: "data-store-selection-and-partitioning"
description: "Choose data stores from access patterns, then design keys, indexes, partitioning, hot-key handling, rebalancing and retention, with the trade-offs written down."
license: "MIT"
---

# Data store selection and partitioning

## 1. Start from access patterns
For each dataset write: the queries (by what key, what range, what filter, what sort), read and write rates, item size and growth, consistency need, retention and deletion rules (including legal erasure). The store follows from this table, not from fashion.

## 2. Store families and when they fit
| Family | Fits | Watch out for |
|---|---|---|
| Relational | Relationships, constraints, transactions, ad-hoc queries; most systems' default | Single-writer limits; cross-shard joins once partitioned |
| Key-value | Point reads and writes by key at high rate; sessions, caches, counters | No secondary queries without extra indexes |
| Document | Self-contained aggregates read together | Cross-document consistency, unbounded documents |
| Wide-column | Huge write volumes, time-ordered rows per key | Query-first modelling, tombstones, hot partitions |
| Search index | Full-text, faceting, relevance | It is a derived copy; rebuildable, not the source of truth |
| Time-series | Metrics, events by time | Cardinality explosions |
| Object storage | Large blobs, media, backups, data lakes | Latency; use a CDN for reads |
| Graph | Deep relationship traversal | Usually unnecessary; check relational first |
| Vector index | Similarity search over embeddings | Filtering, freshness and access control (see AI sub-category) |
Prefer fewer stores; every extra store is a consistency boundary and an operational burden. Keep one source of truth per dataset; others are derived and rebuildable.

## 3. Keys and indexes
- Design primary keys so the main queries are single-partition lookups or range scans.
- Every secondary index costs writes and storage; add those the access table demands.
- Store ids that never change; avoid natural keys that change (emails).

## 4. Partitioning (sharding)
- Partition only when one node cannot hold the data or the write rate (from the estimate).
- Hash partitioning spreads load but loses range queries; range partitioning keeps ranges but risks hot ranges (time-ordered keys).
- Consistent hashing with many virtual nodes, or many more partitions than machines (around 20 per machine), makes rebalancing incremental instead of reshuffling everything.
- Hot keys: detect them (top-k metrics); split with a suffix and merge on read, cache them, or replicate hot items selectively.
- Choose the partition key so related data that must be updated together lives together; cross-partition transactions are expensive.
- Plan rebalancing and resharding before you need them: online, throttled, observable.

## 5. Retention and lifecycle
TTLs, tiering to cheaper storage, compaction, deletion that reaches backups and derived copies.

## Output
Data design table: data, store, access pattern, key or partition key, indexes, consistency, retention, estimated size.

## Pitfalls
- Picking a NoSQL store "for scale" when the data is small and relational.
- Partitioning by a key with skewed traffic (celebrity users, popular products, current day).
- Treating a search or vector index as the source of truth.
