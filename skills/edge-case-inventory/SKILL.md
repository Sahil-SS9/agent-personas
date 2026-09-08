---
name: "edge-case-inventory"
description: "Indexed edge-case checklists across domains; load only what the task needs."
license: "MIT"
---
# Edge Case Inventory

## When to use
Indexed edge-case checklists across domains; load only what the task needs.

## Method
1. Map the operation’s input space, state transitions, external dependencies and side effects before enumerating edge cases.
2. Check empty, missing, duplicate, malformed, boundary-size, Unicode and out-of-order inputs; distinguish invalid values from valid uncommon ones.
3. Cover cancellation, timeout, retry, partial success, concurrency, stale state, permission denial and recovery. Look for duplicated writes and irreversible side effects.
4. Prioritise cases by impact and plausible occurrence; avoid combinatorial lists with no decision value.
5. Convert important cases into concrete fixtures and expected outcomes. Report untested cases separately from executed tests.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
