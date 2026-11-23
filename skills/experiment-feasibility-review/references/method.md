Sharpens: growth-bottleneck-diagnosis, experiment-feasibility-review, search-acquisition-audit
Rights: original distillation; source-specific restrictions retained in ledger; no full-book or source-code reproduction.

# Experiment design and feasibility

## Design before numbers
Name the hypothesis and decision. Define the randomisation unit and keep its assignment persistent. Choose an outcome that can be measured within the experiment yet plausibly supports the business's longer-term goal. Add harm guardrails. Record eligible exposure and exclusions before analysing results.

## Feasibility inputs
Baseline rate; minimum useful detectable change; significance and power convention; allocation; independent eligible units per period; attrition; decision deadline. A sample calculator or statistician must match the actual design. Repeated sessions are not new independent users. Clustered or interacting users may require a different design.

Required duration is only a rough eligibility check: total required units divided by eligible new units per period. It does not remove seasonality, follow-up or data-quality requirements. If the feasible duration exceeds the decision horizon, do not run a ceremonial underpowered test. Use a directional pilot or qualitative study and state its inferential limits.

## Trust before winners
Validate event capture, denominator alignment, assignment and interference. Investigate implausible effects and allocation mismatches rather than celebrating them. Correlation between feature use and retention can reflect heavier usage rather than feature benefit. Without randomised or otherwise justified causal design, report association.

## Stopping and interpretation
Precommit the inference/stopping method. A fixed-horizon method cannot be repeatedly checked and stopped at the first favourable threshold without invalidating its nominal error control. A suitable sequential design is an alternative, not permission for arbitrary peeking. Harm/data-quality stops are distinct from declaring a winner.

A package-level redesign can be tested, but a single package result cannot identify which changed element caused it. A null or inconclusive test is not proof of equivalence. A short-term gain is not automatically a durable gain. Protect user outcomes against narrow metric optimisation.

## No source-table laundering
The community skill offers convenience sample counts. Do not reuse those as authoritative universal values. Record a real calculation and its assumptions for the actual task.
