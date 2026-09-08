---
name: "change-request-evaluator"
description: "Triage feature requests and change requests into evidence-based recommendations."
license: "MIT"
---
# Change Request Evaluator

## Use when
- A stakeholder asks for a new feature or change mid-delivery
- A backlog of requests needs structured triage
- Someone says "this should be quick" without evidence

## Instructions

1. Classify each request: defect / enhancement / strategic pivot. Defects
   route to QA triage; enhancements get full evaluation; pivots need goal
   re-alignment before anything else.
2. Evaluate enhancements on four axes: goal linkage (which business goal,
   stated how), user impact (who and how many), effort/appetite (small/large),
   reversibility. RICE-style scoring is fine but the axes matter more than
   the formula.
3. Check discovery state first (dual-track rule): has this request been
   validated with evidence, or is it an unvalidated idea entering delivery?
   Unvalidated CRs route back to discovery unless trivially reversible.
4. Produce a recommendation: accept now / accept at boundary / reject with
   rationale / split into smaller shippable slices. Include what evidence
   would change the recommendation.
4. Protect committed work: mid-cycle CRs queue unless genuine crisis; the
   cost of interruption is paid by the whole team's throughput.
5. Record the decision and rationale where the requester can see it —
   visible rejection beats silent backlog death.

## Stop conditions
- Never evaluate a CR without understanding the underlying goal first.
- Never accept scope growth into a committed cycle without explicit
  trade-off acknowledgement from the owner.

## Escalation
- Strategic pivots go up to product ownership with your analysis attached,
  not decided unilaterally.
