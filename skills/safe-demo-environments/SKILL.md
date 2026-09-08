---
name: "safe-demo-environments"
description: "Use when booting fake-data app demos for screenshots."
license: "MIT"
---
# Safe Demo Environments

## When to use
Use when booting fake-data app demos for screenshots.

## Method
1. Create a disposable demo configuration with explicitly synthetic data and no production credentials, customer records or live transaction endpoints.
2. Inspect the full connection path including browser code, proxies, callbacks and background jobs. A fake database alone does not isolate external side effects.
3. Bind locally by default and disable outbound messaging, payments and destructive actions. Use the real application UI rather than fabricated screenshots.
4. Verify readiness and exercise the main workflow. Capture meaningful states and report demo-only behaviour distinctly from production capability.
5. Track only resources started for this demo and stop those resources during cleanup. Do not open public tunnels or launch foreground applications without approval.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
