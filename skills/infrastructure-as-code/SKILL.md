---
name: "infrastructure-as-code"
description: "Provision infrastructure as version-controlled, reproducible, reviewed code."
license: "MIT"
---

# Infrastructure as Code

If it's clicked by hand, it's not reproducible and not reviewable.

## 1. Declarative and versioned
- Infra lives in version control; the repo is the source of truth, not the console.
- Declarative desired-state over imperative scripts; converge, don't drift.

## 2. Reproducible and reviewed
- Same code produces the same environment; no snowflake servers.
- Changes go through review and plan-before-apply, like any code.

## 3. Manage state and secrets safely
- Protect and lock remote state; never commit secrets into IaC.
- Modularise for reuse; parameterise per environment.

## Voice
Repo-as-truth. Refuse a hand-clicked production change that isn't in code.
