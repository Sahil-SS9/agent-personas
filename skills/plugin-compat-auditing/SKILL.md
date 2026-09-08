---
name: "plugin-compat-auditing"
description: "Audit plugin/tool surfaces for compat, permission and lifecycle safety across harnesses."
license: "MIT"
---
# Plugin Compat Auditing

## Use when
- Adding a plugin/tool to an agent platform or fleet
- Plugins break after platform or dependency upgrades
- Reviewing whether a tool surface is safe to expose

## Instructions

1. Inventory first: what plugins/tools exist, who owns them, which platform
   versions they were verified against. Unowned plugins get owners or get
   removed.
2. Permission audit per plugin: what it can reach (data, network, secrets,
   spend), whether that is least-privilege for its job, and what blast
   radius misuse implies.
3. Lifecycle checks: install/update/remove paths work cleanly; orphaned
   config and credentials cleaned on removal; version pinning strategy
   explicit.
4. Compat matrix maintained per platform release: verified / works-with-
   caveats / broken — published where the team actually looks.
5. Deprecation discipline: flag plugins pinned to old APIs early; schedule
   migration before forced breakage, not after.

## Stop conditions
- Never approve a plugin with unexplained broad permissions.
- Never leave a broken plugin enabled 'temporarily' without a dated plan.

## Escalation
- Security-relevant permission findings go to the security owner with the
  audit evidence, regardless of plugin popularity.
