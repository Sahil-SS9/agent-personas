# Workflow Placement Fix — making Civitai workflows visible in-UI (verified 2026-08)

**Correction to the "copy to Desktop and drag-drop" guidance:** users expect
workflows to appear in ComfyUI's Workflows browser. The portable build's
browser reads the per-user directory, not the shared one:

- In-UI browser source: `ComfyUI/user/default/workflows/`
- Civitai zips extract to: `ComfyUI/user_data/workflows/` (NOT read by the browser)

Fix: after extracting workflow zips, copy the folders:
```bash
cp -r ComfyUI/user_data/workflows/* ComfyUI/user/default/workflows/
```
Then the user refreshes the page (F5) → Workflows icon → folders visible.

Server-side verification (run before telling the user it's done):
```bash
curl -s "http://127.0.0.1:8188/api/userdata?dir=workflows&recurse=true"
# → JSON array listing each .json path, e.g.
#   ["allInOneDetailerAdetailerControlnet_v51TXT2IMG/TXT2IMG-ADetailer-v5.1-vslinx.json", ...]
```
Note: use the query-param form `?dir=workflows&recurse=true`; the path-style
`/api/userdata/workflows?...` returns 403.

Fallback only if the browser still misbehaves: Desktop drag-drop or
Workflow → Open. But fix the folder first — visibility is the expectation.
