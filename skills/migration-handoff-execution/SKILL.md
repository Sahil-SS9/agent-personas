---
name: "migration-handoff-execution"
description: "Execute migration handoffs with verified evidence safely."
license: "MIT"
---
# Migration Handoff Execution

## When to use
Execute migration handoffs with verified evidence safely.

## Method
1. Verify the handoff’s source revision, destination, acceptance criteria, known gaps and approved cutover scope before executing commands.
2. Inventory live dependencies and preserve a tested backup or rollback path. A copied directory is not proof that the destination runtime uses it.
3. Rehearse the migration against isolated data and test identity, data fidelity, error handling and compatibility at the real integration seams.
4. Execute only the approved phase and record actual commands and outcomes. Stop on unexpected destructive scope or unverifiable state.
5. Read back the destination, exercise the intended workflow and confirm the old route is handled as approved. Do not declare migration complete from file-transfer success alone.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
