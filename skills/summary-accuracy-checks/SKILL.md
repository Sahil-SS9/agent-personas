---
name: "summary-accuracy-checks"
description: "Independently check a written summary, digest or handoff against its source for lost, contradicted or overstated claims."
license: "MIT"
---

# Summary Accuracy Checks

This is a check performed *after* a summary, memory digest or handoff has been written —
not a guide to writing one. The author's job (`evidence-synthesis`, `grounded-citations`)
is to make supported claims. Your job is to catch what the summary lost or distorted on
the way from the source. A summary can read smoothly and still be wrong.

## 1. Bound the comparison
- Take the written summary and the bounded original record it claims to summarise. Work
  only from those two artefacts. Do not fetch new sources or write to any real memory store.
- If the source record is missing or too partial to judge a claim, mark that claim
  `unverifiable` rather than guessing.

## 2. Check each decision-relevant claim
For every claim that could change a decision, classify it against the source:
- **Preserved** — the source supports it at the same strength.
- **Omitted** — a decision-relevant point in the source is absent from the summary. Name it.
- **Contradicted** — the summary states the opposite of, or incompatible with, the source.
- **Overstated** — the summary raises certainty beyond the source: a guess becomes a fact,
  a possibility becomes a commitment, a tentative finding becomes a conclusion.
Link each classification to the specific source span and the specific summary sentence.

## 3. Separate observation from inference
- An observation is what the source records directly. An inference is the author's
  reasoning from it. If the summary presents an inference as an observation, flag it as
  overstated even when the inference is plausible.
- A faithful shorter paraphrase is **not** a failure. Brevity that keeps the meaning and
  the uncertainty passes. Only loss, contradiction or inflated certainty fails.

## 4. Protect disagreement and uncertainty
- An unresolved disagreement in the source must survive the summary. If the summary erases
  it to read cleanly, that is a failure — name the erased disagreement.
- A confirmed decision must stay confirmed; an open question must stay open. Do not let the
  summary collapse the distinction.

## 5. Report by claim, not by vibe
Return a per-claim list: claim → source span → classification (preserved / omitted /
contradicted / overstated / unverifiable) → the exact affected wording. End with the count
of failures and the single most decision-relevant distortion. Do not give a general
"looks good" verdict; a smooth summary with one erased disagreement still fails.

## Voice
Compare, don't rewrite. Quote the source and the summary side by side. Fail a summary that
erases disagreement, upgrades a guess to fact, or cites an unrelated source — and say
exactly which claim broke.
