# System design: Order notification service

Status: Draft v0.2 | Owner: Platform team | Date: 04/11/2026 | Reviewers: Systems Architect, SRE

## Context and goals
An online retailer sends order updates (confirmed, shipped, delayed, delivered) by email, SMS and push. Today the order service calls the email provider inline, so provider slowness delays checkout. Goal: a separate service that delivers every notification at least once, quickly, without ever slowing the order path, and an optional AI-written delay explanation.
Non-goals: marketing campaigns; in-app inbox.

## Requirements
Functional:
- Accept a notification event from the order service and deliver it on the customer's preferred channels.
- Respect opt-outs and quiet hours; keep a delivery history per order for support staff.
- For "delayed" events, add a short plain-English explanation generated from the shipment record.

Non-functional (SLOs, measured at the service boundary over 28 days):

| SLI | Target | Window | Measured at |
|---|---|---|---|
| Event accepted (publish API) latency | p99 < 50 ms | 28 days | API gateway |
| Notification handed to provider after event | p95 < 30 s, p99 < 2 min | 28 days | Dispatcher logs |
| Events eventually delivered or dead-lettered with reason | 99.99% | 28 days | Reconciliation job |
| Publish API availability | 99.95% | 28 days | Synthetic probe + gateway |

## Assumptions and estimates
Assumptions (to confirm with the order team): 2M orders/day, 4 events per order, 1.5 channels per event, peak factor 4 (sale days), event payload 2 KB, history kept 400 days, 3 replicas. Output of `capacity_estimate.py` (rounded):
- Events: 2M x 4 / 86,400 = 93 events/s average, 370 events/s peak.
- Provider sends: 140 sends/s average, 560 sends/s peak.
- History storage: 8M events/day x 2 KB = 16 GB/day; 6.4 TB over 400 days; 19 TB with 3 replicas.
- Delay explanations: 5% of events = 4.6 req/s average, 18 req/s peak; 1,500 input + 120 output tokens; about 2.2K output tok/s at peak.
Binding constraint: provider rate limits (email 500/s, SMS 100/s contracted), not our compute. A single node handles 2,000 events/s, so the design is distributed for availability, not throughput.

## High-level design

| Component | Responsibility | Technology choice | State |
|---|---|---|---|
| Publish API | Validate event, write to outbox table in the order database transaction | Library in order service + outbox relay | Stateless |
| Event log | Durable, partitioned by order id, 7-day retention | Managed log (3 AZs) | Durable |
| Dispatcher | Consume events, apply preferences, fan out per channel, call providers | Stateless workers, 3 AZs | Stateless |
| Preference store | Opt-outs, channels, quiet hours | Key-value store, read-through cache | Durable |
| History store | Delivery attempts per order | Wide-column store, partitioned by order id | Durable |
| Delay explainer | Generate explanation text for delayed orders | Model gateway + hosted LLM | Stateless |

Flow: order service writes the event into its own database with the order change (transactional outbox) -> relay publishes to the event log -> dispatcher consumes per partition, checks preferences, renders templates, sends via providers, records each attempt in history.

## Data design

| Data | Store | Access pattern | Partition key | Consistency | Retention |
|---|---|---|---|---|---|
| Outbox rows | Order DB | Append, relay reads in order | order id | Same transaction as order | Delete after publish |
| Events | Event log | Ordered per order | order id | Per-partition order | 7 days |
| Preferences | KV store | Point read by customer id | customer id | Read-your-writes for the customer | Account lifetime |
| History | Wide-column | Read by order id, newest first | order id | Eventual (seconds) | 400 days |

Ordering matters only within one order, so partitioning by order id keeps per-order order without global ordering. Cross-store transactions are avoided: the outbox gives atomic "order changed + event recorded" without two-phase commit.

## Interfaces
- Publish: in-process call writing an outbox row; returns immediately.
- Provider calls: each send carries an idempotency key = event id + channel, so a retried send is not duplicated where the provider supports keys; otherwise the dispatcher checks history before resending.

## Failure modes and resilience

