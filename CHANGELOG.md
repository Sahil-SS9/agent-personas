# Changelog

## 0.10.0 (draft — build programme in review worktree)

- Revamp agent-team-lead into agent-orchestrator (v2.0.0): the six original members are retained; six new members add the decomposition, scaling, budgeting, verification, synthesis and failure disciplines. Sources studied are recorded privately; public skills contain paraphrased principles only. Handoffs written to evidence-based-ai-delegation (delegation decision), project-strategist (methodology), fleet-governance-operator (fleet health), prompt-agent-engineer (loop design, prompt-level budgets). BREAKING: agent-team-lead remains installable as a deprecated 0.1.0 alias (persona + bundle) until agent-orchestrator passes its independent review gate; the earlier "reality-check voice" composition rule moves into the orchestrator voice.
- New skills: goal-decomposition-and-specialist-routing; scale-to-complexity-and-cost-before-fanout; context-and-token-budgeting-across-workers; verification-subagent; fan-in-synthesis-with-disagreement-surfacing; failure-replanning-and-escalation.
- Add the Rust Rewrite and Porting Specialist persona and bundle (8 skills). Sources studied are recorded privately; public skills contain paraphrased principles only. Boundaries: Rust-to-Rust structural simplification stays with codebase-refactoring-specialist; unowned software goes to clean-room; web performance stays with performance-engineer. No behavioural benchmark exists yet: no pack, cases or scorer are committed, and the keyword-scoring method originally planned is rejected. No uplift is claimed.
- Fold agent-and-skill evaluation INTO ml-eval-engineer (v0.4.0) as a new member group (the collision rule applied: a standalone Evaluator persona would have duplicated llm-as-judge-design and eval-harness-implementation). Four new members: paired-baseline-skilled-benchmarking (the Foundry method productised: frozen cases, two arms, qualified outcome scorers, honest failure modes), trajectory-and-tool-call-eval (task success from tool evidence and artifacts, not final-message tone), judge-calibration-and-tripwires (calibrate-then-trust; satisfaction is not success — judge ratings checked against grounded outcomes; cheap mechanical tripwires first), skill-trust-gate-design (per-version trust gates for third-party agent components, re-vetted on update). Sources studied are recorded privately; public skills contain paraphrased principles only. New handoffs to agent-supply-chain-auditor and prompt-agent-engineer. No behavioural benchmark exists yet for the new members: no pack, cases or scorer are committed; no uplift is claimed.
- Add the Agent Debugger persona and bundle (6 skills): agent-failure-typology (the class names the seam), trace-replay-diagnosis (walk the span tree, replay the divergence step — semantic failures fire no error status), agent-context-and-state-forensics (reconstruct the delivered context before blaming the model; truncation, ordering, pollution, staleness), agent-tool-and-loop-misuse-diagnosis (schema/selection/arguments/fabrication seams; loop exit conditions and retry budgets), agent-observability-instrumentation (agent-span tracing, cost per run, mechanical tripwires; full payloads for the case under review), agent-bug-repro-and-fix-verification (minimal replayable case, one fix at the diagnosed seam, full-run replay, regression case). Sources studied are recorded privately; public skills contain paraphrased principles only. Boundaries written to qa (software tests), devops-sre (service health), prompt-agent-engineer (loop design), agent-orchestrator (execution) and fleet-governance-operator (compliance). No behavioural benchmark exists yet: no pack, cases or scorer are committed; no uplift is claimed.
- Add the Agent Supply-Chain Auditor persona and bundle (5 skills): skill-and-mcp-manifest-vetting (whole-component vetting; marketplace listings are not evidence; capability scored by what it CAN do), payload-and-injection-analysis (component text as attack surface; named payload classes — injection, exfiltration, backdoor, redirection, credential access; quoted not paraphrased), sbom-and-dependency-provenance (BOM from the shipped artifact, pinned, provenance-chained, advisory-overlaid with a check date), update-diff-revetting (every update is an acquisition: diff texts, capability surface and BOM), install-gate-and-quarantine-records (recorded trust decisions, quarantine-with-reason, revocation triggers written at install time). Sources studied are recorded privately; public skills contain paraphrased principles only. Boundaries written to blue-team (runtime defense), tool-evaluator (adoption fit, triage hands off), open-source-maintainer (inbound humans), fleet-governance (internal hygiene), prompt-agent-engineer (injection-defence design) and game-modder (per-vertical). No behavioural benchmark exists yet: no pack, cases or scorer are committed; no uplift is claimed.
- Add draft Context and Memory Engineer (6 members): window budgeting, hybrid retrieval, checkpointing, tiered memory, temporal conflict handling and write-time curation. Corrected overbroad claims about safe context sizes, cache preservation and recency. Private /learn paper-stack notes record actual sections read and remaining gaps; no full-book study or behavioural uplift claimed. Owner demand-evidence gate NOT passed (PROGRAMME build 6); recorded as an open gate, so this persona stays draft regardless of structural checks.

