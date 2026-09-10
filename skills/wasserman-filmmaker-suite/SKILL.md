---
name: wasserman-filmmaker-suite
description: "Use when working with Wasserman Filmmaker Suite tools."
version: 1.0.0
license: MIT
---
# Wasserman Filmmaker Suite

## When to Use

- User references **ScriptBreak, Cork Board, Master Canvas, Blockout, Motion Previs Studio, Circle Take, Stem Studio, Slate, Call Sheet, Sam PDF Studio**, or any `*-mcp` / `*-hermes-plugin` repo in `wassermanproductions`.
- User asks whether one of these (or any OSS repo) can run on their **Windows** PC, or wants to wire up an MCP server / Hermes plugin from the suite.
- User compares the suite's tools or plans an AI-film pre-production pipeline (script → previs → generator handoff).

AI-native filmmaking toolchain by **Sam Wasserman** (`github.com/wassermanproductions`). Script → previs → AI-video pipeline. Nearly every tool has **two layers**:

1. **Desktop GUI app** — optional visual front-end.
2. **Zero-dependency Node MCP server** (`mcp/*-mcp.mjs`, Node ≥ 18) — headless, stdio, **cross-platform by design**. This is the primary way Hermes drives them; the GUI is not required.

Also available: **Hermes plugins** (`*-hermes-plugin` repos) that bundle Hermes tools directly.

## Windows-compatibility map (this user's PC: Win 11, RTX 4070 Ti)

Verified by inspecting each repo's build config + GitHub release assets (method in `references/repo-platform-audit.md`).

| Tool | Framework | Windows status | Fastest path on this PC |
|---|---|---|---|
| **Cork Board** | Electron | ✅ Prebuilt `CorkBoard-Setup.exe` | Download release `.exe` |
| **ScriptBreak** | Tauri | ✅ Prebuilt `ScriptBreak_1.0.0_x64-setup.exe` / `.msi` | Download release `.exe` |
| **Master Canvas** | Electron | ✅ Electron, `win` target set (nsis/zip); ⚠️ no prebuilt Win bin yet | Build from source, or use its Node MCP server headlessly |
| **Blockout** | Electron + electron-vite | ✅ Full Win support (`package:win` NSIS x64 + ffmpeg-for-Win); ⚠️ no published release yet | Build from source (see below), or use `blockout-mcp` headlessly |
| **Motion Previs Studio** | Electron | ⚠️ Only Mac dmg published; has its own `motion-previs-mcp` server | Use the MCP server headlessly |
| **Circle Take** | Electron | ⚠️ Only Mac published currently | MCP not separate yet; GUI buildable |
| **Stem Studio** | Electron | ❌ No Windows target — mac/Linux only | Not usable on this PC |
| **Slate** | TypeScript | Newer, no release published yet | — |
| **Sam PDF Studio** | Swift/native | ❌ macOS-native GUI only | GUI not usable; its `sam-pdf-studio-mcp` engine IS cross-platform |
| **Call Sheet** | native | ❌ macOS menu-bar launcher | Not useful on Windows |

**MCP servers (all cross-platform, work on this PC today):** `blockout-mcp`, `motion-previs-mcp`, `master-canvas-mcp`, `unofficial-davinci-mcp` (drives DaVinci Resolve), `sam-pdf-studio-mcp` (PyMuPDF merge/split/redact/OCR).

**Hermes plugins:** `master-canvas-hermes-plugin` (8 tools + bundled `handoff` skill), `hermes-davinci-resolve-plugin`.

## Installed state (this machine — verified 2026-08-13)

All four suite apps are INSTALLED and verified working:

- **ScriptBreak** → `C:\Users\Hermes\ScriptBreak\scriptbreak.exe` (prebuilt Tauri NSIS, silent install)
- **Cork Board** → `C:\Users\Hermes\CorkBoard\Cork Board.exe` (prebuilt NSIS, then **moved** out of `%LOCALAPPDATA%\Programs` — user preference: suite apps live in their own folders under `~/`)
- **Blockout** → `C:\Users\Hermes\Blockout\Blockout.exe` (built from source v5.1.1 — `npm install` + `npm run package:win`, then silent NSIS)
- **Master Canvas** → no app needed; headless via plugin + MCP

