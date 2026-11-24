---
name: "goal-decomposition-and-specialist-routing"
description: "Use to build an orchestration or multi-agent plan: split the goal into a task graph, assign each task to a suitable agent from the roster, and respect dependencies, agent budget and context limits."
license: "MIT"
---

# Goal decomposition and specialist routing

Step 2. The plan is a graph, not a list: each task has dependencies, a capability it needs, a size, and an output others consume.

## Use when
- After step 1 decides the team size; whenever the goal or roster changes.

## DO NOT use when
- Executing an existing approved plan (task-board-orchestration / workstream-orchestration).

Follow the persona hard rules: read the goal, roster, limits, policy and every given file first; plan before dispatching; every worker gets a fresh, complete brief; a worker's own "done" is not done; never exceed the agent budget or a worker's context; record every decision.

## Procedure
1. **Build the task graph:** id, description, capability needed, size (tokens), output size, depends_on. Reject cycles; split a task that mixes capabilities.
2. **Route each task to a specialist whose capabilities include what it needs.** Put dependent tasks on the same agent when it fits: output that stays local needs no transfer.
3. **Respect the limits:** distinct agents <= budget; for every agent, the tokens of its tasks plus the output tokens of every input passed to it <= context limit. If no assignment fits, report which limit blocks it; do not silently break one.
4. **Declare every cross-agent transfer:** for each dependency edge whose ends sit on different agents, the consuming task lists the input with the FILE the producer writes. Never hand over chat history or transcripts; workers start fresh.
5. **Order into waves:** a task runs only in a wave after all its dependencies.
6. **Assign a verifier** to every task: a different agent from the producer (single-agent plans: a checkable done_check instead).
7. **Lint before launch:** `scripts/plan_lint.py --tasks tasks.json --plan plan.json --roster roster.json --limits limits.json` until it prints `[]`.

## Tools
`scripts/plan_lint.py`: lists missing/extra transfers, history hand-offs, wrong specialists, budget and context overflows, wave-order errors, cycles, empty brief fields, self-verification; exit 1 if any.

## Worked example
Goal: incident write-up from three log sources. Tasks: L1-L3 collect logs (research, 6k tokens, 2k out), T timeline (analysis, needs L1-L3), W write-up (writing, needs T), R review (needs W). Budget 4, context 20k. One researcher holds L1-L3 (18k); analyst T (5k + 6k inputs = 11k); writer W; reviewer R. Transfers: T <- L1, L2, L3 via out/L*.md; W <- T via out/timeline.md; R <- W. Waves: [L1, L2, L3], [T], [W], [R]. plan_lint: [].

## Checklist
- [ ] Graph built, acyclic, one capability per task
- [ ] Every task routed to a capable specialist
- [ ] Budget and per-agent context respected (or the blocking limit reported)
- [ ] Every cross-agent edge declared with a file; no history hand-offs
- [ ] Waves respect dependencies
- [ ] Verifier per task, not the producer
- [ ] plan_lint.py prints []

## Output
plan.json in the team's format, plus the lint result.

## Avoid
- Passing "the conversation so far" to a worker.
- Assuming an output reaches another agent without declaring it.
