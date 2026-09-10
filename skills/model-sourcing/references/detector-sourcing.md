# Detector (.pt) & Utility Model Sourcing Playbook (verified 2026-08)

ComfyUI detailer workflows (Impact-Pack ADetailer style) reference ultralytics
detection models by exact filename. These are frequently invisible to Civitai
search (mature filters) and live on Hugging Face or inside multi-file zips.

## Proven sources, in order of hit rate

1. **Hugging Face `Bingsu/adetailer`** — canonical face/hand/person detectors:
   `face_yolov8{m,n,s}.pt`, `hand_yolov8{n,s}.pt`, `hand_yolov9c.pt`,
   `person_yolov8{m,n,s}-seg.pt`, `deepfashion2_yolov8s-seg.pt`.
   URL: `https://huggingface.co/Bingsu/adetailer/resolve/main/<file>`.
2. **Hugging Face `Anzhc/Anzhcs_YOLOs`** — anime face/eyes/breasts/hair seg
   models. Filenames contain spaces ("Anzhc Face seg 640 v3 y11n.pt") →
   URL-encode as %20. List via
   `https://huggingface.co/api/models/Anzhc/Anzhcs_YOLOs/tree/main`.
3. **Civitai multi-model detection zips** — "Anime NSFW Detection / ADetailer
   All-in-One"-type packs unpack to exact per-class filenames (e.g.
   `ntd11_anime_nsfw_segm_v4_penis.pt`, `_pussy.pt`, `_nipples.pt`, `_all.pt`).
   Download zip → extract → move matching files to
   `models\ultralytics\{bbox,segm}\`.
4. **ComfyUI-Manager catalog cache** — `user/__manager/cache/*model-list.json`,
   shape `{"models": [...]}` (500+ entries with `filename`, `save_path`, `url`).
   Covers sdxl_vae, NMKD upscalers, standard adetailer models.

## Civitai search for detection models
- **Use `X-API-Key: <token>` header, NOT `Authorization: Bearer`** — Bearer
  returns silently empty `{"items":[]}` for queries whose results include mature
  content. Same query, X-API-Key → results. (Verified: adetailerNose, ntd11,
  Anzhc, 99coins all flipped 0→N hits.)
- Query params: `query=...&limit=20&nsfw=true`.
- Many detector models ship as .pt with type "Detection"; zip variants of the
  same version often contain several .pt files.

## Placement
- bbox detectors → `models\ultralytics\bbox\<file>.pt`
- segm detectors → `models\ultralytics\segm\<file>.pt`
- Create the bbox/segm dirs if absent (fresh installs have neither).
- Workflow references are exact and case-sensitive, including odd spellings
  ("Nipple-yoro11x_seg", trailing underscores "adetailerNose_") — match the
  filename byte-for-byte or rename the download to the workflow's spelling.

## Audit pattern
Extract all `.pt/.pth/.safetensors` widget strings from the workflow JSON
(editor-format `nodes[].widgets_values`), then walk the model dirs and diff.
Unfindable files: hand the user the exact filename + destination folder.
