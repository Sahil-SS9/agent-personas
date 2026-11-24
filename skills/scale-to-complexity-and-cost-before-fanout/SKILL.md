---
name: "scale-to-complexity-and-cost-before-fanout"
description: "START HERE for any multi-agent, delegation or orchestration plan: decide whether to use sub-agents at all and how many, from task complexity, parallelism, budget and cost, before splitting the work."
license: "MIT"
---

# Scale to complexity and cost before fan-out

Step 1. Multi-agent work spends many times the tokens of a single agent. Fan out only where the work is genuinely parallel or exceeds one context.

## Use when
- A new goal arrives, before any decomposition or dispatch.

## DO NOT use when
- The owner has fixed the team size; record it and go to step 2.

Follow the persona hard rules: read the goal, roster, limits, policy and every given file first; plan before dispatching; every worker gets a fresh, complete brief; a worker's own "done" is not done; never exceed the agent budget or a worker's context; record every decision.

## Procedure
1. **Classify the goal:**
   - simple lookup or single-file change -> one agent, few tool calls;
   - comparison or a few independent parts -> 2-4 workers;
   - broad research or many independent parts -> more workers, each with a clearly divided responsibility.
2. **Check the three reasons to fan out:** independent parallel parts; information larger than one context window; specialised tools or skills one agent lacks. If none applies, use one agent.
3. **Check the reasons not to:** parts that need shared context or tight back-and-forth (most coding), and a value too low to pay for several times the tokens.
4. **Pick the smallest team that meets the deadline and limits.** Never exceed the agent budget. More agents add coordination failures; keeping task-critical information intact matters more than adding agents.
5. **Write the decision:** class, team size, reason, expected cost.

## Worked example
"Summarise the three ADRs in docs/adr/ into a one-page note." Three short files fit one context; nothing needs a specialist. One agent. A roster of seven specialists and a budget of five do not change that.

## Checklist
- [ ] Goal classified
- [ ] Reasons for and against fan-out checked
- [ ] Smallest sufficient team within budget
- [ ] Decision recorded with expected cost

## Output
Team size and the reason.

## Avoid
- One worker per task by default.
- Fanning out tightly coupled coding work.
