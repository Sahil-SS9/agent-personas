---
name: "regression-attribution"
description: "Classify test failures across two git revisions by."
license: "MIT"
---
# Regression Attribution

## When to use
Classify test failures across two git revisions by.

## Method
1. Choose the suspected change revision and a relevant baseline. Keep both immutable and use isolated worktrees or equivalent read-only snapshots.
2. Run the same test command with matched interpreter, dependencies, fixtures, environment and timeout on both revisions.
3. Classify pass-to-fail as a candidate regression, fail-to-fail as baseline or unresolved, fail-to-pass as a fix and pass-to-pass as unchanged. Preserve actual outputs.
4. Repeat nondeterministic cases and check test ordering or shared state before attributing causality. Missing dependency parity makes the comparison inconclusive.
5. Narrow the candidate change and verify a regression test before repair. Do not delete evidence or label all failures introduced merely because they were noticed after a merge.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
