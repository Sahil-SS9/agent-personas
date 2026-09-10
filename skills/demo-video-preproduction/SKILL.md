---
name: demo-video-preproduction
description: "Use when planning a product demo video from a brief."
version: 1.0.0
license: MIT
---
# Demo Video Pre-Production Pipeline

Class: turning a spoken/written product-demo concept ("showcase what this tech should look like") into a storyboard + shot list + copy-paste prompt sheet for AI video generators (FLUX 3 web UI, etc.).

## Pipeline

1. **Mine the product for vocabulary first.** Clone/read the repo (or docs/screenshots the user provides) before writing a single beat. Use real module names, UI strings, and doctrine text in the storyboard — authenticity is what makes a mock demo credible. If web tools are unconfigured, `git ls-remote` + `git clone` + `git show <branch>:<path>` still work; useful content often lives on non-main branches (`git ls-tree -r --name-only origin/<branch>`).
2. **Build the cork board** (cork-board MCP, headless, `projectPath` inside the user's project folder): create_project → rename/add acts → add cards (one beat = one card, `actTitle` targeting) → add_entity for cast/locations/labels → tag_card. Batch independent calls.
3. **Tag every card with a production taxonomy** so the storyboard doubles as the generation shot list:
   - `FLUX CLIP` — live-action AI generation
   - `UI INSERT` — screen capture / mock UI (real product screenshots are the design anchor)
   - `HUD POV` — first-person overlay shots
   - `START FRAME NEEDED` — hero shots: generate a still first, feed as image start reference for motion consistency
4. **Add THE AGENT as a cast member** (Presence role) for agent-centric products — it never gets a face; it exists as UI, HUD, voice. Show the product's trust doctrine on screen (e.g. agent auto-drafts, human taps CONFIRM).
5. **Write the plan doc** into the project folder (`PLAN-<slug>.md`): act/scene table, runtime budget, locked style prefix (verbatim string repeated in every prompt — match the product's UI palette), prompt discipline rules, and the hero product moments that must land.
6. **Prompts last, full sheet first.** Write all per-shot prompts (flux3-video-directing anatomy) into the Master Canvas package + cork card `prompt` fields before any generation, so structural issues surface before credits burn. Then iterate shot-by-shot during generation, one variable at a time.

## Pacing heuristics

- 3–5 min demo ≈ 20 scene cards across 5 acts; one FLUX clip = one shot, 5–8s default.
- Intercut UI inserts with live-action; use a timer motif (HUD timestamps) for time-critical sequences like MEDEVAC.
- Keep demo content clean: no gore, "training/simulation" framing, humans make every decision.

## Pitfalls

- Don't ask the user for structure decisions you can propose — present the act breakdown, ask only about runtime/pacing (it changes card density).
- Repo may be private/empty on the API (`api.github.com` 404) while `git ls-remote` works — try git before concluding the repo is inaccessible.
- Wasserman suite skills (cork-board, master-canvas, scriptbreak) document macOS paths; on Windows the MCP servers work headless anyway — ignore the /Applications references, pass `projectPath` per call.
