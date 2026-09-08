---
name: "mcp-client-setup"
description: "MCP client: connect servers, register tools (stdio/HTTP)."
license: "MIT"
---
# Mcp Client Setup

## When to use
MCP client: connect servers, register tools (stdio/HTTP).

## Method
1. Check whether the chosen agent supports the required MCP transport and protocol version. Read that client’s configuration documentation rather than copying another client’s schema.
2. Identify the server source, executable or endpoint, required permissions and credential handling. Treat a downloaded server as executable code requiring trust review.
3. Configure a minimal isolated client with only the intended server. Verify startup, capability negotiation, tools/list and one harmless schema-valid call.
4. For server-initiated requests confirm explicit client support and policy; do not infer sampling or elicitation permission from basic tool discovery.
5. Document the tested versions and rollback. Activate a live profile only with approval. Source: https://modelcontextprotocol.io/.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
