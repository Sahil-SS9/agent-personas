# Evidence and limitations

## What has been checked

This release separates packaging integrity, native discovery/loading and task behaviour. None substitutes for the others.

- The complete inventory resolves to 113 logical skills. Duplicate snapshots are not counted as additional capabilities. Twenty personas and twenty-one bundles refer to canonical members.
- Standalone validation checks file hashes, inventory, portable names, descriptions, non-empty instructions, licence presence, relative Markdown targets and composition membership. Negative tests cover tampering, missing/unlisted files, traversal, symlinks, malformed names and incomplete role contracts.
- Staging and execution safeguards are exercised with temporary workspaces and real local fixture processes, including execution opt-in, timeouts and output limits. Those processes are not LLM benchmark results.
- Hermes native listing and full skill-content loading pass for all 113 skills on the inspected local v0.21.0 fork. This is loader evidence, not model reasoning or upstream-only certification.
- Claude Code 2.1.201 reports all 113 skills in native discovery. The attempted model task fails because that test environment has no configured authentication. No model answer or behavioural pass is claimed.
- Five other named clients are documented/staging targets only; their executables are unavailable on the test machine. No new client or model was installed to manufacture a compatibility claim.

Machine-readable checks and exact limitations are in [release-checks.json](../evidence/release-checks.json).

## Historical source evidence

Each skill has a [public evidence card](../evidence) recording its original-source hash, exported-file hash, whether its method was adapted, author credit and any available source-bound test summaries. A source hash identifies an artefact; it does not disclose the private source filesystem or reproduce private tooling.

Where available, historical benchmark records were checked against their referenced source skill using the private integrity checker. The cards retain whether integrity validation actually passed and how many cases/passed cases the record declares. Missing evidence is an empty list, not an implied pass.

These historical tests include scenario and phrase-based checks, controlled tasks and earlier candidate pilots. They are not independent proof that a persona improves real-world outcomes. A parser catching a required phrase does not establish a good decision.

**Portable adaptations are changed artefacts.** Fifty-four methods were rewritten or hardened for portable release. Historical results do not transfer automatically to these instructions, or to new model/harness combinations. Preserved cores may still have changed packaging, metadata and reference context.

## Evaluate your own use case

1. Pin the package and harness/model versions.
2. Select representative successful, failure and approval-boundary tasks.
3. Run an unskilled baseline and the selected skill/persona against the same fixtures and tool permissions.
4. Inspect actual artefacts and traces, not a model's self-rating or keyword hits alone.
5. Record output quality, failures, cost, latency and limitations; repeat before inferring an improvement.

The repository supplies a standalone verification script, an opt-in CLI trial runner and [public smoke tasks](../examples/REVIEW.md). It intentionally does not include the private builder, benchmark runner, hidden cases, account configuration or raw evaluation transcripts.

No general uplift percentage, fully tested seven-harness badge, independent-audit claim or unattended-production guarantee is made.

## Coding collection

See [the scoped coding evidence](coding-specialists.md). Earlier evidence above is retained as historical context, not retroactively attributed to these new packages.
