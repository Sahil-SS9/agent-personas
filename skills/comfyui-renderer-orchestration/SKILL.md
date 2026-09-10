---
name: comfyui-renderer-orchestration
description: "Use when designing MCP-controlled ComfyUI renderers."
version: 1.0.0
license: MIT
---
# ComfyUI Renderer Orchestration

Design and commission reusable, MCP-driven ComfyUI renderers from large user-authored workflows. Treat the user's graph as a reference design, preserve it, and build a clean API-format derivative whose controls are explicit, typed, and independently testable.

## When to use

- A user supplies a large ComfyUI workflow and wants an agent-controlled renderer.
- A renderer needs sequential body-part detailers, segment-specific LoRAs, or bypass switches.
- Hermes must discuss a character or image brief, choose a model, patch a workflow, run it through Comfy MCP, and deliver images.
- A multi-stage graph must be made safer for a constrained GPU.

## Workflow architecture

Start from this stable slice:

```text
CheckpointLoaderSimple
  → global LoraLoader chain
  → CLIPSetLastLayer
  → positive/negative CLIPTextEncode
  → EmptyLatentImage → KSampler → VAEDecode
  → sequential segment gates
  → PreviewImage + SaveImage
```

For each detail segment:

```text
UltralyticsDetectorProvider
  + segment CLIPTextEncode
  + optional SAMLoader
  + FaceDetailer
  → LazySwitchKJ(on_false=previous_image, on_true=detailer_image)
  → PreviewImage
```

A disabled detailer must pass the previous image through. Keep detector, segment prompt, tuning, gate, preview, and output mapping separate in the graph or its companion manifest. This lets the agent choose stages per prompt without changing topology.

## Preserve user work

Never overwrite the user's supplied editor-format reference workflow. Create a sibling API-format derivative using string node IDs, `class_type`, and `inputs`. Editor-format subgraphs, widget arrays, frontend-only bypass nodes, and display names may not transfer directly to headless execution. Rebuild the minimum typed graph and validate it against the live ComfyUI registry.

Add descriptive `_meta.title` values for operator diagnostics. Maintain a manifest mapping human controls to node IDs and input names, including switch polarity, segment order, LoRA scope, detector choice, optional branches, and verification status. See `references/multi-segment-renderer-adaptation.md` for the reusable extraction pattern and checklist.

## LoRA scope

Use two layers:

1. **Global LoRAs:** a chained set before the base sampler. These affect base generation and all subsequent detail stages. Use for global style, broad character/body language, and general image quality.
2. **Segment LoRAs:** branches from the common global `MODEL`/`CLIP` pair into one matching detailer. Use for eyes, hands, chest, skin, accessories, or other localized refinement.

Core `LoraLoader` modifies both `MODEL` and `CLIP`. Therefore every segment LoRA needs paired model and CLIP gates, with the unmodified global branch on `on_false` and the LoRA branch on `on_true`. Set both explicitly for every run. The segment LoRA is active only when its model gate, CLIP gate, and detailer gate are enabled.

Do not apply a segment LoRA globally as a shortcut. Do not infer active scope from a friendly node title; inspect live class definitions, port names, link types, and switch polarity through MCP.

## Segment and safety policy

A first useful contract is face, eyes, nose, lips, hands, and chest/body. Use a dedicated detector when available. If a broad detector is temporarily reused, label it as a fallback and keep that stage off until its mask is visually inspected.

Keep adult-specific or otherwise sensitive segments as explicit opt-in branches. A broad character prompt must not implicitly activate them. Make body-specific prompts distinct from the base prompt, and use conservative denoise for quality-only refinement; increase denoise only when the user wants reconstruction rather than preservation.

## Hardware-aware defaults

Commission with batch size 1 on a 12 GB GPU. Heavy detailers, SAM, Hi-Res, refiner, ControlNet, and IPAdapter can overlap in memory. Keep optional branches off in the agent-facing baseline, then add them one at a time.

Recommended activation order:

```text
all optional stages off
→ face on
→ face + eyes on
→ face + eyes + hands on
→ eyes LoRA on
→ hands LoRA on
→ chest/body branch on
→ optional ControlNet/IPAdapter/Hi-Res/refiner
```

Use a fixed seed and keep model, dimensions, sampler, scheduler, and prompt constant for A/B comparisons.

## MCP validation and execution

Before every run:

1. Resolve exact checkpoint, LoRA, detector, SAM, sampler, and scheduler values from the live MCP node/model registry. Detector names commonly require `segm/` or `bbox/` prefixes.
2. Validate the exact saved API workflow with `mcp__comfy_mcp__validate_workflow`.
3. Require `valid: true`, zero errors, and zero warnings before submitting.
4. Submit with `mcp__comfy_mcp__run_workflow`, preserving the returned prompt ID.
5. Poll `mcp__comfy_mcp__job` to a terminal state.
6. Fetch with `mcp__comfy_mcp__fetch_outputs` and verify an output-type image exists on disk.

A smoke test covers only the exact graph state submitted. If the graph changes afterward, prior coverage is partial and the final graph must be rerun. Report structural validation, exercised stages, and untested branches separately.

Do not call a temp preview a deliverable. A completed render requires a terminal job result, an `output`-type image, and a verified downloaded file.

## Character-sheet orchestration

Keep conversation logic outside the ComfyUI graph. The orchestration layer should maintain:

- an identity lock: face, hair, palette, costume silhouette, accessories, proportions, and personality cues
- shot direction: pose, camera, expression, crop, lighting, environment, and action
- an anchor pass: small candidate batch from a neutral, consistent setup
- six separate view passes: hero three-quarter, front, side, back, head/face, and costume/accessory detail
- deterministic composition: stitch the selected individual images and add labels/metadata outside diffusion so text remains legible

Run the six views as separate MCP jobs using the same identity reference and locked character specification. Per-view retries are preferable to one huge six-sampler graph on a 12 GB card.

## Manager boundary

ComfyUI Manager is package/node lifecycle management, not the conversation orchestrator and not a replacement for workflow QA. A requirements file, cloned repository, or installed package name does not prove the active runtime integration. Read live `server_info` manager mode and inspect the loaded node registry.

Do not migrate the production workspace merely to create a renderer. Compare legacy and registry/package paths in an isolated copy by checking node discovery, dependency mapping, version pins, workflow validation, and one real batch-1 render. Revalidate all workflows after Manager or custom-node changes. Keep the existing workspace untouched until the derivative renderer and detailer-on smoke test are proven.

## Pitfalls

- Never overwrite the user's reference workflow.
- Never assume editor-format JSON is executable API JSON.
- Never silently substitute an old or near-matching asset filename.
- Never use `set_workflow_slot` for dynamic-combo nodes whose values are positionally mispaired; edit the API JSON directly and validate.
- Never enable every detailer, upscale, refiner, ControlNet, and IPAdapter path at once on a constrained GPU.
- Never claim detailer-on or segment-LoRA behavior was tested when only the bypass/base path ran.
- Never treat detector availability as detector suitability.
- Never claim a Manager migration from a requirements file alone.
