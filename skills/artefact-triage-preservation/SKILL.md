---
name: "artefact-triage-preservation"
description: "Triage unknown files safely: identify, fingerprint, chain-of-custody and preserve evidence before any analysis."
license: "MIT"
---

# Artefact triage and preservation

Treat every unknown file as a crime scene: what you touch, you alter. Stabilise before you study.

## When to use
First contact with an unknown artefact: a binary, document, firmware image, disk or memory capture, archive or email attachment.

## Procedure
1. Work on copies only. The original becomes read-only evidence immediately; every derived copy records the original's SHA-256.
2. Identify before tools touch it: file signature/magic, container structure, hashes, size, timestamps. Treat `file` output as a hypothesis — packed or malformed files lie.
3. Establish provenance: where it came from, when, from whom; record the acquisition channel. A sample without provenance is reported as such.
4. Choose the containment level before any execution: presumed hostile unless the owner's scope says otherwise. Execution decisions belong to the runtime-investigation stage, never the triage stage.
5. Package evidence: archive (original + hashes + notes + tool versions + a timeline of every action taken) with a manifest that lets a stranger reproduce the workspace.
6. Triage depth ladder: signature → container/packer hints → strings (as hints, not conclusions) → imports/capabilities (hypotheses) → deeper analysis only with a written question the step will answer.
7. Timebox the pass: triage aims to route the artefact (what is it, how dangerous to handle, what it likely is) — not to answer every question.

## Decision rules
- An execution decision made during triage is a defect: route, do not run.
- `ldd`, debuggers and instrumentation are not read-only operations; if a tool can execute or modify the artefact, it does not belong in triage.
- If identification is ambiguous (packed, obfuscated, unusual entry), say so and hand over the ambiguity, not a forced guess.
- Archive integrity is part of done: the manifest verifies, or the triage is not done.

## Pitfalls
- Opening archives with auto-extraction tools that execute contained code or follow links.
- Treating strings/imports as evidence of behaviour rather than capability hints.
- Losing timestamps by copying without preserving metadata.

## Done
An evidence package with verified hashes, provenance, identification with stated confidence, containment decision, routing recommendation and retained ambiguity.