---
name: "system-governance-and-adoption"
description: "Govern contributions, lint drift, and track adoption as the success metric."
license: "MIT"
---

# System governance and adoption

## When to use
Operating a design system over time.

## Procedure
1. Contribution process: propose (with use case) → design + code + a11y review → version → publish. The process is documented and actually followed.
2. Drift linting: CI detects off-system colours/spacing/type/one-off components; drift is a build failure, not a debate.
3. Track adoption as the metric: usage %, off-system incidents, consumer satisfaction. A perfect unused system is a failure.
4. Migrate incrementally: meet teams where they are; codemods and migration guides over big-bang rewrites.
5. Evolve with evidence: retire unused components, split confused ones, add from real demand — every change justified by adoption data.

## Decision rules
- The system serves product teams, not the reverse: friction in the system is a bug.
- Breaking changes need a migration path and a sunset date before merge.

## Pitfalls
- Governance so heavy teams route around it.
- Systems built in isolation then "launched" to no users.

## Done
A governed, linted, adopted system with contribution process and adoption metrics.