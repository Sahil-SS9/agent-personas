---
name: "agent-config-validation"
description: "Validate agent configuration against its actual runtime schema."
license: "MIT"
---
# Agent Config Validation

## When to use
Validate agent configuration against its actual runtime schema.

## Method
1. Identify the installed runtime version and its authoritative configuration schema before inspecting values. Do not infer current support from old examples.
2. Compare types, defaults, precedence, enabled tools, credential references and fallback routes with the effective runtime configuration.
3. Test proposed changes in an isolated configuration using the actual loader. Check booleans versus strings, null versus omission, list merging and unknown fields.
4. Preserve secrets and create a reversible backup. Apply only approved changes to named profiles; do not restart services as part of a read-only audit.
5. After activation, read back the effective settings and exercise a bounded real call. A parsable file is not proof the runtime uses it.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