- Add draft LLM Inference Optimisation Engineer (6 members): workload diagnosis, quant/kernel quality, per-rank KV capacity, speculative break-even, reproducible ablations and bounded pressure policies. Includes a stdlib capacity estimator, synthetic input and provider-free controls. Sources studied are recorded privately; public skills contain paraphrased principles only.
- Source attribution policy (owner decision 23/11/2026): public files no longer list the research sources behind each method. NOTICE files, evidence cards, reference notes, THIRD-PARTY-NOTICES and this changelog now say provenance is recorded privately. Licence-required notices stay (Nous Research hermes-agent, obra/superpowers, Impeccable, NSA Ghidra, universal-modder, MITRE ATT&CK). Per-skill source ledgers (references/sources.json) were removed. Skill instruction text is unchanged apart from four unbenchmarked 0.10 draft skills, which had inline citations reworded. Older released skills that name authors inside their instructions are unchanged, because editing them would detach their historical evidence.
- Validation: structural integrity and calculator tests are separate from behavioural proof. The earlier Orchestrator keyword pilot is invalid for uplift (transport failures, incomplete receipts and scoring/isolation defects); retained privately. The later orchestrator outcome cycle (easier exam local: at ceiling for every arm; harder exam on glm-5.3, instruction-only, with paid runs under the live Hermes profile — so the baseline is "live Hermes", not plain — and with the exam stating the rules under test, so it cannot show uplift) found no proven uplift. The one recurring field ambiguity and the retry-rule contradiction were fixed at 48bc2fd, and the attempt rule was rewritten again at ebd2798 (one per-node attempt ledger, three dispatches maximum as the owner set); those revised bytes are UNBENCHMARKED and the evidence stays bound to e451afb. All programme builds remain draft, awaiting source completion, corrected outcome tests and owner-selected independent review. Nothing released.

## 0.9.0

- HermaGuard portable reviewer (hermaguard-candidate): added the P4 scope rule — a wording-only change is out of scope (not reviewed, not reported as clean); a one-line behaviour change is in scope. Behaviourally re-tested across all three consumer bundles: 36/36 policy cases agree.

- Owner-directed improvements from a read-only study of three public projects (recorded privately). Four new focused skills, ten improved members, no new persona. Ideas re-specified independently; no upstream code or prompts copied.
- New skills: service-blueprinting (UX Research) maps a journey onto the service system with a line of visibility, owners and wait points, marking unknowns rather than inventing them; summary-accuracy-checks (ML Eval Engineer) independently checks a written summary for omitted, contradicted or overstated claims; critical-path-planning (Project Strategist) computes earliest completion, all tied critical paths and total float, refusing to invent missing estimates; release-permission-review (DevOps/SRE, Risk Release Manager) reviews changed build/publish/deploy policies for over-grants.
- Improved members: technical-diagramming delivers an artefact (editable source, render, text equivalent) not just advice; c4-architecture-modelling adds a before/after topology delta where a moved box is not a rewire; process-notation-selection routes render and accessibility verification on demand; workstream-orchestration adds a wrap-up reserve; release-quality-gates and test-evidence-integrity add requirement-to-evidence traceability; engagement-reporting-remediation adds a redacted evidence handoff a blue-team reader can act on; guardrail-benchmark-harness adds a permission-aware retrieval outcome check; api-security-design adds lifecycle and approval-drift checks; hermaguard-candidate three-consumer handoff verified.
- Benchmark 19/11/26 (paired baseline vs skilled, one model qwen/qwen4-max:free via nous, isolated 1-turn no-tool sessions, keyword-rubric concept presence): per-skill deltas in each evidence card. Diagnostic concept-presence observation on one model, not a sealed multi-model efficacy estimate; no cross-model generalisation claimed.
- Validation: structural catalogue gate (scripts/verify.py) resealed across all files; this also reseals the three draft hash-mismatches left by the prior guidance-only commit.


