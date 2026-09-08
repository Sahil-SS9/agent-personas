Source: https://google.github.io/eng-practices/review/reviewer/standard.html
Author: Google Engineering Practices
Read scope: Full page only
Captured: 2026-09-08T19:32:09.329326+00:00
Rights: original distillation; source rights retained; no source text redistribution.
Target: hermaguard-candidate

# Review disposition: evidence, severity and useful progress

Load when deciding whether a review comment is a defect, a blocker, a clarification or optional advice.

## Procedure
1. For each comment, identify the applicable contract, established policy or code-health principle. Separate demonstrated behaviour from inference and preference. Positive requirements alone do not prohibit unspecified behaviour.
2. Classify: confirmed defect; unverified risk needing evidence; question about an unclear contract; optional improvement or educational note. Severity measures impact; blocking disposition depends on the team's actual policy, not merely severe wording.
3. Prefer a bounded improvement over perfection-seeking, but do not waive known security/correctness regressions. A review recommendation never grants merge, deployment or production authority.
4. For style, consult the project's established guide. If two approaches are equally supported by evidence and no rule chooses one, do not block on personal taste. Design is not automatically a style issue: justify coupling, readability or maintenance concerns concretely.
5. Group according to the requested reporting granularity. If grouped by function, include distinct triggers under that function; if grouped by root cause, group across functions only when the causal explanation is genuinely shared. Do not silently discard a second trigger to meet a count.
6. End with blocking findings, advisory comments, unresolved questions and reviewed/not-reviewed scope. Escalate unresolved policy conflicts to the owner rather than repeatedly expanding the review.

## Acceptance scenarios (not executed by these notes)
- Equivalent well-supported designs: advisory preference, not invented defect.
- A helpful change with harmless naming polish: do not demand perfection.
- Confirmed authorization bypass: remains blocking under applicable security policy despite unrelated code-health improvement.
- One function violates two contracts: one grouped entry retains both concrete triggers when the requested format is function-level.

## Limits
The source establishes review principles, not measurable proof of agent precision. The four-way disposition and output grouping above are our operational synthesis. No independent review or merge approval is implied.
