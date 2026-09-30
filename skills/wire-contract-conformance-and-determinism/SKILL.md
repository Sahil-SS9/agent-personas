---
name: "wire-contract-conformance-and-determinism"
description: "Verify a model or port against the wire contract it claims to implement — because most ports fail on contract details, not on model quality."
license: "MIT"
---

# Wire contract conformance and determinism

## When to use
Adopting a community port or a self-hosted endpoint, or replacing one implementation with another.

## Procedure
1. Obtain the numbered contract requirements: request shape, response shape, scoring semantics, error behaviour, batching.
2. Build a deliberately-broken mock and confirm your conformance tests catch it.
3. Score the implementation against each requirement and record failures individually.
4. Test determinism: identical requests must produce identical decisions across runs.
5. Test the degraded paths: missing option sets, oversized inputs, malformed requests.

## Decision rules
- A port that produces plausible answers can still violate the contract. Conformance is separate from quality.
- Determinism is a contract property, not a nice-to-have, wherever routing decisions are reproduced.
- Score conformance numerically so implementations can be compared.
- Prefer the implementation that conforms over the one that merely works on your sample.

## Decision-output clarification
A plausible happy-path answer never establishes wire-contract conformance. Report that proposition false when only answer quality is evidenced, and assess numbered requirements and repeated-request determinism independently.

Before returning a structured result, check that each field answers the requested proposition, uses the requested types and vocabulary, and agrees with the explanation. Saved evidence is not an action performed by you; a recommended next step is not an executed action.

## Pitfalls
- Judging a port on a couple of happy-path calls.
- Assuming an OpenAI-compatible surface means contract compliance.
- Accepting floating-point-level score drift as harmless when downstream thresholds are hard.

## Done
Every contract requirement has a pass or fail with evidence, determinism is demonstrated, and degraded paths are tested.
