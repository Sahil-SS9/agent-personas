---
name: "mcp-troubleshooting"
description: "Diagnose MCP startup, transport, discovery and execution failures."
license: "MIT"
---
# Mcp Troubleshooting

## When to use
Diagnose MCP startup, transport, discovery and execution failures.

## Method
1. Separate server process startup, transport connectivity, protocol negotiation, tool discovery, authentication and tool execution failures.
2. Capture the installed client/server versions and sanitized error output. For stdio check executable resolution, working directory and non-protocol output on stdout.
3. For HTTP transports inspect endpoint, status, session requirements, auth scope and timeouts using the current protocol documentation.
4. Test discovery before a harmless tool call. Compare advertised schema with the real call and response rather than treating process uptime as health.
5. Keep secrets out of logs, avoid unauthorised restarts and do not widen permissions to make a probe pass. Source: https://modelcontextprotocol.io/.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
