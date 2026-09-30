---
name: "inbound-pr-review"
description: "Review an external pull request: judge intent before diff, check scope against the issue, assess testability, and reach one defensible disposition."
license: "MIT"
---

# Inbound pr review

## When to use
An external pull request needs a judgement.

## Procedure
1. Read the linked issue first. A pull request is an issue with code attached; the intent is what you are judging.
2. Read the diff for correctness, then for scope, then for style. In that order.
3. Check that CI is meaningful for the change and that new behaviour carries a test.
4. Check the change against the contribution policy, especially any change to CI, dependencies, or secrets.
5. Decide whether this is reviewable in one pass. If not, say so and ask for a split rather than silently stalling.
6. Write the review: the decision, the basis, and the single most useful next action.

## Decision rules
- Review for correctness and scope, not personal preference. Style belongs in an automated check.
- A large diff is not automatically rejected; an unfocused diff is.
- Require a test where behaviour changes and a test is feasible.
- If a maintainer could fix it faster than the author can, say so and offer that path instead of a review ping-pong.

## Pitfalls
- Reviewing formatting before understanding intent.
- Accepting an unrelated feature smuggled inside a bug fix.
- Ghosting an author who is waiting on a decision, which converts a contributor into an ex-contributor.

## Done
Exactly one disposition is recorded, and the author has an actionable next step or an honest, explained close.
