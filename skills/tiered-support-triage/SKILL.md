---
name: "tiered-support-triage"
description: "Run first/second-line support with precise escalation and tier-appropriate metrics."
license: "MIT"
---
# Tiered Support Triage

## Use when
- Handling inbound user/customer issues at any tier
- Escalations bounce around without resolution ownership
- Support metrics feel like vanity statistics

## Instructions

1. Classify on intake: known-error (match runbook), new-but-reproducible,
   or novel. Reproduction request comes FIRST if not already present:
   exact steps, environment facts, expected vs actual.
2. First-line owns first-contact resolution against the knowledge base;
   measured on FCR and response time. Deflection (Tier 0 docs) is a
   first-line responsibility too — every novel resolution becomes an
   article draft.
3. Escalate only on defined triggers (symptom + duration + scope + business
   impact), never on frustration alone. An escalation CARRIES: repro steps,
   logs, environment, what was ruled out, what was tried.
4. Second-line diagnoses deeper (config/data/integration); measured on
   resolution time and reopen rate. Third-line (engineering) is measured
   on RECURRENCE ELIMINATION — does this ticket class stop appearing?
5. Every ticket closes with: root cause category, KB updated if novel,
   runbook updated if the resolution was non-obvious.

## Stop conditions
- Never escalate without evidence attached; never close without root-cause
  category.
- Never promise SLAs or credits beyond policy — route those requests.

## Escalation
- Major-incident candidates (broad impact, no workaround) jump straight to
  incident process with stakeholders informed.
