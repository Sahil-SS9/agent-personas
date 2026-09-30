---
name: "guardrail-need-triage-and-claim-classification"
description: "Decide which guardrails a system actually needs and classify each existing claim as enforced, observed, or asserted — before adding anything."
license: "MIT"
---

# Guardrail need triage and claim classification

## When to use
Starting guardrail work, inheriting an estate, or reading a safety claim you have to act on.

## Procedure
1. Enumerate the harms that matter for this system by surface: user input, retrieved content, tool arguments, tool results, outbound messages, code execution, data egress.
2. List every guardrail already claimed to exist, wherever it is claimed (docs, README, dashboards, tickets, someone's memory).
3. Classify each claim: enforced (blocks or halts), observed (logs only), or asserted (no mechanism found).
4. Convert needs into candidate rails; drop needs with no credible harm path.
5. Record both in the Guardrail Register, with a status per rail.

## Decision rules
- A claim with no mechanism is not a guardrail. It is a sentence. Classify it asserted and say so.
- Observation is a legitimate design choice, but it must be labelled observed, never reported as protection.
- A rail protecting a surface that no traffic reaches is not coverage.
- Do not add a rail before you can name the harm it prevents and how you would know it fired.

## Pitfalls
- Accepting a vendor or framework's presence as a guardrail.
- Counting rails instead of mapping them to harms.
- Treating a moderation endpoint's existence as detection.

## Done
Every candidate harm maps to a named rail or an explicit accepted risk; every claim carries a classification with the evidence behind it.
