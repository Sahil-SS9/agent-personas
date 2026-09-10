# Multi-segment renderer adaptation

Use this reference when turning a large user-authored ComfyUI editor workflow into an agent-controlled API workflow.

## Preserve, then extract

- Keep the original editor JSON unchanged as the visual/reference source.
- Build a sibling API-format workflow for Hermes (`<node_id>` → `{"class_type": ..., "inputs": ...}`).
- Add descriptive `_meta.title` values for operator-facing diagnostics, and maintain a companion manifest mapping human controls to node IDs and input names.
- Do not assume editor-format subgraphs, widget arrays, custom bypass nodes, or frontend-only values transfer directly to API JSON. Rebuild typed links and validate against the live server.

## Recommended renderer slice

```text
CheckpointLoaderSimple
  → global LoraLoader chain
  → CLIPSetLastLayer
  → positive/negative CLIPTextEncode
  → EmptyLatentImage → KSampler → VAEDecode
  → sequential segment gates → PreviewImage + SaveImage
```

A segment is:

```text
UltralyticsDetectorProvider
  + segment CLIPTextEncode
  + optional SAMLoader
  + FaceDetailer
  → LazySwitchKJ(on_false=previous_image, on_true=detailer_image)
  → PreviewImage
```

Each segment gate must bypass to the previous image when disabled. Keep detector, prompt, tuning, and gate as separate controls so the agent can choose whether a stage is relevant without rewriting topology.

## LoRA scope

Global LoRAs apply before the base sampler and affect the full image/detail pipeline. Segment LoRAs branch from the common global `MODEL`/`CLIP` pair and route only into their matching detailer. Because core `LoraLoader` modifies both `MODEL` and `CLIP`, use paired model and CLIP switch gates. A segment LoRA is active only when its model gate, CLIP gate, and detailer gate are all enabled.

Keep sensitive/adult-specific body segments as explicit opt-in branches. A broad character prompt must not implicitly activate them.

## Live checks

Before wiring, query the live MCP node catalog for `LoraLoader`, `UltralyticsDetectorProvider`, `FaceDetailer`, `SAMLoader`, and `LazySwitchKJ`. Resolve exact checkpoint/LoRA/detector/SAM filenames, including detector prefixes such as `segm/` and `bbox/`. Validate the complete saved API JSON after every structural mutation.

Detector availability is not detector suitability. If a segment temporarily uses a broad detector fallback, label it in the manifest and keep it disabled until its mask is visually inspected.

## Verification matrix

Use batch 1, fixed seed, and the same prompt/model/dimensions/sampler/scheduler:

1. Base sampler with all optional stages off.
2. One detailer enabled, preferably face.
3. Two adjacent detailers enabled, such as face + eyes.
4. One segment LoRA enabled with its detailer isolated.
5. A hands/body segment enabled.
6. The intended final combination.

A run is complete only when it has a terminal job status, an `output`-type image rather than only temp previews, and a downloaded file that exists at the requested destination. If the graph changes after a smoke test, earlier coverage is partial and the final graph must be re-run.

## Manager comparison checklist

Manager migration is separate from graph design:

- read live `server_info` and record the active manager mode
- inspect the loaded node registry and package/version source
- compare dependency mapping for the same workflow
- compare install/update behavior in an isolated workspace
- validate before and after the change
- perform one real batch-1 render and verify its output
- migrate the main workspace only after the comparison succeeds

A package requirement, a cloned repository, and the active runtime integration are different facts. Never infer one from another.

## Reporting

Report the graph contract and verification scope separately. State which stages were structurally validated, which were actually exercised, and which optional branches remain untested. Deliver the real fetched file path or `MEDIA:` asset; do not call a preview-only artifact a finished render.