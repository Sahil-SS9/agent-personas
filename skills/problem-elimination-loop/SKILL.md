---
name: "problem-elimination-loop"
description: "Convert recurring tickets into permanent fixes via problem management discipline."
license: "MIT"
---
# Problem Elimination Loop

## Use when
- The same ticket class keeps reappearing across weeks
- Workarounds are accumulating into folklore
- Nobody can say which issues are 'fixed forever' vs 'temporarily calm'

## Instructions

1. Track ticket classes, not just tickets: cluster by symptom+cause pair;
   a class with N recurrences is a PROBLEM-candidate with a name.
2. For each problem candidate: quantify cost (tickets/week, affected users,
   minutes lost), identify the underlying defect or gap, and file it to the
   owning team WITH the evidence pack.
3. Workarounds are registered explicitly with expiry intent — a workaround
   without a fix-tracking link is technical debt with a friendly face.
4. After each permanent fix: verify recurrence actually stops (watch the
   class for its typical interval), then close the problem record with the
   before/after data.

## Stop conditions
- Never declare elimination while recurrences continue inside the observed
  window.
- Never let workaround documentation replace the fix backlog entry.

## Escalation
- High-cost problems without an owning team escalate to engineering
  leadership with the quantified cost attached.
