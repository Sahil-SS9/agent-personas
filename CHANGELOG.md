# Changelog

## 0.10.0 (draft — build programme in review worktree)

- Revamp agent-team-lead into agent-orchestrator (v2.0.0): the six original members are retained; six new members add the decomposition, scaling, budgeting, verification, synthesis and failure disciplines. Source study: Anthropic's multi-agent research system and when-to-use-multi-agent guidance, the LangGraph supervisor pattern and its production cases, OpenAI Agents SDK handoffs, MetaGPT's role-chain design, Claude Code Agent Teams, the agency-agents orchestrator and multi-agent-architect files, plus our own orchestration practice (workstream-orchestration, lossless-delegation, agent-dispatch-discipline). Public skills contain paraphrased principles only. Handoffs written to evidence-based-ai-delegation (delegation decision), project-strategist (methodology), fleet-governance-operator (fleet health), prompt-agent-engineer (loop design, prompt-level budgets).
- New skills: goal-decomposition-and-specialist-routing; scale-to-complexity-and-cost-before-fanout; context-and-token-budgeting-across-workers; verification-subagent; fan-in-synthesis-with-disagreement-surfacing; failure-replanning-and-escalation.
- Add the Rust Rewrite and Porting Specialist persona and bundle (8 skills). Source study: the MIT-licensed rust-anything project's recorded-behaviour porting discipline (profile, plan, bridge, record, diff, bench, shadow, gate; per-language bridges; batch-over-per-call economics; the UTF-16/NaN/-0 trap discipline; the honest x18n-core case where gates passed and the bench still said no), plus craft-anything, the Rust API guidelines, clippy, cargo-semver-checks, Miri, criterion, and published production-port case studies (Cloudflare Pingora, Discord, Astral uv/Ruff). Boundaries: Rust-to-Rust structural simplification stays with codebase-refactoring-specialist; unowned software goes to clean-room; web performance stays with performance-engineer. Paired benchmark PENDING as a release gate.
- Fold agent-and-skill evaluation INTO ml-eval-engineer (v0.4.0) as a new member group (the collision rule applied: a standalone Evaluator persona would have duplicated llm-as-judge-design and eval-harness-implementation). Four new members: paired-baseline-skilled-benchmarking (the Foundry method productised: frozen cases, two arms, deterministic scorers, honest failure modes), trajectory-and-tool-call-eval (task success from tool evidence and artifacts, not final-message tone), judge-calibration-and-tripwires (calibrate-then-trust; satisfaction is not success — the published finding that a majority of judge-"satisfied" conversations failed the task; ungrounded judges hit a scale-independent ceiling; cheap mechanical tripwires first), skill-trust-gate-design (per-version trust gates for third-party agent components, re-vetted on update — answering the published finding that over a third of marketplace skills carry security flaws). Source study: Agent-as-a-Judge survey and product practice, judge-reliability benchmarks, satisfaction-success divergence research, and our own benchmarking practice. New handoffs to the supply-chain persona and prompt-agent-engineer. Paired benchmark PENDING as a release gate.
- Validation: structural catalogue gate (scripts/verify.py) passes clean at draft state. The paired benchmark (baseline vs skilled, deterministic scorers) is PENDING and is a release gate; benchmark evidence will be recorded here and on the evidence cards before any release. This is a draft in the review worktree; not released.

## 0.9.0

- HermaGuard portable reviewer (hermaguard-candidate): added the P4 scope rule — a wording-only change is out of scope (not reviewed, not reported as clean); a one-line behaviour change is in scope. Behaviourally re-tested across all three consumer bundles: 36/36 policy cases agree.

