---
name: "ai-systems-architecture-patterns"
description: "AI and LLM systems: choose the simplest architecture that works, from a single model call to workflows to agents, and add platform components (retrieval, guardrails, router, gateway, caches, write actions) only when needed."
license: "MIT"
---

# AI systems: architecture patterns

Sub-category: AI and LLM systems. Use with the core system-design skills; a model call is one more dependency with unusual latency, cost and failure behaviour.

## 1. Is a model needed at all?
Write the task, its inputs and the decision it informs. If rules, search or a classical model do it reliably, use those. A model is justified by language understanding or generation that rules cannot cover, and the design must tolerate its errors.

## 2. Simplest pattern first
1. **Single call** with good instructions, examples and retrieved context. Often enough.
2. **Workflows** (code decides the path): prompt chaining with programmatic checks between steps; routing to specialised prompts or cheaper models; parallel sections or voting; orchestrator and workers for decomposable tasks; evaluator-optimiser loops where quality can be judged.
3. **Agents** (the model decides the path and tools) only when steps cannot be predicted and the extra latency, cost and unpredictability are worth it; with stop conditions and budgets.
Deterministic decisions (permissions, money, routing to people) stay in code, not in the model.

## 3. Platform components, added in this order as needs appear
1. Context: retrieval, query rewriting, structured data access (`ai-systems-rag-architecture`).
2. Guardrails: input checks (personal data leaving to providers, jailbreaks) and output checks (format, policy, factual grounding), with defined behaviour on failure.
3. Router (pick model or pipeline by request type) and model gateway (one access point: keys, quotas, cost tracking, rate limits, provider failover, logging).
4. Caches: prompt-prefix caching first, exact-match next; semantic caching only with a measured hit rate and a tested similarity threshold.
5. Write actions and complex loops (`ai-systems-agent-and-tool-safety`).
Each component adds latency and failure modes; record why it was added.

## 4. Model choice is a dependency decision
Hosted API vs self-hosted (`ai-systems-model-serving-and-capacity`); pin model versions; keep prompts, models and settings in a versioned catalogue; plan for provider deprecations.

## 5. ML system debt to design out
Changing anything changes everything (prompts, models, retrieval settings, data); glue code around opaque components; undeclared consumers of model outputs; hidden feedback loops where outputs feed future inputs or training. Version and isolate them; monitor inputs and outputs.

## Output
AI section of the design: why a model, chosen pattern and why simpler ones fail, components with reasons, model access path, deterministic vs model decisions.

## Pitfalls
- Starting with a multi-agent framework for a task a single call solves.
- Frameworks hiding the actual prompts and responses.
- Letting the model make authorisation or money decisions.
