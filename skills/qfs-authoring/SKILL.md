---
name: "qfs-authoring"
description: "Turn demo promises into qualification functional specifications with traceable evidence."
license: "MIT"
---
# QFS Authoring

## Use when
- Capabilities were shown in a demo and must become committed, testable scope
- Preparing release-candidate qualification criteria
- Auditing whether shipped behaviour matches demonstrated claims

## Instructions

1. Capture every demo claim as a numbered commitment: what was shown,
   under which conditions, in which environment.
2. Convert commitments to acceptance criteria with owners and evidence
   links (test IDs, recordings). Demo-to-spec-to-test traceability is the
   whole point — no orphan promises.
3. Define the qualification gate: which criteria must pass for release,
   which degrade gracefully, which are explicitly out of scope now.
4. Reconcile post-release: shipped behaviour audited against the QFS;
   deltas become follow-up requirements or documented limitations.

## Stop conditions
- Never let a demoed capability ship without its QFS entry passing or being
  explicitly descoped with stakeholder sign-off.
- Never write criteria that cannot be evidenced by a test or observation.

## Escalation
- Claims/product divergence discovered late escalates to PM and the account
  owner together — never silently patched or silently dropped.
