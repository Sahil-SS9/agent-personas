---
name: "evidence-led-convergence"
description: "Drive forks and migrations to mergeable or scrap verdicts."
license: "MIT"
---
# Evidence Led Convergence

## When to use
Drive forks and migrations to mergeable or scrap verdicts.

## Method
1. Inventory competing implementations, branches, dependencies and user-approved behaviour before deciding what to merge or discard.
2. Reproduce claims against exact revisions and representative acceptance tasks. Preserve the strongest working implementation rather than preferring the newest branch.
3. Classify differences as required behaviour, compatible improvement, regression, duplicate or unresolved. Record the source and reasoning for each disposition.
4. Integrate in bounded steps with focused and wider tests, verifying cross-component contracts rather than relying on green isolated modules.
5. Preserve recovery references and require approval for destructive history changes. Report one final verified state with visible unresolved limits.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
