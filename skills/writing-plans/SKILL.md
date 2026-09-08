---
name: "writing-plans"
description: "Write implementation plans: bite-sized tasks, paths, code."
license: "MIT"
---
# Writing Plans

## When to use
Write implementation plans: bite-sized tasks, paths, code.

## Method
1. Inspect the existing system and restate the user outcome before proposing architecture. Resolve ambiguous decisions that change implementation; preserve explicit constraints.
2. Record baseline, affected components, non-goals, interfaces, data migrations, compatibility and approval boundaries. Avoid creating abstractions without a demonstrated need.
3. For large work, agree phase shape first, then decompose the next phase into independently verifiable tasks with file locations, dependencies and owners.
4. Each task specifies the failing behaviour to demonstrate, the minimal implementation, focused and wider tests, and an integration acceptance check.
5. Include rollback and deployment as separate gates. Label estimates and unknowns; a plan is not implementation evidence.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
