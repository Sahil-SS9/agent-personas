# Impact Pack SAM models and empty model dropdowns

## SAMLoader model source (ComfyUI-Impact-Pack)
- `modules/impact/impact_pack.py` registers folder `sams` →
  `<ComfyUI>/models/sams/` with all supported pt extensions.
- SAMLoader lists files ending `.pt`/`.pth`/`.safetensors`, EXCLUDING names
  containing `'hq'` (SAM-HQ models use a separate registry).
- **Empty dropdown = `models/sams/` missing or empty.** Create the directory,
  drop in a SAM file, and reopen/reload the node. The dir may not exist on a
  fresh install.
- Recognized model kinds by filename: `vit_h` → vit_h, `vit_l` → vit_l,
  else vit_b (via `sam_model_registry`); `sam2*.pt` / `sam2.1*.pt` names map
  through `sam2_config_table` and need their bundled YAML configs.
- `'ESAM'` appears only if ComfyUI-YoloWorld-EfficientSAM is installed.
- Common starter model: `sam_vit_b` (~375 MB) from the segment-anything repo;
  `sam_vit_h` (~2.4 GB) for max quality.

## Optional-input rule (the actual diagnostic lesson)
- FaceDetailer's `sam_model_opt` input is OPTIONAL. Detailers work with just a
  bbox/segm detector (e.g., UltralyticsDetectorProvider YOLO models); SAM is
  only consulted when connected AND the loader executed.
- A SAMLoader with `model_name: null` whose output feeds optional inputs and
  which is absent from the error's `executed` list CANNOT be the cause of the
  failure.
- Check the executed list in the error message (`messages[].execution_error.
  executed`) before chasing SAM.

## Editor-format workflow gotcha
- In editor-format JSON, nodes inside group nodes (e.g., vslinx-style
  all-in-one detailer workflows) don't appear in the top-level `nodes` array.
  Grep the raw JSON for the node type string (e.g., `"SAMLoader"`) to find
  widgets/values; `extra.groupNodes` may be empty when groups are baked in.
- Group inner nodes live at `definitions/subgraphs[N]/nodes[..]`, where the
  subgraph's `id` equals the group node's uuid-hash `type`. Confirmed layout
  for the "allInOneDetailer...TXT2IMG" vslinx workflow: SAMLoader at
  `definitions/subgraphs[0]/nodes[29]`, widgets `[null, "Prefer GPU"]`.

## Concrete fix (download + patch a saved null model_name)
1. The `models/sams/` dir is not auto-created on portable installs. Official
   Meta checkpoint (a torch **zip container**, ~357 MB):
   ```bash
   mkdir -p "<install>/models/sams"
   curl -sL -o "<install>/models/sams/sam_vit_b_01ec64.pth" \
     "https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth"
   ```
2. Verify it's real (foil an HTML error page): `open(path,'rb').read(16)[:4] == b'PK\x03\x04'`.
3. `/object_info` refreshes live — no restart:
   `curl -s http://127.0.0.1:8188/object_info/SAMLoader | python3 -m json.tool`
   → `required.model_name[0]` should now list the file.
4. If a SAVED workflow still carries `"model_name": null`, patch the editor JSON
   (back up first):
   ```python
   sub = wf["definitions"]["subgraphs"][0]
   for n in sub["nodes"]:
       if n.get("type") == "SAMLoader":
           n["widgets_values"] = ["sam_vit_b_01ec64.pth", "Prefer GPU"]
   ```
   Then reload the workflow in the editor.

## Silent no-output (no error but detail preview empty)
- `status: success` + `execution_success` with NO output image is a *silent*
  dead branch, not a crash. Inspect `/history`: a node present in the prompt
  graph but with no stored output across runs never produced data.
  Distinct from it, and check separately: `hostbuf_file_reader_read failed` is
  a DynamicVRAM streaming hiccup — see `references/dynamic-vram-errors.md`.
