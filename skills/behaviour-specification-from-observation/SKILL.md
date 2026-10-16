---
name: behaviour-specification-from-observation
description: "Turn observed behaviour into a compatibility contract."
version: 0.2.0
author: Hermes
license: MIT
---

# Behaviour specification from observation

Turn externally observable behaviour into an implementation-ready contract. Do not infer hidden source structure when the evidence only supports outputs.

## Inputs and boundary
Record authority, target/version/platform, test environment, fixture provenance, hashes and the question being answered. Use only synthetic or owner-authorised inputs. Separate observation from interpretation; label every statement observed, derived or unknown.

## Procedure
1. Inventory the public surface: inputs, outputs, state, timing, environment, persistence and side effects.
2. Build a matrix of normal, boundary, malformed and safe negative-control cases.
3. Capture exact output shape, ordering, encoding, numeric tolerance, error class/message policy, retries and idempotency.
4. Model state transitions, concurrency assumptions and reset conditions explicitly.
5. Repeat compatibility-critical observations with an independent fixture or run; document nondeterminism and platform variance.
6. Convert observations into invariants plus executable examples. Do not copy source, proprietary assets or expressive text into the implementation packet.
7. Review unknowns and unresolved legal/licensing boundaries before handoff.

## Contract format
Each requirement has: ID; input fixture/hash; precondition; action; expected output/error; tolerance; state transition; oracle; provenance; confidence; known exclusions. Include a versioned change log.

## Verification
A specification is implementation-ready only when every requirement has an oracle and example, every negative control differs for a stated reason, unknowns are visible, and a second observation supports each compatibility-critical claim. A passing example is not proof of untested behaviour.
