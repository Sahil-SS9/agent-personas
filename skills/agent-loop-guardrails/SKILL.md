---
name: "agent-loop-guardrails"
description: "Wrap agent loops in deterministic gates, scoped permissions and stop rules."
license: "MIT"
---

# Agent loop guardrails

## When to use
Any agent that takes actions, calls tools, or loops autonomously.

## Procedure
1. Scope permissions like a privileged tool: least privilege, sandbox where possible, approval gates on irreversible actions. Prompt injection is assumed, not hypothetical.
2. Deterministic feedback gates around nondeterministic behaviour: compilers, tests, schema validators, lint checks — failures feed back for self-correction before human review.
3. Loop bounds: turn budgets, cost budgets, and a hard stop list (what the agent may never do).
4. State design: what the agent must remember, what is transient, what is external — stale memory is a failure mode to design out.
5. Observability: every agent run logs inputs, actions, outputs, costs. An unobservable agent is unaccountable.

## Decision rules
- Autonomy is granted per-action-class, never wholesale; irreversible + unreviewed is never allowed.
- A capability without a stop rule does not ship.
- Success once proves nothing; require repeated eval passes before trusting a loop.

## Pitfalls
- Agent permissions granted for convenience and left standing.
- Turn budgets absent, so loops run away.

## Done
A scoped, gated, bounded, observable agent loop with designed failure modes.