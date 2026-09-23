---
name: "reference-doc-generation"
description: "Generate accurate reference docs from source so they never drift."
license: "MIT"
---

# Reference Doc Generation

Reference material must be exhaustive and exact — let the source produce it.

## 1. Generate, don't hand-copy
- API/config reference should be generated from code/schema so it can't drift.
- Hand-written reference rots the moment the code changes.

## 2. Complete and consistent
- Every parameter, return, error and default documented in a uniform shape.
- Reference is for lookup: terse, precise, no narrative.

## 3. Pair with prose
- Generated reference plus hand-written explanation/how-to; each does its job.
- Link reference entries to the tasks that use them.

## Voice
Generate-the-exhaustive. Refuse maintaining a hand-typed parameter table beside live code.
