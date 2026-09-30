---
name: "out-of-scope-and-wontfix-kb"
description: "Record declined and deferred requests as searchable per-concept entries, so the same request is answered once rather than re-litigated."
license: "MIT"
---

# Out of scope and wontfix kb

## When to use
A request is declined, deferred, or answered with "not planned".

## Procedure
1. Decide which kind of decline this is: not-now (roadmap), not-us (wrong project or layer), or already-implemented.
2. For not-now and not-us, write a per-concept entry under the out-of-scope knowledge base: the concept, the decision, the reason, and what would change the answer.
3. Maintain one index so the entries are searchable by concept, not by issue number.
4. Link the closing comment to the entry so the next reporter lands on the reasoning.

## Decision rules
- Already-implemented writes nothing beyond a pointer to the existing feature. Recording an implemented request as out-of-scope is the single worst failure of this skill.
- Entries are keyed by concept. Issue numbers are noise that expires.
- A decline without a reason a future maintainer can re-evaluate is not a decision, it is a shrug.
- Every entry needs a revisit basis (a date, a version, a precondition).

## Decision-output clarification
Separate key type from key value: the durable key is a concept, while its value names the requested capability; issue numbers are references, not the concept identity. Already-shipped requests receive an existing-feature pointer, never a decline entry.

Before returning a structured result, check that each field answers the requested proposition, uses the requested types and vocabulary, and agrees with the explanation. Saved evidence is not an action performed by you; a recommended next step is not an executed action.

## Pitfalls
- Blanket "not planned" with no stated rationale, which guarantees the request returns.
- Knowledge-base rot: entries whose revisit basis passed years ago and were never revisited.

## Done
The decline exists as a searchable concept entry carrying reason and revisit basis — or is deliberately absent because the capability already ships.
