---
name: "architecture-characteristics-driven-design"
description: "Elicit the few driving quality attributes and give each a measurable target."
license: "MIT"
---

# Architecture-characteristics-driven design

Design from the qualities the system must exhibit, not from a favourite technology.

## When to use
At the start of any system design, before drawing structure or naming tools.

## Procedure
1. Elicit candidate characteristics from the problem + constraints: performance, scalability, availability, latency, security, evolvability, cost, operability, data integrity.
2. Rank ruthlessly. Mark at most the 3-5 that actually shape structure as "driving". An "everything is critical" list is a non-decision — force trade choices.
3. For each driving characteristic, write a measurable fitness target (e.g. p99 < 200 ms, RTO < 5 min, 99.9% monthly availability). Drop any "-ility" you cannot make testable; it is an aspiration, not a requirement.
4. Record the implicit characteristics you are consciously NOT optimising, so later reviewers know the trade was deliberate.

## Decision rules
- No structure decision is justified until its driving characteristic is named and quantified.
- Prefer the characteristic the domain truly needs over the strongest available (strong consistency and five-nines have real cost).
- If two driving characteristics conflict (e.g. latency vs strong consistency), state the conflict and the chosen balance explicitly.

## Pitfalls
- Copying a reference architecture's characteristics instead of eliciting the system's own.
- Untestable adjectives ("fast", "secure") passed off as requirements.

## Done
A ranked, quantified list of driving characteristics with deliberate non-goals, ready to drive structure.
