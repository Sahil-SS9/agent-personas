---
name: "api-compatibility-analysis"
description: "Classify every proposed API change as compatible or breaking across all three dimensions."
license: "MIT"
---

# API compatibility analysis

## When to use
Every proposed change to a published contract, without exception.

## Procedure
1. Check all three dimensions: source compatibility (client code compiles/runs), wire compatibility (serialization matches), semantic compatibility (reasonable expectations hold). Old clients must keep working within a major version.
2. Classify the change: SAFE — adding optional components, adding enum values to request-only enums, additive fields with back-compatible defaults. BREAKING — removing or renaming anything (rename = remove+add), moving fields between files or into/out of oneofs, changing field types, changing resource names, changing defaults, changing value formats (e.g. IPv4 → IPv6), changing default serialization.
3. Apply the judgement rule: code depends on behaviour even when undocumented — do not change visible semantics reasonable user code relies on. When in doubt, it is breaking.
4. For breaking needs: new major version; version explicitly (semver-shaped); announce deprecations with timelines and a migration path; never remove in minor/patch.

## Decision rules
- Every change gets a written compatible/breaking classification with reasoning — "should be fine" is not a classification.
- Prefer additive evolution; when a replacement field is added alongside the old, specify resolution of conflicting inputs explicitly.
- Pagination added after launch must not shrink what older clients receive by default.

## Pitfalls
- Treating wire-compatible as safe when source compatibility breaks (type changes, file moves).
- Silently changing output-only field formats.

## Done
Per-change classification across all three dimensions with a versioning decision and deprecation path where breaking.