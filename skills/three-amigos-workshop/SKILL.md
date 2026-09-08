---
name: "three-amigos-workshop"
description: "Run 3 Amigos sessions that turn stories into example-driven acceptance criteria."
license: "MIT"
---
# Three Amigos Workshop

## Use when
- A story is about to enter development (1-2 weeks out, not earlier)
- Acceptance criteria are contested, vague or unwritten
- Requirements misunderstandings keep surfacing during review instead of before

## Instructions

1. Convene the three perspectives: business (PO/BA) brings the problem and
   business rules; developer brings feasibility, constraints and design
   implications; tester/QA brings edge cases and measurability. Additional
   perspectives join when relevant (security, ops), but three is the core.
2. The business participant presents the PROBLEM with concrete examples —
   who needs this, why, what they can do afterwards (not solution screens).
3. Derive acceptance criteria AS EXAMPLES collaboratively: realistic input/
   outcome pairs covering normal paths, edge cases and failure modes. Where
   shared understanding matters, examples become executable specifications
   (Specification-by-example habit).
4. Timebox: 15-30 minutes per story. If it overruns, the story is too big —
   slice it and re-convene on the slice.
5. Output is written down in the ticket: agreed examples, open questions
   with owners, and a definition-of-done check. Unwritten agreements do not
   count.
6. Cadence: fold into backlog refinement for flow; call ad-hoc sessions when
   a story is unclear or criteria are disputed.

## Stop conditions
- Never leave a session without written, example-based acceptance criteria.
- Never use 3 Amigos to design solutions — it discovers WHAT, not HOW.

## Escalation
- Persistent disagreement on criteria escalates to the Product Manager as a
  discovery gap, not forced consensus in the room.
