# Civitai REST API — Field Notes (verified 2026-08)

Base: `https://civitai.com/api/v1` · Auth: `Authorization: Bearer <key>`
(Header auth confirmed; `?token=` works for downloads.)
`civitai.red` is the same backend as `civitai.com` (red = NSFW-allowed domain).
Official reference: https://developer.civitai.com/site/reference/ (replaces the old GitHub wiki).

## Users
- `GET /me` — Authenticated. Returns id, username, tier. **There is NO `/user` endpoint** (404).
- `GET /users?ids=1,2` / `?query=prefix` — username lookup, public.

## Models
- `GET /models/{id}` — full model + `modelVersions[]` (pick one's `id`).
- `GET /model-versions/{versionId}` — the workhorse. Returns:
  - `model.name`, `model.type` (Checkpoint/LORA/LoCon/TextualInversion/Workflows/Wildcards/CheckpointMerge...)
  - `version.name`, `baseModel`, `trainedWords`/trigger words
  - `files[]`: `{id, name, sizeKB, downloadUrl, type, metadata{fp,size}}`
- `GET /model-versions/by-hash/{hash}` — identify a file you already have.
- `GET /models?username=X` — models PUBLISHED by user (usually 0 for curators; collections ≠ published).

## Downloads
- `downloadUrl` + `&token=<key>` (or header) → direct file.
- Resumable: `curl -L -f --retry 5 --retry-delay 3 -C - -o out "<url>?token=KEY"`.
- Workflow zips: unzip into `user_data/workflows/` so they appear in the UI browser.

## Collections — the minefield (verified against official docs)
- `GET /collections` and `GET /collections/{id}` are **PUBLIC-ONLY and metadata-only**.
  - No endpoint exposes a collection's items. `userId`/`username`/`user` filters are silently ignored (returns the global feed).
  - Private collections 404 and are indistinguishable from missing — **by design**.
  - tRPC internals (`/api/trpc/collection.*`) reject API keys (401).
- Workaround that works: ask the user for individual model URLs (fastest), or scrape the rendered collection page's `__NEXT_DATA__` JSON (auth cookie `civitai_token=<key>` works in a browser session).
- **Moderation gate:** a freshly-public collection shows "This content hasn't been rated yet / Pending review" to everyone but the owner, including APIs. Temporary; retry later.

## Vault
- `GET /vault/all`, `/vault/check-vault` — user's saved-for-download vault; often empty. Not the same as collections.

## Rate limits & behavior
- Public endpoints are edge-cached (`s-maxage=300`); authenticated calls skip cache.
- Respect `Retry-After` on 429. A ~0.3s sleep between version lookups is safe.
- Restricted regions silently clamp results to SFW.
