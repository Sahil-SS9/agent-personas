# Civitai API Endpoint Notes (observed response shapes, 2026-08-04)

All under `https://civitai.com/api/v1`. Official docs: developer.civitai.com
(wiki github.com/civitai/civitai/wiki is deprecated/redirects).

## GET /me  (Authenticated)
```json
{"id": 9396419, "username": "Noctis_articuno_3", "email": "...",
 "tier": null, "profilePicture": null}
```
Note: `GET /user` does not exist (404 → HTML page, not JSON error).

## GET /models/{id}  (Public)
Top-level model object; `modelVersions[]` ordered newest-first:
```json
{"modelVersions": [{"id": 2832991, "name": "v6.0_Illustrious", ...}, ...]}
```
Use `modelVersions[0].id` when the user's URL has no `?modelVersionId=`.

## GET /model-versions/{id}  (Public)
```json
{
  "id": 2832991, "name": "v6.0_Illustrious",
  "model": {"id": 1377820, "name": "...", "type": "LORA"},
  "baseModel": "Illustrious",
  "files": [{
    "id": 2719141, "name": "AddMicroDetails_Illustrious_v6.safetensors",
    "sizeKB": 223121, "type": "Model",
    "metadata": {"fp": "fp16", "size": null, "format": "SafeTensor"},
    "downloadUrl": "https://civitai.com/api/download/models/2832991?fileId=2719141"
  }],
  "trainedWords": ["addmicrodetails"],
  "settings": {"strength": 0.5}
}
```
`type` values observed: Checkpoint, CheckpointMerge, LORA, LoCon,
TextualInversion, Workflows, Wildcards. LoCon ≠ LORA string — route both to
`models/loras` explicitly.

## GET /collections  (Public, edge-cached)
```json
{"items": [{"id": ..., "name": ..., "type": "Model", "read": "Public",
            "itemCount": 15, "user": {"id": ..., "username": ...}}],
 "metadata": {"nextCursor": ...}}
```
Params: `limit` (1–100), `cursor` (Newest sort only), `query`, `sort`,
`nsfw`. **`userId`/`username`/`user` params are accepted but IGNORED** —
always returns the global feed.

## GET /collections/{id}  (Public)
Metadata only (`id, name, description, read, type, nsfwLevel, tags, user`).
No items field, ever. Private → 404 (indistinguishable from missing).

## GET /vault/all, /vault/check-vault  (Authenticated)
User's vaulted versions: `{"items": [], "totalItems": 0, ...}` — empty unless
the user actively vaults. Not a route to "files on my profile".

## Non-working routes (tested, do not retry)
- `/collections/{id}/items`, `/collections/{id}/models` → 404 HTML
- `/collections?include=models` → param ignored, metadata only
- `/api/v2/*` → 404
- `/api/trpc/collection.getById` with API key → 401 JSON:
  "Please use the public API instead" (tRPC is cookie-session only)
- `/models?collectionId=X` → param ignored, returns 0 matches

## Rate limits & caching
- Public endpoints: `Cache-Control: public, s-maxage=300`.
- Conservatively rate-limited → on 429 respect `Retry-After`; loop with ~0.3s sleep.
- Authenticated calls skip cache.

## Downloads
`GET /api/download/models/{versionId}?fileId={fileId}` → 302 redirect to CDN.
`curl -L -O` works without auth for public models. Civitai may require
`token=` query param for early-access/mature files.
