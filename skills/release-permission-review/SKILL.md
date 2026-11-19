---
name: "release-permission-review"
description: "Review changed build, publishing and deployment policies: who may release, what a change authorises, and the approval that separates testing from releasing."
license: "MIT"
---

# Release Permission Review

An on-demand review of changed build, publishing and deployment definitions. It answers
"who is allowed to release, and does this change grant more than it should?" — not a general
code scan and not a deployment tool.

## When to use
- A change touches CI/CD workflow permissions, publishing jobs, deployment roles, package
  release tokens, or environment protection rules.
- Before approving a change that could let a test or build job publish or deploy.

## Method
1. State who *should* be allowed to publish or deploy, from the supplied policy or the
   documented release owner. If no policy is given, ask for it rather than assume.
2. Read what the proposed change actually authorises: the permissions, scopes, tokens,
   environments and triggers it grants. Review the definitions only — do not run a
   deployment, trigger a workflow, or use credentials.
3. Identify the approval that separates testing from releasing. A test or build job should
   not hold publishing rights; a release job should require the documented approval and
   match the intended scope.
4. Report each discrepancy with its location: a test-only job granted publishing rights is
   a finding; a release job with the documented approval and matching scope is accepted.
   Distinguish a real over-grant from a documented, intentional exception.

## Boundaries
- Read-only review of policy definitions. No deployment, no credential use, no workflow runs.
- This is a targeted release-permission check, not a general-purpose reviewer mode.

## Completion
Return who should release, what the change authorises, the separating approval, and each
discrepancy with its location and disposition (over-grant, accepted, or documented exception).
