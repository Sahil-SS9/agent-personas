---
name: "offensive-scope-discipline"
description: "Enforce scope, evidence-handling and legal boundaries through the whole engagement."
license: "MIT"
---

# Offensive scope discipline

## When to use
Continuously, throughout any authorised offensive engagement.

## Procedure
1. Written authorisation before any contact: what, where, when, how, who to call. Store it; refer to it on every scope question.
2. Explicit out-of-bounds list: no data destruction, no service degradation, no persistence without written approval, no third-party systems.
3. Handle discovered data under evidence discipline: minimal access, documented handling, immediate escalation for sensitive/third-party exposure.
4. Time-box and check-point: log every action with timestamps; keep the working record re-buildable.
5. Stop conditions: real third-party compromise, unexpected production impact, or out-of-scope access = stop, contain, escalate.

## Decision rules
- Ambiguity resolves conservative: if it might be out of scope, it is out of scope until clarified in writing.
- Curiosity is not authorisation. The most damaging temptation is the interesting finding just past the boundary.
- Engagement artefacts (tools, payloads, notes) are inventoried and cleaned up; nothing is left behind.

## Pitfalls
- Scope creep through chained systems.
- Operating without a current escalation contact.

## Done
Engagement with authorisation on file, working log, inventoried artefacts, and zero out-of-bounds actions.