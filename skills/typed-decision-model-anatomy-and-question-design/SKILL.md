---
name: "typed-decision-model-anatomy-and-question-design"
description: "Explain how typed-decision models actually work, and design the question and option set that determines whether they can work at all."
license: "MIT"
---

# Typed decision model anatomy and question design

## When to use
Deciding whether a decision belongs to a small classifier, or designing the question to ask it.

## Procedure
1. Establish the mechanism: a small encoder, one forward pass, a typed question over a supplied option set, a score per option. No tokens are generated, so structured-output error is zero by construction.
2. Map the question shape: choice, score, or yes/no; how many options; whether the option set is fixed or open.
3. Check that the decision is expressible as a chosen option. If it needs free text, it is a generation task.
4. Design the option set so options are mutually exclusive and the correct answer is always present.
5. Fix the question text, because the model's behaviour is question-sensitive and the contract must be stable.

## Decision rules
- The question and option set are the interface. Changing wording changes results; version them.
- Wider option sets are harder; a model that works at two options may not at twelve.
- The option set must contain a defensible correct answer for every input, including the boring ones.
- Anatomy differs by family: some compile the recipe into the artefact, others run a separate decision head. Know which you are deploying.

## Pitfalls
- Treating a decision model as a small language model.
- Adding an option late without re-benchmarking.
- Assuming a question that reads well to you is unambiguous to the model.

## Done
The mechanism is stated, the question shape is fixed and versioned, and the option set is exclusive with a defined correct answer for every input class.
