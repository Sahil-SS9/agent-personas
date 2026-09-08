# Getting started

## Pick a building block

Use `skill:<name>` for one method, `bundle:<name>` for its coordinated members, or `persona:<name>` for the same skills plus an explicit role contract. Names are listed in [the catalogue](../CATALOGUE.md).

Run these commands from the repository root:

```bash
python3 scripts/verify.py
python3 scripts/try_profile.py --select persona:travel-expert --harness claude --dest ../travel-trial
```

The destination must not already exist. The helper verifies the source catalogue first, copies only the selected skills, writes `staging.json`, and includes `PERSONA.md` for a persona. It never edits an existing live profile or overwrites a destination.

The stage command tests file placement and membership, not native activation. Launch your chosen agent in that directory and explicitly ask it to read the role contract and use its installed members. Check its actual skill list or loader trace. Do not accept the agent saying “loaded” as proof.

## Try a task

- [Travel role](../examples/travel-expert.txt): requirements, uncertainty and booking boundaries.
- [Claim verification](../examples/claim-verification.txt): misleading numerical claim with missing evidence.
- [Review criteria](../examples/REVIEW.md): what to inspect and what a smoke run cannot establish.

You can use any self-contained prompt file. Keep customer records, secrets and production credentials out of trial workspaces.

## Optional non-interactive agent CLI

This uses your installed CLI, not a direct model API. The command is a JSON array of literal arguments; `{prompt}` is substituted without a shell. Configure authentication in your CLI first.

Example for the inspected Claude Code 2.1.201 interface:

```bash
python3 scripts/try_profile.py \
  --select skill:claim-verification --harness claude \
  --dest ../claim-trial \
  --prompt-file examples/claim-verification.txt \
  --command-json '["claude","-p","{prompt}","--tools","Read,Skill","--allowedTools","Read,Skill","--permission-mode","dontAsk","--no-session-persistence","--setting-sources","project","--settings","{\"disableAllHooks\":true}","--strict-mcp-config","--mcp-config","{\"mcpServers\":{}}","--model","sonnet","--max-budget-usd","0.30","--output-format","stream-json","--verbose"]' \
  --allow-execution --acknowledge-unsandboxed --timeout 120
```

Without `--allow-execution`, a supplied command is not executed. Both execution flags are required by the CLI. The tool allows at most 600 seconds and bounds captured output. No tools, runtimes or dependencies are installed automatically.

**Read before running:**

- Separate working directories are not a security sandbox. The CLI may still access its normal account, filesystem and network. Use the CLI’s own restrictions; never add permission-bypass flags merely to get a passing run.
- Authentication is normally supplied by your CLI’s existing account. Ambient API-key environment variables are deliberately not forwarded by default. Environment-only authentication needs an explicit supported authentication setup in that CLI; do not put secret values in command arguments or committed files.
- The helper runs no hidden `--version` or secondary commands. Record `your-agent --version` separately and retain the command/model identity alongside results.
- Raw CLI output may contain private data despite basic token redaction. Inspect it before sharing. Reports are printed to stdout, not silently uploaded.
- A successful process exit means `process-completed`, not good behaviour. `native_loading` remains `unverified` and `behaviour` remains `unreviewed` until checked against actual evidence.
- POSIX timeout cleanup terminates the owned process group. On Windows the direct child is terminated; descendant-process containment is not guaranteed. Windows execution has not been exercised for this release.

For other harnesses, use a documented non-interactive argv array for your installed version. There is intentionally no guessed universal CLI command. [Compatibility and primary documentation](compatibility.md).

## Hermes trial

The staging helper creates `hermes-home/skills/` rather than touching the default profile. Use the staged directory as an isolated `HERMES_HOME` when invoking Hermes. Configure authentication and any model settings intentionally in that isolated home; the helper does not copy credentials or live configuration. Native loader checks can run without model inference.

## Adopt into a real profile

1. Finish the trial and review the exact instructions and required tools.
2. Back up the target profile configuration.
3. Install only the selected member skill directories at the documented loader root for that profile.
4. Explicitly include the persona contract through your host’s supported profile/system-instruction mechanism. Do not assume `PERSONA.md` is auto-loaded by every client.
5. Verify discovery, member availability, role boundaries and one representative task.

A bot profile additionally needs its host’s channel/account configuration. A sub-agent profile additionally needs its host’s dispatch policy. Neither is provisioned by this catalogue.

## Update and remove

Keep the source release and customised copies separate. Compare changed files before updating; never overwrite local edits automatically. The catalogue hashes bind the release snapshot, so editing a file intentionally makes its integrity check fail until the publisher issues a new snapshot. That is expected, not an instruction to bypass verification.

The trial helper writes only a new directory and makes no registration changes. Close processes you launched before removing that trial directory. For live installations, remove only the files recorded for that installation and detach its persona instructions; follow your harness’s uninstall mechanism where applicable. Never delete shared members still used by other profiles.
