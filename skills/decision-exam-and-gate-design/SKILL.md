---
name: "decision-exam-and-gate-design"
description: "Design the frozen exam and the gate that decides pass or fail, so a candidate is judged on the decision that matters rather than on accuracy."
license: "MIT"
---

# Decision exam and gate design

## When to use
Before benchmarking any candidate model.

## Procedure
1. Freeze a labelled set from real inputs, with a held-out split that is never used for tuning.
2. Define the classes by consequence: must-keep, should-keep, must-drop. These are asymmetric and deliberately so.
3. Set the gates: must-keep recall at 100 percent, and a bounded relevant-miss rate.
4. Define the utility measure — noise reduction or rejection rate — as the number that justifies the work.
5. Version the exam and record its composition, so results are comparable across candidates.

## Decision rules
- Gate on what you cannot afford to lose first, then measure what you gained.
- Accuracy is the wrong headline. A model that keeps everything scores well on accuracy and delivers nothing.
- Utility must be reported alongside recall, or a filter that never filters looks perfect.
- Freeze the exam before the first candidate, not after the first disappointing result.

## Decision-output clarification
Qualification requires every hard gate AND the declared utility floor. Passing utility never offsets failed must-keep recall. Held-out items are not permitted tuning inputs: recommend the training or separate validation split instead, while reporting any observed leakage explicitly. Keep recommended tuning separate from the proposed invalid split.

Before returning a structured result, check that each field answers the requested proposition, uses the requested types and vocabulary, and agrees with the explanation. Saved evidence is not an action performed by you; a recommended next step is not an executed action.

## Pitfalls
- Tuning thresholds on the held-out set while calling it held out.
- Omitting the must-drop class, which makes the utility metric meaningless.
- Changing the exam between candidates and comparing the scores.

## Done
The exam is frozen with a recorded composition, the gates are asymmetric and stated, and the utility measure is defined as a number.
