---
name: "cross-language-semantics-traps"
description: "Hunt the semantics that break ports silently: string indexing, NaN and -0, float printing, signed division, sort order — encode them, never guess them."
license: "MIT"
---
# Cross-Language Semantics Traps

## Use when
- Porting between languages with different string, number or ordering
  semantics (which is all of them).
- A port passes simple tests but fails edge inputs.
- Designing the recorded-case generators before replay.

## Instructions

1. Strings are the first trap: JavaScript and Java index by UTF-16 code
   units (an emoji is two positions), Rust indexes by Unicode scalar. A port
   that indexes by Rust chars will look correct in tests and be wrong on
   emoji, combining marks and astral text. Use generated UTF-16-aware
   helpers when the host semantics must survive.
2. Numbers: the host may have values JSON cannot even express — undefined,
   NaN, Infinity, -0, lone surrogates. Cross them as explicit markers, and
   translate at the boundary; never let a silent JSON round-trip eat them.
3. Floats: printing and parsing differ per platform; a one-ULP difference
   through a serialisation layer is a real port bug the replay must catch.
   Numeric ports declare their tolerance up front or match exactly.
4. Integer edges: signed division and modulo (negative operands differ
   across languages), overflow behaviour, and int-where-float-was-expected
   inputs all get generated cases.
5. Ordering: map iteration order and sort stability differ across
   languages; if the original's output order is observable, it is part of
   the behaviour and gets recorded cases.
6. Nondeterminism in whole-program output (timestamps, UUIDs, key order) is
   handled by normalisers recorded with the cases — never by re-running
   until it matches.

## Stop conditions
- Never hand-write edge cases you believe matter; generate them per
  parameter so coverage is systematic.
- Never "fix" a trap mismatch by adjusting the test.
- Never assume string indexing semantics match because the types look alike.

## Escalation
- A trap the port cannot reproduce exactly (host-defined behaviour with no
  Rust equivalent) becomes a recorded decision: reimplement the host
  semantics in Rust, or keep the unit behind the bridge — owner decides.
