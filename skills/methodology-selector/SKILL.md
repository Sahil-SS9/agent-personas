---
name: "methodology-selector"
description: "Evaluate a project or change request and recommend the best-fit delivery approach."
license: "MIT"
---
# Methodology Selector

## Use when
- Kicking off a new project, feature, or significant change request
- Asked "should we use agile/waterfall/Shape Up/lean for this?"
- A delivery approach is failing and the team suspects mis-fit

## Instructions

1. Score the request against the six decision dimensions BEFORE naming any
   methodology: requirements stability; stakeholder availability; risk
   tolerance (predictable plan vs learning); team experience; regulatory
   constraints; time-to-market pressure.
2. Map the profile to an approach:
   - Stable requirements + low availability + fixed scope -> predictive
     (waterfall) elements
   - Uncertain requirements + engaged stakeholders + learning needed ->
     agile iteration
   - Mixed -> design a hybrid that isolates predictable elements (compliance,
     procurement, infra) and iterates the uncertain customer-facing core
   - Product work with appetite for scope cuts + senior small team ->
     Shape Up-style cycles with shaped pitches
3. For engineering-practice fit inside the chosen approach:
   - TDD default where behaviour is precisely specifiable
   - Specification-by-example (BDD/ATDD) ONLY where acceptance criteria are
     genuinely shared with non-developers AND collaboration time exists;
     tooling without collaboration is expensive scripting
   - Lean/Kanban flow for continuous-arrival operational work
4. Name the prioritisation regime explicitly per decision: RICE-style
   scoring OR appetite capping (Shape Up) — never mix vocabularies
   mid-decision. Appetite caps investment regardless of score.
5. Present the recommendation with the scored table, the chosen approach,
   its known failure modes for THIS context, and a review checkpoint
   (approaches are re-assessed at boundaries, never silently drifted).
5. Change requests during committed cycles: classify defect/enhancement/
   pivot; queue to next boundary unless crisis; every accepted CR needs goal
   linkage + appetite + acceptance examples.

## Stop conditions
- Never recommend a methodology by org fashion or prior project habit alone.
- Never leave hybrid design vague ("we'll mix it") — name which elements are
  predictive and which iterative.

## Escalation
- Regulatory or contractual constraints override efficiency preferences;
  flag compliance-owned elements explicitly in the recommendation.
