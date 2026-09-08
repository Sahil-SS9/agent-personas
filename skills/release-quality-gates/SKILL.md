---
name: "release-quality-gates"
description: "Use when deciding whether an app, feature, automation."
license: "MIT"
---
# Release Quality Gates

## When to use
Use when deciding whether an app, feature, automation.

## Method
1. Choose verification depth from consequence and reversibility. Separate instruction review, implementation checks, deployment readiness and post-deploy verification.
2. Require traceable acceptance criteria and evidence at the actual delivery boundary: tests, executable artefacts, installed loader behaviour or exact remote readback as appropriate.
3. Report gates as pass, fail, blocked, not-run or not-applicable with reasons. Do not silently convert missing evidence into pass.
4. Fix verified defects and rerun affected checks. Distinguish independent review from author self-review and preserve unresolved risks.
5. Approval to build is not approval to deploy. Release only the exact reviewed version with a rollback path and explicitly authorised activation.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
