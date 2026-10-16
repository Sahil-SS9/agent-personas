---
name: clean-room-boundary-and-provenance
description: "Separate observation, specification and implementation."
version: 0.2.0
author: Hermes
license: MIT
---

# Clean-room boundary and provenance

Keep observation and implementation contexts separate so a compatible implementation is based on behaviour and an independently reviewed specification. This is process guidance, not legal advice.

## Gate before work
State the lawful authority, target, jurisdictions, licence/contract scope, intended distribution and excluded material. Escalate legal, anti-circumvention, trademark, asset and commercial-use questions to qualified counsel or the owner.

## Two-context procedure
1. Create separate observation and implementation workspaces with access controls, timestamps and hashes.
2. Observation may record externally visible inputs, outputs, errors, state transitions, timing and environment. Do not transfer source code, decompiler text, non-public implementation detail, proprietary assets or expressive content.
3. Have an independent reviewer transform observations into a behaviour specification containing examples, invariants, tolerances and explicit unknowns.
4. Freeze the approved specification and clean/redistributable fixtures. The implementer works only from that packet.
5. Maintain a provenance ledger for every implementation decision: requirement ID, fixture, author, date, dependency licence and generated artefact hash.
6. Run a boundary audit before parity testing and again before release. Quarantine any contaminated packet; do not silently edit its history.

## Verification
The implementation workspace must be reproducible from the approved specification and clean fixtures alone. The audit must list excluded material, unresolved questions, reviewers and corrective action. Never claim legal compliance or clean-room status merely because source files were not copied.
