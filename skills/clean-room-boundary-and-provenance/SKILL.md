---
name: clean-room-boundary-and-provenance
description: "Separate observation, specification and implementation."
version: 0.1.0
author: Hermes
license: MIT
---

# Clean-room boundary and provenance

Keep observation and implementation contexts separate so a compatible reimplementation is based on behaviour and an independently authored specification. This is a process discipline, not legal advice.

## Procedure
1. Write the intended compatibility target, lawful authority, jurisdictions and excluded material before analysis.
2. Create separate observation and implementation records with independent timestamps, hashes and access controls.
3. Observation notes may contain facts about inputs, outputs, errors, state transitions and timing. Do not copy source code, non-public implementation text, proprietary assets or expressive content into the implementation record.
4. Have a reviewer convert observations into a behaviour specification with examples, invariants, error semantics and explicit unknowns.
5. Implement only from the reviewed specification and clean fixtures. Maintain a provenance ledger for every implementation decision.
6. Escalate licensing, contractual, anti-circumvention, trademark, asset and distribution questions to qualified counsel or the owner.

## Verification
The boundary review must prove that implementation inputs are the approved specification and clean fixtures, not raw proprietary artefacts.
