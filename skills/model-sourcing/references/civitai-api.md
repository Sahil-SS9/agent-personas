# Civitai API — Verified Endpoint Notes (Aug 2026)

Base URL: `https://civitai.com/api/v1/` · Auth: `Authorization: Bearer <token>`
Official reference: https://developer.civitai.com/site/reference/

## Verified live (all probed with a real token)

| Endpoint | Status | Notes |
|---|---|---|
| `GET /me` | 200 | Token verification + account info: `{id, username, email, tier}` |
| `GET /user` | **404** | Does NOT exist — common wrong guess |
| `GET /models?username=X` | 200 | Models published by a user |
| `GET /collections` | 200 | **Public global feed only.** `userId`, `username`, `user` params all silently ignored — results are other users' collections |
| `GET /collections/{id}` | 200/404 | Public collections only; private = 404, indistinguishable from missing |
| `GET /user/collections`, `/users/{id}/collections`, `/v2/collections` | 404 | Do not exist |
| `GET /vault/all` | 200 | User's vaulted files (paginated envelope) |
| `GET /vault/check-vault` | 200 | Returns `[]`/ids |

## The private-collections limitation (from official docs, verbatim gist)

> "Only **public** collections are ever returned — private collections are
> unreachable, and a private collection is indistinguishable from a missing
> one. There is no 'my collections' mode here — own-collection discovery is
> a per-user (authoring) surface, not public discovery."

**Implication:** when a user says "my files are in a folder on my profile" and
that folder is a private collection, no API probing will find it. Skip straight
to the workaround:

1. Ask user to set the collection visibility to **Public** (profile → collection
   → edit → visibility), then `GET /collections/{id}` works.
2. Or have them paste the model page URLs; resolve each with `GET /models/{id}`
   → modelVersions → files (each file has `id`, `name`, `sizeKB`, `type`
   (Model/LoRA/VAE...), `format`, `downloadUrl`).

## Download URL pattern

```
https://civitai.com/api/download/models/{versionId}
?token=<token>   # optional; needed for mature/restricted content
```

With comfy-cli:
```
comfy model download --url "https://civitai.com/api/download/models/{versionId}" \
  --relative-path models/<folder> --set-civitai-api-token <token>
```

## Rate limiting & caching

- Public endpoints: `Cache-Control: public, s-maxage=300, stale-while-revalidate=150`
- `/collections` is conservatively rate-limited → honor `Retry-After` on 429
- Authenticated calls skip cache
- Region gating: responses may be silently clamped SFW regardless of `nsfw` param

## Token handling

- Store: `<project>/secrets/civitai.env` as `CIVITAI_API_TOKEN=<key>`
- Read in shell: `KEY=$(sed -n 's/^CIVITAI_API_TOKEN=//p' secrets/civitai.env)`
- Never print the key into chat output, logs, or memory
