---
name: "mcp-integration-engineering"
description: "Build and validate MCP/ACP integrations across protocol, logic and client layers."
license: "MIT"
---
# MCP Integration Engineering

## Use when
- Building or hardening an MCP server, connector or ACP integration
- An integration fails only in production or only with certain clients
- Preparing an agent-tool surface for external consumers

## Instructions

1. Treat the integration as THREE layers that fail differently: protocol
   (handshake, version negotiation, capability advertisement), server logic
   (schema drift, result shapes), client integration (config, auth, env).
   Test each layer with its own technique; most outages hide in the
   protocol layer because it is the least examined.
2. Pin the spec date you validated against (MCP revisions ship frequently)
   and re-verify on spec updates.
3. Four-layer test pyramid: in-memory unit tests on handlers -> contract
   tests for schema/protocol compliance -> full-stack integration with real
   protocol + MOCKED downstreams (never mock the SDK itself) -> acceptance
   scenarios from the LLM's perspective + production probes.
4. Validation floor before exposure: deterministic tool discovery across
   calls; every advertised tool matches its schema; unsafe inputs rejected
   before reaching backend; least-privilege auth; traceability from agent
   decision to connector call; experimental tools flagged off in production.

## Stop conditions
- Never expose a tool whose schema you have not contract-tested.
- Never claim protocol compliance without naming the spec revision tested.

## Escalation
- Protocol-layer regressions after upstream spec changes escalate to the
  platform owner with captured handshake traces attached.
