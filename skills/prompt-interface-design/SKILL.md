---
name: "prompt-interface-design"
description: "Design prompts as versioned, structured interfaces with stated contracts."
license: "MIT"
---

# Prompt interface design

## When to use
Writing or improving any prompt for repeated use.

## Procedure
1. Write the contract: inputs, expected behaviour, output format, failure behaviour. If you cannot state the contract, the prompt is not ready.
2. Structure before verbosity: role, task, constraints, output schema, examples. Examples earn tokens by disambiguating; otherwise cut.
3. Version the prompt like code: ID, changelog, rationale per change.
4. Anticipate failure: what happens with empty input, hostile input, ambiguous instructions? State the fallback behaviour in the prompt itself.
5. Prefer the smallest prompt that passes the eval set; token cost is a real cost.

## Decision rules
- Prompt changes are code changes: eval-gated, reviewed, revertible.
- One prompt, one job: multi-purpose mega-prompts become unmaintainable; split by task.
- Explicit beats implied: models cannot infer unstated constraints reliably.

## Pitfalls
- Copying "magic prompts" without understanding why they work.
- Unversioned edits to a working prompt.

## Done
Versioned contract-complete prompt with output schema and fallback behaviour.