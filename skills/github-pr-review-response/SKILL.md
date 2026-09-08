---
name: "github-pr-review-response"
description: "Triage and respond to PR review comments on upstream repos."
license: "MIT"
---
# Github Pr Review Response

## When to use
Triage and respond to PR review comments on upstream repos.

## Method
1. Read the pull request, current branch and every unresolved review thread. Distinguish actionable defects, questions, preferences and obsolete comments.
2. Verify each finding against current code and trace the original requirement. Reproduce a suspected defect before changing implementation.
3. Make the smallest coherent correction with regression coverage; retain incompatible suggestions as explicit decisions rather than silently implementing both.
4. Respond with the actual fix or evidence-based explanation and link the relevant change. Do not mark a thread resolved before its request is addressed.
5. Check the final diff, tests and remote revision after an authorised push. Posting comments, resolving threads and merging require the appropriate user approval.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
