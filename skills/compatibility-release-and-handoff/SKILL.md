---
name: compatibility-release-and-handoff
description: "Package compatible work with evidence and rollback."
version: 0.1.0
author: Hermes
license: MIT
---

# Compatibility release and handoff

Prepare a reimplementation for review or distribution without overstating compatibility. This skill does not approve publication, commercial use or legal compliance.

## Procedure
1. Generate a compatibility matrix by version, platform, feature and known limitation.
2. Re-run parity, security, malformed-input and resource-limit tests in a clean environment.
3. Inventory dependencies, licences, notices, generated artefacts, test fixtures and excluded proprietary material.
4. Produce a migration guide, rollback procedure, safe default configuration and support boundary.
5. Sign the manifest with the project’s approved mechanism when available; otherwise record hashes and build inputs.
6. Obtain owner/legal approval for distribution-sensitive cases before publishing.

## Verification
The handoff is complete only when an independent reader can reproduce the tested result and identify what is not compatible.
