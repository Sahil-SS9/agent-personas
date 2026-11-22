---
name: "agent-bug-repro-and-fix-verification"
description: "Turn an agent finding into a fixed defect: minimal replayable case, one verified fix at the diagnosed seam, and a regression case that guards it."
license: "MIT"
---
# Agent Bug Repro and Fix Verification

## Use when
- A diagnosis exists and the fix is about to ship.
- The fix must be proven, not assumed.
- The same bug must never come back unnoticed.

## Instructions

1. Minimal case first: reduce the failing run to the smallest replay that
   still fails — same divergence, same failure class, fewest moving parts.
   A fix verified only on the full noisy run proves nothing specific.
2. State the fix's prediction before applying it: "with this change, the
   minimal case replays clean AND the divergence point moves / disappears".
   After the change, check both.
3. Verify at the diagnosed seam, then at the original scene: the minimal
   case first, then the FULL original failing run replayed end to end. A
   fix that handles the minimal case but regresses the full run is not a
   fix.
4. One fix per change: if the change touched two seams, the verification
   proves nothing — split it and verify each.
5. Add the regression case to the run suite: the minimal case, its expected
   behaviour, and a scorer — so the defect class is guarded forever, not
   until the next refactor.
6. Record the finding chain: classification → divergence evidence → seam →
   fix → replay results → regression case id. Anyone reviewing the fix
   later should see the whole chain, not just "fixed".

## Stop conditions
- Never fix without a replayable case.
- Never call a fix verified without the full original run replayed.
- Never ship a fix that lacks its regression case.

## Escalation
- Fixes that require touching another persona's ground (rail config, tool
  spec owned elsewhere) escalate with the case and the prediction — the
  owner persona applies it, the debugger verifies the replay.
