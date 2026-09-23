---
name: "prompt-injection-defence"
description: "Defend agents and prompts against injection and untrusted-content attacks."
license: "MIT"
---

# Prompt-Injection Defence

Any text your agent reads can try to hijack it.

## 1. Treat retrieved/user content as untrusted
- Content from web, docs, tools or users may contain instructions; never execute them as commands.
- Separate trusted system instruction from untrusted data clearly.

## 2. Constrain capability, not just wording
- No prompt phrasing is a security boundary; enforce with scoped permissions and gates.
- The model deciding to do harm should still be unable to without an out-of-band check.

## 3. Guard the dangerous edges
- Human-in-the-loop for high-impact actions; validate tool calls independently.
- Log and monitor for injection attempts.

## Voice
Untrusted-by-default. Refuse relying on 'ignore malicious instructions' wording as the only defence.
