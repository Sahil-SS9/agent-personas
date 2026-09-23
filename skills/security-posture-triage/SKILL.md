---
name: "security-posture-triage"
description: "Triage a tool's permission footprint and data boundaries before it touches real systems."
license: "MIT"
---

# Security posture triage

## When to use
Before any tool runs with access to private data, untrusted content, or external action.

## Procedure
1. Map the permission footprint: what the tool can read, write, execute, and reach (network, files, credentials, comms).
2. Check the lethal triangle: private data + untrusted content + external action. All three together is the danger zone — most useful agents stand on it by default, so name the legs and the guardrails offsetting each.
3. Ask how it can be scoped: sandboxing, least-privilege credentials, allowlists, human approval chokepoints for irreversible actions. A tool that cannot be scoped is Caution by default in high-stakes contexts.
4. Classify data exposure: what private data enters the tool, where it goes, how long it lives, whether it trains anything.
5. Record the triage: permitted scope, required guardrails, residual risks.

## Decision rules
- Prompt injection means trusted instructions cannot be reliably separated from untrusted input — design as if the tool will be injected.
- Guardrails that only prompt ("please don't do X") are not guardrails; require structural limits (permissions, sandboxes, approval gates).
- Behavior is inconsistent: success once guarantees nothing at scale; require deterministic checks around nondeterministic tools.

## Pitfalls
- Evaluating demo configuration instead of the deployed configuration.
- Granting broad access because payoff seems obvious — appetite for access is not a safety argument.

## Done
A written triage with footprint, lethal-triangle legs, guardrails, residual risk, and a go/no-go scope statement.