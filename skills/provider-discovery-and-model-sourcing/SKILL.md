---
name: "provider-discovery-and-model-sourcing"
description: "Sweep for every route to a model — direct, aggregator, reseller, free tier, credit grant — and map a required model to the routes that serve it."
license: "MIT"
---

# Provider discovery and model sourcing

## When to use
Sourcing a model, or refreshing the landscape because a supplier changed.

## Procedure
1. Sweep by route type, not by vendor: first-party labs, GPU clouds, hosted routers, open-source gateways, free-tier gates, subscription-as-provider, CLI-to-API adapters, credit grants, decentralised inference, resellers.
2. For a specific model, build the reverse map: which routes serve it, and at what price and terms.
3. Record each route with its access path and what has to be true for it to work.
4. Note upcoming routes separately and keep them in the watch register.

## Decision rules
- Work in routes, not vendors; one vendor usually offers several.
- A route is only a candidate if a model you actually need is reachable through it.
- Keep discovery leads separate from currently usable candidates. A directory listing, announced launch or unreachable serving probe is a discovery lead, not evidence of current reachability.
- When reporting current reachability, mark an unverified or unreachable route false even if it remains worth investigating. Do not use “candidate” to mean both a discovery lead and a usable route; the structured decision must agree with the explanation.
- Aggregator coverage is a claim; verify the model is genuinely served before recommending.
- Deduplicate: resellers of the same upstream are one supply dependency, however many sites front it.

## Decision-output clarification
Keep the discovery lead, verified reachable candidate, graded provisional route and approved integration as separate stages. A reachable candidate still needs identity, model, retention and terms checks; qualification does not authorise spending or deployment.

Before returning a structured result, check that each field answers the requested proposition, uses the requested types and vocabulary, and agrees with the explanation. Saved evidence is not an action performed by you; a recommended next step is not an executed action.

## Pitfalls
- Treating a directory listing as availability.
- Assuming a free tier covers production traffic.
- Missing that two cheap routes share one upstream outage.

## Done
A reverse map from required model to routes, each with its access path and evidence of serving.
