---
name: "provider-brief-authoring"
description: "Write the brief a decision-maker can act on: the requirement, the ranked routes, the verdicts, the rejected routes, and the recommendation with its residual risk."
license: "MIT"
---

# Provider brief authoring

## When to use
Delivering a sourcing recommendation, or revisiting one.

## Procedure
1. State the requirement in the user's terms: the model, the workload, the constraints, the budget.
2. Rank routes, one row per route rather than per vendor.
3. Give each a verdict with the one-line basis.
4. List the rejected routes and the disqualifier that removed each.
5. State what remains unknown, then the recommendation with its residual risk and the fallback.

## Decision rules
- Separate verified from partially verified from unverified. Never launder a claim into a fact by repetition.
- An unknown is a line item, not an omission. Omissions read as certainty.
- Every recommendation carries a fallback and an exit cost.
- If the honest answer is that no route qualifies, say that.

## Pitfalls
- Recommending the cheapest option when a gate failure should have excluded it.
- Presenting one route as settled when two are close; state the trade-off instead.
- Reporting a price without the basis and date.

## Done
The brief names the requirement, ranked routes with verdicts, rejected routes with reasons, unknowns, and a recommendation with its fallback.
