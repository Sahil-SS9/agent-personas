# Repo platform-audit method — judging cross-platform support without guessing

Use this whenever the user asks "can this tool/app run on my PC?" for an open-source repo.
Deterministic source inspection beats guessing or trusting the README's marketing line.
All commands are git-bash / POSIX.

## 1. Establish a baseline: what does the user run?

Pin the target platform explicitly before auditing (e.g. Windows 11, RTX 4070 Ti).
The verdict is relative to that machine, not "is it cross-platform in the abstract."

## 2. Enumerate the org's repos (discovery)

When the user says "look at the other repos like X", list the whole org:

```bash
curl -fsSL "https://api.github.com/users/<ORG>/repos?per_page=100&sort=updated" \
  | python3 -c "import json,sys; [print(r['name'],'|',r.get('language'),'|',r.get('description')) for r in json.load(sys.stdin)]"
```

Then grab per-repo descriptions so you can bucket into "core product" vs "MCP server" vs
"plugin" vs "supporting/irrelevant" — the org often ships each app with a sibling
`*-mcp` and `*-hermes-plugin` repo.

## 3. Determine the app framework — this decides Windows buildability

Clone shallow and read the root for framework markers:

```bash
cd /tmp && git clone --depth 1 https://github.com/<ORG>/<repo>.git insp-<repo>
cd insp-<repo> && ls -1
```

Framework → platform capability:

| Marker | Framework | Cross-platform? |
|---|---|---|
| `electron/` dir + `electron-builder` devDep | Electron | ✅ buildable for mac/win/linux |
| `src-tauri/` + `tauri.conf.json` | Tauri (Rust) | ✅ mac/win/linux |
| `*.xcodeproj` / `*.swift` / `SwiftUI` | Native macOS | ❌ Windows impossible (GUI) |
| `package.json` with no electron/tauri | Likely web/CLI | Depends on scripts |

## 4. Read the build config — look for explicit `win` target

For Electron apps, `package.json` `build` (or `electron-builder.yml`):

```bash
python3 -c "import json; d=json.load(open('package.json')); print(json.dumps((d.get('build') or {}).get('win'),indent=1))"
```

- `build.win.target: [nsis, zip]` → Windows installer IS configured.
- A dedicated script like `"package:win": "npm run prepare:ffmpeg:win && ... electron-builder --win nsis --x64"` → Windows is a first-class build target.
- For Tauri: `bundle.targets` being `"all"` includes Windows `.msi`/`.exe`.

## 5. Check the release assets — does a prebuilt binary actually exist?

A configured target is not the same as a shipped binary. Query the latest release:

```bash
curl -fsSL "https://api.github.com/repos/<ORG>/<repo>/releases/latest" \
  | python3 -c "import json,sys; d=json.load(sys.stdin); print('tag:',d.get('tag_name')); [print(a['name']) for a in d.get('assets',[])]"
```

- Asset names are the ground truth: `*-Setup.exe`, `*.msi`, `*-Windows-*.zip`, `*.AppImage`, `*.dmg`, `*.deb`.
- `(no release)` or "Mac-only" assets but a configured `win` target → **buildable from source on Windows**, not downloadable yet.

## 6. Skim `install.sh` — it is usually macOS-only

These repos ship a bash installer that curl-DMGs + `open` + `hdiutil` + `xattr -cr`. That is
Apple-specific; on Windows do NOT run install.sh — either download the `.exe` (if published)
or build from source. A Gatekeeper "damaged" note (`xattr -cr`) is a macOS-only concern.

## 7. Check for a sibling MCP server — the cross-platform shortcut

Files named `mcp/<name>-mcp.mjs` that self-describe as "zero-dependency Node ≥ 18 stdio
bridge" are **cross-platform by design**. When no Windows GUI binary exists (or building is
heavy), the MCP server still gives the full functional workflow headlessly. Wire it as stdio:

```json
{ "command": "node", "args": ["<abs-path>/mcp/<name>-mcp.mjs"], "env": { "<PROJECT_VAR>": "/abs/project.json" } }
```

## 8. Report honestly

Give a per-tool verdict table (Framework / Windows status / fastest path), separate
"downloadable today" from "buildable", and always note the headless-MCP fallback. State
"no installs/pulls done, per your instruction" explicitly if the user asked for review only.
