---
name: "event-driven-contract-design"
description: "Design async and event-driven contracts: events, webhooks and delivery guarantees."
license: "MIT"
---

# Event-Driven Contract Design

Async contracts are promises too — with harder failure modes.

## 1. Events are versioned contracts
- Define event schema, meaning and versioning like any API; consumers depend on shape.
- Additive evolution; a breaking event change breaks every subscriber silently.

## 2. Delivery semantics, stated
- Declare at-least-once vs exactly-once; design consumers to be idempotent.
- Ordering guarantees (or lack of) must be explicit, not assumed.

## 3. Webhooks need a contract
- Retries with backoff, signatures for authenticity, and a replay/dead-letter path.
- Document expected consumer response and timeout.

## Voice
Idempotent-by-design. Refuse an at-least-once event stream with non-idempotent consumers.
