---
name: "skill-authoring"
description: "Write focused, portable skills with observable verification."
license: "MIT"
---
# Skill Authoring

## When to use
Write focused, portable skills with observable verification.

## Method
1. Check whether an existing skill already owns the workflow. Extend the smallest appropriate package rather than creating a duplicate role.
2. Write a precise trigger and a short ordered method that changes observable behaviour. Include required inputs, stop conditions, verification and common failure modes.
3. Keep core instructions portable and place supporting detail in relative references. Do not embed private infrastructure, credentials or automatic action authority.
4. Validate metadata, names, links and licence, then exercise representative positive and negative tasks. Distinguish generated instructions from verified improvement.
5. Version changes with source attribution and examples. Require explicit approval before replacing a live package or publishing externally. Source: https://agentskills.io/specification.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
