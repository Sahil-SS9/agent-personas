# ACE-Step Directory Anatomy

**Path:** `~/Suno/ACE-Step-1.5/`

Complete breakdown of every file and directory in the ACE-Step 1.5 installation.

---

## `.bat` Files — Day-to-Day Use

| File | Purpose |
|------|---------|
| **`start_api_server.bat`** | 🟢 Start the REST API on port 8001. Double-click to launch. |
| **`close_api_server.bat`** | 🔴 Kill whatever's holding port 8001 (zombie or live). Double-click. |
| **`start_gradio_ui.bat`** | Launch Gradio web UI instead of the API (visual interface). |
| **`start_gradio_ui_manual.bat`** | Gradio UI with full manual controls (advanced settings). |
| **`check_update.bat`** | Check for ACE-Step git updates. Run occasionally. |
| **`merge_config.bat`** | Merge upstream config changes with your `.env` after updates. |
| **`install_uv.bat`** | Install the `uv` package manager. Run once. Already done. |
| **`quick_test.bat`** | Smoke test after installation. |
| **`test_env_detection.bat`** | Debug GPU/environment detection. |
| **`test_git_update.bat`** | Debug update mechanics. |

> **Hardware-specific files** (skip — user runs RTX 4070 Ti / NVIDIA CUDA):
> `start_api_server_rocm.bat`, `start_api_server_xpu.bat`, `setup_xpu.bat`, `start_gradio_ui_rocm*.bat`, `start_gradio_ui_xpu*.bat`

---

## `.sh` Files — Ignore on Windows

All `.sh` files are Linux/Mac equivalents of the `.bat` files. Not usable on Windows 10.

---

## Key Directories

| Directory | Contents |
|-----------|----------|
| **`acestep/`** | 🧠 Core Python package — API server, model loading, DiT, VAE, LM, training, inference |
| **`.venv/`** | Python virtual environment (managed by `uv`, do not modify manually) |
| **`checkpoints/`** | 💾 Downloaded model weights (~6GB total: DiT sft, VAE, LM 0.6B). Cached; not re-downloaded. |
| **`gradio_outputs/`** | 🎵 Generated audio files from Gradio UI sessions |
| **`docs/`** | Documentation markdown files |
| **`examples/`** | Example generation scripts |
| **`scripts/`** | Utility/helper scripts |
| **`assets/`** | UI static assets |
| **`openrouter/`** | OpenRouter integration code |
| **`.cache/`** | HuggingFace model cache (auto-populated) |

---

## Config Files

| File | Role |
|------|------|
| **`.env`** | ⚙️ **Your active config** — model choice (sft/turbo), LM size, device, API key. Edit this. |
| **`.env.example`** | Template with all available settings + inline docs. Copy to `.env` to start fresh. |
| **`pyproject.toml`** | Python project metadata + dependency declarations |
| **`uv.lock`** | Lockfile with pinned dependency versions (auto-managed by `uv`) |
| **`requirements.txt`** | Legacy pip requirements (for reference; `uv` reads `pyproject.toml`) |
| **`proxy_config.txt.example`** | Proxy configuration template |

---

## Python Scripts

| File | Size | Purpose |
|------|------|---------|
| **`cli.py`** | 90 KB | Main CLI entry point — the `acestep-api` command lives here |
| **`profile_inference.py`** | 79 KB | Benchmark inference performance |
| **`train.py`** | 9 KB | Model fine-tuning |
| **`generate_examples.py`** | 6 KB | Batch generate example audio |

---

## Documentation

| File | Topic |
|------|-------|
| **`README.md`** | Main docs — install, usage, API reference, config |
| **`README-XPU.md`** | Intel XPU-specific instructions (skip) |
| **`AGENTS.md`** | Guidelines for AI coding agents editing the repo |
| **`CONTRIBUTING.md`** | How to contribute code upstream |
| **`SECURITY.md`** | Security policy |
| **`LICENSE`** | MIT License |

---

## Docker (not used — running locally)

- `Dockerfile` — container build for CUDA
- `Dockerfile.jetson` — container build for NVIDIA Jetson
- `docker-compose.yml` — orchestration for CUDA
- `docker-compose.jetson.yml` — orchestration for Jetson

---

## Git / CI

- `.git/` — git repository metadata
- `.gitignore` — 5.7 KB, comprehensive ignore rules
- `.githooks/` — git hooks (auto-formatting, linting)
- `.github/` — GitHub Actions workflows, issue templates
- `.claude/` — Claude Code project context
- `.editorconfig` — editor settings (indentation, charset)

---

## TL;DR — Files You Actually Touch

1. **`start_api_server.bat`** — start the server
2. **`close_api_server.bat`** — stop it / clear zombies
3. **`.env`** — configure model quality, LM size
4. **`gradio_outputs/`** — grab your generated audio
