---
name: format-grammar-reconstruction
description: "Recover and validate a file or message grammar."
version: 0.1.0
author: Hermes
license: MIT
---

# Format grammar reconstruction

Recover a file or message format as a testable grammar. This skill does not copy proprietary assets or claim writer compatibility from a single sample.

## Procedure
1. Preserve samples, provenance, hashes and version/platform context.
2. Search existing public specifications and implementations; record licence and compatibility before reusing anything.
3. Build a field table from multiple samples: offsets, widths, endianness, encodings, lengths, flags, checksums, compression, nesting and unknown bytes.
4. State competing hypotheses and design samples that distinguish them. Do not label padding or unknown bytes from appearance alone.
5. Implement a minimal reader first, then a writer only for fields whose semantics are evidenced. Keep unknown data lossless where possible.
6. Validate decode → encode → decode, malformed inputs, truncation, boundary values, version changes and negative controls.
7. Report byte-level mismatches, semantic mismatches, unsupported variants and licence provenance.

## Verification
The acceptance matrix must show sample coverage, round-trip result, malformed-input behaviour and every field still classified as unknown.
