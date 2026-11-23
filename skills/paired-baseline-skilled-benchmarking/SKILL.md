---
name: "paired-baseline-skilled-benchmarking"
description: "Show whether a skill, persona or bundle makes a real difference: red/green authoring, held-out paired trials, and outcome, quality, misses and harm scored separately."
license: "MIT"
---
# Paired Baseline-Skilled Benchmarking

## Use when
- Deciding whether a skill, persona or agent change earns its place.
- Anyone claims a skill "improves" behaviour without a number.
- Writing a new skill and needing to know it fixes a real failure.

## Instructions

1. Two gates, two jobs. The AUTHORING gate builds the skill red/green: run
   the realistic task without the skill first and record what goes wrong;
   write only what fixes those failures; re-run until it passes. The
   EVIDENCE gate proves value on separate held-out tasks, written before
   authoring and never shown to the author. Passing the authoring cases
   proves nothing about value; only held-out results count.
2. A case counts as RED only if the baseline fails it in at least 3 of 5
   runs. A single failed baseline run can be chance. If the baseline
   already passes, the case cannot show uplift: keep it in the regression
   set instead.
3. Give facts, not the method. The task states the situation, numbers and
   allowed answer values; the rule or procedure the skill teaches lives
   only in the skill. A prompt that states the rule hands the baseline the
   skill for free. Where possible, vary rules and thresholds per task so
   memory cannot pass.
4. Define every answer field in the prompt. An undefined field read two
   ways fails every arm alike and looks like a skill finding.
5. Score four things separately, never as one blended number:
   - outcome: required actions present, prohibited actions absent, by
     deterministic checks on the work product;
   - misses: each fixture hides known issues; count found, missed, false
     alarms and false claims of compliance;
   - quality: blind pairwise comparison of the arms' outputs, order
     swapped, ties allowed, by the owner or a judge validated against the
     owner's labels;
   - harm and cost: anything the plain agent did right that the skill
     broke, off-task output, and tokens and time per success.
   Keyword presence is never evidence of task correctness.
6. Qualify every check before spend: it must accept the reference answer
   and a second, differently worded good answer, and reject unsafe,
   keyword-only, empty and always-refuse answers.
7. Arms: no capability, the previous or nearest existing version, and the
   candidate. For a persona, also run its skills without the persona
   wrapper; the wrapper must add something on top or it is packaging.
8. Run 5 trials per task and arm, with the task as the unit, and report
   paired differences with confidence intervals. One trial is a sample, not
   a result.
9. Prove the intervention applied (the candidate's source bytes are in its
   input, hash-bound, and absent from the baseline), isolate every arm from
   the live assistant profile, score only final answers, and never count a
   transport error as a score. Force-injected instructions overstate
   real-world value; test native loading separately.
10. Keep a regression set of tasks the plain agent already handles well. A
    skill that fixes one thing and breaks another has not earned its place.
11. Report per task and per measure: which cases improved, which
    regressed, which were at ceiling. Claim uplift only when the candidate
    beats both the baseline and the previous version on outcome or misses,
    with no safety regression, on held-out tasks. A ceiling result means
    "not measured here", not "useless".
12. State the measurement's limits: model, judge, case authorship, sample
    size. Claims are per task set and per model; cross-model claims need
    cross-model runs.

## Stop conditions
- Never claim uplift from the cases used to write the skill.
- Never claim uplift without the baseline and previous-version numbers beside it.
- Never edit cases between arms, and never rerun until it passes.
- Never let a model write the expected answers without human review.

## Escalation
- Regressions in the skilled arm go back to the capability author with the
  failing cases; the capability changes or the claim dies.
