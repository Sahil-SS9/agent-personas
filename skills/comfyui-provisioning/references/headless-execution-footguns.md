# ComfyUI Headless Execution Footguns (comfy run / comfy-mcp)

Verified by actually running the vsLinx All-in-One and Legendaer Basic_V37
workflows headless via `comfy run` / `mcp__comfy_mcp__run_workflow` on a local
portable install. **`comfy run` and `validate_workflow` are stricter than the
ComfyUI UI** — workflows that run fine interactively can be un-runnable
headless, in ways that waste real GPU time and produce only confusion.

---

## 1. `Image Filter` interactive gate KILLS headless runs (top cause of "renders keep dying")

**Node:** `Image Filter` (cg-image-filter pack), found in the vsLinx All-in-One
TXT2IMG (node `624`, feeds the upscale step). It is an **interactive "pick which
image to continue"** gate with widgets `timeout: 90` and `ontimeout: "send none"`.

**Mechanism:** In the ComfyUI UI, a human clicks to select/advance it. Run
headless, nobody clicks → after `timeout` (90 s) it fires an interrupt that
**aborts the whole pipeline** at the upscale stage.

**Diagnosis signature** (in `user/comfyui.log`): every `got prompt` is followed
~90–140 s later by `Processing interrupted` / `Prompt executed in N seconds`,
with **no saved image produced**. Responses `Ignoring response {"special":"-1"...}`
(-1 = Image Filter timeout) and `{"special":"-3",...}` (-3 = interrupt) confirm it.
The `job` status comes back `cancelled` with only a temp `ComfyUI_temp_*.png`
output (a CN/preview frame), never the final render.

**Fix:** bypass/remove the `Image Filter` node and rewire the downstream image
input (e.g. the `vsLinx_UpscaleByFactorWithModel` node that consumes `.image`)
to the base VAE-decode node directly. On a **copy**, never the user's original.
Removing the node makes the pipeline pass straight through.

**Lesson:** any interactive-gated mega-workflow is a headless trap. If a job
keeps getting `Processing interrupted` ~90–140 s in with no output, look for an
`Image Filter` / human-in-the-loop gate, not a code error.

---

## 2. `easy hiresFix.rescale_after_model` — comfy-cli client vs server type conflict

**Node:** `easy hiresFix` (Easy-Use pack), in Legendaer Mega workflows (Basic_V37
has two, feeding the detailer chain and the save path).

**Conflict:**
- comfy-cli **client-side pre-check** (`comfy run` / `validate_workflow`) wants
  `rescale_after_model` as a **COMBO (string or number)** — `'True'` string.
- The **server runtime** `object_info` says it's a **boolean**:
  `[[false, true], {"default": true}]` — rejects the string.
- There is **no value satisfying both**: string `"True"` → runtime rejects;
   real bool `true` → client rejects ("expected COMBO (string or number), got bool").

This is a comfy-cli validator bug / schema mismatch, not a workflow mistake.

**Fix:** set the `easy hiresFix` nodes to `mode: 4` (bypassed) in a copy of the
editor JSON. Bypassed nodes become passthrough, so `rescale_after_model` never
appears in the converted graph, and `SaveImage` still receives the detailer
output through the bypass. Then `validate_workflow` passes (0 errors) and
`run_workflow` executes.

---

## 3. rgthree display-name `class_type` blockers

`comfy run` rejects workflows containing UI-toolbar nodes whose display keys are
NOT registered class_types, even though the UI loads them fine:

- `Label (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Bypasser (rgthree)`

Error: `class_type 'X (rgthree)' not found in object_info` during
`workflow_unknown_nodes` / `prompt_rejected`.

**Fix:** bypass/remove these UI-only nodes from a copy, OR avoid them by building
a clean standard-node graph (below).

Note: `validate_workflow` and the *runtime* `comfy run` can DISAGREE —
`validate_workflow` may report `valid: true` while `comfy run` still fails on a
different (runtime) check, and vice-versa. Always run the actual `comfy run`
submission to know the real answer; read the failure hint.

