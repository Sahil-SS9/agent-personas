---
name: "obsidian"
description: "Read, search, and create notes in the Obsidian vault."
license: "MIT"
---
# Obsidian

## When to use
Read, search, and create notes in the Obsidian vault.

## Method
1. Identify the authorised vault and its existing folders, templates and naming rules. Read related notes before creating a new one.
2. Preserve Markdown, frontmatter, internal links and attachments. Prefer a focused edit to rewriting an entire note.
3. For renames inspect backlinks and update only affected references. Do not delete notes merely because they look duplicated without checking context.
4. Keep private vault material out of public outputs. Handle sync conflicts explicitly rather than silently selecting one side.
5. Verify the saved file and local links. The host supplies filesystem access; this skill does not require a particular plugin or sync provider. Source: https://help.obsidian.md/.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
