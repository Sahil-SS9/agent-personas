---
name: "agent-artifact-attribution-and-scratch-routing"
description: "Attribute debris to the agent session that created it — with evidence — and route future agent scratch output to a home that will not accumulate."
license: "MIT"
---

# Agent artifact attribution and scratch routing

## When to use
Files appear that no human remembers making, especially outside the project tree.

## Procedure
1. Match creation time against session logs, transcript timestamps and process records.
2. Inspect content for identifiers: session ids, task ids, tool names, model names, temp-path patterns.
3. Check for the scratch conventions of the agent runtime in use.
4. Attribute with evidence; where evidence is absent, mark UNATTRIBUTED and keep it.
5. Propose the routing change: a declared scratch location with a retention policy, so the same debris stops appearing.

## Decision rules
- Attribution requires evidence. Plausible is not attributed; it is UNATTRIBUTED.
- Never delete a file merely because it looks agent-generated.
- Fixing the source beats sweeping the symptom: a cleanup that does not route future output will be repeated forever.
- Record the session id where known, so the producing run can be inspected.

## Pitfalls
- Guessing the creator from the file's name or extension.
- Cleaning the symptom while leaving agents writing to the project root.
- Attributing a human's file to an agent and deleting it.

## Done
Items are attributed with evidence or marked UNATTRIBUTED, and a routing change is proposed that prevents recurrence.
