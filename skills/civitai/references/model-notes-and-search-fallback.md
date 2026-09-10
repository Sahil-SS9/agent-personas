# Civitai — Gathering model notes & resolving models the search API can't find

Session-proven (2026-08, Illustrious checkpoint notes gathering). Patterns that
extend the main `civitai` SKILL.md, which assumes you already have a model id/URL.
Here the model is **unknown** or the search API fails to surface a model that
is known to exist on the site.

## 1. `GET /api/v1/models?query=<q>` is incomplete — do not trust a null hit

The text-search endpoint (`/models?query=Diving&types=Checkpoint`) can return
**zero results for a real, popular model** (worked example: "Diving-Illustrious
Anime — Niji-Muted Color", ID 1170176, was invisible to every text query tried:
`diving`, `niji`, `nijimuted`, `muted color`, `diving illustrious`). A null
result is NOT proof the model doesn't exist. Do not conclude "not on Civitai".

## 2. Resolution path when a local checkpoint file has no Civitai ID

Checkpoint `.safetensors` files downloaded via the API usually embed **no**
Civitai model/version id in `__metadata__` (verified: `ss_models`,
`modelspec.title` = "ComfyUI 1", etc., but no cifitez id). So you cannot
resolve a local file back to its page from metadata alone — you must match
by **filename** to a specific `modelVersions[].files[].name`.

To find an unnamed/unsearchable model in practice:

1. **Read the local filename** for distinctive tokens (e.g.
   `divingIllustrious_nijimutedcolorVol2.safetensors` → author "Diving",
   variant "Niji-Muted Color vol2").
2. **Web-search the distinctive tokens** (`web_search`) — often surfaces the
   Civitai model page, a mirror (civitai.me, pixai.art), or a **Civitai post**
   posted *to* the model (posts carry the model URL in "Posted to
   `https://civitai.com/models/<ID>/...`"). The post snippet is the most reliable
   way to extract a model ID the search API hides.
3. `GET /models/<id>` → list `modelVersions[]`; match the local file to the
   version whose `files[].name` equals the local basename (glob/lowercase —
   e.g. `plantMilkModelSuite_hempII.safetensors` ↔ version "Hemp II").
4. Pull that version's `baseModel` + `trainedWords`, and read the **model
   `description`** for the author's recommended settings (next section).

## 3. Recommended settings live in the model `description`, not per-version

Authors put sampler / scheduler / CFG / steps / resolution / negative-prompt
recommendations in the **model-page `description`** (HTML). To extract them:

1. `GET /models/{id}` (Bearer token).
2. `re.sub(r'<[^>]+>', ' ', description)` then collapse whitespace.
3. The last ~1.5–2k chars usually hold the "Recommended Settings" block (CFG,
   sampler, Karras/other scheduler, resolution, steps, negative prompt string).
   The CUTOFF pitfall: fetch the WHOLE description and read its tail — truncating
   at a char budget (e.g. first 2200 chars) can clip the settings that live at
   the end. Use `desc[-1800:]` for the notes block, not `desc[:N]`.
4. If a model is a multi-series page (e.g. Plant Milk "Model Suite"), the
   description enumerates every series/variant with its own sampler hint —
   find the line for the exact variant you hold (e.g. "Hemp II → Euler or
   Euler a").

## 4. Checkpoint "baked-in VAE" vs external VAE (note it in the report)

Notes should state whether the checkpoint ships `+VAE` baked in (Diving vol2,
Retrordinary, Plant Milk) vs requires an explicit SDXL VAE (Amanesse →
`XL_VAE_C`). This changes ComfyUI wiring and is always worth a line.

## Verify before reporting

- Confirm the exact local filename ↔ Civitai `files[].name` match; version
  names are not unique across models, so key on the file, not the version title.
- Cross-check `baseModel` (all five Illustrious models came back `Illustrious`).
