---
name: "update-diff-revetting"
description: "Updates are the attack window: re-vet on every update by diffing the new component against the recorded old one — behaviour, permissions and text."
license: "MIT"
---
# Update Diff Re-vetting

## Use when
- A vetted component publishes an update.
- A dependency or remote reference changes silently.
- A fleet policy says components stay current — safely.

## Instructions

1. The update IS the acquisition: a re-vet on update is part of the trust
   gate, never an optional step. Updates are where quiet behaviour changes
   land while everyone watches the version number.
2. Diff the texts, not the release notes: instruction files, tool
   descriptions, assets and scripts, old against new. Flag every behaviour-
   bearing change — new instructions, changed endpoints, new tool scopes,
   softened constraints.
3. Diff the capability surface: permissions, network endpoints, credential
   access, dependency pins. A permission that grew with no release-note
   mention is a quarantine-grade finding.
4. Diff the BOM: new dependencies, version moves, source changes — resolved
   and compared against the previous BOM (see the SBOM skill).
5. Rate the diff: no behaviour change (note and pass), behaviour change
   within stated scope (re-verify the changed behaviour), behaviour change
   beyond stated scope or new capability (full re-vet at the new risk tier).
6. Record the decision: the fleet runs the vetted version until the re-vet
   passes; auto-update never outruns the gate. A failed re-vet recommends
   pinning the last vetted version — the owner or the host applies the pin,
   this skill only records it.

## Stop conditions
- Never auto-adopt an update past the gate.
- Never accept "bug fixes and improvements" as a diff.
- Never let capability growth pass without a tier re-check.

## Escalation
- Updates that add credential, network or shell scope escalate to the owner
  with the diff — the owner signs the tier change, or the fleet stays
  pinned.
