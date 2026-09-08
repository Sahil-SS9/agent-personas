---
name: "experiment-feasibility-review"
description: "Choose a feasible and honest experiment design."
license: "MIT"
---
# Experiment Feasibility Review

## When to Use
Use before running an experiment, declaring a winner or committing scarce traffic. Do not apply a one-size-fits-all sample table.

## Inputs
Decision horizon, randomisation unit, eligible new units per period, baseline, minimum useful effect, allocation, alpha/power, follow-up, dependencies, guardrails and approved stopping design. Record which quantities are supplied versus calculated.

## Procedure
1. Distinguish a sample requirement already calculated for this design from an illustrative number. If it is not approved for the design, request a matched statistical calculation; do not quietly use it as fact.
2. Divide the TOTAL required independent units by eligible new units per period. Round recruitment periods upward, add follow-up and precommitted cycle coverage. Never divide a per-arm requirement as if it were the total or count returning sessions as new units.
3. If traffic or the requirement is unknown, report feasibility unknown. If recruitment cannot fit the deadline, do not run an underpowered ceremony. Propose a bounded usability study, instrumented diagnostic pilot or interviews; label the outcome directional, not causal or representative.
4. Before inference, inspect persistent assignment, intended allocation versus observed counts, eligibility, event losses, contamination and follow-up. Allocation mismatch is an investigation trigger, not a licence to rebalance the report after seeing outcomes.
5. Honour the precommitted fixed horizon or validated sequential method. Statistical significance is not a permission to stop early. Separate data-integrity and harm stops from success declarations.
6. Report absolute percentage-point change separately from relative change. A qualified primary-metric benefit does not establish revenue, retention or long-term benefit. A breached guardrail can defeat an otherwise positive primary metric.
7. On a completed, trustworthy experiment with acceptable guardrails, a recommendation to roll out can be justified; do not reflexively reject all experiments. Keep execution pending its approval.

## Output Contract
Design; input provenance; unit; sample method; total/per-arm counts; recruitment and follow-up horizon; feasibility; primary outcome; uncertainty; guardrails; stopping rule; decision; limitations; approval boundary.

## Stop Rules
No causal winner when assignment/instrumentation is untrusted. No guaranteed revenue from activation or click metrics. No experiment execution, tracking changes or spending without authority. Stop after one bounded diagnostic cycle and escalate unresolved design questions.

## Verification
Use arithmetic tools; preserve their input/output receipts. Check zero traffic, unknown traffic, exact horizon boundaries and total-versus-per-arm scope. A positive and a harmful completed experiment must lead to different decisions.

## References
- [Source method](references/method.md): original distillation; restrictions in the included ledger.
