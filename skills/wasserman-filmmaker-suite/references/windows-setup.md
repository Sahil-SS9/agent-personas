# Wasserman Suite — Windows Setup Detail (session-verified 2026-08-13)

Concrete commands and outputs from the actual install. Prereqs already on the
machine: Node v22, npm 10, git 2.54, Python 3.11, ffmpeg 8.1.

## 1. Prebuilt apps (ScriptBreak, Cork Board)

```bash
cd ~/Downloads
curl -fL -o ScriptBreak-setup.exe "https://github.com/wassermanproductions/scriptbreak/releases/latest/download/ScriptBreak_1.0.0_x64-setup.exe"
curl -fL -o CorkBoard-Setup.exe  "https://github.com/wassermanproductions/cork-board/releases/latest/download/CorkBoard-Setup.exe"
./ScriptBreak-setup.exe //S        # silent NSIS (double slash in git-bash)
./CorkBoard-Setup.exe //S
```

Default targets: ScriptBreak → `C:\Users\Hermes\ScriptBreak\` (Tauri per-user);
Cork Board → `%LOCALAPPDATA%\Programs\cork-board\`. Both drop desktop shortcuts.

## 2. Moving an installed Electron app (Cork Board precedent)

```bash
# 1) kill the auto-launched app (spaced names break //FI filters — use grep)
tasklist | grep -i cork
taskkill //IM "Cork Board.exe" //F   # may need plain: taskkill /F /PID <pid>
# 2) move
mv "C:/Users/Hermes/AppData/Local/Programs/cork-board" "C:/Users/Hermes/CorkBoard"
# 3) repoint the desktop shortcut via PowerShell COM
powershell.exe -NoProfile -Command "$ws = New-Object -ComObject WScript.Shell; $sc = $ws.CreateShortcut('C:\Users\Hermes\Desktop\Cork Board.lnk'); $sc.TargetPath = 'C:\Users\Hermes\CorkBoard\Cork Board.exe'; $sc.WorkingDirectory = 'C:\Users\Hermes\CorkBoard'; $sc.Save()"
```

Gotcha: `mv` on a running app's folder = "Device or resource busy". Kill first.

## 3. Blockout source build → installer

```bash
cd ~/Projects && git clone --depth 1 https://github.com/wassermanproductions/blockout.git
cd blockout
npm install                 # 608 pkgs, ~10s, deprecation warnings are noise
npm run package:win         # prepare:ffmpeg:win + verify + vite build + electron-builder
# produces release\Blockout-<ver>-win-x64.exe  (~170MB NSIS)
./release/Blockout-*-win-x64.exe //S //D=C:\\Users\\Hermes\\Blockout   # //D LAST, unquoted
```

Build log ends with `building block map` — that IS success. Installer auto-launches
the app; first run sits at the New Project dialog (control.json not written until a
project is open — MCP bridge is dormant until then).

## 4. MCP wiring (creative profile config.yaml)

Direct YAML edit via Python (CLI `config set` mangles lists — see
`hermes-config-editing` skill):

```python
import yaml
path = r'C:\Users\Hermes\AppData\Local\hermes\profiles\creative\config.yaml'
data = yaml.safe_load(open(path, encoding='utf-8'))
data.setdefault('mcp_servers', {}).update({
  'cork-board':    {'command':'node','args':['C:/Users/Hermes/Projects/cork-board/mcp/cork-board-mcp.mjs'],'enabled':True},
  'scriptbreak':   {'command':'node','args':['C:/Users/Hermes/Projects/scriptbreak/mcp/scriptbreak-mcp.mjs'],'enabled':True},
  'master-canvas': {'command':'node','args':['C:/Users/Hermes/Projects/master-canvas/mcp/master-canvas-mcp.mjs'],'enabled':True},
  'blockout':      {'command':'node','args':['C:/Users/Hermes/Projects/blockout/mcp/blockout-mcp.mjs'],'enabled':True},
})
yaml.dump(data, open(path,'w',encoding='utf-8'), default_flow_style=False, allow_unicode=True, sort_keys=False)
```

## 5. MCP stdio smoke test (works for any stdio MCP server)

```bash
printf '%s\n' \
 '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"t","version":"0.1"}}}' \
 '{"jsonrpc":"2.0","method":"notifications/initialized"}' \
 '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}' \
 | timeout 15 node <server>.mjs
```

Expected tool counts (2026-08): cork-board 25, scriptbreak 11, master-canvas 14,
blockout 34. A real functional probe: cork-board `apply_preset` with
`{"presetId":"demo-ava"}` then `get_board` → 36 cards / 4 acts / 6 cast.
