---
name: format-grammar-reconstruction
description: "Recover and validate a file or message grammar."
version: 0.2.0
author: Hermes
license: MIT
---

# Format grammar reconstruction

Recover a file or message format as a testable grammar. Do not copy proprietary assets or claim writer compatibility from a single sample.

## Procedure
1. Preserve a multi-sample corpus with provenance, hashes, version/platform and permission. Keep originals immutable.
2. Search public prior art and licence constraints before inventing a format. Record what is known, hypothesised and unknown.
3. Align samples, identify magic/version/length/offset/encoding/endianness/checksum and optional/repeated fields. Use a field registry with confidence and evidence offsets.
4. Implement a read-only parser first. Add valid, truncated, corrupt, unknown-version and boundary fixtures; require safe failure and bounded resource use.
5. Express the grammar in a reviewable executable form (for example Kaitai or an equivalent local parser) and compare it against every stock sample.
6. Implement a writer only after parser coverage is adequate. Test decode→encode→decode and, where required, byte-level canonical output; otherwise compare semantics.
7. Record unresolved bytes and do not label guesses as fields.

## Verification
Pass requires corpus-wide parse success, expected rejection of malformed fixtures, no out-of-bounds/resource blow-up, round-trip metrics, version notes and reproducible hashes. One successful decode is discovery, not proof.
