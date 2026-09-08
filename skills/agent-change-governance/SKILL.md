---
name: "agent-change-governance"
description: "Record agent changes, approvals, handoffs and verified outcomes."
license: "MIT"
---
# Agent Change Governance

## When to use
Record agent changes, approvals, handoffs and verified outcomes.

## Method
1. Keep an append-only decision record for consequential agent changes: request, rationale, alternatives, owner, scope, approval and evidence.
2. Distinguish permission to investigate, implement, merge, publish and activate. Approval of one stage does not grant the rest.
3. Track profile and skill changes by exact version with rollback references. Preserve rejected options and superseded decisions rather than rewriting history.
4. Resolve cross-role conflicts through a named decision owner. Transfer context with facts, artefacts, unresolved decisions and the next verification gate.
5. Verify completion at the actual external boundary and make unverified or blocked work visible. Never manufacture approvals or independent review.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
