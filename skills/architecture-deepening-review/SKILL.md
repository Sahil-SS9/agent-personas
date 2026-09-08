---
name: "architecture-deepening-review"
description: "Find architectural deepening opportunities in a."
license: "MIT"
---
# Architecture Deepening Review

## When to use
Find architectural deepening opportunities in a.

## Method
1. Look for interfaces that expose too much implementation detail relative to the capability they provide. Inspect concrete callers before recommending consolidation.
2. Identify repeated caller obligations, pass-through layers, exception propagation and changes that routinely require edits across modules.
3. Propose a deeper module only when it can hide real complexity behind a smaller stable contract. Separate essential domain complexity from accidental indirection.
4. Compare incremental alternatives with compatibility, testability and migration costs. Avoid turning unrelated responsibilities into a single large module.
5. Validate the proposal on representative call paths and retain existing behaviour with tests before implementation.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
