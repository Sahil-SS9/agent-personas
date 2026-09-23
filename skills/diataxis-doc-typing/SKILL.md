---
name: "diataxis-doc-typing"
description: "Type every document by its job (tutorial/how-to/reference/explanation) before writing."
license: "MIT"
---

# Diátaxis doc typing

## When to use
Before writing or reviewing any documentation.

## Procedure
1. Name the document type first: tutorial (learning, guaranteed success), how-to (task completion for the experienced), reference (lookup, mechanical accuracy), explanation (understanding, context).
2. One document, one job: split pages that mix types; a mixed page serves nobody.
3. Match structure to type: tutorials = steps with checkpoints; how-tos = goal-first recipes; reference = ordered, complete, scannable entries; explanations = narrative with why.
4. State the audience's assumed knowledge at the top; route readers to prerequisites instead of embedding tutorials mid-reference.

## Decision rules
- Reference pages never narrate; tutorial pages never skip steps.
- When a request mixes types ("write a guide that also serves as API reference"), split the deliverable.

## Pitfalls
- READMEs that are simultaneously tutorial, reference and marketing.
- Explaining theory inside a task recipe.

## Done
Every doc typed, single-job, audience-stated, correctly structured.