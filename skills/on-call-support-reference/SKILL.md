---
name: "on-call-support-reference"
description: "Use when designing or improving sustainable on-call support."
license: "MIT"
---
# On Call Support Reference

## When to use
Use when designing or improving sustainable on-call support.

## Method
1. Triage by user impact, severity and ongoing risk. Identify the incident owner, communication channel and next update point.
2. Collect a timeline and the most useful diagnostic evidence without exposing credentials or customer data.
3. Prefer reversible mitigation that restores service while preserving evidence. Separate symptom containment from a proven root-cause fix.
4. Escalate when the consequence or required permission exceeds the responder’s authority; provide the current hypothesis, attempted actions and observed results.
5. Verify recovery using the user-facing path and record follow-up work. A quiet alert alone does not prove recovery.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
