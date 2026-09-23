---
name: "design-system-versioning-migration"
description: "Version, release and migrate the system without breaking consumers."
license: "MIT"
---

# Versioning & Migration

The system is shared infrastructure: change it like an API.

## 1. Semantic versioning with intent
- Breaking token/component changes are major; communicate them like breaking API changes.
- Deprecate before removing: mark, warn, provide the replacement, then remove.

## 2. Migration is your job, not theirs
- Ship codemods or clear migration guides for breaking changes.
- Expand-migrate-contract: add the new, move consumers, remove the old.

## 3. Release discipline
- Changelog every release; consumers must know what moved and why.
- Batch breaking changes into planned majors, not a drip of surprises.

## Voice
API-grade change control. Refuse deleting a token consumers still use without a deprecation path.
