# Headless Triage Cases — 2026-08-13 session

Real `/history/<pid>` payloads from diagnosing two failed headless submissions of
`Hermes Text2Image 5.1.json` (vslinx TXT2IMG-ADetailer v5.1, 207 nodes) on a
Windows portable ComfyUI v0.30.0, RTX 4070 Ti. The third submission succeeded (~96 s,
output `TXT2IMG_ADetailer_2026-08-13-213557.png`, model `hyphoria_v002`).

## Case 1 — Seed overflow → silent validation short-circuit (TWO fake successes)

**Cause:** patch code set `d['137']['inputs']['seed'] = random.randint(1, 2**62)`.
Node 137 is an `easy seed` node whose max is `1125899906842624` (2^50).

**Queue response (`POST /prompt`):**

```json
"node_errors": {
  "137": {
    "errors": [{
      "type": "value_bigger_than_max",
      "message": "Value 3811464773581601343 bigger than max of 1125899906842624",
      "details": "seed",
      "extra_info": { "input_name": "seed",
        "input_config": ["INT", {"default": 0, "min": 0, "max": 1125899906842624}] }
    }],
    "dependent_outputs": ["227","224","259","29","532","231","228","225","230","229","226"],
    "class_type": "easy seed"
  }
}
```

Note `259` (the Image Saver) in `dependent_outputs` — that alone predicts no file.

**History payload (the trap):**

```json
"messages": [
  ["execution_start",   {"timestamp": 1786674333958}],
  ["execution_cached",  {"nodes": [], "timestamp": 1786674334058}],
  ["execution_success", {"timestamp": 1786674334126}]
]
```

168 ms "success". Outputs contained only `MathExpression|pysssss`, `PreviewImage`,
`ShowText|pysssss` nodes — nodes whose inputs don't depend on the seed. Everything
downstream of node 137 (checkpoint load is independent, but the sampler chain was
not) silently skipped. `execution_cached: nodes: []` means "no cache hits", NOT an
error — don't let it distract you.

**Fix:** clamp seeds to the node's `input_config` max; always print `node_errors`
from the queue response before polling.

## Case 2 — execution_interrupted mid-run (cancel, not crash)

Third submission (seed fixed, `node_errors: 0`) ran the real chain ~130 s, then:

```json
["execution_interrupted", {
  "node_id": "624", "node_type": "Image Filter",
  "executed": ["436","547","562","564","570","133","137","141","144", "..."],
  "timestamp": 1786674756087
}]
```

`executed` listed the full base-gen chain (checkpoint 436, LoRA stacks, sliders) —
sampling had progressed normally. A stray temp preview (`ComfyUI_temp_qfdep_*.png`,
2.9 MB) with a timestamp ~1 min newer than the run's own temp preview proved UI
activity mid-run. The ComfyUI UI and the HTTP API share ONE queue and ONE interrupt
button; the open browser UI's red interrupt (or a UI-queued job) killed the headless
job. `execution_interrupted` = cancel signal; a genuine crash logs
`execution_error` with a traceback instead.

**Fix:** none needed technically — re-queue verbatim and keep hands off the UI.
Re-run completed in 96 s with 12 outputs including the final Image Saver PNG.

## Working patch set for `Hermes Text2Image 5.1.json` (this session)

```python
d['436']['inputs']['ckpt_name'] = 'hyphoria_v002.safetensors'  # base ckpt swap
d['259']['inputs']['modelname'] = 'hyphoria_v002'              # Image Saver label
d.pop('282', None); d.pop('1139', None)                        # headless-crash nodes
d['142']['inputs']['Xi'] = 1                                   # batch 1
d['1050']['inputs']['text'] = SUBJECT_PROMPT                   # danbooru-style subject
d['266']['inputs']['Xf'] = 6.0                                 # CFG (float slider!)
d['137']['inputs']['seed'] = random.randint(1, 1125899906842624)  # <= 2^50
```

All LoRA-stack entries (`547` main, `562` face, `564` eyes, `570` hands) referenced
files present on disk — no disabling needed this run. Check `models/loras/` and set
`inputs['lora_N']['on'] = False` for any missing file before queueing.
