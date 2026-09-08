# Coding specialists

Use these complementary roles to turn engineering methods into repeatable actions—not to grant extra tools or claim expertise.

- **Software implementation specialist:** trace the actual execution path, verify the changed contract and report what ran.
- **Codebase refactoring specialist:** establish compatibility evidence, separate preparatory restructuring from new behaviour and report honest simplification outcomes.
- **Adversarial code reviewer:** investigate plausible failure paths and return justified findings—or no findings. No quota for bugs.

These roles reuse shared verification, change-impact and test methods. They complement the existing engineering/QA roles; they are not a replacement for release sign-off. Roles coordinate work; their focused methods can be used without a persona.

## Safe adoption

Start with one role in a new workspace. The catalogue's `scripts/try_profile.py` accepts the persona name with any documented harness target. Read the persona contract explicitly; native persona discovery is not universal. See [getting started](getting-started.md).

```sh
python3 scripts/try_profile.py --select persona:codebase-refactoring-specialist --harness codex --dest ../refactoring-trial
```

This stages files only. It does not contact a model, install into a live profile or make a security sandbox. Every role's member skills must be available; copying only PERSONA.md omits part of the instructions.

## Scope of the evidence

Experimental, not independently certified. Earlier private comparisons tested implementation, refactoring and review edge cases. They did not establish general coding-accuracy superiority. The useful signal was operational: performing checks before changes, preserving caller contracts, handling retries and reviewing transaction boundaries.

Final release-text confirmation used the refactoring role on three disposable cases, comparing baseline and release instructions on the same configured model (reported identifier: `gpt-5.6-sol`). All six runs passed their final acceptance checks. There was no final correctness advantage over baseline.

The repeated preparation case and the fresh credential-dependent collaboration case both showed the release role running meaningful compatibility tests before structural edits, then testing restructuring separately from the feature. Baseline edited first. Deliberate contract mutations were caught by both sets of early release-role tests. For the small, already-covered rename, the role reused the existing tests without inventing new tests or abstractions.

Preparation took longer than baseline. This was one new run per arm per case, a small synthetic workload, and controller-reviewed chronological tool evidence—not independent or blinded review. The difficult-dependency case used an existing substitution seam; it does not prove the exception for every legacy system requiring a new production-code seam. Broader repetitions, models, languages and repositories remain untested.

All three personas and their bundles passed byte-for-byte filesystem staging through the seven documented harness targets (42 selections). That is not 42 native agent executions. Existing [native compatibility evidence](compatibility.md) is separate.

Read the individual [evidence cards](../evidence/) and member reference guides. No broad uplift percentage is advertised. Instructions can still be ignored; tools, budgets and permissions affect outcomes. Review generated tests for real sensitivity to contract failures.

## Versioning

The catalogue release is `0.2.0-experimental`. Member skill and persona versions are independent. The refactoring source revision is `0.3.0-preparation-candidate`; the implementation and review source revisions remain `0.2.0-specialist-candidate`. Candidate labels describe source maturation, not installation state.

This is a portable adaptation of reviewed research candidates. Local paths, source intake tooling, private research files and hidden evaluations are not distributed. [Source synthesis](../skills/codebase-simplification-campaign/SOURCE-SYNTHESIS.md) records the selected methods and attribution.
