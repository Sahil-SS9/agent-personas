# Wiring a local ComfyUI to an agent via Comfy MCP (official `comfy-mcp`)

Goal: let an agent (Hermes) drive the ComfyUI you provisioned locally — run workflows,
generate images/video/audio/3D, and inspect the live node/model catalog — by exposing the
ComfyUI's own node/model/LoRA lists through MCP. Two-package stack:

- `comfy-cli` (≥1.14) — the **engine** every comfy-mcp tool wraps. Required even though you
  already have a working portable install; the MCP server communicates with ComfyUI through it.
- `comfy-mcp` (PyPI: `comfy-mcp`) — the first-party local MCP server. `comfy-mcp` is the command
  an MCP client launches; it speaks MCP over **stdio**. It does NOT auto-launch ComfyUI (it has a
  `launch_comfyui` tool, but expects a server already running for execution).

Docs: https://docs.comfy.org/agent-tools/mcp (Local Comfy MCP Connection section).

## Architecture — and how to make it survive an agent/IDE update

The one design rule that matters: **never install `comfy-cli`/`comfy-mcp` into the agent's own
venv** (e.g. Hermes's `.../hermes-agent/venv/`). Agent updates can recreate that venv and wipe
any pip-installed MCP server. Instead:

```
Agent venv:        .../hermes-agent/venv/        ← leave UNTOUCHED (updates are safe)
Dedicated venv:    ~/hermes-mcp/comfy-mcp-env/   ← comfy-cli + comfy-mcp live here
Agent MCP config:  mcp_servers.comfy-mcp → absolute .exe path + COMFY_BIN env   ← pointer only
```

This mirrors the pattern the `mnemosyne` MCP server already uses (its `.exe` lives outside the
agent venv and is referenced by absolute path). When the agent updates, only its own venv is
touched; the dedicated venv and the config pointer survive. The only thing that breaks the too-common
install-into-agent-venv approach is a fresh agent install; this layout avoids it entirely.

## Setup steps (Windows, proven)

1. Create a dedicated venv **using a native Windows path for uv** (see the uv pitfall below —
   a POSIX path silently mangles):
   ```
   uv venv "C:/Users/<user>/hermes-mcp/comfy-mcp-env" --python 3.11
   uv pip install --python "C:/Users/<user>/hermes-mcp/comfy-mcp-env/Scripts/python.exe" \
       "comfy-cli>=1.14.0" comfy-mcp
   ```
   Produces `comfy.exe`, `comfy-cli.exe`, `comfycli.exe`, `comfy-mcp.exe` under `Scripts\`.

2. Point comfy-cli at the portable install. comfy-cli's `set-default` REJECTS the outer portable
   wrapper (`.../ComfyUI_windows_portable`) with `not_in_workspace` — the workspace root is the
   **inner** `ComfyUI` folder (the one containing `main.py`):
   ```
   <venv>/Scripts/comfy.exe --skip-prompt set-default "C:/Users/<user>/ComfyUI/ComfyUI_windows_portable/ComfyUI"
   ```
   Verify with `comfy --workspace <inner> model list` (shows the user's real checkpoints).

3. Make sure ComfyUI is running (`curl http://127.0.0.1:8188/system_stats`). The MCP server
   expects a live server for execution tools.

4. Register the server in the agent's MCP config. Use **absolute paths** for both the command and
   `COMFY_BIN` (MCP clients launch stdio servers with a filtered environment whose `PATH` often
   does not include the dedicated venv, so `COMFY_BIN` is what makes `comfy` resolvable):
   ```yaml
   mcp_servers:
     comfy-mcp:
       command: C:/Users/<user>/hermes-mcp/comfy-mcp-env/Scripts/comfy-mcp.exe
       enabled: true
       env:
         COMFY_BIN: C:/Users/<user>/hermes-mcp/comfy-mcp-env/Scripts/comfy.exe
   ```

5. Verify: `hermes mcp list` shows `comfy-mcp ✓ enabled`; `hermes mcp test comfy-mcp` reports
   tools discovered.; call the `mcp__comfy_mcp__server_info` tool (≈ `comfy env`) and confirm it
   returns the live `running`, `workspace`, `gpu`, and the full custom-node pack list.

## Hermes-specific registration quirks

- `hermes mcp add <name> --command <cmd> --env KEY=VALUE` **connects and reports success but can
  silently fail to persist the config entry** (observed on v0.20.0; `hermes mcp list` / config.yaml
  stay unchanged). Workaround: write the entry directly with
  `hermes config set mcp_servers.<name>.<key> <value>` for each of `command`, `enabled`, and
  `env.COMFY_BIN`. That writes correctly to the per-profile `config.yaml`.
- Hermes will refuse an agent tool trying to `patch` its own `config.yaml` ("cannot modify
  security-sensitive configuration") — always use `hermes config` for this.

## Tool surface (once connected)

The official server exposes ~39 tools, including `server_info` (env/compat/freshness),
`generate_image` (fast on-ramp), `run_workflow`, `run_template`, `job` (inspect/cancel),
`list_partner_models` + `partner_generate` (cloud partner models), `search_models`/`search_templates`/
`nodes`, `launch_comfyui`/`stop_comfyui`, `fetch_outputs`. Tool names appear with an
`mcp__comfy_mcp__` prefix in Hermes.

## Pitfalls

- **uv on Windows mangles POSIX paths**: `uv venv ~/hermes-mcp/...` (or `/c/...`) can create the
  env at a bogus `C:\c\Users\...` path. Always pass **native Windows paths** (`C:/Users/...`) to uv.
  If a venv goes missing after creation, check for a stray `C:\c\` directory and remove it.
- **`comfy set-default` rejects the portable wrapper dir** — the workspace root is the inner
  `ComfyUI` folder that holds `main.py`.
- **ComfyUI must already be running** for execution tools; the server does not auto-launch it.
- `server_info` `freshness` reports `core.outdated` when ComfyUI core trails the latest — an
  advisory to offer updating, not a setup error.
- This is the **Local** MCP connection — it drives your own machine's install (sees your models,
  LoRAs, custom nodes, runs on your GPU). A separate Comfy Cloud connection exists but is a
  different server/endpoint; don't confuse the two.
