![Choose your agent: six illustrated specialist personas with different perspectives and a shared goal](assets/agentpersonas.jpeg)

# Agent Personas

### Connect your agents to the skills their job needs.

A catalogue of **23 personas, 24 specialised skill bundles and 117 reusable skills** for building dedicated agents, sub-agents and bots. Choose a role, load its methods, and use the agent platform you already have.

[Choose a persona](#choose-your-first-persona) · [Try it](#try-a-persona-in-a-few-minutes) · [Browse everything](CATALOGUE.md) · [Platform compatibility](docs/compatibility.md) · [Evidence](docs/evidence.md)

## The connection between agents and skills

An agent gives you a model, tools and somewhere to run work. A skill gives it a method for a particular task. Putting a folder of skills beside an agent still leaves you to decide what its job is, which methods belong together, when to use them and what a finished result should contain.

Agent Personas packages that connection. Each persona defines a role and working expectations, then connects it to a specialised bundle of reusable skills. You can give an agent a research job with source-verification methods, or an implementation job with testing and review methods, without assembling the instructions from scratch each time.

```text
Your agent platform
  │  provides the model, tools, memory and permissions
  ▼
Persona
  │  defines the job, decisions, boundaries and completion criteria
  ▼
Specialised skill bundle
  │  selects the complementary methods the role needs
  ▼
Focused skills
     guide individual tasks and checks
```

The persona provides direction; its skills provide procedures. Your platform remains in charge of execution and permissions.

## What that looks like in practice

Take the [Software Implementation Specialist](personas/software-implementation-specialist/PERSONA.md). Its job is to deliver bounded features and fixes with verification. Its bundle connects that job to:

| Method | What it contributes |
|---|---|
| Implementation delivery | Trace the execution path, define the change and exercise the delivery boundary |
| Test-driven development | Establish a failing behaviour check before implementing the change |
| Systematic debugging | Investigate causes rather than cycle through speculative fixes |
| Backend contract design | Preserve the boundaries that callers and integrations depend on |
| Simplification | Review working changes for avoidable complexity |
| Adversarial review | Investigate plausible defects and support findings with evidence |

A refactoring persona has a different emphasis: establish compatibility tests before restructuring, preserve observable behaviour and measure simplification without deleting functionality to hit a target. A research persona instead coordinates source checking, synthesis and citations.

These are written working methods. They give you a starting point to inspect and adapt, rather than a promise that a model will follow every instruction.

## Choose your first persona

Start with the outcome you need. The coding roles sit alongside research, design, product and everyday-use roles in the same catalogue.

| You want to… | Start with |
|---|---|
| Build a feature or fix a bug | [Software Implementation Specialist](personas/software-implementation-specialist/PERSONA.md) |
| Simplify a module or codebase | [Codebase Refactoring Specialist](personas/codebase-refactoring-specialist/PERSONA.md) |
| Review a change for reproducible defects | [Adversarial Code Reviewer](personas/adversarial-code-reviewer/PERSONA.md) |
| Research a topic with traceable sources | [Grounded Researcher](personas/grounded-researcher/PERSONA.md) |
| Challenge and refine a design | [Design Partner](personas/design-partner/PERSONA.md) |
| Decide what to build and why | [Product Manager](personas/product-manager/PERSONA.md) |
| Connect systems and verify their boundaries | [Integration Specialist](personas/integration-specialist/PERSONA.md) |
| Coordinate an agent team | [Agent Team Lead](personas/agent-team-lead/PERSONA.md) |
| Learn through practice and feedback | [Practice-Based Learning](personas/practice-based-learning/PERSONA.md) |
| Plan a trip around practical constraints | [Travel Expert](personas/travel-expert/PERSONA.md) |

[Browse all personas, bundles and skills →](CATALOGUE.md)

## Try a persona in a few minutes

You need Git and Python 3.10+ for the optional staging helper. Reading and using the instruction files does not require Python.

### 1. Get the catalogue and verify it

```bash
git clone https://github.com/Sahil-SS9/agent-personas.git
cd agent-personas
python3 scripts/verify.py
```

The verifier checks package structure, file integrity, membership and local references. It does not contact a model or require credentials.

### 2. Stage one role in a new workspace

```bash
python3 scripts/try_profile.py \
  --select persona:software-implementation-specialist \
  --harness codex \
  --dest ../implementation-agent-trial
```

Replace `codex` with `claude`, `hermes`, `openclaw`, `commandcode`, `pi` or `opencode` as appropriate. The helper copies the persona and its member skills into a new directory. It refuses to overwrite an existing destination and does not change your live profiles.

### 3. Give your agent a concrete job

Open your agent in the staged workspace, explicitly load `PERSONA.md` and its relevant member skills, then give it a bounded task. For example, in a disposable copy of your project:

> Read PERSONA.md and load the relevant member skills. Investigate this failing test, implement a scoped fix and report the checks you ran. Do not merge or deploy.

Staging files does not itself load them into a model. It is also not a security sandbox: use your platform's permission controls. The [getting-started guide](docs/getting-started.md) covers activation and optional CLI smoke runs in more detail.

## Use the pieces your setup needs

| Building block | Choose it when… | Selection |
|---|---|---|
| Persona | You want a dedicated role with its working contract and member skills | `persona:grounded-researcher` |
| Bundle | Your agent already has a role, but needs a coordinated set of methods | `bundle:software-implementation-specialist` |
| Skill | You only need one procedure | `skill:claim-verification` |

You can adapt a persona for a main agent, a scoped sub-agent or a bot. Configure the account, model, tools, memory and channels through your chosen platform. This repository does not provision those resources or grant permission to publish, deploy or access production systems.

Keep shared methods in skills rather than copying them into every persona. That lets you reuse a method across roles and review changes without maintaining several competing copies. Install one version per intended scope to avoid discovery collisions.

## Bring your own agent platform

The instruction cores are portable Markdown. Installation guidance is separate, so the roles do not require one vendor's runtime or delegation API.

| Documented targets | What to check |
|---|---|
| Codex, Claude Code, Hermes | Discovery location, explicit persona loading and your permission settings |
| OpenClaw, Command Code, Pi, OpenCode | The same checks against your installed client version |

The [compatibility matrix](docs/compatibility.md) distinguishes documented installation routes, filesystem staging, native discovery and agent execution. A passing staging test is not a claim that every role has been run successfully in every client. The JSON persona and bundle manifests describe this catalogue's composition; they are not universal native-agent schemas.

## Methods you can inspect, evidence you can check

The catalogue includes source attribution, method references and [per-skill evidence cards](evidence/). Coding methods draw on selected material about legacy-code seams, preparatory refactoring, API compatibility, testing and review. The [coding evidence notes](docs/coding-specialists.md) explain what the comparisons covered and where the limits remain.

We test package integrity separately from agent behaviour. Some behavioural comparisons showed useful changes in the order and depth of checks; others had equal outcomes or exposed regressions. Release status does not turn those observations into universal accuracy or speed claims. The [evidence guide](docs/evidence.md) keeps those distinctions visible.

The private builder, raw research and hidden evaluation suite are not distributed. The consumer verification and staging scripts run independently of that tooling.

## Adapt it, then share what you find

Pick a role you have work for, try it on a bounded task and adjust it to your workflow. Reports showing a missed check, an unclear trigger or a redundant method are especially useful. Include the persona, platform, task and observed behaviour so others can reproduce the issue.

[Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [Release history](CHANGELOG.md)

## Licence and acknowledgements

Original content and consumer code are MIT licensed. Attribution and applicable third-party terms are recorded in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md) and package notices.

The browsable catalogue structure takes inspiration from [magnus919/agent-skills](https://github.com/magnus919/agent-skills); the quick start and composable presentation draw on [mattpocock/skills](https://github.com/mattpocock/skills). Neither project endorses this catalogue.
