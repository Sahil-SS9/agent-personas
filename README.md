![Choose your agent: six illustrated specialist personas with different perspectives and a shared goal](assets/agentpersonas.jpeg)

# Agent Personas

### Connect your agents to the skills their job needs.

A catalogue of **47 personas, 48 specialised skill bundles and 292 reusable skills** for building dedicated agents, sub-agents and bots. Choose a role, load its methods, and use the agent platform you already have.

[Choose a persona](#choose-your-first-persona) · [Try it](#try-a-persona-in-a-few-minutes) · [Browse all roles and bundles](#browse-all-personas-and-skill-bundles) · [Platform compatibility](docs/compatibility.md) · [Evidence](docs/evidence.md)

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

## Browse all personas and skill bundles

The directory below covers all 47 persona role contracts and 48 skill bundles. A persona defines the job, boundaries and completion criteria; a bundle selects methods without assigning a role. Each row links to both separately. Counts are declared member skills, not unique skills across the catalogue; shared skills are counted in each package that includes them.

Paired personas and bundles currently have identical membership. Expand a group to inspect the linked skills for each entry. The standalone `knowledge-librarian-bundle` has no matching persona. Conditional members are included in counts but activate only when relevant and authorised; they grant no dispatch permission.

### Software, architecture and data

| Persona role contract | Skill bundle | Use it to… | Member skills |
|---|---|---|---:|
| [software-implementation-specialist](personas/software-implementation-specialist/PERSONA.md) | [software-implementation-specialist](bundles/software-implementation-specialist/bundle.json) | Build bounded features and fix bugs with verification. | 6 |
| [codebase-refactoring-specialist](personas/codebase-refactoring-specialist/PERSONA.md) | [codebase-refactoring-specialist](bundles/codebase-refactoring-specialist/bundle.json) | Simplify code while preserving observable contracts. | 5 |
| [adversarial-code-reviewer](personas/adversarial-code-reviewer/PERSONA.md) | [adversarial-code-reviewer](bundles/adversarial-code-reviewer/bundle.json) | Review code for reproducible correctness and security defects. | 3 |
| [systems-architect](personas/systems-architect/PERSONA.md) | [systems-architect](bundles/systems-architect/bundle.json) | Design systems from constraints and record architectural decisions. | 5 |
| [api-contract-designer](personas/api-contract-designer/PERSONA.md) | [api-contract-designer](bundles/api-contract-designer/bundle.json) | Define APIs, compatibility rules and error contracts. | 6 |
| [integration-specialist](personas/integration-specialist/PERSONA.md) | [integration-specialist](bundles/integration-specialist/bundle.json) | Connect systems and verify protocol, logic and client boundaries. | 6 |
| [data-engineer](personas/data-engineer/PERSONA.md) | [data-engineer](bundles/data-engineer/bundle.json) | Design schemas, optimise queries and build checked data pipelines. | 7 |
| [performance-engineer](personas/performance-engineer/PERSONA.md) | [performance-engineer](bundles/performance-engineer/bundle.json) | Measure web performance and control regressions. | 6 |
| [qa-test-evidence-architect](personas/qa-test-evidence-architect/PERSONA.md) | [qa-test-evidence-architect](bundles/qa-test-evidence-architect/bundle.json) | Choose test strategies and investigate flaky tests with evidence. | 10 |
| [open-source-maintainer](personas/open-source-maintainer/PERSONA.md) | [open-source-maintainer](bundles/open-source-maintainer/bundle.json) | Triage contributions and maintain repository policy. | 11 |
| [frontend-ux-engineer](personas/frontend-ux-engineer/PERSONA.md) | [frontend-ux-engineer](bundles/frontend-ux-engineer/bundle.json) | Build accessible interfaces with clear hierarchy and purposeful motion. | 8 |

<details>
<summary>Inspect member skills: software, architecture and data</summary>

#### software-implementation-specialist

[implementation-delivery](skills/implementation-delivery/SKILL.md) · [test-driven-development](skills/test-driven-development/SKILL.md) · [systematic-debugging](skills/systematic-debugging/SKILL.md) · [backend-contract-design](skills/backend-contract-design/SKILL.md) · [simplify-swarm-candidate](skills/simplify-swarm-candidate/SKILL.md) · [hermaguard-candidate](skills/hermaguard-candidate/SKILL.md)

#### codebase-refactoring-specialist

[codebase-simplification-campaign](skills/codebase-simplification-campaign/SKILL.md) · [architecture-layering-review](skills/architecture-layering-review/SKILL.md) · [test-evidence-integrity](skills/test-evidence-integrity/SKILL.md) · [simplify-swarm-candidate](skills/simplify-swarm-candidate/SKILL.md) · [hermaguard-candidate](skills/hermaguard-candidate/SKILL.md)

#### adversarial-code-reviewer

[hermaguard-candidate](skills/hermaguard-candidate/SKILL.md) · [claim-verification](skills/claim-verification/SKILL.md) · [test-evidence-integrity](skills/test-evidence-integrity/SKILL.md)

#### systems-architect

[architecture-characteristics-driven-design](skills/architecture-characteristics-driven-design/SKILL.md) · [c4-architecture-modelling](skills/c4-architecture-modelling/SKILL.md) · [decomposition-tradeoff-analysis](skills/decomposition-tradeoff-analysis/SKILL.md) · [architecture-decision-records](skills/architecture-decision-records/SKILL.md) · [evolutionary-architecture-fitness-functions](skills/evolutionary-architecture-fitness-functions/SKILL.md)

#### api-contract-designer

[resource-oriented-contract-design](skills/resource-oriented-contract-design/SKILL.md) · [api-compatibility-analysis](skills/api-compatibility-analysis/SKILL.md) · [contract-error-and-pragmatics-design](skills/contract-error-and-pragmatics-design/SKILL.md) · [api-security-design](skills/api-security-design/SKILL.md) · [event-driven-contract-design](skills/event-driven-contract-design/SKILL.md) · [openapi-spec-authoring](skills/openapi-spec-authoring/SKILL.md)

#### integration-specialist

[mcp-integration-engineering](skills/mcp-integration-engineering/SKILL.md) · [third-party-api-integration](skills/third-party-api-integration/SKILL.md) · [plugin-compat-auditing](skills/plugin-compat-auditing/SKILL.md) · [mcp-client-setup](skills/mcp-client-setup/SKILL.md) · [mcp-troubleshooting](skills/mcp-troubleshooting/SKILL.md) · [backend-contract-design](skills/backend-contract-design/SKILL.md)

#### data-engineer

[schema-design-and-evolution](skills/schema-design-and-evolution/SKILL.md) · [query-and-index-optimisation](skills/query-and-index-optimisation/SKILL.md) · [pipeline-quality-observability](skills/pipeline-quality-observability/SKILL.md) · [lakehouse-architecture-selection](skills/lakehouse-architecture-selection/SKILL.md) · [analytics-dimensional-modelling](skills/analytics-dimensional-modelling/SKILL.md) · [streaming-vs-batch-design](skills/streaming-vs-batch-design/SKILL.md) · [data-governance-privacy](skills/data-governance-privacy/SKILL.md)

#### performance-engineer

[core-web-vitals-optimisation](skills/core-web-vitals-optimisation/SKILL.md) · [asset-and-bundle-budgets](skills/asset-and-bundle-budgets/SKILL.md) · [perf-regression-monitoring](skills/perf-regression-monitoring/SKILL.md) · [runtime-rendering-performance](skills/runtime-rendering-performance/SKILL.md) · [profiling-methodology](skills/profiling-methodology/SKILL.md) · [backend-api-latency](skills/backend-api-latency/SKILL.md)

#### qa-test-evidence-architect

[test-strategy-shapes](skills/test-strategy-shapes/SKILL.md) · [flaky-test-manager](skills/flaky-test-manager/SKILL.md) · [edge-case-inventory](skills/edge-case-inventory/SKILL.md) · [failing-test-triage](skills/failing-test-triage/SKILL.md) · [three-amigos-workshop](skills/three-amigos-workshop/SKILL.md) · [regression-attribution](skills/regression-attribution/SKILL.md) · [release-quality-gates](skills/release-quality-gates/SKILL.md) · [test-driven-development](skills/test-driven-development/SKILL.md) · [systematic-debugging](skills/systematic-debugging/SKILL.md) · [test-evidence-integrity](skills/test-evidence-integrity/SKILL.md)

#### open-source-maintainer

[inbound-issue-triage-and-severity](skills/inbound-issue-triage-and-severity/SKILL.md) · [out-of-scope-and-wontfix-kb](skills/out-of-scope-and-wontfix-kb/SKILL.md) · [inbound-pr-review](skills/inbound-pr-review/SKILL.md) · [pr-disposition-and-salvage](skills/pr-disposition-and-salvage/SKILL.md) · [maintainer-communication-crafting](skills/maintainer-communication-crafting/SKILL.md) · [contribution-policy-authoring](skills/contribution-policy-authoring/SKILL.md) · [reviewer-delegation-and-codeowners](skills/reviewer-delegation-and-codeowners/SKILL.md) · [contributor-vetting-and-spam-gate](skills/contributor-vetting-and-spam-gate/SKILL.md) · [code-of-conduct-enforcement](skills/code-of-conduct-enforcement/SKILL.md) · [release-notes-and-changelog](skills/release-notes-and-changelog/SKILL.md) · [project-health-and-maintainer-load-review](skills/project-health-and-maintainer-load-review/SKILL.md)

#### frontend-ux-engineer

[visual-hierarchy-craft](skills/visual-hierarchy-craft/SKILL.md) · [ux-flow-and-heuristics](skills/ux-flow-and-heuristics/SKILL.md) · [ui-component-composition](skills/ui-component-composition/SKILL.md) · [purposeful-motion](skills/purposeful-motion/SKILL.md) · [design-teardown-review](skills/design-teardown-review/SKILL.md) · [frontend-architecture](skills/frontend-architecture/SKILL.md) · [responsive-layout-systems](skills/responsive-layout-systems/SKILL.md) · [frontend-testing](skills/frontend-testing/SKILL.md)

</details>

### Design, research and media

| Persona role contract | Skill bundle | Use it to… | Member skills |
|---|---|---|---:|
| [design-partner](personas/design-partner/PERSONA.md) | [design-partner](bundles/design-partner/bundle.json) | Challenge designs and document trade-offs and decisions. | 7 |
| [design-system-engineer](personas/design-system-engineer/PERSONA.md) | [design-system-engineer](bundles/design-system-engineer/bundle.json) | Maintain design tokens, component contracts and adoption. | 6 |
| [accessibility-engineer](personas/accessibility-engineer/PERSONA.md) | [accessibility-engineer](bundles/accessibility-engineer/bundle.json) | Audit accessibility and verify keyboard and screen-reader flows. | 6 |
| [ux-research](personas/ux-research/PERSONA.md) | [ux-research](bundles/ux-research/bundle.json) | Gather user evidence tied to product decisions. | 6 |
| [grounded-researcher](personas/grounded-researcher/PERSONA.md) | [grounded-researcher](bundles/grounded-researcher/bundle.json) | Verify claims and produce cited research with explicit uncertainty. | 6 |
| [image-generation](personas/image-generation/PERSONA.md) | [image-generation](bundles/image-generation/bundle.json) | Create consistent imagery using character references and named styles. | 7 |
| [video-generation](personas/video-generation/PERSONA.md) | [video-generation](bundles/video-generation/bundle.json) | Plan generated video, prompts, timing and model costs. | 12 |
| [growth-experimentation-strategist](personas/growth-experimentation-strategist/PERSONA.md) | [growth-experimentation-strategist](bundles/growth-experimentation-strategist/bundle.json) | Choose feasible growth experiments with measured evidence. | 7 |
| [product-demo-specialist](personas/product-demo-specialist/PERSONA.md) | [product-demo-specialist](bundles/product-demo-specialist/bundle.json) | Rehearse decision-focused demos and turn claims into testable scope. | 5 |

<details>
<summary>Inspect member skills: design, research and media</summary>

#### design-partner

[design-grilling](skills/design-grilling/SKILL.md) · [architecture-documentation](skills/architecture-documentation/SKILL.md) · [architecture-deepening-review](skills/architecture-deepening-review/SKILL.md) · [architecture-layering-review](skills/architecture-layering-review/SKILL.md) · [backend-contract-design](skills/backend-contract-design/SKILL.md) · [writing-plans](skills/writing-plans/SKILL.md) · [c4-model-reference](skills/c4-model-reference/SKILL.md)

#### design-system-engineer

[design-token-architecture](skills/design-token-architecture/SKILL.md) · [component-library-contracts](skills/component-library-contracts/SKILL.md) · [system-governance-and-adoption](skills/system-governance-and-adoption/SKILL.md) · [theming-multibrand](skills/theming-multibrand/SKILL.md) · [design-system-documentation](skills/design-system-documentation/SKILL.md) · [design-system-versioning-migration](skills/design-system-versioning-migration/SKILL.md)

#### accessibility-engineer

[wcag-conformance-audit](skills/wcag-conformance-audit/SKILL.md) · [keyboard-and-sr-testing](skills/keyboard-and-sr-testing/SKILL.md) · [inclusive-content-and-forms](skills/inclusive-content-and-forms/SKILL.md) · [aria-semantic-authoring](skills/aria-semantic-authoring/SKILL.md) · [automated-a11y-ci](skills/automated-a11y-ci/SKILL.md) · [accessible-dynamic-components](skills/accessible-dynamic-components/SKILL.md)

#### ux-research

[momtest-interviewing](skills/momtest-interviewing/SKILL.md) · [proportionate-research-design](skills/proportionate-research-design/SKILL.md) · [insight-to-action-synthesis](skills/insight-to-action-synthesis/SKILL.md) · [usability-testing-design](skills/usability-testing-design/SKILL.md) · [survey-quant-research](skills/survey-quant-research/SKILL.md) · [journey-map-persona-artefacts](skills/journey-map-persona-artefacts/SKILL.md)

#### grounded-researcher

[claim-verification](skills/claim-verification/SKILL.md) · [evidence-synthesis](skills/evidence-synthesis/SKILL.md) · [grounded-citations](skills/grounded-citations/SKILL.md) · [arxiv](skills/arxiv/SKILL.md) · [competitor-news-monitor](skills/competitor-news-monitor/SKILL.md) · [landscape-monitoring](skills/landscape-monitoring/SKILL.md)

#### image-generation

[character-sheet-design](skills/character-sheet-design/SKILL.md) · [style-vocabulary-selection](skills/style-vocabulary-selection/SKILL.md) · [interactive-style-refinement](skills/interactive-style-refinement/SKILL.md) · [concept-development-session](skills/concept-development-session/SKILL.md) · [storyboard-to-shots](skills/storyboard-to-shots/SKILL.md) · [image-generation-workflow](skills/image-generation-workflow/SKILL.md) · [comfyui](skills/comfyui/SKILL.md)

#### video-generation

[h3-prompt-crafting](skills/h3-prompt-crafting/SKILL.md) · [lyric-aligned-video-planning](skills/lyric-aligned-video-planning/SKILL.md) · [video-cost-routing](skills/video-cost-routing/SKILL.md) · [comfyui-workflow-management](skills/comfyui-workflow-management/SKILL.md) · [multi-shot-storytelling](skills/multi-shot-storytelling/SKILL.md) · [comfyui-video-generation](skills/comfyui-video-generation/SKILL.md) · [comfyui](skills/comfyui/SKILL.md) · [terminal-demo-video](skills/terminal-demo-video/SKILL.md) · [motion-notation-prompting](skills/motion-notation-prompting/SKILL.md) · [h3-audio-dialogue-syntax](skills/h3-audio-dialogue-syntax/SKILL.md) · [temporal-animation-techniques](skills/temporal-animation-techniques/SKILL.md) · [h3-style-picker](skills/h3-style-picker/SKILL.md)

#### growth-experimentation-strategist

[growth-bottleneck-diagnosis](skills/growth-bottleneck-diagnosis/SKILL.md) · [experiment-feasibility-review](skills/experiment-feasibility-review/SKILL.md) · [search-acquisition-audit](skills/search-acquisition-audit/SKILL.md) · [market-research](skills/market-research/SKILL.md) · [pricing-strategy](skills/pricing-strategy/SKILL.md) · [feature-prioritisation](skills/feature-prioritisation/SKILL.md) · [claim-verification](skills/claim-verification/SKILL.md)

#### product-demo-specialist

[demo-scenario-design](skills/demo-scenario-design/SKILL.md) · [qfs-authoring](skills/qfs-authoring/SKILL.md) · [demo-production-workflow](skills/demo-production-workflow/SKILL.md) · [safe-demo-environments](skills/safe-demo-environments/SKILL.md) · [prd-authoring](skills/prd-authoring/SKILL.md)

</details>

### Product, delivery and operations

| Persona role contract | Skill bundle | Use it to… | Member skills |
|---|---|---|---:|
| [product-manager](personas/product-manager/PERSONA.md) | [product-manager](bundles/product-manager/bundle.json) | Frame problems, define outcomes and prioritise features. | 4 |
| [product-owner](personas/product-owner/PERSONA.md) | [product-owner](bundles/product-owner/bundle.json) | Order backlogs and slice deliverable stories. | 4 |
| [project-strategist](personas/project-strategist/PERSONA.md) | [project-strategist](bundles/project-strategist/bundle.json) | Evaluate projects and choose delivery approaches. | 4 |
| [risk-release-manager](personas/risk-release-manager/PERSONA.md) | [risk-release-manager](bundles/risk-release-manager/bundle.json) | Track risks and verify releases, rollback and post-release checks. | 4 |
| [devops-sre](personas/devops-sre/PERSONA.md) | [devops-sre](bundles/devops-sre/bundle.json) | Manage SLOs, progressive delivery and incident response. | 6 |
| [automation-engineer](personas/automation-engineer/PERSONA.md) | [automation-engineer](bundles/automation-engineer/bundle.json) | Replace measured toil with observable, reversible automations. | 6 |
| [support-specialist](personas/support-specialist/PERSONA.md) | [support-specialist](bundles/support-specialist/bundle.json) | Resolve support issues and eliminate recurring causes. | 4 |
| [filesystem-hygiene-steward](personas/filesystem-hygiene-steward/PERSONA.md) | [filesystem-hygiene-steward](bundles/filesystem-hygiene-steward/bundle.json) | Identify file debris and prepare evidence-backed cleanup candidates. | 11 |
| [fleet-governance-operator](personas/fleet-governance-operator/PERSONA.md) | [fleet-governance-operator](bundles/fleet-governance-operator/bundle.json) | Inspect agent fleets and govern changes through approval gates. | 9 |
| [blue-team-security](personas/blue-team-security/PERSONA.md) | [blue-team-security](bundles/blue-team-security/bundle.json) | Plan prevention, detection and rehearsed incident response. | 6 |
| [red-team-security](personas/red-team-security/PERSONA.md) | [red-team-security](bundles/red-team-security/bundle.json) | Investigate authorised attack paths and report reproducible findings. | 6 |

<details>
<summary>Inspect member skills: product, delivery and operations</summary>

#### product-manager

[prd-authoring](skills/prd-authoring/SKILL.md) · [feature-prioritisation](skills/feature-prioritisation/SKILL.md) · [market-research](skills/market-research/SKILL.md) · [pricing-strategy](skills/pricing-strategy/SKILL.md)

#### product-owner

[story-slicing](skills/story-slicing/SKILL.md) · [backlog-refinement](skills/backlog-refinement/SKILL.md) · [meeting-action-items](skills/meeting-action-items/SKILL.md) · [morning-pulse](skills/morning-pulse/SKILL.md)

#### project-strategist

[methodology-selector](skills/methodology-selector/SKILL.md) · [change-request-evaluator](skills/change-request-evaluator/SKILL.md) · [writing-plans](skills/writing-plans/SKILL.md) · [writing-spec](skills/writing-spec/SKILL.md)

#### risk-release-manager

[risk-register-manager](skills/risk-register-manager/SKILL.md) · [release-readiness-manager](skills/release-readiness-manager/SKILL.md) · [release-quality-gates](skills/release-quality-gates/SKILL.md) · [test-evidence-integrity](skills/test-evidence-integrity/SKILL.md)

#### devops-sre

[slo-and-error-budget-operations](skills/slo-and-error-budget-operations/SKILL.md) · [progressive-delivery-and-rollback](skills/progressive-delivery-and-rollback/SKILL.md) · [production-health-ownership](skills/production-health-ownership/SKILL.md) · [infrastructure-as-code](skills/infrastructure-as-code/SKILL.md) · [cicd-pipeline-design](skills/cicd-pipeline-design/SKILL.md) · [observability-instrumentation](skills/observability-instrumentation/SKILL.md)

#### automation-engineer

[toil-elimination-sequence](skills/toil-elimination-sequence/SKILL.md) · [safe-automation-delivery](skills/safe-automation-delivery/SKILL.md) · [workflow-incident-readiness](skills/workflow-incident-readiness/SKILL.md) · [orchestration-scheduling-design](skills/orchestration-scheduling-design/SKILL.md) · [automation-secrets-handling](skills/automation-secrets-handling/SKILL.md) · [automation-cost-budgeting](skills/automation-cost-budgeting/SKILL.md)

#### support-specialist

[tiered-support-triage](skills/tiered-support-triage/SKILL.md) · [problem-elimination-loop](skills/problem-elimination-loop/SKILL.md) · [failing-test-triage](skills/failing-test-triage/SKILL.md) · [meeting-action-items](skills/meeting-action-items/SKILL.md)

#### filesystem-hygiene-steward

[filesystem-inventory-and-provenance](skills/filesystem-inventory-and-provenance/SKILL.md) · [unused-orphan-and-load-bearing-confirmation](skills/unused-orphan-and-load-bearing-confirmation/SKILL.md) · [agent-artifact-attribution-and-scratch-routing](skills/agent-artifact-attribution-and-scratch-routing/SKILL.md) · [duplicate-and-hardlink-dedup-safety](skills/duplicate-and-hardlink-dedup-safety/SKILL.md) · [safe-deletion-proposal-and-gate](skills/safe-deletion-proposal-and-gate/SKILL.md) · [quarantine-move-and-restore-safety](skills/quarantine-move-and-restore-safety/SKILL.md) · [pre-deletion-backup-and-retention-proof](skills/pre-deletion-backup-and-retention-proof/SKILL.md) · [workspace-convention-and-gitignore-hygiene](skills/workspace-convention-and-gitignore-hygiene/SKILL.md) · [build-ci-and-package-artifact-sprawl-control](skills/build-ci-and-package-artifact-sprawl-control/SKILL.md) · [cleanup-cadence-and-new-debris-monitoring](skills/cleanup-cadence-and-new-debris-monitoring/SKILL.md) · [storage-pressure-and-reclaim-forensics](skills/storage-pressure-and-reclaim-forensics/SKILL.md)

#### fleet-governance-operator

[skill-catalogue-audit](skills/skill-catalogue-audit/SKILL.md) · [audit-engine](skills/audit-engine/SKILL.md) · [agent-profile-review](skills/agent-profile-review/SKILL.md) · [scheduled-output-contract](skills/scheduled-output-contract/SKILL.md) · [scheduled-job-audit](skills/scheduled-job-audit/SKILL.md) · [agent-config-validation](skills/agent-config-validation/SKILL.md) · [agent-change-governance](skills/agent-change-governance/SKILL.md) · [evidence-synthesis](skills/evidence-synthesis/SKILL.md) · [grounded-citations](skills/grounded-citations/SKILL.md)

#### blue-team-security

[attck-control-mapping](skills/attck-control-mapping/SKILL.md) · [incident-response-lifecycle](skills/incident-response-lifecycle/SKILL.md) · [control-hygiene-basics](skills/control-hygiene-basics/SKILL.md) · [detection-engineering](skills/detection-engineering/SKILL.md) · [vulnerability-management-prioritisation](skills/vulnerability-management-prioritisation/SKILL.md) · [threat-intel-forensics](skills/threat-intel-forensics/SKILL.md)

#### red-team-security

[attack-path-modelling](skills/attack-path-modelling/SKILL.md) · [finding-verification-and-chaining](skills/finding-verification-and-chaining/SKILL.md) · [offensive-scope-discipline](skills/offensive-scope-discipline/SKILL.md) · [recon-enumeration-methodology](skills/recon-enumeration-methodology/SKILL.md) · [web-app-exploitation-technique](skills/web-app-exploitation-technique/SKILL.md) · [engagement-reporting-remediation](skills/engagement-reporting-remediation/SKILL.md)

</details>

### Agents, models and knowledge

| Persona role contract | Skill bundle | Use it to… | Member skills |
|---|---|---|---:|
| [agent-team-lead](personas/agent-team-lead/PERSONA.md) | [agent-team-lead](bundles/agent-team-lead/bundle.json) | Brief agent teams and verify their delivered outcomes. | 6 |
| [ai-guardrails-engineer](personas/ai-guardrails-engineer/PERSONA.md) | [ai-guardrails-engineer](bundles/ai-guardrails-engineer/bundle.json) | Identify, place and test guardrails against the harms they address. | 11 |
| [evidence-based-ai-delegation](personas/evidence-based-ai-delegation/PERSONA.md) | [evidence-based-ai-delegation](bundles/evidence-based-ai-delegation/bundle.json) | Choose human, assisted or delegated work from risk and measured value. | 3 (1 conditional) |
| [prompt-agent-engineer](personas/prompt-agent-engineer/PERSONA.md) | [prompt-agent-engineer](bundles/prompt-agent-engineer/bundle.json) | Design versioned prompts and bounded, observable agent loops. | 7 |
| [ml-eval-engineer](personas/ml-eval-engineer/PERSONA.md) | [ml-eval-engineer](bundles/ml-eval-engineer/bundle.json) | Design task-valid model evaluations and report their limits. | 6 |
| [provider-hunter](personas/provider-hunter/PERSONA.md) | [provider-hunter](bundles/provider-hunter/bundle.json) | Find model providers and verify their identity and terms. | 12 |
| [text-classifier-specialist](personas/text-classifier-specialist/PERSONA.md) | [text-classifier-specialist](bundles/text-classifier-specialist/bundle.json) | Evaluate, host and monitor small classifiers and decision models. | 12 |
| [knowledge-librarian](personas/knowledge-librarian/PERSONA.md) | [knowledge-librarian](bundles/knowledge-librarian/bundle.json) | Curate knowledge, memory and skills with provenance and freshness. | 9 |
| No matching persona | [knowledge-librarian-bundle](bundles/knowledge-librarian-bundle/bundle.json) | Maintain linked knowledge, memory and the shared skill library. | 9 |
| [technical-writer](personas/technical-writer/PERSONA.md) | [technical-writer](bundles/technical-writer/bundle.json) | Write audience-matched documentation and verify its claims. | 6 |
| [tool-evaluator](personas/tool-evaluator/PERSONA.md) | [tool-evaluator](bundles/tool-evaluator/bundle.json) | Trial tools against capability gaps and pre-agreed evidence. | 6 |

<details>
<summary>Inspect member skills: agents, models and knowledge</summary>

#### agent-team-lead

[agent-dispatch-discipline](skills/agent-dispatch-discipline/SKILL.md) · [workstream-orchestration](skills/workstream-orchestration/SKILL.md) · [writing-plans](skills/writing-plans/SKILL.md) · [phased-plan-execution](skills/phased-plan-execution/SKILL.md) · [reviewed-agent-development](skills/reviewed-agent-development/SKILL.md) · [task-board-orchestration](skills/task-board-orchestration/SKILL.md)

#### ai-guardrails-engineer

[guardrail-need-triage-and-claim-classification](skills/guardrail-need-triage-and-claim-classification/SKILL.md) · [defence-surface-coverage-and-rail-placement](skills/defence-surface-coverage-and-rail-placement/SKILL.md) · [policy-to-control-decomposition](skills/policy-to-control-decomposition/SKILL.md) · [least-privilege-capability-design](skills/least-privilege-capability-design/SKILL.md) · [rail-failure-mode-and-budget](skills/rail-failure-mode-and-budget/SKILL.md) · [guard-model-selection-and-calibration](skills/guard-model-selection-and-calibration/SKILL.md) · [rail-runtime-wiring](skills/rail-runtime-wiring/SKILL.md) · [constraint-compliance-audit](skills/constraint-compliance-audit/SKILL.md) · [guardrail-change-control-and-drift-monitoring](skills/guardrail-change-control-and-drift-monitoring/SKILL.md) · [guardrail-benchmark-harness](skills/guardrail-benchmark-harness/SKILL.md) · [rail-adversarial-review](skills/rail-adversarial-review/SKILL.md)

#### evidence-based-ai-delegation

[ai-task-suitability-review](skills/ai-task-suitability-review/SKILL.md) · [delegation-value-measurement](skills/delegation-value-measurement/SKILL.md) · [agent-dispatch-discipline](skills/agent-dispatch-discipline/SKILL.md) (conditional)

#### prompt-agent-engineer

[prompt-interface-design](skills/prompt-interface-design/SKILL.md) · [agent-loop-guardrails](skills/agent-loop-guardrails/SKILL.md) · [prompt-eval-regression](skills/prompt-eval-regression/SKILL.md) · [rag-retrieval-design](skills/rag-retrieval-design/SKILL.md) · [tool-function-calling-design](skills/tool-function-calling-design/SKILL.md) · [prompt-injection-defence](skills/prompt-injection-defence/SKILL.md) · [token-cost-latency-optimisation](skills/token-cost-latency-optimisation/SKILL.md)

#### ml-eval-engineer

[holistic-eval-design](skills/holistic-eval-design/SKILL.md) · [contamination-and-staleness-audit](skills/contamination-and-staleness-audit/SKILL.md) · [honest-eval-reporting](skills/honest-eval-reporting/SKILL.md) · [eval-harness-implementation](skills/eval-harness-implementation/SKILL.md) · [llm-as-judge-design](skills/llm-as-judge-design/SKILL.md) · [safety-redteam-eval](skills/safety-redteam-eval/SKILL.md)

#### provider-hunter

[provider-discovery-and-model-sourcing](skills/provider-discovery-and-model-sourcing/SKILL.md) · [unit-economics-normaliser](skills/unit-economics-normaliser/SKILL.md) · [price-claim-sanity-check](skills/price-claim-sanity-check/SKILL.md) · [discount-entitlement-arbitration](skills/discount-entitlement-arbitration/SKILL.md) · [provider-identity-and-payment-integrity](skills/provider-identity-and-payment-integrity/SKILL.md) · [model-attestation-probing](skills/model-attestation-probing/SKILL.md) · [zdr-retention-verification](skills/zdr-retention-verification/SKILL.md) · [source-legitimacy-grading-and-leeway](skills/source-legitimacy-grading-and-leeway/SKILL.md) · [verdict-and-terms-change-governance](skills/verdict-and-terms-change-governance/SKILL.md) · [provider-brief-authoring](skills/provider-brief-authoring/SKILL.md) · [new-provider-onboarding](skills/new-provider-onboarding/SKILL.md) · [watch-register-and-exit-operations](skills/watch-register-and-exit-operations/SKILL.md)

#### text-classifier-specialist

[typed-decision-model-anatomy-and-question-design](skills/typed-decision-model-anatomy-and-question-design/SKILL.md) · [confidence-and-calibration-mechanics](skills/confidence-and-calibration-mechanics/SKILL.md) · [llm-call-displacement-audit](skills/llm-call-displacement-audit/SKILL.md) · [decision-exam-and-gate-design](skills/decision-exam-and-gate-design/SKILL.md) · [exam-validity-and-robustness-proof](skills/exam-validity-and-robustness-proof/SKILL.md) · [classifier-candidate-benchmark](skills/classifier-candidate-benchmark/SKILL.md) · [decision-head-training-and-label-supply](skills/decision-head-training-and-label-supply/SKILL.md) · [self-host-and-serving-stack](skills/self-host-and-serving-stack/SKILL.md) · [wire-contract-conformance-and-determinism](skills/wire-contract-conformance-and-determinism/SKILL.md) · [fail-open-gate-and-band-policy](skills/fail-open-gate-and-band-policy/SKILL.md) · [decision-model-monitoring-cost-and-drift](skills/decision-model-monitoring-cost-and-drift/SKILL.md) · [ecosystem-recon-and-pattern-mining](skills/ecosystem-recon-and-pattern-mining/SKILL.md)

#### knowledge-librarian

[linked-knowledge-maintenance](skills/linked-knowledge-maintenance/SKILL.md) · [obsidian](skills/obsidian/SKILL.md) · [memory-promotion](skills/memory-promotion/SKILL.md) · [session-librarian](skills/session-librarian/SKILL.md) · [claim-verification](skills/claim-verification/SKILL.md) · [evidence-synthesis](skills/evidence-synthesis/SKILL.md) · [grounded-citations](skills/grounded-citations/SKILL.md) · [wiki-automation-llm](skills/wiki-automation-llm/SKILL.md) · [skill-authoring](skills/skill-authoring/SKILL.md)

#### knowledge-librarian-bundle

[linked-knowledge-maintenance](skills/linked-knowledge-maintenance/SKILL.md) · [obsidian](skills/obsidian/SKILL.md) · [memory-promotion](skills/memory-promotion/SKILL.md) · [session-librarian](skills/session-librarian/SKILL.md) · [claim-verification](skills/claim-verification/SKILL.md) · [evidence-synthesis](skills/evidence-synthesis/SKILL.md) · [grounded-citations](skills/grounded-citations/SKILL.md) · [wiki-automation-llm](skills/wiki-automation-llm/SKILL.md) · [skill-authoring](skills/skill-authoring/SKILL.md)

#### technical-writer

[diataxis-doc-typing](skills/diataxis-doc-typing/SKILL.md) · [precision-editing](skills/precision-editing/SKILL.md) · [docs-lifecycle-ownership](skills/docs-lifecycle-ownership/SKILL.md) · [docset-information-architecture](skills/docset-information-architecture/SKILL.md) · [reference-doc-generation](skills/reference-doc-generation/SKILL.md) · [technical-diagramming](skills/technical-diagramming/SKILL.md)

#### tool-evaluator

[ringed-technology-recommendation](skills/ringed-technology-recommendation/SKILL.md) · [security-posture-triage](skills/security-posture-triage/SKILL.md) · [timeboxed-adoption-trial](skills/timeboxed-adoption-trial/SKILL.md) · [total-cost-of-ownership-analysis](skills/total-cost-of-ownership-analysis/SKILL.md) · [vendor-lockin-exit-assessment](skills/vendor-lockin-exit-assessment/SKILL.md) · [stack-compatibility-check](skills/stack-compatibility-check/SKILL.md)

</details>

### Learning and everyday planning

| Persona role contract | Skill bundle | Use it to… | Member skills |
|---|---|---|---:|
| [learning-tutor](personas/learning-tutor/PERSONA.md) | [learning-tutor](bundles/learning-tutor/bundle.json) | Build competence-based learning plans with retrieval and feedback. | 6 |
| [practice-based-learning](personas/practice-based-learning/PERSONA.md) | [practice-based-learning](bundles/practice-based-learning/bundle.json) | Improve independent performance through practice and corrective feedback. | 2 |
| [career-skill-portfolio-strategist](personas/career-skill-portfolio-strategist/PERSONA.md) | [career-skill-portfolio-strategist](bundles/career-skill-portfolio-strategist/bundle.json) | Plan affordable career experiments that produce evidence. | 3 |
| [personal-finance](personas/personal-finance/PERSONA.md) | [personal-finance](bundles/personal-finance/bundle.json) | Plan saving, debt repayment, diversified investing and financial protection. | 6 |
| [deal-hunter](personas/deal-hunter/PERSONA.md) | [deal-hunter](bundles/deal-hunter/bundle.json) | Compare verified sourcing options, landed costs and seller reliability. | 7 |
| [travel-expert](personas/travel-expert/PERSONA.md) | [travel-expert](bundles/travel-expert/bundle.json) | Research and plan trips around practical constraints. | 5 |

<details>
<summary>Inspect member skills: learning and everyday planning</summary>

#### learning-tutor

[retrieval-and-spacing-design](skills/retrieval-and-spacing-design/SKILL.md) · [direct-practice-projects](skills/direct-practice-projects/SKILL.md) · [feedback-loop-calibration](skills/feedback-loop-calibration/SKILL.md) · [curriculum-sequencing](skills/curriculum-sequencing/SKILL.md) · [diagnostic-assessment-design](skills/diagnostic-assessment-design/SKILL.md) · [motivation-habit-design](skills/motivation-habit-design/SKILL.md)

#### practice-based-learning

[practice-loop-design](skills/practice-loop-design/SKILL.md) · [independent-performance-review](skills/independent-performance-review/SKILL.md)

#### career-skill-portfolio-strategist

[career-option-prototyping](skills/career-option-prototyping/SKILL.md) · [skill-portfolio-evidence-review](skills/skill-portfolio-evidence-review/SKILL.md) · [market-research](skills/market-research/SKILL.md)

#### personal-finance

[behaviour-first-budgeting](skills/behaviour-first-budgeting/SKILL.md) · [simple-long-horizon-investing](skills/simple-long-horizon-investing/SKILL.md) · [risk-protection-review](skills/risk-protection-review/SKILL.md) · [tax-wrapper-optimisation](skills/tax-wrapper-optimisation/SKILL.md) · [goal-retirement-projection](skills/goal-retirement-projection/SKILL.md) · [debt-payoff-strategy](skills/debt-payoff-strategy/SKILL.md)

#### deal-hunter

[landed-cost-sourcing](skills/landed-cost-sourcing/SKILL.md) · [seller-verification-protocol](skills/seller-verification-protocol/SKILL.md) · [negotiation-batna-discipline](skills/negotiation-batna-discipline/SKILL.md) · [source-discovery-search](skills/source-discovery-search/SKILL.md) · [market-price-benchmarking](skills/market-price-benchmarking/SKILL.md) · [requirement-spec-matching](skills/requirement-spec-matching/SKILL.md) · [post-purchase-tco](skills/post-purchase-tco/SKILL.md)

#### travel-expert

[travel-destination-research](skills/travel-destination-research/SKILL.md) · [travel-itinerary-builder](skills/travel-itinerary-builder/SKILL.md) · [travel-deal-scout](skills/travel-deal-scout/SKILL.md) · [travel-logistics-checklist](skills/travel-logistics-checklist/SKILL.md) · [travel-booking-tracker](skills/travel-booking-tracker/SKILL.md)

</details>

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

Staging files does not itself load them into a model. Use your platform's permission controls for workspace safety. The [getting-started guide](docs/getting-started.md) covers activation and optional CLI smoke runs in more detail.

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

## Local release candidate status

The local 0.4.0 candidate contains owner-accepted bounded instruction clarifications without further benchmarks. Historical evidence cards and comparisons apply only to their recorded old hashes, not revised instruction bytes. The frozen 67-asset quality gate remains blocked (48 all-dimension passes, 19 correctness failures); updated instructions are unbenchmarked. Deterministic package checks are separate from behavioural qualification and publication approval. See the [local release decision and residuals](docs/local-release-candidate.md).

## Adapt it, then share what you find

Pick a role you have work for, try it on a bounded task and adjust it to your workflow. Reports showing a missed check, an unclear trigger or a redundant method are especially useful. Include the persona, platform, task and observed behaviour so others can reproduce the issue.

[Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [Release history](CHANGELOG.md)

## Licence and acknowledgements

Original content and consumer code are MIT licensed. Attribution and applicable third-party terms are recorded in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md) and package notices.
