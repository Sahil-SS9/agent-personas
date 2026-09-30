---
name: "inbound-issue-triage-and-severity"
description: "Triage an incoming issue: find the ask, dedupe against history, classify, set severity from impact and reach, and issue a durable agent brief."
license: "MIT"
---

# Inbound issue triage and severity

## When to use
A new or updated issue arrives and nobody has decided what it is or how much it matters.

## Procedure
1. Read the whole report including comments; identify the actual ask before the diagnosis.
2. Search for duplicates and prior rejections by title, subsystem and error string. Link to the canonical rather than re-deciding.
3. Classify into one of the two category families and exactly one state; the invariant is one state, never zero and never two.
4. Set severity from impact x reach (data loss, security, silent wrongness) — never from the reporter's tone or capitalisation.
5. Produce a durable brief: the goal, the constraints, the definition of done, and the types of change allowed. Briefs name the goal and type, not file paths.
6. Set expectations in the thread: what happens next and, honestly, when.

## Decision rules
- Exactly one state at a time; record transitions, not a label pile.
- A support question is not a bug; answer it without creating a bug record.
- Severity is a claim about consequence. If you cannot state the consequence, it is not high.
- Never ask a reporter to reproduce something you can reproduce yourself.

## Decision-output clarification
Report the resolved classification and recommended single active state separately from any conflicting proposed labels; do not endorse a two-state pile. Distinguish a reply category from the actual message: if a caller requests a controlled category, use that vocabulary and place explanation in its explanation field. For support, answer the documented usage question without inventing an unavailable option or creating a bug.

Before returning a structured result, check that each field answers the requested proposition, uses the requested types and vocabulary, and agrees with the explanation. Saved evidence is not an action performed by you; a recommended next step is not an executed action.

## Pitfalls
- Severity inflation, which destroys the meaning of the field within weeks.
- Recording an already-implemented request in the out-of-scope knowledge base: it poisons every later duplicate check.
- Reopening a closed decision with no new evidence.

## Done
The issue carries exactly one state, a severity with a stated basis, a canonical link if duplicates exist, and either a brief or a stated reason there is none.
