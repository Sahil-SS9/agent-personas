---
name: "honest-eval-reporting"
description: "Report evaluation evidence with conditions, variance and explicit unknowns."
license: "MIT"
---

# Honest eval reporting

## When to use
Every time evaluation results leave the lab and reach a decision-maker.

## Procedure
1. Separate measured fact from interpretation; label each. A number without its conditions is not evidence.
2. Include the full provenance block: dataset version + date, prompt/template, decoding parameters, seeds/runs, scorer identity, execution date.
3. Report failures and unknowns visibly: what was not measured, what could not be reproduced, what the scores do not cover.
4. Unverifiable claims get marked unverifiable, never silently dropped or auto-passed.
5. Regression beats inflation: prefer the conservative number with provenance. If a later run contradicts an earlier one, investigate before publishing either.

## Decision rules
- No headline claims from a single run without variance or caveat.
- A changed score must carry a changed condition or a change record — unexplained movement is investigated, not celebrated.
- Decision-maker version of the report states: what we know, how we know it, what we don't know, what it means for the decision.

## Pitfalls
- cherry-picking the best run
- reporting relative deltas without absolute numbers
- burying conditions in footnotes nobody reads

## Done
A report a sceptical third party could reproduce: conditions, provenance, variance, unknowns, and interpretation labelled as interpretation.