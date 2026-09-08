---
name: "writing-spec"
description: "Write or revise spec.md and close a council REVISE verdict."
license: "MIT"
---
# Writing Spec

## When to use
Write or revise spec.md and close a council REVISE verdict.

## Method
1. Restate the user problem, desired outcome, scope, non-goals and existing constraints before describing a solution.
2. Define observable behaviours, inputs and outputs, error cases, data contracts, permission boundaries and acceptance evidence.
3. Trace each requirement to a decision or source. Resolve reviewer findings explicitly; do not mark a revision addressed without showing the change.
4. Separate locked decisions from open questions. Include compatibility, migration, rollback, operational limits and verification where applicable.
5. Keep implementation detail only where it constrains correctness. Obtain approval for substantive scope changes and never treat a written spec as a delivered feature.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
