---
name: "session-librarian"
description: "Organize sessions by prompt: find, rename, archive, prune."
license: "MIT"
---
# Session Librarian

## When to use
Organize sessions by prompt: find, rename, archive, prune.

## Method
1. Use the chosen agent’s documented session search and export interfaces. Identify the exact session by metadata and content before acting.
2. Separate discovery, summarisation, renaming, archiving and deletion. A request to locate a conversation does not authorise removing it.
3. Preserve original transcript evidence and timestamps; label summaries as derived. Exclude secrets and unrelated personal content from exports.
4. Before bulk changes produce a dry-run list and seek approval for exact targets. Retain a recoverable backup where the platform supports one.
5. Read back the updated session metadata or exported artefact. Report unsupported operations instead of editing opaque runtime databases.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
