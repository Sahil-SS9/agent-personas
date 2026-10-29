# Changelog

## 0.7.0 (on main; not tagged)

- Add the Programme Director and Radio Scriptwriter personas for AI-hosted radio, with their 13 member skills.
- Programme Director (six skills): plans a block against a shelf, keeps the schedule honest, chairs aircheck critique and runs the ear-test protocol on real audio.
- Radio Scriptwriter (seven skills): writes spoken scripts for the ear from cited evidence only, in each host's own voice, with openings and reactions that vary, and never grades its own work.
- Evidence: every member passes its persona's hand-authored exam cases, scored by a deterministic script with no model calls. One behavioural trial ran the whole seven-skill persona against a no-skill arm on the station's own local model, three topics, one sample each: the station's own checks found no station-level fault in either arm and craft findings fell from 15 to 7. Limits are on each card: one sample per topic, one model, not the catalogue's two-case benchmark standard, no blind human read.
- Catalogue, README and CATALOGUE counts updated; structural gate passes.

## 0.6.0 (on main; not tagged)

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
