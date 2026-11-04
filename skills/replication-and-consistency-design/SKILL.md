---
name: "replication-and-consistency-design"
description: "Decide replication topology, quorums and the consistency model per operation, and keep multi-entity changes correct without distributed transactions, using outbox, sagas and idempotent receivers."
license: "MIT"
---

# Replication and consistency design

## 1. Why replicate, and how
Replicate for durability, availability and read scaling or locality. Topologies:
- **Single leader**: simple ordering; writes limited to one node; failover must be automatic and safe (fencing), using a proven consensus service, never home-grown heartbeats.
- **Multi-leader**: writes in several regions; needs conflict resolution.
- **Leaderless quorums**: n replicas, write quorum w, read quorum r; r + w > n makes reads overlap the latest write; reads tolerate n - r failures, writes n - w. Sloppy quorums and hinted handoff trade consistency for write availability.
Synchronous replication protects data but adds latency; asynchronous risks losing recent writes on failover. State the recovery point you accept.

## 2. Consistency per operation
- Linearisable: behaves like one copy, no stale reads. Needed for uniqueness, locks, balances, leader election. Costs latency and availability under partition.
- Read-your-writes, monotonic reads, causal: what most user-facing features actually need.
- Eventual: converges when writes stop; fine for feeds, counters, analytics.
Decide per operation, not per system. Write it in the data design table.

## 3. CAP and PACELC, used properly
"Pick two of three" misleads. Partitions are rare; when one happens, each operation chooses availability or consistency (and the choice can differ by operation and data). In normal running, replication still trades latency against consistency (PACELC). Document: behaviour under partition, behaviour in normal running, and how state is reconciled afterwards.

## 4. Time and ordering
Do not order events across machines by wall-clock time; clocks drift and jump. Use a single sequencer, a log, logical clocks, or version vectors to detect concurrent updates. Deletes in replicated stores need tombstones.

## 5. Changes across entities without 2PC
At scale, atomic transactions stay inside one entity (one partition key). Between entities:
- **Transactional outbox**: write the state change and the outgoing event in the same local transaction; a relay publishes the event. No lost or phantom events.
- **At-least-once messaging plus idempotent receivers**: receivers record processed message ids (or use natural idempotency) so redelivery is harmless.
- **Sagas**: a sequence of local transactions with compensating actions for undo; orchestrated (a coordinator) or choreographed (events). Design the compensations and the visible intermediate states.
Two-phase commit across services blocks when the coordinator fails; avoid it unless both sides are one database product built for it.

## 6. Conflict handling
When concurrent writes are allowed: last-writer-wins only where losing an update is acceptable; otherwise merge (application rules, CRDTs) or surface conflicts.

## Output
Per dataset: topology, replication mode, quorum settings, consistency per operation, partition behaviour, cross-entity mechanism (outbox, saga, idempotency key).

## Pitfalls
- Promising exactly-once delivery: aim for at-least-once delivery with idempotent effects.
- Read-after-write bugs from routing reads to lagging followers.
- Failover without fencing, giving two leaders.
