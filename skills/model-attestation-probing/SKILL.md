---
name: "model-attestation-probing"
description: "Test whether the service actually serves the model it claims, rather than inferring it from the catalogue."
license: "MIT"
---

# Model attestation probing

## When to use
Before recommending a route, and periodically for routes carrying real traffic.

## Procedure
1. Record the claimed model identity: name, version, context length, and any stated quantisation.
2. Probe behaviour that discriminates the claimed model from cheaper substitutes: tokeniser edge cases, context limits, knowledge cut-offs, refusal and style fingerprints.
3. Compare responses across the route and a trusted reference; look for systematic differences rather than single answers.
4. Check whether the response metadata is honest where it is exposed.
5. Repeat, because routing can change without notice.

## Decision rules
- A catalogue entry is a claim. Attestation is a test.
- Single-prompt comparisons prove nothing; use discriminating probes and repeat.
- Undocumented quantisation is a quality change, not a detail.
- If you cannot discriminate, say so instead of asserting parity.

## Pitfalls
- Treating an OpenAI-compatible endpoint as proof of the model.
- Concluding from one clever prompt.
- Failing to re-test after a provider changes its terms or pricing.

## Done
Each claimed model carries a probe result at a recorded date, and any mismatch is labelled.
