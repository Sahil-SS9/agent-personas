# Inspecting & Reviewing Saved ComfyUI Workflows (via CLI + MCP)

How to figure out **which workflow the user is actually running** and **review the
full graph** of a saved workflow file through the comfy-cli / comfy-mcp surface.
Purposely inspection-only — no execution. Pairs with the `comfyui` skill's execution
scripts (run_workflow.py etc.) and this skill's MCP wiring
(`references/comfy-mcp-wiring.md`).

## 1. Determine "which workflow is currently in use?"

**There is NO reliable server-side answer.** ComfyUI does not persist "the currently
open workflow" anywhere queryable:
- `/queue` and `/history` show only executed jobs — empty while idle.
- `user/default/comfyui.db` is the assets/tags gallery DB, not open-tab tracking.
- Reading the ComfyUI browser tab (e.g. over CDP) can return a **STALE or UNSAVED
  graph** (`document.title` shows `*Unsaved Workflow - ComfyUI`) that is NOT what the
  user is running. Do NOT trust the browser tab as ground truth.

**Trust, in order:**
1. **Ask the user directly** — they know what they loaded. (Both auto-guesses this
   session — "newest saved file" and "browser tab" — were wrong; the real answer was
   a *third*, older-but-current file.)
2. `comfy workflow list --where local` — authoritative saved-file inventory with
   `modified` (epoch-ms) to see recent activity.
3. `curl http://127.0.0.1:8188/object_info/CheckpointLoaderSimple` — lists which
   **checkpoints are INSTALLED**, not which is **loaded**. Installed ≠ in-use.

Pitfall: the **newest-saved JSON** in `user/default/workflows/` is often a *different*
workflow than the one currently open. Timestamps reflect "what I last exported/saved,"
not "what's on the canvas."

## 2. Review a saved workflow file's full graph

Portable installs save editor-format JSON at `user/default/workflows/<name>.json`
(top-level `nodes` + `links` arrays, NOT API-format `class_type`).

**Link tuple:** `[link_id, origin_node_id, origin_slot, target_node_id, target_slot, type]`
— flows FROM `origin_node_id/origin_slot` TO `target_node_id/target_slot`.

Node census + active/bypassed state:
```bash
python3 -c "
import json,collections
wf=json.load(open('Basic_V37.json',encoding='utf-8'))
print('nodes',len(wf['nodes']),'links',len(wf['links']))
for t,c in collections.Counter(n.get('type') for n in wf['nodes']).most_common(25): print(c,t)
# mode: 0=active (or absent), 4=bypassed, 2=muted
"
```
Trace which checkpoints feed the sampler/detailers (follow MODEL/CLIP/VAE links):
```bash
python3 -c "
import json
wf=json.load(open('Basic_V37.json',encoding='utf-8'))
id2={n['id']:n for n in wf['nodes']}
for l in wf['links']:
    if l[1]==45 and l[4] in ('MODEL','CLIP','VAE'):
        print('ckpt 45 ->', id2[l[3]].get('type'),'[',l[3],']', l[4])
"
```
- `widgets_values` per node = the node's real settings (resolution, cfg, denoise,
  model, prompt) — pairs positionally to `object_info`.
- **Dormant subsystem tells:** wiring nodes present for ControlNet/IPAdapter but with
  no model loaded (e.g. `ControlNetLoader` → `control_net_name: null`) or paths
  bypassed means the feature is OFF even though the nodes exist. Read toggles, not
  just node presence.

## 3. list_workflow_slots positional-alignment trap (IMPORTANT)

`comfy workflow slots` / the MCP `list_workflow_slots` tool pairs slot NAMES onto
values **positionally**. Nodes with dynamic/partner combos — **UltimateSDUpscale,
FaceDetailerPipe, DetailerForEach, any Impact/EditDetailer node** — under-report their
input schema, so every later pairing shifts. A node's declared typing then associates
values with the WRONG slot names (real example: `48.steps` showing `"randomize"`,
`48.denoise`→`0.16`, `48.tile_width`→`"Linear"`, `32.drop_size`→`16`).

**Consequence:** do NOT write via `set-slot` / `set_workflow_slot` on these nodes —
the write would land in a different field. The CLI itself warns: *"Do not set them
... Edit the workflow JSON directly, or use a template without dynamic-combo partner
nodes."* For review, read `widgets_values` from the file, not the misaligned slot
table. The tool reports these as `suspect_slots` / a `warning` — honor it.

## 4. comfy-cli `discover` — command surface relevant to inspection

`comfy discover` returns the full schema. Families useful for review:
- workflows: `list`, `get`, `save`, `delete`, `slots`, `set-slot`, `vary`, `notes`,
  `compose`, `decompose`, `fragment ls/show/validate`, `validate`
- nodes: `ls`, `show`, `search`, `upstream`, `downstream`, `path`, `types`,
  `categories`, `refresh`, `deps`
- models: `search`, `show`, `list-folders`, `list-folder`, `download*`
- `workflow notes` / MCP `list_workflow_notes` reads embedded Note/MarkdownNote nodes —
  the author's usage notes + tag references (quality-tier tables, lighting/style cheats).

## 5. Example: Cheonma's NoobAI/Illustrious set (Aug 2026)

`comfy workflow list --where local` showed **12 saved workflows** in three families:
1. **Legendaer V37 Mega** (civitai user Legendaer): `Basic_V37` / `Standard_V37` /
   `Advanced_V37` / `Advanced_QwenVL_V37` / `Advanced_Gemma_V37` / `Detailer_V37` —
   NoobAI-XL/Illustrious, Impact-Pack detailers (FaceDetailerPipe + DetailerForEach),
   ImpactWildcardProcessor prompts, `hyphoria_v002` base.
2. **vsLinx All-in-One** v5.1 (TXT2IMG + IMG2IMG): 215 nodes / 418 links, 8-stage
   FaceDetailer chain, two checkpoints (base + refiner), IPAdapter/ControlNet dormant.
3. **MiniMax H3**: all-in-one + Turbo LoRA ref (`references/minimax-h3-files.md`).

The **actual current** workflow was **Basic_V37** (76 nodes / 141 links, base
`hyphoria_v002`, cfg 8, 20 steps euler_ancestral/normal, 4-anatomy-detailer chain +
2 easy hiresFix). It differed from BOTH the newest-saved file (vsLinx all-in-one) and
a stale browser tab (a 10-node MiniMax probe). Lesson: ask, cross-check `workflow
list`, and never trust the newest timestamp or the tab.
