# Civitai SEARCH Auth — X-API-Key vs Bearer (verified 2026-08-04)

Critical gotcha for model SEARCH (not lookups, not downloads):

- `Authorization: Bearer <token>` on `GET /models?query=...` returns
  **HTTP 200 with silently empty `{"items":[]}`** whenever the result set
  would include mature content (detection models, NSFW LoRAs, etc.).
- The same query with **`X-API-Key: <token>`** header returns results.

Verified flips (0 hits Bearer → N hits X-API-Key): `adetailerNose`,
`ntd11`, `Anzhc`, `99coins`, `PitEyeDetailer`, `Nipple`, `CockAndBall`.
Both headers work fine for `/me`, `/models/{id}`, `/model-versions/{vid}`.

Search recipe:
```
curl -s -G "https://civitai.com/api/v1/models" \
  --data-urlencode "query=Anzhc" \
  --data-urlencode "limit=20" \
  --data-urlencode "nsfw=true" \
  -H "X-API-Key: $KEY"
```

Diagnosis rule: HTTP 200 + empty items on a plausible query =
**auth-header problem, not a missing model**. Retry with X-API-Key before
concluding the model doesn't exist or escalating to the user.