| Component | Failure | Detection | Impact | Mitigation |
|---|---|---|---|---|
| Publish API | Outbox relay stalls | Outbox age alarm > 60 s | Notifications delayed, orders unaffected | Relay runs in 2 AZs with leader lease; replay from outbox |
| Event log | One AZ lost | Broker health, consumer lag | None if 2 AZs remain | 3-AZ replication, producer acks from 2 |
| Dispatcher | Worker crash mid-send | Consumer lag, partition rebalance | Duplicate send possible | At-least-once + idempotency key + history check |
| Dispatcher | Provider slow or down | p99 provider latency, error rate per provider | Backlog grows for that channel | Per-channel queues and worker pools (bulkhead); timeout 2 s; failed sends retried later from a delay queue; backlog drained newest-first for time-sensitive events |
| Preference store | Unavailable | Read errors | Cannot check opt-out | Serve cached preferences up to hard TTL 1 h; if none, hold the event (never send to a possibly opted-out customer) |
| History store | Write failures | Error rate | Support cannot see attempts | Buffer writes in the event log; history is not on the send path |
| Delay explainer | Model or gateway outage, slow output | Gateway error rate, p95 time to first token | Explanation missing | 3 s deadline; send the standard delay template without explanation; no fallback model on the hot path |

Static stability: the dispatcher needs only the log, the preference cache and providers; it never calls the control plane to keep sending. Capacity is provisioned for losing one of three AZs (each runs at most two-thirds utilised).

## Overload and traffic management
- Timeouts: provider calls 2 s (p99.9 of provider latency is 800 ms); preference reads 100 ms; explainer 3 s overall deadline.
- Retries: only in the dispatcher (single layer); exponential backoff with full jitter, cap 5 min, then delay queue; per-provider retry budget of 10% of sends; only idempotent sends are retried.
- Rate limits: token bucket per provider at 90% of contracted limits; per-merchant fairness limits so one merchant's bulk update cannot starve others.
- Shedding: under backlog, informational events (e.g. "out for delivery" older than 2 h) are dropped with a recorded reason; transactional events are never dropped.
- Backlog metric: age of oldest unprocessed event per partition, alarm at 2 min.

## Security and privacy
- Trust boundary at the publish API; only the order service can publish (service identity, mTLS).
- Phone numbers and emails encrypted at rest; history stores masked contact details only.
- Provider credentials in the secrets manager, rotated quarterly; least-privilege roles per component.
- The delay explainer receives only shipment status and dates, never customer contact details.

## Operations and rollout
- Dashboards: the four golden signals per component, consumer lag, oldest-event age, provider error rate, explainer cost per day.
- Rollout: shadow mode (dispatcher runs, providers stubbed) for one week; then 5% of orders by order-id hash; then 50%; then 100%. Rollback = switch publish flag back to the inline path.
- Runbooks: provider outage, backlog drain, replaying the dead-letter queue.

## Cost
- Providers dominate: about 12M sends/day; SMS is 70% of spend, so default to push and email where the customer allows.
- Infrastructure: log, KV, wide-column and 6 dispatcher nodes, estimated well under provider spend.
- Explanations: 400K requests/day x (1,500 x $3 + 120 x $15) / 1M = about $2,500/day at list prices; a cheaper routed model and a 400-token input cap are first levers. Daily spend cap enforced at the gateway.

## AI and LLM components
- Use: one bounded model call per delayed order to turn a shipment record into two sentences. No agent and no tools: a single templated call is enough.
- Access: through the model gateway (keys, per-team quotas, cost tracking, rate limits). If the provider is down, the standard template is sent; no hot-path fallback model.
- Budgets: max 1,500 input tokens, 120 output tokens, one call per event, daily spend cap; requests over budget skip the explanation.
- Untrusted content: carrier free-text notes are untrusted input (indirect prompt injection); they are quoted as data, and the output is checked against an allow-list format (two sentences, no URLs, no contact details) before sending.
- Evaluation: 300 labelled historic delays scored for factual match to the shipment record and tone before launch; weekly sample review in operation; regression run on any prompt or model change.
- No write actions: the model cannot send or change anything; the dispatcher decides what is sent.

## Alternatives considered

| Option | Why rejected |
|---|---|
| Keep inline provider calls with longer timeouts | Order checkout latency would still depend on providers |
| Two-phase commit between order DB and log | Blocking on coordinator failure; outbox gives the same atomicity |
| One queue for all channels | One slow provider would delay every channel |
| Agent that decides channel and wording | Unnecessary autonomy; deterministic rules cover channel choice |

## Risks and open questions
1. Confirm peak factor for sale days with the order team (assumed 4).
2. Do both SMS providers support idempotency keys? If not, duplicates are possible after crashes.
3. Legal review of storing masked contact history for 400 days.
4. Carrier note quality: what share of delays have usable notes for explanations?
