---
name: "mcp-spec-reference"
description: "Reference MCP 2025-06-18 basic protocol rules."
license: "MIT"
---
# Mcp Spec Reference

## When to use
Reference MCP 2025-06-18 basic protocol rules.

## Method
1. Pin the protocol revision and identify client/server capabilities before interpreting a message or transport behaviour.
2. Separate initialisation, capability negotiation, request/response correlation, notifications and lifecycle handling.
3. Validate tool schemas and result/error shapes against the selected revision. A transport connection alone does not prove protocol conformance.
4. Treat optional capabilities as negotiated, not universally available. Review authentication and server-initiated requests against the client’s actual policy.
5. Cite the relevant official section and report version-dependent uncertainty. Source: https://modelcontextprotocol.io/specification/.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
