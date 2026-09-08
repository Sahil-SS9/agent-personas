# Agent Personas

## Give your agents a job, not another giant prompt.

Build dedicated agents, sub-agents and bots from **117 reusable skills, 23 personas and 24 bundles**. Start with a role, add the methods it needs, and keep the agent harness you already use.

[Browse the catalogue](CATALOGUE.md) · [Choose your harness](docs/compatibility.md) · [Try a profile](docs/getting-started.md) · [Inspect the evidence](docs/evidence.md)

## Why use this?

A research agent needs more than “be a researcher”. It needs a way to verify sources, handle uncertainty and turn findings into a usable answer. A delivery agent needs scope, handoff rules and a clear definition of done.

This catalogue packages those working instructions so you do not have to recreate them for every profile.

- **Start with a role, not a blank prompt.** Choose a mission, working style and explicit boundaries.
- **Compose instead of duplicate.** Reuse focused methods across several agents rather than maintaining giant prompts for each one.
- **Make handoffs clear.** Define what each agent owns, what it passes on and when it asks for approval.
- **Keep control.** The instructions are ordinary files. Your harness controls tools, permissions, memory and model choice.
- **Check before you adopt.** Read the instructions, inspect available evidence and try a task in your own environment.

## Choose the right building block

| Building block | What it gives you | Example |
|---|---|---|
| Skill | One focused working method | Verify a claim; design a practice loop; review a backend contract |
| Bundle | Complementary skills selected together | A travel research, itinerary, quote and logistics toolkit |
| Persona | A mission, voice, decision rules and coordinated skills | A research partner, product owner, design partner or travel expert |

A persona is a working contract, not a costume. A **profile** is the host-specific setup that gives that contract a model, tools, memory and permissions. Use it for a dedicated main agent, a scoped sub-agent or a bot connected through your existing platform. This repository does not create accounts, provision bots or grant tool access.

## What can you build?

| You need… | Start here |
|---|---|
| Findings you can trace to sources | [Grounded Researcher](personas/grounded-researcher/PERSONA.md) |
| A partner who challenges design assumptions | [Design Partner](personas/design-partner/PERSONA.md) |
| A growth experiment worth running | [Growth Experimentation Strategist](personas/growth-experimentation-strategist/PERSONA.md) |
| Practice with feedback, not just explanations | [Practice-Based Learning](personas/practice-based-learning/PERSONA.md) |
| A trip with clear constraints and booking boundaries | [Travel Expert](personas/travel-expert/PERSONA.md) |
| A bounded engineering quality workflow | [QA Test Evidence Architect](personas/qa-test-evidence-architect/PERSONA.md) |
| Implement a bounded change with real verification | [Software Implementation Specialist](personas/software-implementation-specialist/PERSONA.md) |
| Simplify code while preserving observable behaviour | [Codebase Refactoring Specialist](personas/codebase-refactoring-specialist/PERSONA.md) |
| Review plausible failures without manufacturing findings | [Adversarial Code Reviewer](personas/adversarial-code-reviewer/PERSONA.md) |

[See every persona, skill and bundle →](CATALOGUE.md)

## Try it without changing your live setup

Requires Python 3.10+ for the optional helper scripts. Reading and using the Markdown packages does not require Python.

From this repository:

```bash
# Free local integrity checks: no model or credentials needed.
python3 scripts/verify.py

# Stage one complete role in a NEW workspace. No live profiles are changed.
python3 scripts/try_profile.py \
  --select persona:travel-expert \
  --harness claude \
  --dest ../travel-agent-trial
```

Choose `codex`, `claude`, `hermes`, `openclaw`, `commandcode`, `pi` or `opencode`. Use `skill:claim-verification` for a single skill, or `bundle:travel-expert` for the member skills without a role contract.

Open your agent in the staged workspace. Ask it to read `PERSONA.md`, load the relevant installed skills, and work on a concrete task. Try the supplied [travel task](examples/travel-expert.txt). A role is not fully active until its instructions and required members are available.

For repeatable CLI smoke runs, see the [tested script workflow](docs/getting-started.md). Model execution is opt-in and may incur charges. The staging directory is not a security sandbox; use your CLI’s permissions and sandbox settings.

## Bring your own harness

The core uses portable `SKILL.md` packages and ordinary role documents. It does not depend on one vendor’s tools, memory system or delegation API.

Installation routes are documented for **Codex, Claude Code, Hermes, OpenClaw, Command Code, Pi and OpenCode**. The [compatibility matrix](docs/compatibility.md) distinguishes documented routes, tested filesystem staging, native discovery and actual agent execution. Bundle manifests are our composition format—not a claim that every client natively understands them.

## Evidence, not mystery

Each skill has an [evidence card](evidence/) with its public content identity, adaptation status and available historical comparisons. Public smoke examples are inspectable so you can try them yourself.

This is an **experimental release**, not a promise that every package improves every model. Private-source results are labelled separately from checks on the portable release. Some comparisons were inconclusive or exposed regressions; those are not hidden behind a “tests passed” badge. [Read what the evidence does—and does not—show.](docs/evidence.md)

The private builder, internal benchmarking suite, hidden test cases and raw private transcripts are **not included**. The two consumer scripts stand alone.

## Adapt and contribute

Install one delivery format to avoid duplicate skills. Start with a narrow role, try it on real work and adapt its instructions to your needs. Keep your edits under version control; compare updates rather than overwriting a customised profile.

[Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [Changes](CHANGELOG.md)

## Licence and acknowledgements

Original content and consumer code are MIT licensed. Attribution and applicable third-party notices are preserved in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).

The browsable structure takes inspiration from [magnus919/agent-skills](https://github.com/magnus919/agent-skills); the quick start and composable, benefit-led presentation draw on [mattpocock/skills](https://github.com/mattpocock/skills). Neither project endorses this catalogue.
