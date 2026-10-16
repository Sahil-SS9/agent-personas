---
name: compatibility-release-and-handoff
description: "Package compatible work with evidence and rollback."
version: 0.2.0
author: Hermes
license: MIT
---

# Compatibility release and handoff

Prepare a reimplementation for review or distribution without overstating compatibility. This skill does not approve publication, commercial use or legal compliance.

## Release packet
1. Generate a compatibility matrix by target version, platform, feature, error path and known gap.
2. Attach reproducible build inputs, lockfiles, output hashes, test manifest, parity results and environment details.
3. Produce an asset/dependency licence ledger and confirm no proprietary source, game assets, credentials or unapproved reference material is bundled.
4. Document install, upgrade, uninstall, migration, rollback and data-retention procedures. Use a disposable staging installation first.
5. Mark unsupported behaviour and confidence honestly; distinguish observed parity, inferred compatibility and untested claims.
6. Obtain owner/legal/security approval where the scope requires it. Sign and archive the packet.

## Verification gates
Clean rebuild matches hashes; focused and regression suites pass; negative controls remain negative; rollback restores the pre-release state; a second operator can reproduce the result; release notes identify target versions and limitations. No gate may be waived by “it launches”.
