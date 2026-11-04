---
name: "ai-systems-agent-and-tool-safety"
description: "AI and LLM systems: design agents and tool use safely: read versus write tools, least privilege, approval gates for irreversible actions, step, token, time and spend budgets, prompt-injection containment and output handling."
license: "MIT"
---

# AI systems: agent and tool safety

Sub-category: AI and LLM systems. Runtime guardrail engineering and red-teaming belong to the AI Guardrails Engineer and security personas; this skill sets the architecture they enforce.

## 1. Inventory tools by effect
| Tool | Read or write | Reversible? | External effect? | Data it can reach | Approval |
|---|---|---|---|---|---|
Read tools perceive; write tools act. Irreversible or external writes (payments, refunds, emails, deletes, production changes) need the strongest controls.

## 2. Least privilege and controlled autonomy
- Give the agent only the tools and scopes the task needs; per-user delegated credentials rather than a super-user service account; separate read and write credentials.
- Enforce permissions in the tool layer, not in the prompt; the model can be talked out of instructions.
- Human approval gates for irreversible or high-impact writes unless the user has granted standing approval for that class of action; show the exact action and parameters for approval.
- Dry-run and preview modes; idempotency keys on write tools so retries do not repeat effects.

## 3. Budgets and stop conditions
Maximum steps, tokens, wall-clock time and spend per task and per user per day; loop detection (same tool and arguments repeated); clear failure states returned to the user. Unbounded consumption is a cost and availability risk.

## 4. Prompt injection and untrusted content
Anything retrieved, browsed, emailed, uploaded or returned by a tool is data, not instructions. Contain the blast radius: an agent that has read untrusted content should not hold powerful write tools in the same step without approval; keep secrets out of prompts (system prompts leak); validate model output before passing it to interpreters, SQL, shells, browsers or other systems (improper output handling).

## 5. Observability and accountability
Log every plan, tool call, argument, result and approval with ids; traces per task; alerts on unusual tool use; a kill switch to disable a tool or the agent.

## 6. Risk checklist
Map each relevant OWASP LLM risk and NIST GenAI risk (confabulation, information security, data privacy, human-AI configuration, value chain) to a control, its location and how it is tested.

## Output
Tool inventory with approvals, permission model, budgets and stop rules, injection containment, output validation, logging and kill switch, risk-to-control table.

## Pitfalls
- One powerful tool account shared by all users.
- "The prompt tells it not to" as a control.
- Agents that can both read untrusted email and send payments without a gate.
