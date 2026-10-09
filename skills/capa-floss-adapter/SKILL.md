---
name: "capa-floss-adapter"
description: "Use capa capability rules and FLOSS string deobfuscation as triage hypothesis generators, always with manual verification."
license: "Apache-2.0"
---

# capa / FLOSS adapter

capa maps code to capability rules; FLOSS deobfuscates stack/encoded strings. Both are HYPOTHESIS generators: their output ranks where to look, and is never a conclusion. (Adapter structure original; tools are MIT/Apache third-party projects referenced, not embedded.)

## When to use
Early triage and targeted sweeps on executable artefacts; most valuable on packed-adjacent or unfamiliar samples. Requires: tools installed/hosted in the analysis environment, version recorded.

## Procedure
1. Run as evidence-backed triage: capa with its rule-version and match-locations; FLOSS with its decoded-string listings tied to addresses. Archive raw outputs with the evidence package.
2. Verify before reporting: each capability match is confirmed by reading the code path (the binary-structure-assembly loop) before it becomes a finding; mismatches between rule hits and actual code are recorded too.
3. Use FLOSS decoded strings to re-seed the search: config keys, C2 formats, command tables — then decode and hash the recovered artefacts through the security-investigation member.
4. Record limitations honestly: capa cannot reason about dynamically-decrypted capabilities it never saw; packed samples under-report; version-specific rules drift.

## Decision rules
- A capability label never appears in a report without its verifying evidence or an explicit "rule-hits only, unverified" tag.
- Strings (plain or decoded) are hints; behaviour requires the mechanism chain.

## Pitfalls
- Copying capa output into findings verbatim.
- Treating a rule-version change as a behaviour change in the artefact.

## Done
Raw outputs archived, per-rule verification status recorded, decoded artefact hashes captured, limitations stated.