- Owner-directed improvements from a read-only study of BaaRai/ARTEX, elementalsouls/Claude-BugHunter and cathrynlavery/diagram-design. Four new focused skills, ten improved members, no new persona. Ideas re-specified independently; no upstream code or prompts copied (ARTEX AGPL-3.0; BugHunter content CC BY 4.0; diagram-design MIT with separate asset terms).
- New skills: service-blueprinting (UX Research) maps a journey onto the service system with a line of visibility, owners and wait points, marking unknowns rather than inventing them; summary-accuracy-checks (ML Eval Engineer) independently checks a written summary for omitted, contradicted or overstated claims; critical-path-planning (Project Strategist) computes earliest completion, all tied critical paths and total float, refusing to invent missing estimates; release-permission-review (DevOps/SRE, Risk Release Manager) reviews changed build/publish/deploy policies for over-grants.
- Improved members: technical-diagramming delivers an artefact (editable source, render, text equivalent) not just advice; c4-architecture-modelling adds a before/after topology delta where a moved box is not a rewire; process-notation-selection routes render and accessibility verification on demand; workstream-orchestration adds a wrap-up reserve; release-quality-gates and test-evidence-integrity add requirement-to-evidence traceability; engagement-reporting-remediation adds a redacted evidence handoff a blue-team reader can act on; guardrail-benchmark-harness adds a permission-aware retrieval outcome check; api-security-design adds lifecycle and approval-drift checks; hermaguard-candidate three-consumer handoff verified.
- Benchmark 19/11/26 (paired baseline vs skilled, one model qwen/qwen4-max:free via nous, isolated 1-turn no-tool sessions, keyword-rubric concept presence): per-skill deltas in each evidence card. Diagnostic concept-presence observation on one model, not a sealed multi-model efficacy estimate; no cross-model generalisation claimed.
- Validation: structural catalogue gate (scripts/verify.py) resealed across all files; this also reseals the three draft hash-mismatches left by the prior guidance-only commit.


## 0.8.0

- Add the System Designer persona and bundle (18 skills: 17 new plus the shared c4-architecture-modelling). Core: requirements and SLOs, capacity estimation, data stores and partitioning, replication and consistency, caching and CDNs, messaging and workflows, failure modes and resilience, overload and traffic management, security, operability and rollout, cost, and the design document and review. AI and LLM systems sub-category: architecture patterns, RAG architecture, model serving and capacity, agent and tool safety, evaluation and operations. Persona and bundle manifests list both groups in `member_groups`.
- Systems Architect (0.3.1): add the reciprocal handoff to System Designer. No member changes.
- Source study: Google SRE book and workbook chapters, Amazon Builders' Library, AWS Well-Architected and its Generative AI Lens, Azure Architecture Center patterns, system-design-primer, OWASP LLM Top 10, NIST AI 600-1, Anthropic's agent guidance, 13 papers, and the authors' own published material for Designing Data-Intensive Applications, System Design Interview, Release It! and AI Engineering (the books themselves were not available). Public skills contain paraphrased principles only.
- Tools: a dependency-free capacity calculator (QPS, storage, bandwidth, nodes with failure-domain headroom, LLM tokens, replicas and cost) with known-answer tests, and a design-document completeness checker with a template and a worked example.
- Benchmark 04/11/26 (whole persona core vs no skill, one frontier model, isolated no-tool sessions, deterministic scorers): all 9 closed decision cases at ceiling in both arms; three open design tasks, two trials each: webhook service 5/7, 5/7 -> 6/7, 6/7; AI support assistant 7/9, 5/9 -> 9/9, 8/9; analytics right-sizing 5/6, 5/6 -> 6/6, 6/6 (a tie on the rubric; the difference is the document standard). Skilled answers were 2-3x longer and slower. Three checker defects and one scorer defect found on inspection were corrected and recorded. Controller-authored cases, not independent review.
- Validation: structural catalogue gate and deterministic re-authoring.

## 0.7.0

