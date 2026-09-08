Source: https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/
Author: Malcolm Featonby
Read scope: Full article prose, not linked articles or a book
Captured: 2026-09-08T19:32:09.322374+00:00
Rights: original distillation; source rights retained; no source text redistribution.
Target: implementation-delivery

# Remote operations: intent and uncertain outcomes

Load when implementing a mutating remote operation or its retries, not for every local function.

## Failure model
A timeout means the caller does not know the outcome; it does not establish that the side effect failed. Identify the caller, operation, target resource, remote effect, deduplication store and response persistence boundaries. Mark which boundaries share a transaction and which do not.

## Procedure
1. Define the idempotency key scope: caller or tenant plus operation and caller-supplied intent identifier. Equal payloads can represent distinct legitimate operations; do not deduplicate by payload hash alone.
2. Store original request parameters with the key. Reuse with conflicting intent is a validation conflict, not permission to silently overwrite or repeat the effect. Define which fields express intent under the actual API contract.
3. Specify first arrival, concurrent duplicate, completed duplicate and ambiguous/in-progress states. Decide whether duplicate callers wait, receive a stable pending result, or reconcile; do not invent an HTTP status or timing promise without a contract.
4. Where possible, commit deduplication state and local mutation atomically. A local database transaction cannot include an arbitrary remote charge. If that boundary is external, use the provider's idempotency contract or reconciliation keyed to the same intent. Otherwise report the guarantee as limited instead of claiming exactly-once. This cross-service application is our synthesis, not a universal mechanism supplied by the article.
5. Record retry response semantics explicitly. Semantically equivalent is not necessarily byte-identical: resource status may change while resource identity and operation meaning remain stable. Preserve a stricter existing response-replay contract where required.
6. Define retention, expiry, token reuse and late arrival after resource deletion. The resource lifetime plus grace period in the source is an EC2 example, not a universal TTL. Never pick a retention number from intuition or recreate a deleted resource on a late retry contrary to the declared contract.
7. Bound retries and escalate uncertain outcomes. This article does not authorise indefinite retries or a specific retry/backoff schedule.

## Evidence packet
Return key scope, intent fields, state table, atomicity boundary, crash windows, retry semantics, retention rationale, and tests actually run. If concurrency is out of scope, say so rather than suggesting it was tested.

## Acceptance scenarios (not executed by these notes)
- Two simultaneous requests with the same scoped intent produce only the contracted effect.
- Effect succeeds but response is lost; retry reconciles without a second effect.
- Local success-record write fails after a remote effect; retry must not blindly repeat it.
- Same key across tenants remains isolated; changed intent on the same scoped key conflicts.
- Retry after resource deletion or token expiry follows the documented retention rule.

## Negative control
Two identical orders with different caller intent identifiers must remain distinct. A read-only operation need not acquire a deduplication ledger.
