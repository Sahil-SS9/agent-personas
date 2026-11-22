---
name: "recorded-behaviour-equivalence"
description: "Record the original's behaviour on generated edge cases and semantic traps; a port is done only when every recorded case replays identically."
license: "MIT"
---
# Recorded-Behaviour Equivalence

## Use when
- Porting or rewriting a unit whose behaviour must not change.
- "It passes the tests" is claimed as port completion.
- You need a definition of done that a port cannot talk its way past.

## Instructions

1. The original is the source of truth: run it on generated edge cases and
   on every semantic trap in every parameter, and save what it returns and
   throws as a replay file (one case per line). Edge generators cover:
   non-ASCII and emoji strings, -0, NaN, integers where floats are expected,
   empty and maximal inputs.
2. Trap coverage is per parameter: string length and case, signed division
   and modulo, overflow edges, float printing, map and sort order, missing
   inputs. A case file that never probed a parameter proves nothing about it.
3. Replay the cases against the port exactly the way the original's callers
   call it — same entry point, same argument shapes, bridge included.
4. Numeric code may declare a float tolerance up front (a relative share,
   chosen and recorded before replay); anything else must match exactly.
5. Ship path: run both original and port side by side in shadow mode —
   return the original's result, log mismatches, keep an old/new switch —
   until the replay is clean, then flip.
6. The recording is the proof and the limit: it only catches what it covers.
   Say what was not recorded; do not claim equivalence beyond the cases.

## Stop conditions
- Never accept a port with any unreplayed case.
- Never widen the tolerance after seeing a mismatch.
- Never mark a port done from unit tests alone when recorded cases exist.

## Escalation
- Mismatches that reveal original-behaviour bugs (the original itself is
  wrong) go to the owner: fix the original, re-record, or mark the divergence
  as a decision — never silently "improve" behaviour in the port.
