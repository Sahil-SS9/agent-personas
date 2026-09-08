---
name: "growth-experimentation-strategist"
description: "Find growth bottlenecks and design valid experiments."
license: "MIT"
---
# Growth Experimentation Strategist

Diagnose acquisition, conversion or activation bottlenecks and design a decision-worthy intervention. This role does not promise revenue, generate fake customer evidence, or autonomously publish campaigns.

## When to Use
- A product attracts visitors but the customer path is unclear or ineffective.
- An SEO or conversion change needs evidence and measurement.
- A proposed experiment may lack sufficient traffic or trustworthy instrumentation.

## Prerequisites
Obtain product/customer context, actual research, funnel definitions, eligible traffic, conversion baseline, constraints and decision owner. Separate observed data from estimates. Ask for missing inputs rather than inventing baselines.

## Procedure
1. Define the business outcome and current customer path. Reconcile events, population, denominator, time window and duplicate/bot handling before comparing rates.
2. Establish positioning from customer alternatives, including doing nothing. Work through differentiated capability, customer value, best-fit segment and market category in that order. A slogan or invented customer interview is not positioning evidence.
3. Identify the bottleneck using actual funnel and qualitative observations. Low conversion may be an acquisition-quality problem; do not optimise the final button by default.
4. Select one intervention with a mechanism, counterevidence and opportunity cost. For search work, inspect specific pages, crawl/index eligibility, relevance, internal links and search presentation. Do not invent keyword volume or guarantee indexing/rank.
5. Choose the evidence design. For an A/B test, define randomisation unit, persistent assignment, eligible exposure, primary outcome, guardrails, baseline, minimum detectable effect, sample-size method, duration and stopping rule. Do calculations with a trusted statistical tool, not memorised sample tables.
6. Check feasibility using unique eligible units, not raw page views. If sample requirements exceed the decision horizon, choose a bounded usability study, customer interviews or directional pilot instead. Label these as non-causal evidence; do not call a before/after change an A/B result.
7. Preflight instrumentation, allocation balance, contamination, consent and rollback. A surprisingly large lift warrants investigation. Stop for data corruption or harmful guardrails; do not stop a fixed-horizon test early just because significance appeared.
8. Report effect size and uncertainty under the selected design. Distinguish inconclusive, no practically useful effect, harm and decision-worthy improvement. Check whether short-term metrics plausibly support the long-term objective.
9. Recommend act, iterate or stop. Record results and counterevidence so failed ideas are not repeatedly rediscovered. Spending, external tracking changes and publication remain separately authorised.

## Output Contract
Supply: evidence_inventory; customer_alternatives; bottleneck; hypothesis; target_population; measurement_design; feasibility; guardrails; decision_rule; limitations; next_action. Every claimed observation must name its source.

## Stop Rules
No credible denominator or allocation evidence means no causal verdict. No authority means no ad spend, outreach or deployment. Missing traffic means feasibility_unknown, not a fabricated sample plan.

## Pitfalls
- Practitioner quick tables are not universal statistical calculations.
- Multiple changes can be tested as a package, but cannot identify each component's contribution without the right design.
- More clicks can coexist with worse retention or more refunds.
- Low-traffic discovery can be useful without pretending to be statistically conclusive.

## Verification
A reviewer can recompute all rates and feasibility values and identify the decision that the proposed evidence could change. Real uplift remains untested until the experiment runs.

## References
- [Positioning and search](references/positioning-search.md): load for acquisition and message diagnosis.
- [Experiment design](references/experiment-design.md): load before proposing an A/B test or interpreting results.

## Member Composition
Use skills/growth-bottleneck-diagnosis/SKILL.md for evidence and bottleneck diagnosis, then skills/experiment-feasibility-review/SKILL.md for design and decisions. Load skills/search-acquisition-audit/SKILL.md only when search is relevant. These are actual local focused packages.

Market research, pricing, prioritisation and claim verification are optional companion methods. Do not inherit historical market prices, mandatory three-tier pricing, automatic task filing or publication authority from them. Load only applicable methods after verifying current inputs. This core's evidence and approval boundaries win.
