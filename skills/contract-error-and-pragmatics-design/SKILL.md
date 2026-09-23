---
name: "contract-error-and-pragmatics-design"
description: "Design errors, pagination, idempotency and field behaviour as first-class contract parts."
license: "MIT"
---

# Contract error and pragmatics design

## When to use
Finalising any API contract: errors and client-facing mechanics are part of the contract, not afterthoughts.

## Procedure
1. Design the error structure with stable codes and consistent shape; document every error with the same rigour as success paths.
2. Distinguish client-fault (fix the request) from server-fault (retry with backoff) in the error semantics; clients will build retry logic on this — make it reliable.
3. Treat as first-class: pagination (default page sizes that don't silently change old-client assumptions), filtering, field masks for partial updates, long-running operations for slow work, request identification for deduplication.
4. Make Create idempotent (client-supplied IDs or idempotency keys) so network retries converge instead of duplicating.
5. Document field behaviour per field: required, optional, output-only, immutable — client generators and validators depend on it.

## Decision rules
- An error a client cannot act on is a defect: every documented error states its cause and the client's next move.
- Pagination added late must default to behaviour compatible with the previously-returned full set, or be a major version.
- Slow operations are modelled as long-running operations, never as long-blocking requests.

## Pitfalls
- 200-OK-with-error-body designs.
- Undocumented output-only fields that client validators choke on.

## Done
Documented error catalogue, pagination/filtering/idempotency decisions, and field-behaviour annotations covering the whole surface.