---
name: "sre-incident-response-reference"
description: "Apply Google SRE incident response principles and roles."
license: "MIT"
---
# Sre Incident Response Reference

## When to use
Apply Google SRE incident response principles and roles.

## Method
1. Declare incident scope, severity and ownership from observed impact. Establish a shared timeline and communication cadence.
2. Separate incident command, investigation and communication responsibilities when the response size justifies it; avoid competing uncoordinated changes.
3. Rank hypotheses using evidence and choose reversible mitigations with explicit success and abort criteria.
4. Verify recovery from the affected user path, then monitor for recurrence. Preserve logs and explain residual risk before closing.
5. Run a blameless review with contributing conditions, detection gaps and owned corrective actions. Source: https://sre.google/sre-book/managing-incidents/.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
