---
name: "async-messaging-and-workflow-design"
description: "Design queues, streams, pub/sub and long-running workflows: delivery guarantees, ordering keys, idempotent consumers, retries and dead letters, backpressure, backlog recovery and fairness."
license: "MIT"
---

# Asynchronous messaging and workflow design

## 1. Go asynchronous for a reason
Decouple a slow or unreliable step from the user's request, smooth bursts (queue-based load levelling), fan out to many consumers, or run long workflows. Asynchrony adds delay, ordering questions, backlogs and harder debugging; say what the user sees while work is pending.

## 2. Pick the primitive
| Need | Primitive |
|---|---|
| Work items processed once by one of many workers | Queue with competing consumers |
| Ordered, replayable event history; many independent readers | Log or stream, partitioned by key |
| Notify many subscribers | Pub/sub topic |
| Multi-step business process with waits and compensation | Workflow engine or saga orchestrator |
Large payloads go to object storage; send a reference (claim check).

## 3. Delivery and idempotency
Assume at-least-once delivery. Every consumer must be idempotent: dedupe on a message id stored with the effect, or make the operation naturally idempotent. "Exactly once" is at-least-once delivery plus idempotent effects. Producers publish via a transactional outbox so state and event cannot diverge.

## 4. Ordering
Global order is expensive and rarely needed. Order per entity by partitioning on its key (order id, account id); process a key's messages sequentially without blocking other keys. Know what happens on retry and rebalance (reordering).

## 5. Failures and poison messages
Retry with backoff and jitter, a maximum attempt count, then a dead-letter queue with the reason. Alert on dead letters; give operators a safe replay tool. Distinguish transient from permanent errors.

## 6. Backpressure, backlogs and fairness
- Measure age of the oldest message (and age at first attempt), not only depth. Alarm on age against the freshness SLO.
- Backlogs turn short outages into long recoveries. Bound retention, provision drain capacity above steady state, and decide the drain order: for time-sensitive work, process fresh messages first and sideline old ones to a spillover queue.
- Per-tenant limits so one tenant's surge cannot create a system-wide backlog; protect every stage, not only the front door.

## 7. Workflows and sagas
Model each step as a local transaction with a compensating action; persist workflow state; make each step idempotent; set timeouts on waits; show intermediate states to users honestly ("payment pending").

## Output
Per flow: producer, primitive, key and ordering, delivery semantics, idempotency mechanism, retry policy, DLQ and replay, backlog metric and alarm, fairness limits.

## Pitfalls
- Queues used to hide an undersized consumer (backlog grows forever).
- Consumers that are not idempotent; duplicate charges, emails or shipments.
- A single queue shared by unrelated workloads (one slow consumer delays all).
