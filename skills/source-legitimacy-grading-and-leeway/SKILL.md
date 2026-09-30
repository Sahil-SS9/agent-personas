---
name: "source-legitimacy-grading-and-leeway"
description: "Assign a defensible verdict to a provider on weighted evidence, and apply graduated leeway so genuinely new providers are admitted provisionally rather than rejected for newness."
license: "MIT"
---

# Source legitimacy grading and leeway

## When to use
Deciding whether a provider may be used, and at what confidence.

## Procedure
1. Score each signal family on explicit evidence, not impressions.
2. Apply the always-required gates first. Failing one is disqualifying regardless of total score.
3. Check hard disqualifiers, each requiring evidence and an attempted challenge before it is applied.
4. Assign the verdict tier from the score.
5. For a provider that is new rather than suspicious, apply leeway: a missing-signal set, a score floor, an exposure cap, and an expiry with re-review.

## Decision rules
- Leeway is granted by missing-signal set, never by inflating scores.
- A newborn provider with clean identity and honest surfaces is a provisional admission, not a rejection. Newness is not a disqualifier.
- Catalogue size scores nothing. A graded provider may have fewer models than a disqualified one.
- Never write fake. Unreachable is not the same as dishonest; record the error instead.
- Hard disqualifiers need evidence plus a challenge attempt.

## Pitfalls
- Letting a big catalogue lift a low-integrity route.
- Treating absence of evidence as evidence of absence for a genuinely new service.
- Applying a hard disqualifier from a single unverified observation.

## Done
Every provider carries a scored verdict, the gates it passed or failed, and either a tier or a recorded disqualifier with its evidence.
