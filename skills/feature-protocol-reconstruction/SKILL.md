---
name: "feature-protocol-reconstruction"
description: "Rebuild how software works: recover features, algorithms and wire protocols into documentation a developer can use."
license: "MIT"
---

# Feature and protocol reconstruction

Turn "what does this thing do" into documentation an engineer can act on: recovered features, algorithms, file formats and wire protocols.

## When to use
Interoperability work, vendor EOL recovery, security review of a protocol or file format, documentation of undocumented software, or due diligence on acquired artefacts.

## Procedure
1. Define the reconstruction contract first: what the deliverable documents (feature inventory, algorithm, format, protocol), at what fidelity, with what evidence standard. Scope creep here is expensive downstream.
2. Recover functionality top-down and bottom-up simultaneously: entry points and UI/CLI surface map the feature inventory; string references, constants and error tables anchor purpose; call graphs connect them.
3. For protocols: separate framing (sync words, lengths, checksums), session (handshake, state), and payload encodings. Extract state machines explicitly — transitions, not prose. Enumerate message types and validate counts against the evidence.
4. For file formats: locate parsers via magic constants and error strings; recover field order, endianness and constraints by constructing test inputs and observing accept/reject edges.
5. Where source lineage exists, differential matching (exact/similar function and symbol correlates) transfers names and semantics from a known sibling; accept matches only when semantics corroborate.
6. Validate the reconstruction empirically: an encoder/decoder or test client that round-trips against the real implementation is the proof of a format/protocol reconstruction; a feature inventory is proven by walking each feature live.
7. Record confidence per claim: which parts are byte-verified, which inferred, which unknown. Unknowns are explicit, not smoothed.

## Decision rules
- A protocol documented without a validating implementation is a draft, labelled as such.
- When evidence conflicts, byte behaviour wins over symbol names; symbol names win over similarity scores.
- Legal and authorisation boundaries are part of scope: reconstruction for interoperability/security review within the owner's rights, never licence circumvention or DRM breaking without explicit owner authority.

## Pitfalls
- Documenting the happy path of a protocol while missing its error/edge states.
- Confusing "the parser accepts X" with "X is the only valid encoding".
- Presenting inferred names as recovered ground truth.

## Done
A reconstruction deliverable (docs, state machines, format specs) with per-claim evidence class and an empirical validation artefact.