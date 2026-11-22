---
name: "skill-and-mcp-manifest-vetting"
description: "Vet third-party agent components — skills, MCP servers, plugins — at install time: manifest, permissions, external calls and referenced assets, before any agent loads them."
license: "MIT"
---
# Skill and MCP Manifest Vetting

## Use when
- A third-party skill, prompt-pack, MCP server or agent plugin is about to
  be installed.
- A component arrives from a marketplace or registry.
- A fleet needs an install-time trust gate.

## Instructions

1. Vet the WHOLE component, not its description: the manifest, every
   instruction file, referenced assets and scripts, declared tools and their
   scopes, network endpoints, and credential access. Published audits have
   found double-digit percentages of marketplace skills carrying at least
   one security flaw — treat "marketplace listing" as zero evidence.
2. Inventory the capability surface: which tools the component can invoke,
   which paths it reads/writes, whether it can reach the network or
   credentials, and whether its instructions can steer the host agent's
   behaviour beyond its stated job.
3. MCP servers get an extra layer: tool schemas declare inputs and outputs
   but not capability requirements — a server that claims to "search files"
   may also execute shell commands. Diff the advertised purpose against the
   actual capability list, and flag every undeclared capability.
4. Check provenance at the source: repo ownership, release history,
   maintainer identity, license, and whether the shipped artifact matches
   the published source. Unmaintained or renamed-owner components get a
   maintenance-risk flag, not a pass.
5. Score the component's risk tier by what it CAN do, not what it claims to
   do: read-only helper (light gate) up to shell/network/credential access
   (full gate plus owner sign-off).
6. Record the verdict: vetted version, evidence examined, risk tier, and
   the revocation triggers.

## Stop conditions
- Never install an unvetted component into a working agent profile.
- Never trust the marketplace listing or install count as vetting.
- Never accept undeclared capabilities silently.

## Escalation
- Components requiring credential, network or shell scope escalate to the
  owner with the vetting report — the owner signs, the gate records.