- Add the Business Process Analyst persona and bundle (9 skills): cited fact ledgers from transcripts and documents, a Level 1 to 4 process architecture with a level-fit coverage matrix, BPMN 2.0 modelling with label and end-state rules, portable .bpmn files with diagram interchange, Lucidchart delivery (BPMN import, CSV process import, Standard Import API), a visual standard for every map (sizes, grid, lines, fonts, accessible colour, icons, title, legend and breadcrumb), other notations, improvement-opportunity analysis, and validation and sign-off.
- Source study: the OMG BPMN 2.0.2 standard, the eCH-0158 BPMN conventions, WCAG 2.2, nine peer-reviewed papers on process-model quality and comprehension, and the authors' own published material for Fundamentals of BPM, BPMN Method and Style, Real-Life BPMN and Workflow Modeling (book chapters themselves were not available). Public skills contain paraphrased principles only.
- Tools: a dependency-free BPMN structure and style checker with an L3 template, and a Lucid Standard Import visual-standard checker with a three-page linked Lucid template. Both checkers caught every seeded defect (15 and 18). Lucidchart import was not exercised.
- Benchmark 04/11/26 (whole persona core vs no skill, one frontier model, isolated no-tool sessions, deterministic scorers): all 14 closed decision cases and the BPMN artefact at ceiling in both arms; Lucid artefact 3/5 -> 4/5; two open-ended tasks, two trials each: first working output 4/6, 4/6 -> 6/6, 6/6 and standard-look Lucid map 4/8, 4/8 -> 8/8, 7/8. Two scorer defects found on inspection were corrected and recorded. Controller-authored cases, not independent review.
- Validation: structural catalogue gate and deterministic re-authoring.

## 0.6.0

- Game Modder rebuilt around building mods: 10 new skills (idea-to-route, Unity, Unreal, Bethesda and script extenders, Java/.NET loaders, native hooks, content and asset pipeline, cross-game mashups and bridges, in-game oracles and verification, publishing and download supply-chain safety), with the original 5 skills kept as guardrails. Asset generation follows each user's own choice of local tools, paid services or both. Research: public loader and tool documentation, rehan-remade/universal-modder (MIT) as a cross-check, and a survey of 1,723 game-modding repositories.
- Benchmark 19/10/26 (replaces the ceiling-only result below for these 35 skills): 70 hand-authored decision cases scored deterministically, plus 8 executable build tasks graded in a no-network sandbox. Decision cases: 44 uplift, 25 at ceiling, 1 equal, 0 regressions. Build tasks: 2 uplift (safe save migration 6/9 -> 9/9; route selection 9/10 -> 10/10), 6 at ceiling. One trial per arm on a frontier model; per-skill results are in each evidence card.

- Add clean-room-reimplementation-engineer and game-modder personas, each with five focused skills and explicit authorisation, provenance, compatibility and rollback boundaries.
- Harden reverse-engineering-specialist from 11 to 15 members with runtime metadata routing, authorised traffic/API mapping, format grammar reconstruction and bounded local agent bridges.
- Source study completed using public primary documentation plus the existing private `/learn` and `/learn book` learning boundary; public skills contain paraphrased procedures only, not source text.
- Validation: structural catalogue gate and isolated staging pass. The corrected benchmark resume key now includes fixture identity (the old key silently skipped duplicate skill fixtures). Two local model conditions (`auto` and `active:aux`) ran 28 fixtures each (56 base/skilled pairs per model across 14 skills); both scored 100% base and 100% skilled, with 28/28 ceiling pairs and zero measured uplift or regressions. This is a valid ceiling result, not certification.
- No live profile activation or publication is included.

## 0.4.0 (packaged; not published)

- Add five agent and OSS ecosystem operations personas with 57 consolidated focused skills: open-source-maintainer (11), ai-guardrails-engineer (11), provider-hunter (12), filesystem-hygiene-steward (11), text-classifier-specialist (12).
- Consolidate every persona to at most 12 skills, matching the largest bundle already in the catalogue; 82 drafted skills were reduced to 57 by merging overlapping behaviours rather than dropping capability.
- Validation: the structural gate, an independent re-verified hash manifest, and deterministic re-authoring all pass. Behavioural benchmarking ran against two local models with no provider calls and no spend, over 57 authored fixtures: the stronger model moved from 95 to 98 percent, the weaker from 77 to 100 percent, with zero regressions on either.
- These skills have NOT been through the private scenario-benchmark pipeline referenced by 0.3.0. The benchmark above is a standalone fixture set scored by content only; over half the fixtures sit at ceiling against the stronger model and cannot separate skill from prior knowledge, so it is reported as indicative, not as pipeline certification.
- No live profile activation is part of this public package.


## 0.5.0

