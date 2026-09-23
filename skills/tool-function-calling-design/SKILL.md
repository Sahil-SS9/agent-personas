---
name: "tool-function-calling-design"
description: "Design agent tools and function calling for reliable, bounded execution."
license: "MIT"
---

# Tool & Function-Calling Design

An agent is only as reliable as the tools you hand it.

## 1. Design tools like an API
- Clear names, typed params, and descriptions the model can actually reason about.
- One tool, one job; overloaded tools confuse selection.

## 2. Validate and bound
- Validate arguments before executing; never trust model-generated inputs blindly.
- Scope permissions per tool; destructive actions need explicit gates.

## 3. Handle failure in the loop
- Return structured, actionable errors the agent can recover from.
- Make tools idempotent where possible; bound retries and cost.

## Voice
Tools-as-contracts. Refuse handing an agent an unbounded, unvalidated destructive tool.
