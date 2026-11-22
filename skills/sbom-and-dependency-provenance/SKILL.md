---
name: "sbom-and-dependency-provenance"
description: "Produce and read an agent-component bill of materials: every dependency, its source, its version pin and its upgrade path — before it enters the fleet."
license: "MIT"
---
# SBOM and Dependency Provenance

## Use when
- A component carries or declares dependencies (packages, runtimes, remote
  skills, MCP servers).
- You need to know what a component ACTUALLY pulls in.
- An agent bill of materials is due.

## Instructions

1. Build the component's bill of materials from the shipped artifact, not
   the README: declared dependencies, transitive dependencies, remote
   references, post-install scripts, and anything fetched at runtime.
   The published lesson is stable: what runs is what matters, not what is
   advertised.
2. Pin and record: every dependency gets an exact version and source in the
   record. Floating versions and unpinned remote references are risk
   findings, not conveniences — the component changes without a release.
3. Provenance chain: for each dependency, record who publishes it, from
   where, under what license, and whether the shipped bytes match the
   published source. Dependency-name typosquatting is a real acquisition
   risk; the chain check catches it.
4. Transitive depth with proportionality: one level deep for read-only
   helpers; full resolution for anything with shell, network or credential
   access.
5. Vulnerability overlay: map the BOM against published advisories at vet
   time, and record the date of the check — a clean BOM is clean as of its
   check date, and says so.
6. The BOM is a living record: re-resolved on every update, and the diff
   between old and new BOM is what the re-vet reviews.

## Stop conditions
- Never accept "no dependencies" from the README without resolving what the
  artifact actually references.
- Never ship an unpinned runtime fetch in a trusted component.
- Never present a BOM as clean without its check date.

## Escalation
- Dependencies with known advisories, dead maintenance or unresolvable
  provenance escalate with the BOM entry and the options (pin, patch,
  refuse).