---

## 4. THE RELIABLE PATTERN — clean standard-node API txt2img

For agent-generated headless renders, **do NOT fight the mega-workflows.** Build
a minimal API graph using only core class_types — it validates and runs headless
flawlessly every time. Proven 7-node template (SDXL/Illustrious family, e.g.
`hyphoria_v002.safetensors`):

```json
{
 "3": {"class_type":"CheckpointLoaderSimple","inputs":{"ckpt_name":"hyphoria_v002.safetensors"}},
 "4": {"class_type":"CLIPTextEncode","inputs":{"text":"<positive>","clip":["3",1]}},
 "5": {"class_type":"CLIPTextEncode","inputs":{"text":"<negative>","clip":["3",1]}},
 "6": {"class_type":"EmptyLatentImage","inputs":{"width":1024,"height":1024,"batch_size":1}},
 "7": {"class_type":"KSampler","inputs":{"model":["3",0],"positive":["4",0],"negative":["5",0],
       "latent_image":["6",0],"seed":12345,"steps":24,"cfg":7.0,
       "sampler_name":"euler_ancestral","scheduler":"normal","denoise":1.0}},
 "8": {"class_type":"VAEDecode","inputs":{"samples":["7",0],"vae":["3",2]}},
 "9": {"class_type":"SaveImage","inputs":{"images":["8",0],"filename_prefix":"MY_PREFIX"}}
}
```

- `EmptySDXLLatentImage` may NOT be registered — use `EmptyLatentImage` for SDXL.
- `CheckpointLoaderSimple` bundles MODEL/CLIP/VAE (outputs 0,1,2) — no separate
  ModelSampling/VAELoader needed for a basic render.
- Keep prompts as plain strings (a trailing comma that makes a tuple is a real
  bug — `text` will be read as a node-ref and fail with `dangling_edge`).
- Save this as `references/templates/` or a saved workflow for reuse.

Use the extracted-from-history API graph (below) when the user specifically
wants the mega-workflow's full detailer chain.

---

## 5. Running a specific mega-workflow headless (best order)

1. **Prefer extracting the exact API graph from server history** of a UI run
   that already succeeded: `GET /history?prompt_id=<id>` → `[num, id, GRAPH, meta]`,
   index `[2]` is the clean API graph the server actually accepted. Edit only the
   prompt/model and re-POST. This sidesteps ALL client-side validation.
2. Otherwise bypass the footgun nodes (`Image Filter`, `easy hiresFix`, rgthree
   labels) on a **copy**, validate, then run.
3. Hand-built UI→API conversion of complex Impact/rgthree workflows is
   **error-prone** (widget-to-input misalignment, missing required widget inputs
   like `mode`, `populated_text`, `model_name`, `Select to add Wildcard`) — avoid
   unless you can resolve every bypassed-passthrough (bypassed nodes pass their
   first input link through; e.g. `41.model` in Basic_V37 resolves through
   bypassed `69→63→54` back to `27` Power Lora Loader).

---

## 6. Misc session notes
- comfy-cli `run` job comes back `cancelled` (not `failed`) when a headless run
  is interrupted by an Image Filter / interrupt — an empty outputs list + temp
  preview + `cancelled` status = the interactive gate fired, not a crash.
- `JOB_STATUS` `running` in the `job` tool while the ComfyUI UI shows nothing:
  comfy-cli submitted jobs don't paint live previews to the browser tab — it IS
  running server-side. Confirm via `curl /queue` (queue_running) + `get_logs`
  (sampling progress bars), not the UI.
- `Error: extra_pnginfo[0] is not a dict or missing 'workflow' key` in the log is
  a **harmless** Image-Saver metadata warning from comfy-cli submissions (no
  embedded workflow JSON) — it does NOT stop the save.
- `search_files (target='files')` can miss workflow JSONs under nested
  `user/default/workflows/*/` subfolders — use `find`/terminal for inventory.
