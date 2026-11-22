---
name: "port-plan-and-decision-records"
description: "Plan the port as ordered units with decision records and a glossary; pieces that import each other move together, and the plan survives across sessions."
license: "MIT"
---
# Port Plan and Decision Records

## Use when
- The port is bigger than one function: a module, a service, a whole app.
- Sessions will hand the porting work between each other.
- Decisions about scope and mapping keep being re-litigated.

## Instructions

1. Plan units before porting: list the units in port order with the risk
   notes at file:line precision, the bridge each unit needs, and how each
   external dependency maps to a Rust crate (full fit, partial fit, none).
2. Move pieces, not scattered files: units that import each other move
   together in one wave; splitting an import cycle across waves doubles the
   bridge surface for nothing.
3. Number every decision the port depends on, each with a recommended
   answer, and settle them with the owner BEFORE the port bakes them in.
4. Record settled decisions as ADRs in a DECISIONS file the port carries;
   record the original's term-to-Rust-name mapping in a glossary so naming
   stays consistent across every unit.
5. Keep a unit map with states (unported / in-progress / gated / lifted);
   a session claims one unit before starting and leaves a handoff note for
   the next session — the plan, not anyone's memory, carries the port.
6. Cutover steps only a human can do (deploys, DNS, secrets) are scripted
   into one interactive script with a way back at each step; the port agent
   writes the script, the owner runs it.

## Stop conditions
- Never port a unit whose decisions are unsettled.
- Never split an import-connected piece across waves.
- Never rely on session memory for port state.

## Escalation
- Dependencies with no Rust crate, or a partial one, go to the owner with
  options (keep behind the bridge, replace, wrap) — the mapping table drives
  the conversation.
