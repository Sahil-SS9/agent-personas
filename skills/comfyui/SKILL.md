---
name: "comfyui"
description: "Generate images, video, and audio with ComfyUI —."
license: "MIT"
---
# Comfyui

## When to use
Generate images, video, and audio with ComfyUI —.

## Method
1. Identify the authorised ComfyUI endpoint and confirm its version, available node classes, models and workflow compatibility. Do not install nodes or download models without permission.
2. Start from a known workflow and inspect each required node input. Keep UI workflow documents distinct from API execution graphs; verify the expected representation.
3. Use approved local assets and a bounded job. Record prompt, seed, model identifiers and workflow identity before submission.
4. Follow the actual job identifier through queue state and completion history. Retrieve outputs belonging to that job and inspect the generated media.
5. Handle missing nodes, model mismatch, memory pressure and failed jobs explicitly. Cancel only the owned job; never clear another user’s queue. Source: https://docs.comfy.org/.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
