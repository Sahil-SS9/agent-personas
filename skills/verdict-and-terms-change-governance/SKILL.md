---
name: "verdict-and-terms-change-governance"
description: "Re-test when a provider changes and communicate the change: verdicts expire, and silent term changes are the common failure."
license: "MIT"
---

# Verdict and terms change governance

## When to use
A provider updates pricing, terms, catalogue, ownership or status; or a verdict reaches its expiry.

## Procedure
1. Maintain re-test triggers: terms, pricing, catalogue, entity, registrar, ownership, status page, sub-processor list.
2. Hash the contract surfaces you graded so you can detect change cheaply.
3. On change, re-run only the affected signals, not the whole dossier.
4. Recompute the verdict and record the delta.
5. Communicate the change to whoever depends on the route, with what they must do.

## Decision rules
- Verdicts expire. An unexpired verdict is a statement about a date, not about today.
- Re-verify the minimum set on change; do not re-litigate the whole dossier.
- A downgrade is urgent when it affects data terms, not only when it affects price.
- A provider that changes terms without notice has told you something about itself; record it.

## Decision-output clarification
Keep notification required, drafted, sent and acknowledged as separate evidence states. An unsent draft cannot establish that an owner was notified; a record of a draft is not a completed notification record. Expiry still requires re-verification when no terms change is observed.

Before returning a structured result, check that each field answers the requested proposition, uses the requested types and vocabulary, and agrees with the explanation. Saved evidence is not an action performed by you; a recommended next step is not an executed action.

## Pitfalls
- Leaving a verdict in place because nothing appeared to change.
- Re-testing price and not retention.
- Announcing a change without stating the migration step.

## Done
Every verdict has an expiry and a trigger set, and each change has a recorded delta and a notified owner.
