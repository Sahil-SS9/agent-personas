---
name: "incident-response-lifecycle"
description: "Run incidents through prepare → detect/analyse → contain/eradicate/recover → learn."
license: "MIT"
---

# Incident response lifecycle

## When to use
Security incidents and any suspicion of one.

## Procedure
1. Prepare before incidents: playbooks per incident class, escalation contacts, tooling access, evidence-handling rules.
2. Detect & analyse: scope first — what is affected, what is the entry point, what is the current activity. Act on analysis, not adrenaline.
3. Contain (stop spread), eradicate (remove access/tools), recover (restore from verified-clean sources) — in that order. Preserve evidence for analysis before wiping.
4. Declare early; communicate on a cadence; keep a timestamped working record of every action (what, when, why, by whom).
5. Post-incident: blameless postmortem within days; each incident produces at least one detection or control improvement.

## Decision rules
- Containment before curiosity: stop the spread before the full forensic story.
- Restore only from verified-clean backups; assume persistence until proven absent.
- A incident without a postmortem will repeat.

## Pitfalls
- Wiping evidence in the rush to recover.
- Single-person response with no handover.

## Done
An incident handled through the full lifecycle with records, and the improvement loop closed.