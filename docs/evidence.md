# Evidence and validation

## What has been checked

This release separates packaging integrity, native discovery/loading and task behaviour, so you can trust exactly what each check covers.

- The historical 0.1.0 inventory resolved to 113 logical skills; duplicate snapshots are not counted as additional capabilities. That release's twenty personas and twenty-one bundles referred to canonical members.
- Standalone validation checks file hashes, inventory, portable names, descriptions, non-empty instructions, licence presence, relative Markdown targets and composition membership. Negative tests cover tampering, missing/unlisted files, traversal, symlinks, malformed names and incomplete role contracts — so you can verify every download yourself.
- Staging and execution safeguards are exercised with temporary workspaces and real local fixture processes, including execution opt-in, timeouts and output limits.
- Hermes native listing and full skill-content loading pass for all 113 skills on the inspected local v0.21.0 fork — real loader evidence on a working agent platform.
- Claude Code 2.1.201 reports all 113 skills in native discovery.
- Five other named clients are documented/staging targets; the machine-readable checks in [release-checks.json](../evidence/release-checks.json) show precisely what was exercised on each.

Machine-readable checks are in [release-checks.json](../evidence/release-checks.json).

## Source provenance

Each skill has a [public evidence card](../evidence) recording its original-source hash, exported-file hash, whether its method was adapted, author credit and available source-bound test summaries. A source hash identifies an artefact without disclosing the private source filesystem or reproducing private tooling.

Historical benchmark records were checked against their referenced source skills using the private integrity checker. The cards record whether integrity validation passed and how many cases each record declares, so provenance is auditable rather than asserted.

These historical tests include scenario and phrase-based checks, controlled tasks and candidate pilots that verified the skills produce the intended procedures and decision points.

**Portable adaptations are changed artefacts.** Fifty-four methods were rewritten or hardened for portable release. Preserved cores may have changed packaging, metadata and reference context; the evidence cards bind results to their exact source.

## Evaluate fit in your own environment

The catalogue is built to be measured, not just trusted:

1. Pin the package and harness/model versions.
2. Select representative successful, failure and approval-boundary tasks.
3. Run an unskilled baseline and the selected skill/persona against the same fixtures and tool permissions.
4. Inspect actual artefacts and traces, including a model's self-rating and keyword hits.
5. Record output quality, failures, cost and latency; repeat to quantify the improvement.

The repository supplies a standalone verification script, an opt-in CLI trial runner and [public smoke tasks](../examples/REVIEW.md). The private builder, benchmark runner, hidden cases, account configuration and raw evaluation transcripts stay private — you get the outputs, not the machinery.

## Coding collection

See [the scoped coding evidence](coding-specialists.md), including recorded baseline-versus-release comparisons on a configured model.

## 0.3.0 role collection validation

This package adds 19 roles and 118 focused skills. Every skill passed the private scenario-benchmark pipeline, and packaging plus narrow real-task pilots were verified before release. Methods draw on authoritative books, standards and primary documentation; per-skill evidence cards record provenance and validation scope. Use the bundled verification and smoke tooling to confirm behaviour in your own harness and model before production use.