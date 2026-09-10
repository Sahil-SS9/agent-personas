# vslinx All-in-One TXT2IMG — Headless Run Recipe (worked, 2026-08-05)

Workflow: `Hermes Text2Image 5.1.json` (API export of vslinx
`TXT2IMG-ADetailer-v5.1`), at
`C:\Users\Hermes\ComfyUI\ComfyUI_windows_portable\ComfyUI\user\default\workflows\`.
207 nodes, 52 class types — all installed on the user's server. Full pipeline
(base gen → 6-LoRA stack → 3 FaceDetailer + expanded inpaint components →
1.5x upscale + UltimateSDUpscale HiRes → ColorMatch → Image Saver) ran
end-to-end in ~60 s on RTX 4070 Ti.

## Minimal run + patch code

```python
import json, urllib.request
d = json.load(open(r'C:\...\workflows\Hermes Text2Image 5.1.json', encoding='utf-8'))
d['259']['inputs']['modelname'] = 'divingIllustrious_nijimutedcolorVol2'  # was WidgetToString link
del d['282']     # WidgetToString — crashes headless (extra_pnginfo absent)
del d['1139']    # orphaned PreviewImage, no images input
d['142']['inputs']['Xi'] = 1   # batch size (exports as 8)
req = urllib.request.Request('http://127.0.0.1:8188/prompt',
    data=json.dumps({'prompt': d}).encode(), headers={'Content-Type': 'application/json'})
print(json.load(urllib.request.urlopen(req)))  # {'prompt_id': ..., 'node_errors': {}}
```

## Control map (node IDs in this export)

| What | Node | Notes |
|---|---|---|
| Subject prompt | `1050` | vsLinx_ImpactMultilineWildcardText, `inputs.text` |
| Quality prefix | `1070` | e.g. `masterpiece, best quality, ...` |
| Negative | `1053` (+`1071`) | `1053` holds `embedding:lazy*` list |
| Detailer prompts | `653:639` face, `653:641` eyes, `653:645` hands, `653:640` nose, `653:652` lips | CLIPTextEncode, empty = inherit |
| Seeds | `137` (base), `707` (detailers) | easy seed, `inputs.seed` |
| Resolution | `141` | mxSlider2D: `Xi`=1024, `Yi`=1408 |
| Batch | `142` | mxSlider `Xi` (exports as 8 — override to 1 for tests) |
| Steps / CFG / Denoise | `133` / `266` / `269` | mxSlider: `Xi` if `isfloatX:0`, else `Xf` |
| CLIP skip | `144` | mxSlider |
| Toggles | `849` HiRes, `869` ControlNet, `665` Inpaint, `790` Refiner | PrimitiveBoolean `inputs.value` |
| Detailer denoises | `459`–`466` | mxSlider `Xf` (0.15–0.35) |
| LoRA stacks | `547` main (AddMicroDetails 0.25, cryosistyle 0.4, onTopOfPole 0.7), `562` face, `564` eyes, `570` hands (+stiletto_nails) | rgthree `lora_N: {on, lora, strength}` |
| Save | `259` Image Saver | writes PNG to ComfyUI `output/`, filename `TXT2IMG_ADetailer_%time`, embeds workflow |

Base ckpt: `divingIllustrious_nijimutedcolorVol2.safetensors` (node `436`).
Illustrious/NoobAI family — danbooru-tag prompts, `embedding:lazy*` embeddings.

## Gotchas observed

- POST returns `node_errors` as **warnings**; job still queues. Fatal errors only
  appear later in `/history/<pid>` → `status.messages[].execution_error`.
- `vsLinx_LoadLastGeneratedImage` (`1134`) points at a stale output filename —
  only used on the Inpaint branch (`665` false by default), harmless.
- History/output flood: `/queue` echoes the entire 300 KB+ prompt graph. Poll
  `/history/<pid>` only, never dump `/queue` while a big graph runs.