- Add the Reverse Engineering Specialist persona and bundle: 7 core skills plus 4 conditional tool adapters (11 total). It works at the strongest analysis level available, from format tools to decompilers, integration layers and isolated runtime, and states which level it used.
- Reverse-engineering methods cover competing hypotheses with evidence for and against, information-gain-driven next steps, source-to-sink and pre-authorisation tracing, indirect-dispatch and library-boundary resolution, cross-version comparison and durable case state. When installed tools cannot answer a question, it searches for and evaluates new tools, then proposes them for approval instead of stopping.
- Expand the Frontend UX Engineer from 8 to 12 skills: art direction across ten style families with no default style, tool-agnostic image and video asset production, live render verification with independent review, and design comparison prototyping.
- Publish the 0.3.0 and 0.4.0 collections in this release; the full catalogue tables now list every persona, bundle and skill.
- Owner-accepted revisions without a further benchmark: evidence cards apply only to the versions they record, and no new uplift is claimed.

## 0.4.0 (published in 0.5.0)

- Add five agent and OSS ecosystem operations personas with 57 consolidated focused skills: open-source-maintainer (11), ai-guardrails-engineer (11), provider-hunter (12), filesystem-hygiene-steward (11), text-classifier-specialist (12).
- Consolidate every persona to at most 12 skills, matching the largest bundle already in the catalogue; 82 drafted skills were reduced to 57 by merging overlapping behaviours rather than dropping capability.
- Current candidate: owner-accepted unbenchmarked instruction revisions. Deterministic consumer-package integrity and archive reproduction are checked separately; private deterministic re-authoring is unavailable because the original authoring specs were lost.
- Earlier draft fixtures reported stronger-model results of 95 to 98 percent and weaker-model results of 77 to 100 percent with no scored regressions. These historical observations concern the old draft bytes only, not this revised candidate; they are not a current qualification claim.
- These skills have NOT been through the private scenario-benchmark pipeline referenced by 0.3.0. The benchmark above is a standalone fixture set scored by content only; over half the fixtures sit at ceiling against the stronger model and cannot separate skill from prior knowledge, so it is reported as indicative, not as pipeline certification.
- No live profile activation is part of this public package.


## 0.3.0 (published in 0.5.0)

- Add 19 personas and bundles with 118 new focused skills, each validated through the private scenario-benchmark pipeline before packaging.
- Packaging and narrow task pilots verified; measure fit in your own environment with the included verification and smoke tooling.
- No live profile activation is part of this public package.

## 0.2.1

- Integrate coding personas and bundles into the main catalogue with released status; retain historical evidence limits.
- Add the supplied agent-persona illustration above the README title.
- Rebuild the README around agent/persona/bundle/skill composition, role selection and a complete first-use path.
- Preserve package identifiers, member selection and engineering procedures. Older prerelease tags remain immutable history.

## 0.2.0-experimental

- Add implementation, refactoring and adversarial-review personas and matching bundles, plus four focused coding methods.
- Preserve existing packages and composition identifiers.
- Add version-bound source attribution and scoped operational evidence. Final refactoring checks cover preparation, a dependency seam and proportional handling of a small edit; reported accuracy matched baseline while adding repeatable pre-change checks.
- Verify byte-for-byte staging of the three new personas and bundles across all seven documented targets. Native execution coverage is recorded per target in the checks file.
- Keep all builder, training-source intake and hidden evaluation tooling private.


## 0.1.0-experimental

- Initial portable catalogue covering the complete inventoried logical skill set, including explicitly adapted standalone historical-source methods.
- Twenty role contracts and twenty-one bundle manifests compose canonical skills without embedded duplicate skill copies.
- Portable method adaptations replace host-bound operational examples; historical results are not transferred as proof of the rewritten output.
- Benefit-led catalogue and installation documentation cover seven agent harnesses with explicit verification limits.
- Standalone integrity checking and opt-in agent-CLI trials; no private builder or internal benchmark suite is distributed.
- Original content and consumer code released under MIT, with applicable third-party notices preserved.


## Owner-accepted local candidate clarifications

Bounded instruction and handoff clarifications applied after frozen evidence review; no new model calls or benchmarks. Frozen results and the blocked quality gate are preserved. Updated instruction behaviour remains unmeasured. See [local candidate status](docs/local-release-candidate.md).
