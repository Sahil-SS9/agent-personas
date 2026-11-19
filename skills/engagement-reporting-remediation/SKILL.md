---
name: "engagement-reporting-remediation"
description: "Turn findings into a report leadership and engineers can act on."
license: "MIT"
---

# Engagement Reporting & Remediation

The deliverable is not the exploit; it is the report that gets things fixed.

## 1. Write for two audiences
- Executive summary: business risk in plain language.
- Technical detail: reproduction steps, evidence, affected assets.

## 2. Actionable remediation
- Every finding carries a concrete fix and a prioritised severity.
- Rank by exploitability x impact, so the team fixes the right thing first.

## 3. Enable verification
- Give enough to reproduce and to confirm the fix later.
- Offer retest; a finding is closed only when re-verified.

## 4. Hand over evidence safely
- Each finding carries a private evidence reference (where the full proof lives) and a
  shareable redacted extract that still supports the conclusion. Redaction must remove
  identifiers and secrets without redacting away the affected behaviour.
- Record the affected revision, impact, limitations, the remediation owner, and the status
  after recheck. A finding is closed only when re-verified at the new revision.
- If the observation is missing, report it as unconfirmed — never present a guess as proof.
- The report must let a defensive (blue-team) reader act without loading any hunting tooling.

## Voice
Fix-oriented. Refuse a report that lists exploits with no remediation or priority.
