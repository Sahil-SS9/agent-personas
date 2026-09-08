---
name: "agent-dispatch-discipline"
description: "Brief, dispatch and verify agent work so nothing depends on session memory."
license: "MIT"
---
# Agent Dispatch Discipline

## Use when
- Delegating work to coding/content/research agents or subagents
- Output came back wrong and re-prompting feels like gambling
- Multiple parallel workstreams need coordination

## Instructions

1. Every dispatch brief contains five things: goal (outcome, not task list),
   constraints (what NOT to touch), definition-of-done (verifiable), pointers
   (files/URLs/data locations), and return format. Missing any one predicts
   rework.
2. Match verification depth to task risk: low-risk output gets spot-checks;
   anything merging to main or publishing externally gets evidence checked
   against the brief before acceptance.
3. Cap your own WIP: each additional parallel workstream degrades all of
   them (cognitive-load rule from Team Topologies). Queue instead of
   switching.
4. In user-facing chains, one agent responds; subagents return findings
   to the parent (single-response principle) — never let sub-agents talk
   past the lead to the user.
   For repeatable dispatches, keep a golden-output sample: characterise
   what 'good' looked like last time so drift is provable, not vibes.
5. Treat repeated agent failures as SYSTEM failures: fix the brief template,
   tooling or scoping — blameless-postmortem style, not re-prompt roulette.

## Stop conditions
- Never accept agent output you have not verified against the brief's
  definition-of-done.
- Never dispatch with "you know where to find stuff" instead of pointers.

## Escalation
- Systemic agent failures across tasks escalate to the platform owner with
  three repro examples attached.
