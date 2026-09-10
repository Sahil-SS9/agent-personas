---
name: civitai
description: "Use when resolving/downloading Civitai models via API."
version: 1.0.0
license: MIT
---
# Civitai — API, Model Resolution & Downloads

Civitai is the primary distribution channel for SD/Illustrious/Pony/Flux
checkpoints, LoRAs, embeddings, wildcards, and ComfyUI workflows. This skill
covers programmatic interaction with its REST API: token auth, what the API
can and cannot see, and the proven path from a list of Civitai URLs to a
ComfyUI download manifest.

Companion to the `comfyui` skill (local lifecycle/execution); this one covers
the model-source side.

## Auth

- API key: civitai.com → profile icon → **Account Settings → API Keys** (shown once).
- Store as `CIVITAI_API_TOKEN=<key>` in a `secrets/civitai.env` file inside the
  project folder; read with sed/grep; never echo the token into output.
- Header: `Authorization: Bearer $KEY`.
- Base URL: **https://civitai.com/api/v1** — always the .com domain for API.
  civitai.red is the mature-content mirror of the same site; same model IDs,
  same backend, but some .red pages are login-gated for browser scraping.

## Verified endpoints (all tested 2026-08-04)

| Endpoint | Auth | What you get |
|---|---|---|
| `GET /me` | required | user id, username, email, tier (`/user` does NOT exist — 404) |
| `GET /models/{id}` | public | model + `modelVersions[]` (use [0].id when URL lacks ?modelVersionId) |
| `GET /model-versions/{vid}` | public | `files[]` {id, name, sizeKB, downloadUrl, metadata.fp}, model.type, baseModel |
| `GET /collections/{id}` | public | metadata only — **never items** |
| `GET /collections` | public | global public feed — user filters ignored |
| `GET /vault/all`, `/vault/check-vault` | required | user's vaulted model versions |

Download URL shape: `https://civitai.com/api/download/models/{versionId}?fileId={fileId}`
(redirects — use `curl -L`).

## Collections limitation (the big pitfall)

Confirmed against official docs (developer.civitai.com):

- Collections endpoints return **public collections only**. There is **no "my
  collections" mode**, even with a valid token.
- `userId` / `username` / `user` query params are silently ignored — you get
  the site-wide feed. Don't waste time on filter variants.
- Private collections 404, indistinguishable from nonexistent.
- `/collections/{id}` never includes items; no `/items` subroute; internal
  tRPC endpoints reject API keys with 401 ("use the public API").
- Newly-public collections enter **pending review** — invisible to everyone
  (even logged-out owner views) until moderation clears, usually quickly.

**The working pattern:** ask the user for direct model URLs instead, then
resolve each via `/models/{id}` + `/model-versions/{vid}`. Direct lookups
bypass all collection gating. This resolved 22/22 links in one pass.

## Canonical workflow: URL list → manifest → downloads

1. Parse each URL: model id from path, version id from `?modelVersionId=`
   (fall back to `modelVersions[0].id`).
2. `GET /model-versions/{vid}` → `files[]`.
3. Route by `model.type` into the ComfyUI folder (table below).
4. Emit `manifest.json` (names, sizes, downloadUrls, destinations).
5. Download with `curl -L -o <dest>/<name> "<downloadUrl>"`.

Run `scripts/resolve_links.py 1297813:2776351 1377820 ...` — does steps 1–4
(`modelId` or `modelId:versionId` args; token from env or `--token-file`).
Response shapes: `references/endpoint-notes.md`.
Video-model VRAM/variant mapping (MiniMax H3): `references/minimax-h3-notes.md`.

**Model already on disk, need its page/notes:** checkpoints carry no embedded
Civitai id, and the text-search API can miss real models. Resolve by filename →
web-searching tokens → a "Posted to .../models/<ID>" snippet, then match the
file to a version and read recommended settings from the description tail.
Full recipe + the settings-extraction CUTOFF pitfall:
`references/model-notes-and-search-fallback.md`.

## Civitai type → ComfyUI folder

| Civitai type | ComfyUI folder | Notes |
|---|---|---|
| Checkpoint, CheckpointMerge | `models\checkpoints` | |
| LORA, LoCon | `models\loras` | modern ComfyUI loads LoCon from loras natively |
| TextualInversion | `models\embeddings` | prompt syntax `embedding:name` |
| Workflows | `user_data\workflows` | usually .zip — extract after download |
| Wildcards | `wildcards\` | needs a wildcard-capable node pack (e.g. Impact Pack) |

Anything else → mark `REVIEW` in the manifest rather than guessing a folder.

## Pitfalls

1. `/api/v1/user` → 404. The endpoint is `/me`.
2. Public endpoints are edge-cached (s-maxage=300) and rate-limited; on 429
   respect `Retry-After`. Sleep ~0.3 s between calls in loops.
3. Region gating can silently clamp responses to SFW on the green domain.
4. `sizeKB` → divide by 1024 for MB; zip/Other-type files are legitimately tiny.
5. Workflow JSON and node packs from Civitai execute arbitrary Python —
   inspect before running (same trust profile as `eval`).
6. Some model pages on .red are login-gated in browser, but the API resolves
   the same IDs anonymously — prefer the API over scraping.
7. Version names are not unique across models; always key manifest entries by
   (model_id, version_id).
