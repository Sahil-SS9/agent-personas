---
name: "system-design-document-and-review"
description: "Write and review the system design document: the iterative design loop, required sections, diagrams, alternatives and open questions, with a template, a worked example and a completeness checker."
license: "MIT"
---

# System design document and review

## 1. The design loop
1. Scope and targets (`system-design-requirements-and-slos`).
2. Simplest design that could work, on one machine, with numbers (`capacity-and-load-estimation`). Ask: is it possible without magic? Can it be simpler?
3. Scale it: which resource binds, what must be distributed (data, caching, messaging skills).
4. Break it: failure modes, overload, security (resilience, overload and security skills). Is it resilient when a component, a zone, a dependency fails?
5. Can we do better? Iterate; record what each iteration changed and why.
6. Operate and pay for it (operability and cost skills).
For AI features, add the AI sub-category skills at step 2 and step 4.

## 2. Required sections
Use `templates/system-design-doc-template.md`: context and goals; requirements with an SLO table; assumptions and estimates with units; high-level design with a component table and diagram; data design; interfaces; deep dives; failure-mode table covering every component; overload and traffic management; security and privacy; operations and rollout; cost; AI and LLM components when any model is used; alternatives considered; risks and open questions. A worked example passing every check: `templates/example-design-order-notifications.md`.

## 3. Diagrams
C4 context and container views (shared member `c4-architecture-modelling`), one sequence diagram per critical flow, and a deployment view showing failure domains when availability matters. Diagrams as code (Mermaid, PlantUML, Structurizr) so they are reviewed with the text.

## 4. Alternatives and decisions
For each significant choice list the options and why each was rejected. Consequential, hard-to-reverse decisions go to an ADR (handoff to Systems Architect).

## 5. Check before review
`python3 scripts/check_design_doc.py design.md` checks: every required section present and non-empty; at least one measurable SLO (percentile with unit or availability %); estimates with units and stated assumptions; a component table, and a complete failure-mode row (failure, detection, impact, mitigation) for every component; timeouts stated; retries paired with backoff, jitter, idempotency and a budget or single layer; no exactly-once claim without idempotency or dedupe; warnings on 100% availability, average-only latency, untested fallback and two-phase commit; listed alternatives and open questions; and, when any AI component appears, an AI section with evaluation, consumption budgets, prompt-injection controls, model access and outage plan, and approval gates for write actions. It checks completeness and consistency only; it cannot tell whether the design is good.

## 6. Review
Review against the Well-Architected lenses (operational excellence, security, reliability, performance efficiency, cost, sustainability) and the failure-mode table. Reviewers try to break it: what happens at 10x load, when the biggest dependency is down, when a zone goes, when a bad deploy ships? Record findings and the decision taken on each.

## Output
A design document that passes the checker, with diagrams, the estimate output, decisions and open questions addressed to named owners.

## Pitfalls
- A diagram without numbers or failure modes.
- Designing everything to the same depth instead of deep-diving where it is hard.
- Calling the design final; list the next bottleneck.