## 0.8.0

- Add the System Designer persona and bundle (18 skills: 17 new plus the shared c4-architecture-modelling). Core: requirements and SLOs, capacity estimation, data stores and partitioning, replication and consistency, caching and CDNs, messaging and workflows, failure modes and resilience, overload and traffic management, security, operability and rollout, cost, and the design document and review. AI and LLM systems sub-category: architecture patterns, RAG architecture, model serving and capacity, agent and tool safety, evaluation and operations. Persona and bundle manifests list both groups in `member_groups`.
- Systems Architect (0.3.1): add the reciprocal handoff to System Designer. No member changes.
- Sources studied are recorded privately; public skills contain paraphrased principles only.
- Tools: a dependency-free capacity calculator (QPS, storage, bandwidth, nodes with failure-domain headroom, LLM tokens, replicas and cost) with known-answer tests, and a design-document completeness checker with a template and a worked example.
- Benchmark 04/11/26 (whole persona core vs no skill, one frontier model, isolated no-tool sessions, deterministic scorers): all 9 closed decision cases at ceiling in both arms; three open design tasks, two trials each: webhook service 5/7, 5/7 -> 6/7, 6/7; AI support assistant 7/9, 5/9 -> 9/9, 8/9; analytics right-sizing 5/6, 5/6 -> 6/6, 6/6 (a tie on the rubric; the difference is the document standard). Skilled answers were 2-3x longer and slower. Three checker defects and one scorer defect found on inspection were corrected and recorded. Controller-authored cases, not independent review.
- Validation: structural catalogue gate and deterministic re-authoring.

## 0.7.0

- Add the Business Process Analyst persona and bundle (9 skills): cited fact ledgers from transcripts and documents, a Level 1 to 4 process architecture with a level-fit coverage matrix, BPMN 2.0 modelling with label and end-state rules, portable .bpmn files with diagram interchange, Lucidchart delivery (BPMN import, CSV process import, Standard Import API), a visual standard for every map (sizes, grid, lines, fonts, accessible colour, icons, title, legend and breadcrumb), other notations, improvement-opportunity analysis, and validation and sign-off.
- Sources studied are recorded privately; public skills contain paraphrased principles only.
- Tools: a dependency-free BPMN structure and style checker with an L3 template, and a Lucid Standard Import visual-standard checker with a three-page linked Lucid template. Both checkers caught every seeded defect (15 and 18). Lucidchart import was not exercised.
- Benchmark 04/11/26 (whole persona core vs no skill, one frontier model, isolated no-tool sessions, deterministic scorers): all 14 closed decision cases and the BPMN artefact at ceiling in both arms; Lucid artefact 3/5 -> 4/5; two open-ended tasks, two trials each: first working output 4/6, 4/6 -> 6/6, 6/6 and standard-look Lucid map 4/8, 4/8 -> 8/8, 7/8. Two scorer defects found on inspection were corrected and recorded. Controller-authored cases, not independent review.
- Validation: structural catalogue gate and deterministic re-authoring.

## 0.6.0

- Game Modder rebuilt around building mods: 10 new skills (idea-to-route, Unity, Unreal, Bethesda and script extenders, Java/.NET loaders, native hooks, content and asset pipeline, cross-game mashups and bridges, in-game oracles and verification, publishing and download supply-chain safety), with the original 5 skills kept as guardrails. Asset generation follows each user's own choice of local tools, paid services or both. Research recorded privately; where method structure was informed by universal-modder (MIT), its notice applies (see THIRD-PARTY-NOTICES).
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
