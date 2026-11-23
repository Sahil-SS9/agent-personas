---
name: "judge-calibration-and-tripwires"
description: "Calibrate judges before trusting them: satisfaction is not success, ungrounded judges hit a ceiling, and cheap tripwires catch what judges miss."
license: "MIT"
---
# Judge Calibration and Tripwires

## Use when
- Any LLM judge scores agents, answers or trajectories.
- A judge's ranking is about to decide a promotion.
- Judge results are being reported as if they were ground truth.

## Instructions

1. Calibrate-then-trust: before a judge's verdicts count, measure the judge
   against grounded, verifiable outcomes on a known set. A judge is only
   trusted for the case shapes it was calibrated on — and the calibration
   result ships with every judge-based number.
2. Satisfaction is not success: user-simulator judges rated conversations
   "satisfied" while a majority of those conversations FAILED the task
   (reported finding; not reproduced here). Subjective ratings carry essentially
   no task-success information; never promote on satisfaction alone.
3. Expect a ceiling without ground truth: across frontier scales, ungrounded
   judges converge to a narrow band on hard cases — model scale alone does
   not buy alignment. Provide ground truth where it exists; where it does
   not, say what the judge cannot resolve.
4. Structure what you can: rubrics and structured criteria improve judge
   alignment, but do not transfer uniformly across judge-generator pairs —
   re-calibrate per pair when either side changes.
5. Cheap tripwires beat heroic judging: a zero-cost mechanical check (a
   completion bit, a schema validation, a length check) catches whole
   classes of regression — truncation, format collapse, empty outputs —
   that a sophisticated judge reads past. Wire tripwires first.
6. Watch for the polished-output trap: judges over-trust finished-looking
   answers and miss hidden process failures; an inspection plan that names
   where evidence lives beats a smarter judge reading past it.

## Stop conditions
- Never report a judge score without its calibration evidence.
- Never let a judge resolve what a mechanical check can.
- Never promote on satisfaction ratings alone.

## Escalation
- Where judges disagree with grounded outcomes beyond the calibrated band,
  stop using the judge for that shape and report the disagreement — the
  gate, not the judge, is what is broken.
