---
name: behaviour-specification-from-observation
description: "Turn observed behaviour into a compatibility contract."
version: 0.1.0
author: Hermes
license: MIT
---

# Behaviour specification from observation

Describe externally observable behaviour as a contract that another engineer can implement. This skill does not infer hidden source structure when the evidence only supports outputs.

## Procedure
1. Define the public surface: inputs, outputs, state, timing, environment and side effects.
2. Build normal, boundary, malformed and adversarial-but-safe cases using synthetic or authorised fixtures.
3. Record exact output shapes, ordering, encoding, numeric tolerances, error classes, retry rules and persistence semantics.
4. Model state transitions and idempotency explicitly; distinguish deterministic output from timestamps, random values and platform variance.
5. Add negative controls that look similar but must produce a different result.
6. Mark each statement observed, derived or unknown. Require a second observation for claims that drive compatibility.

## Verification
A specification is implementation-ready when each requirement has an example, an oracle, a tolerance and a provenance entry.
