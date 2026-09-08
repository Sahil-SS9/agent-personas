---
name: "comfyui-workflow-management"
description: "Manage ComfyUI workflows through verified execution."
license: "MIT"
---
# Comfyui Workflow Management

## When to use
Manage ComfyUI workflows through verified execution.

## Method
1. Treat a workflow as versioned executable configuration with node classes, edges, model dependencies, inputs and expected outputs.
2. Distinguish editor layout from API prompt representation. Validate node identifiers, types, required fields and references against the actual running installation.
3. Change one meaningful variable at a time and save a new revision with rationale. Preserve a known-good workflow and the assets needed to replay it.
4. Exercise the changed workflow with a bounded job, follow its exact identifier and inspect every required output. JSON validity alone is not execution evidence.
5. Record unsupported nodes or model versions rather than silently substituting them. Source: https://docs.comfy.org/.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
