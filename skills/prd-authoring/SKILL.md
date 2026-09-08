---
name: "prd-authoring"
description: "Write outcome-first product requirement docs with pre-committed success metrics."
license: "MIT"
---
# PRD Authoring

## Use when
- A feature/problem is approved for specification
- Stakeholders disagree on what is being built or why
- A PRD exists but nobody can name its success metric

## Instructions

1. Open with the problem: who hurts, how often, what they do today, and the
   evidence it matters. No solution language before this section exists.
2. State requirements as outcomes + constraints, not screens: what must be
   true for the user, what is explicitly out of scope.
3. Commit success metrics BEFORE build: adoption/engagement/business KPI,
   each with baseline, target, and measurement method.
4. Frame the opportunity space before the chosen solution (Torres's
   Opportunity Solution Tree): outcome -> candidate opportunities -> why
   THIS solution. Name the leading indicator per slice — the small user
   behaviour that predicts success (Seiden).
5. Validate problem claims with past-behaviour interviews, not opinion
   requests (Mom Test: talk about their life, not your idea).
6. Include risks and open questions visibly; a PRD without open questions
   has not been honestly written.

## Stop conditions
- Never ship a PRD whose metrics were chosen after the solution.
- Never write requirements that specify UI before behaviour.

## Escalation
- If the problem statement cannot be evidenced, escalate back to discovery —
  do not paper over it with confident prose.