Sources cloned at `C:\Users\Hermes\Projects\{blockout,cork-board,scriptbreak,master-canvas,unofficial-davinci-mcp}`.

**DaVinci Resolve MCP (2026-08-15):** `unofficial-davinci-mcp` cloned to `~/Projects/unofficial-davinci-mcp` (Apache-2.0, Python MCP server, 37 tools) but **NOT installed/wired** — user has no Resolve yet; will install Resolve after first Flux 3 clips, then set up. Windows gotchas: `install_bridge.py` only handles macOS/Linux — hand-copy `bridge/resolve_bridge.py` to `%APPDATA%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Utility`; `resolve_api.py` lacks Windows scripting paths (may need `RESOLVE_SCRIPT_API` env); voice extra is macOS-only (`rumps`). Interchange tier (FCPXML/EDL/cube LUT) works everywhere.

All 4 MCP servers are **wired in the creative profile config.yaml** (`mcp_servers`: `cork-board`, `scriptbreak`, `master-canvas`, `blockout` — `command: node`, args point at each repo's `mcp/*.mjs`) and **smoke-tested live**: cork-board 25 tools, scriptbreak 11, master-canvas 14, blockout 34. Real round-trip proven: cork-board `apply_preset` (`presetId: 'demo-ava'`) → `get_board` = 36 cards / 4 acts. `master-canvas-hermes-plugin` installed + enabled (needs gateway restart / new chat to register its 8 tools).

## Key facts & gotchas

- **Silent NSIS from git-bash**: `./Setup.exe //S` (double slash — MSYS eats a single one). Custom dir: `//D=C:\path` as the LAST argument, unquoted.
- **NSIS installers auto-launch the app** after install — expect live processes immediately; kill them before moving install folders.
- **`tasklist //FI "IMAGENAME eq Cork Board.exe"` rejects spaced image names** ("Invalid argument") — use `tasklist | grep -i cork` instead. `taskkill //IM` has the same quirk.
- **Moving an installed Electron app**: kill all its processes first (`mv` fails with "Device or resource busy" otherwise), then repoint the desktop shortcut via PowerShell `WScript.Shell` COM (`.TargetPath` + `.WorkingDirectory`). Full recipe in `references/windows-setup.md`.
- **Blockout's control bridge (`~/.config/blockout/control.json`) exists ONLY while the app runs with a project open.** On first launch it sits at the New Project dialog and writes nothing — that's normal, not a broken MCP.
- **cork-board MCP arg name is `presetId`, not `preset`** — `apply_preset` with the wrong key returns "No preset with id undefined".
- **Rebuilding Blockout** (update flow): `cd ~/Projects/blockout && git pull && npm install && npm run package:win` → installer in `release\` → silent reinstall.

- **Blockout** (`wassermanproductions/blockout`, Apache-2.0): grey-box 3D previs + camera/cast marks, exports motion-reference packages for **Seedance / Veo / Kling / LTX / Wan**. This is the suite's previs heart and the one most worth building on this PC. `blockout-mcp.mjs` header notes it was "modified for cross-platform Windows support in 2026".
- The skill docs for ScriptBreak/Master Canvas/Cork Board record paths like `/Applications/ScriptBreak.app` and `xattr -cr` (macOS Gatekeeper). **Ignore those on Windows** — they're Apple-specific install residue from the profile they were first installed on. Use the Windows installer/NSIS path instead.
- `install.sh` scripts in these repos are **macOS-only** (curl DMGs, `open`, `hdiutil`) — do not run them on Windows.
- GUI apps are "no AI calls": the app exports prompt packs / JSON, and the LLM (you) does the generation. The MCP servers read/write plain on-disk project JSON — fully usable without any GUI.
- Everything in the suite runs local-first: no accounts, no cloud, no telemetry. Suggested donation (ko-fi) if used commercially.

## Generator handoff → this user's stack (FLUX3 / BFL + MiniMax H3)

Blockout's generator targets are **extensible JSON data, not code**. `src/engine/profiles.ts`
(`BUILTIN_PROFILES`) states: *"Updating a model is a config edit. Users can add profiles as
JSON in the project's profiles/ folder."* Each profile declares `kind` (video/image),
`maxDuration`, `aspects`, `exportWidth`, `fps`, `refModes` (`firstFrame`/`lastFrame`/
`referenceVideo`/`depthVideo`/`stills`), `attachHint`, `adherenceClause`. So a missing
generator is a config add, not a fork.

**Neither FLUX3 (BFL) nor MiniMax H3 ships as a built-in Blockout profile.** Built-ins today:
Seedance 2.0, Veo 3.1, Kling 2.x, LTX 2.3, Wan 2.2 (video) + GPT Image 2, Nano Banana, Ideogram,
Krea 2 (stills). Blockout also emits a **ComfyUI workflow JSON** (`src/renderer/export/comfy.ts`,
depth/video-reference pipeline for Wan/LTX nodes) — repointable at other local pipelines.

Practical mapping for this PC:
- **FLUX3 (BFL, free promo, via built-in `bfl_flux3_*` tools):** FLUX3 takes text + first-frame/
  keyframe **stills** (no full reference-video injection). So Blockout's value = lock composition
  via the exported first-frame still + the `prompt.txt`, then translate the camera move into FLUX3's
  native **timed camera + timing-beat prose** (see `flux3-video-directing`). Exported MP4 can't be
  fed as motion control, only as framing reference.
- **MiniMax H3:** consumes a true **reference video** (`reference_video` / r2va mode) and
  `first_frame`/`last_frame`. Blockout's reference MP4 + stills map directly. On local ComfyUI H3
  (ref2va + Turbo LoRA), adapt Blockout's exported ComfyUI workflow; on the API, feed the MP4 as
  the r2va reference (`minimax-video-generation` skill).
- To generate for these, ADD a `flux3` / `minimax-h3` profile JSON in the project `profiles/`
  folder (kind video, refModes per above) instead of using the built-in list.

## Visualizing suite work in the Hermes desktop

Neither Master Canvas nor Blockout has an existing **visual** desktop plugin (the
`master-canvas-hermes-plugin` is agent-side Python tools only — no live pane). The Hermes desktop
SDK (`@hermes/plugin-sdk`, disk plugin at `~/.hermes/profiles/<p>/desktop-plugins/<id>/plugin.js`)
**does** support building one: a `PANES_AREA` pane with a live `<canvas>` (render Master Canvas
board / Blockout blocking plan from the project JSON), a `ROUTES_AREA` sidebar page, and live data
via `host.onEvent('*', fn)` + a scoped Python backend `ctx.rest`/`ctx.socket` (socket is no-op on
OAuth remotes — always keep a polling fallback). See the bundled `hermes-desktop-plugins` skill
for the plugin-authoring surface.

## Workflow with Hermes

1. **Install path decision:** prefer the prebuilt Windows installer (`Cork Board`, `ScriptBreak`); for ones without a Win binary, prefer the **Node MCP server** (zero-dep) over building the GUI unless the user explicitly wants the visual app.
2. **Wire the MCP server** as stdio: `command: node`, `args: ["<abs>/mcp/<name>-mcp.mjs"]`, optional `env` for the project file (e.g. `SCRIPTBREAK_PROJECT`, `CORK_BOARD_PROJECT`).
3. For the GUI companions, build from source on Windows where a prebuilt binary isn't published:
   - Electron apps (Master Canvas, Blockout, Motion Previs, Circle Take): `npm install` then `npm run desktop:dist` (or `electron-builder --win nsis --x64`). Blockout needs `npm run package:win` which prep's ffmpeg for Windows first.
   - **Prereq on Windows:** Node.js ≥ 18 and a build toolchain (e.g. VS Build Tools) for any native deps.

## References

- `references/repo-platform-audit.md` — the reusable method for judging cross-platform support of any OSS tool repo from its build config + release assets.
- `references/windows-setup.md` — session-verified install detail: download URLs, silent-NSIS commands, Electron-app relocation + shortcut fix-up, Blockout source build, config YAML edit, and the generic stdio MCP smoke-test one-liner.
- `references/flux-minimax-h3-profile.md` — Generator profiles for Flux 3 (Hailuo API) and MiniMax H3 (local ComfyUI), plus handoff integration steps.

## Related / overlapping skills note

- `scriptbreak`, `cork-board`, `master-canvas` (user-owned skills in `creative/`) document the individual apps from their original macOS install. This umbrella is the Windows-aware, suite-level map.
