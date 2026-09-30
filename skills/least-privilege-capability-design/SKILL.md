---
name: "least-privilege-capability-design"
description: "Constrain what an agent can reach by design — capability grants, not instructions — accepting that declared permissions are documentation unless enforced."
license: "MIT"
---

# Least privilege capability design

## When to use
Designing or reviewing the blast radius of an agent, tool or plugin.

## Procedure
1. Enumerate the capabilities the task genuinely needs: files, network, credentials, exec, message-send, spend.
2. For each, define the narrowest grant that still works.
3. Enforce the grant at the boundary the capability is exercised at, not in the prompt.
4. Test that a granted capability cannot be widened by text alone.
5. Record the grant so it can be revoked.

## Decision rules
- Declared permissions in a manifest are documentation until something enforces them. Say which it is.
- If a prompt-only restriction is the only control, the control is advisory; label it.
- Credential reach is a capability. Scope the key, not the request.
- Egress is a capability: where can output go?

## Pitfalls
- Assuming a tool description's permission list is enforced.
- Granting a broad key because scoping is inconvenient.
- Blocking input while leaving exfiltration paths open.

## Done
Each capability has a narrowed grant, an enforcement point, and a revocation path — and advisory-only controls are labelled advisory.
