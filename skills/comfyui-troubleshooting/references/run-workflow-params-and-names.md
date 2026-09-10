# run_workflow.py parameter + ComfyUI naming reference

Non-obvious facts learned driving the bundled `comfyui` skill's `run_workflow.py`
against a local ComfyUI 0.30 server. Confirmed live this session.

## Injecting args — verified param names and node mapping

`run_workflow.py` injects `--args` keys via the workflow's auto-derived schema
(`_inline_schema` → `extract_schema`). A minimal API-format SDXL txt2img
workflow exposes these params (node → field):

| Arg key | Maps to |
|---|---|
| `prompt` | positive CLIP text encode → `text` |
| `negative_prompt` | negative CLIP text encode → `text` (**NOT `negative`**) |
| `ckpt_name` | `CheckpointLoaderSimple` → `ckpt_name` |
| `seed`, `steps`, `cfg`, `sampler_name`, `scheduler`, `denoise` | `KSampler` |
| `width`, `height`, `batch_size` | `EmptyLatentImage` |

- The negative-prompt schema key is **`negative_prompt`**. Passing `negative`
  silently emits `unknown parameter 'negative' (not in schema), skipping`.
- `seed: -1` auto-randomizes (logged as a warning).

## ComfyUI sampler names ≠ A1111/Civitai names

Civitai pages say "Euler a", "DPM++ 2M", etc. ComfyUI requires underscored
internal names. Get the authoritative list live:
`curl http://127.0.0.1:8188/object_info/KSampler` → `input.required.sampler_name[0]`
and `...scheduler[0]`. Mapping for the common ones:

| A1111/Civitai name | ComfyUI `sampler_name` |
|---|---|
| Euler a | `euler_ancestral` |
| Euler | `euler` |
| DPM++ 2M | `dpmpp_2m` |
| DPM++ 2M SDE | `dpmpp_2m_sde` |
| DPM++ SDE | `dpmpp_sde` |
| DPM++ 3M SDE | `dpmpp_3m_sde` |
| HeunPP2 | `heunpp2` |

Schedulers are identical (`karras`, `sgm_uniform`, `simple`, …). `Restart`
sampler is NOT in the KSampler list on this build.

A wrong sampler name returns `value_not_in_list` at validation — not a crash.

## Workflow JSON authoring

- **Do NOT put a top-level non-node key (e.g. `"_comment"`) in the workflow
  JSON** — ComfyUI 0.30 `execution.validate_prompt` crashes on it, causing HTTP
  500 on EVERY submission. See the SKILL.md section for full detail.
- `extract_schema` tolerates `_comment`, but submission does not — the two paths
  diverge, so schema-success ≠ run-success.
- Checkpoint `ckpt_name`: case-sensitive, includes the extension, must match an
  installed file (else `value_not_in_list`).

## VAE note for Illustrious-era checkpoints
Modern Illustrious/NoobAI checkpoints bake the VAE in. `CheckpointLoaderSimple`
node returns conditioning/model/VAE — the VAE output feeds `VAEDecode` directly;
no separate VAE loader needed. (Legacy SDXL checkpoints like `sd_xl_base`
still need an external VAE.)
