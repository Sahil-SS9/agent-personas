---
name: comfyui-headless-jobs
description: "Use when running or debugging headless ComfyUI jobs via API."
version: 1.0.0
license: MIT
---
# ComfyUI Headless Jobs — Submit & Diagnose via HTTP API

## When to Use

- Queueing a ComfyUI workflow without the UI (`POST /prompt` against `http://127.0.0.1:8188`).
- A headless run "completed" but no output file appeared, or completed impossibly fast.
- Deciding whether a failed run is a crash, a cancel, or a validation short-circuit.

## Submission pattern (proven on Windows portable, v0.30.0)

```python
import json, urllib.request
d = json.load(open(WORKFLOW_JSON, encoding='utf-8'))   # API-export format: {node_id: {class_type, inputs}}
# patch inputs by node id, then:
req = urllib.request.Request('http://127.0.0.1:8188/prompt',
    data=json.dumps({'prompt': d}).encode(), headers={'Content-Type': 'application/json'})
resp = json.load(urllib.request.urlopen(req))
pid = resp['prompt_id']           # poll /history/<pid>, NEVER dump /queue (echoes 300KB+ graph)
```

- API-export JSON keys are **string node IDs**; widget values live under `inputs` (mxSlider: `Xi` when `isfloatX:0`, else `Xf`).
- Patch only existing input keys — unknown keys are silently ignored.
- Unicode workflow filenames break naive open() on some shells — glob from Python instead of hardcoding paths.

## Failure-signature triage (read /history/<pid> → status.messages)

| Signature in messages | Meaning | Action |
|---|---|---|
| `execution_success` in <1s, outputs are only MathExpression/Preview/ShowText | **Validation short-circuit**: an upstream node failed validation, every dependent node (incl. samplers + savers) was skipped | Re-POST and inspect `node_errors` in the queue response — it names the node, the input, and the accepted range |
| `execution_error` with traceback | Real crash (OOM, missing model, node bug) | Read `exception_message`; fix and retry |
| `execution_interrupted` at node X after long runtime | **Cancel signal, not a crash** — someone pressed Interrupt in the UI or hit /interrupt | Re-queue; ask user not to touch Run/Interrupt while a headless job cooks (the UI and API share one queue) |

## Pitfalls (session-verified)

- **`easy seed` node max is 2^50 (1,125,899,906,842,624).** `random.randint(1, 2**62)` overflows it → `value_bigger_than_max` in `node_errors` → the whole downstream graph silently never executes, yet history reports "success". Always clamp seeds to the node's `input_config` max. This exact failure cost two fake-success runs.
- **`node_errors` at queue time are not always harmless warnings.** Read them before polling: each entry lists `dependent_outputs` — if your Save/Image Saver node id is in that list, the run will produce nothing.
- **`execution_cached: nodes: []`** just means zero cache hits — it is not itself an error signal.
- **UI and API share the same queue and interrupt button.** A headless job can be killed from the open UI; a stray temp preview with a newer timestamp than your run's means UI activity happened mid-run.
- **Polling:** `GET /history/<pid>` returns nothing until the job finishes — silence = still running, not lost. Poll every 5–6s; check `status.status_str` and `status.completed`.

## Verification

- Success = an `output`-type entry in `history[pid]['outputs']` (e.g. Image Saver's PNG) — temp-type images are previews, not deliverables.
- Confirm on disk: newest file in `ComfyUI/output/` matches the reported filename and `modelname` patch.

## References

- `references/headless-triage-cases.md` — full diagnostic transcripts from the 2026-08-13 session (seed-overflow short-circuit, UI-interrupt mid-run) with exact message payloads.
- Full vslinx TXT2IMG control map + patch recipe lives in the **creative profile's** `comfyui-troubleshooting` skill (`references/vslinx-allinone-headless.md`) — load it cross-profile when driving that specific workflow.
