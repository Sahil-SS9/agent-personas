---
name: "paired-baseline-skilled-benchmarking"
description: "Measure an agent's or skill's uplift with paired runs: same cases with and without the capability, deterministic scorers, and the failure modes stated."
license: "MIT"
---
# Paired Baseline-Skilled Benchmarking

## Use when
- Deciding whether a skill, persona or agent change earns its place.
- Anyone claims a skill "improves" behaviour without a number.
- Choosing between capability candidates on evidence.

## Instructions

1. One change, two arms: the SAME frozen case set runs once without the
   capability (baseline) and once with it (skilled). Cases are written and
   frozen before either arm runs; nothing is edited between arms.
2. Score with typed or outcome verifiers, qualified before use: every
   check must accept the reference answer and a second, semantically
   different good answer, and must reject unsafe, keyword-only and empty
   controls. Keyword presence is NOT evidence of task correctness — a
   phrase matcher fails sound paraphrases and passes contradictions. Where
   a judge must score, its calibration is a separate explicit step (see the
   judge skill), and its verdict is diagnostic, not proof.
3. Prove the intervention actually applied: the skilled arm must show the
   capability's source bytes in its input (hash-bound), and the baseline
   must not. A skill merely installed is not a skill loaded.
4. Run a comparator arm, not just a baseline: the nearest existing variant
   (an older version of the same capability) belongs in the matrix, because
   "better than nothing" is not the claim being made.
5. Repeat the non-ceiling cases: one trial per arm is a sample, not a
   result; report per-arm counts across repeats and treat single reversals
   as sampling variance until reproduced.
6. One change, two arms: the SAME frozen case set runs without the
   capability (baseline) and with it (skilled), and with the comparator
   where one exists. Cases are written and frozen before either arm runs;
   nothing is edited between arms. Score only model-visible final answers,
   never reasoning traces, and never let transport errors count as scores.
7. One turn, no tools, isolated context per arm unless the capability itself
   is multi-turn — then both arms run the same multi-turn shape, and the
   harness difference is only the capability. Isolation means a scoped
   home or direct API transport: the live assistant profile (memory, skills
   index, repository state, exposed tools) must never leak into a
   benchmark arm.
8. Report per case and per arm, not just totals: which cases flipped, which
   regressed, which were at ceiling in both. A ceiling result ("both arms
   perfect") is a valid negative finding — the capability added nothing
   measurable on that set, and the case set must say what it can no longer
   detect.
9. State the failure modes of the measurement itself: model used, judge
   bias, case authorship, single-run noise. Controller-authored cases are
   not independent review; label them as such.
10. Uplift is claimed per case set and per model, never generalised to
    "makes agents better" — cross-model generalisation needs the
    cross-model runs.

## Stop conditions
- Never claim uplift without the baseline number beside it.
- Never edit cases between arms, and never rerun until it passes.
- Never let a benchmark whose cases can all hit ceiling pass as evidence of
  a capability's value.

## Escalation
- Regressions in the skilled arm go back to the capability author with the
  failing cases; the capability changes or the claim dies.
