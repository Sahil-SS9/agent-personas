---
name: model-sourcing
description: "Use when sourcing models from Civitai/Hugging Face."
version: 1.0.0
license: MIT
---
# Model Sourcing

Find, vet, and download model weights from public hubs (Civitai, Hugging Face)
into a local generation stack (ComfyUI or similar). Covers API auth, endpoint
quirks, quantization selection for the GPU, disk budgeting, and placement.

## Support files

- `references/civitai-api.md` — verified Civitai endpoint table, the
  private-collections limitation + workarounds, download URL patterns,
  token handling.
- `references/minimax-h3.md` — MiniMax H3 video model: file→folder map,
  quant picks for 12 GB VRAM, workflow templates, hardware notes.

## When to use

- User shares Civitai links, collections, or an API key
- Planning which model files/quants to download for a specific GPU
- Budgeting disk before large downloads (video models run 15–65 GB each)
- Routing downloads into correct ComfyUI model folders

## Core workflow

1. **Inventory before downloading** — enumerate files + sizes via API, never guess:
   - Hugging Face: `curl -s "https://huggingface.co/api/models/{org}/{repo}/tree/main?recursive=true"`
     returns JSON array with `path` + `size` per file. Sum it, print a table.
   - Civitai: `GET /api/v1/models/{id}` → versions → file metadata.
2. **Budget disk** — sum chosen files, compare to free space, keep ≥20% headroom.
3. **Pick quantization for the GPU** — fp8/int8/nvfp4 for 8–16 GB VRAM;
   bf16/fp16 full precision only for ≥24 GB. Size tables in the reference files.
4. **Auth if needed** — Civitai: `Authorization: Bearer <token>`; verify with
   `GET /api/v1/me`. HF public repos usually need no token.
5. **Download** — prefer `comfy-cli` for ComfyUI placement:
   `comfy model download --url <url> --relative-path models/<folder>`
   (add `--set-civitai-api-token <token>` for Civitai URLs).
6. **Verify** — file sizes match the API listing; model appears in
   `comfy model list` / the UI dropdown.

## Civitai quick facts (full detail in references/civitai-api.md)

- Verify token: `GET /api/v1/me` — **not** `/api/v1/user` (that endpoint 404s).
- `/collections` is a **public global feed only** — `userId`/`username` filters
  are silently ignored. There is **no "my collections" mode**.
- Private collections are unreachable via API by design (404, indistinguishable
  from missing). Don't burn calls probing — ask the user to make the collection
  public or paste model URLs directly, then use `GET /collections/{id}` /
  `GET /models/{id}`.
- Vault: `GET /vault/all` lists files the user vaulted.

## Workflow-aware sourcing

When sourcing a model set for ComfyUI, inspect the user's existing workflow directory before downloading or replacing anything. Existing workflows may reference a different quantization or model family than the files being sourced. After downloading, verify exact filenames and sizes on disk, then compare the workflow's loader values against the installed files. If a workflow is supplied as an editor-format JSON, it can be placed in the user's workflow folder for UI registration, but it is not directly executable through the REST API until exported to API format.

For large model sets, separate these phases: (1) download and file verification, (2) workflow placement/registration, (3) node/dependency verification, and (4) execution. A user instruction to hold or not start ComfyUI blocks phase 4 and any launch action; continue only with explicitly authorized read-only inspection or file placement.

## Pitfalls

1. `/api/v1/user` does not exist — use `/api/v1/me` for token verification.
2. Civitai collections filters lie: user-scoped params return the site-wide feed.
   Check response ownership client-side before trusting results.
3. Private collection ≠ broken collection — both are 404. Escalate to the user
   instead of retrying endpoint variants.
4. Collections endpoint is edge-cached and conservatively rate-limited — honor
   `Retry-After` on 429.
5. Never pull bf16 video weights onto a consumer card — check the size table
   first; they can be 3× the fp8 variant.
6. Store tokens in `<project>/secrets/civitai.env` as `CIVITAI_API_TOKEN=<key>`;
   never echo the token into chat output or memory.
7. Region gating: Civitai responses may be silently SFW-clamped.
