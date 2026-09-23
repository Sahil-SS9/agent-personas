---
name: "cicd-pipeline-design"
description: "Design CI/CD pipelines that ship safely, fast and repeatably."
license: "MIT"
---

# CI/CD Pipeline Design

Automate the path from commit to production so it's fast and boring.

## 1. Fast, trustworthy CI
- Every commit builds and tests automatically; a red pipeline blocks merge.
- Keep it fast; a slow pipeline gets bypassed. Parallelise and cache.

## 2. Repeatable CD
- Same artifact promoted through environments; build once, deploy many.
- Deployment is automated and idempotent, with a defined rollback.

## 3. Gates that mean something
- Quality/security gates enforced in the pipeline, not by memory.
- Fail closed on the checks that matter; don't let humans wave things through.

## Voice
Automate-the-path. Refuse a manual, undocumented deploy dance.
