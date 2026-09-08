# Harness compatibility

Checked 8 September 2026. This is a portable instruction catalogue, not a replacement for a harness's runtime, authentication or permissions.

| Harness | Trial skill root relative to new workspace | Evidence level |
|---|---|---|
| Codex | `.agents/skills/` | Documented discovery path; staging tested; executable unavailable here |
| Claude Code | `.claude/skills/` | Native discovery observed with 2.1.201; model run blocked by missing authentication |
| Hermes | `hermes-home/skills/` with isolated `HERMES_HOME` | Native list and full-content loading checked using local v0.21.0 fork; not an upstream-only certification |
| OpenClaw | `.agents/skills/` | Documented project path; staging tested; executable unavailable here |
| Command Code | `.commandcode/skills/` | Documented project path; staging tested; executable unavailable here |
| Pi agent | `.pi/skills/` | Documented project path; staging tested; executable unavailable here |
| OpenCode | `.opencode/skills/` | Documented project path; staging tested; executable unavailable here |

Staging tests check our path selection and copying, not the target application's loader. These seven targets are not seven verified end-to-end agent deployments. Windows and macOS execution are not certified by the Linux checks.

## Primary references

- [Codex skills](https://developers.openai.com/codex/skills): project and user discovery using `.agents/skills`.
- [Claude Code skills](https://code.claude.com/docs/en/skills): project `.claude/skills`, user `~/.claude/skills`, explicit invocation and automatic selection.
- [Hermes skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills): per-home skills. The trial home intentionally does not inherit live model credentials or configuration.
- [OpenClaw skills](https://docs.openclaw.ai/tools/skills): workspace and project/personal agent paths, precedence and agent allowlists. The latest direct extraction was security-blocked; project-path corroboration was available in indexed official-language documentation. Recheck the installed version before adoption.
- [Command Code troubleshooting](https://commandcode.ai/docs/troubleshooting/common-issues): `.commandcode/skills`, frontmatter validation and `cmd skills list --debug`. The indexed `/docs/skills` URL returned 404 during the latest direct check; this alternative official page documents discovery. The executable is normally `cmd`, not necessarily `commandcode`.
- [Pi skills documentation](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md): `.pi/skills` and user skill locations. The historical badlogic/pi-mono link redirects to this maintained location.
- [OpenCode skills](https://opencode.ai/docs/skills/): `.opencode/skills`, Claude-compatible and agent-compatible roots; name must match folder and use lowercase alphanumeric single-hyphen segments.

## Personas, sub-agents and bots

SKILL.md is the shared discovery convention. `persona.json` and `bundle.json` are this catalogue's composition metadata, not universal native agent schemas.

`PERSONA.md` is deliberately plain Markdown. Include it explicitly through the selected host's profile/system-instruction mechanism. The trial helper does not install a native agent definition or claim that arbitrary Markdown is automatically loaded.

For a sub-agent, map the role contract and member skills into that host's supported worker configuration. For a bot, also configure identity, account, channels and permissions in the bot host. Review these bindings separately; do not embed production accounts or dispatch tools in portable instructions.

## Collision and permission rules

Install one chosen version of a skill name per intended scope. Hosts may give workspace copies precedence over user or bundled copies, or hide skills through allowlists. Inspect the actual discovery report; a correct file on disk does not prove that the intended version won.

The catalogue includes focused domain methods that mention tools such as MCP, ComfyUI or arXiv because those are their subjects. That is different from requiring a particular agent harness to load the skill. Each role's dependencies and approval boundaries are declared separately.
