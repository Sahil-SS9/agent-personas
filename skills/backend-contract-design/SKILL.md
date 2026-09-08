---
name: "backend-contract-design"
description: "Design backend-neutral contracts that real backends satisfy."
license: "MIT"
---
# Backend Contract Design

## When to use
Design backend-neutral contracts that real backends satisfy.

## Method
1. Define the caller-visible contract before choosing an implementation: inputs, outputs, ordering, consistency, errors, cancellation and resource ownership.
2. Test two meaningfully different backends against the same behavioural conformance suite. Do not let the first backend impose undocumented constraints on the second.
3. Specify atomicity and rollback for multi-step writes, concurrent access, duplicate requests and partial failure. Preserve domain error semantics across adapter boundaries.
4. Treat export/import as a contract: type fidelity, identity, schema versions, provenance and verification of restored data must survive a round trip.
5. Reject incomplete adapters explicitly rather than returning fake successful defaults. Record unsupported capabilities and ensure callers handle them deliberately.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
