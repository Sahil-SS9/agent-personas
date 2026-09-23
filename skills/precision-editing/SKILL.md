---
name: "precision-editing"
description: "Edit for active voice, consistency, testability and BLUF ordering."
license: "MIT"
---

# Precision editing

## When to use
Every draft, before it leaves.

## Procedure
1. BLUF: conclusion/action first, detail after. The first sentence of each section carries it.
2. Active voice, present tense, concrete nouns; cut needless words and hedges ("simply", "just", "obviously").
3. Terminology consistency: one concept, one term; build a term list for the doc set and enforce it.
4. Testability: every behavioural claim ("retries automatically", "runs in under a minute") must match reality — verify or cut.
5. Code blocks: copy-pasteable, complete, with expected output shown.
6. Read it as the audience: skim headings only — does the skeleton tell the story?

## Decision rules
- If a sentence can be misread, it will be; rewrite, do not clarify in a footnote.
- Inaccurate docs are worse than missing docs: wrong docs actively mislead.

## Pitfalls
- Documentation that narrates the system's history instead of the reader's task.
- Example code with placeholders that do not run.

## Done
Front-loaded, consistent, verified copy that a skimmer can follow.