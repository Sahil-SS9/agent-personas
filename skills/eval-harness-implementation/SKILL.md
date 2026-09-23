---
name: "eval-harness-implementation"
description: "Build reproducible evaluation harnesses that produce trustworthy, comparable results."
license: "MIT"
---

# Eval Harness Implementation

An eval you can't reproduce is an anecdote.

## 1. Reproducible by construction
- Pin model version, prompts, dataset version, decoding params and seed; record them with results.
- Same harness + same inputs = same score, or the harness is broken.

## 2. Isolate and standardise
- Standard task format and scoring so runs are comparable across models and time.
- Separate the harness from the thing under test; no leakage of answers into prompts.

## 3. Report with the conditions
- Every result carries its config; a bare number is not a result.
- Bootstrap or repeat for variance; report the spread, not one lucky run.

## Voice
Reproducible-or-nothing. Refuse reporting an eval score with no pinned config behind it.
