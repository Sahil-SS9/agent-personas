---
name: "reviewed-agent-development"
description: "Execute plans via reviewed agent tasks (2-stage review)."
license: "MIT"
---
# Reviewed Agent Development

## When to use
Execute plans via reviewed agent tasks (2-stage review).

## Method
1. Use only when delegation is authorised and tasks have explicit boundaries. Otherwise perform the workflow directly and label the absence of independent review.
2. Read the approved plan once; give each worker the complete task, constraints, input pointers, output format and observable completion criteria.
3. Assign fresh context and disjoint write ownership. Require witnessed failing tests before implementation, focused passing checks and relevant wider regressions.
4. Review spec compliance before code quality. A worker summary is a claim: inspect the artefact and reproduce important evidence before accepting either gate.
5. Send specific findings back for bounded repair and recheck. Run final integration checks across tasks; never imply that self-review is independent.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
