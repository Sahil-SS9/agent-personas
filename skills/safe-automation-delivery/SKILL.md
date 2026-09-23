---
name: "safe-automation-delivery"
description: "Deliver automations that are idempotent, observable, rollback-safe, and failure-bounded."
license: "MIT"
---

# Safe automation delivery

## When to use
Building or changing any automated workflow, script, or pipeline.

## Procedure
1. Design idempotency first: same input → same intended effect; retries converge instead of duplicating. Key operations idempotently; make side effects dedupable.
2. Bound the blast radius: dry-run mode as default, explicit scope limits, rollback path proven before first real run, human approval gate for irreversible actions.
3. Make every run observable: structured output recording what ran, what changed, what failed, with evidence links. An automation whose success cannot be verified did not succeed.
4. Apply 12-factor discipline: config in the environment; backing services as attached resources; strict build/release/run separation; stateless processes; fast startup and graceful shutdown; logs as event streams; dev/prod parity. One-off admin tasks run as one-off processes against the same codebase — never snowflake shell history.
5. Write the failure playbook before the success path ships: top failure modes, detection, first response, rollback, owner.

## Decision rules
- Non-idempotent side effects are defects in an automation, not quirks.
- No irreversible action without an approval gate and a proven rollback.
- Success claims require verifiable output; "it seemed to work" is a failure.

## Pitfalls
- Testing only the happy path on the happy data.
- Rollback that has never been executed until the night it is needed.

## Done
An idempotent, observable, rollback-safe automation with failure analysis, dry-run evidence, and documented ownership.