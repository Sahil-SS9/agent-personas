---
name: "capability-evaluation"
description: "Evaluate existing capabilities during rebuild programmes."
license: "MIT"
---
# Capability Evaluation

## When to use
Evaluate existing capabilities during rebuild programmes.

## Method
1. Define the real user capability and its delivery boundary before comparing implementations. An installed package or reachable endpoint is not proof of a useful capability.
2. Inventory existing behaviour, dependencies, ownership, cost and failure modes. Reuse verified components before proposing replacements.
3. Compare keep, repair, replace and retire against the same representative acceptance tasks. Record unsupported assumptions and migration costs.
4. Verify the recommendation with actual artefacts and failure cases. Keep code readiness, deployment readiness and observed user outcomes separate.
5. Present the trade-off and exact approval requested. Do not start a migration or delete the old system during assessment.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
