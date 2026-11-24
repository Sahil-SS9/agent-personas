---
name: "shadow-rollout-and-cutover"
description: "Use when a proven Rust port is going to production or replacing the original: shadow-run both and compare live outputs, switch per unit behind a kill switch, then cut over and retire the original."
license: "MIT"
---

# Shadow rollout and cutover

Step 9. Tests prove the port on recorded inputs; production traffic confirms it.

## Use when
- After gate and benchmark verdict say ship.

## DO NOT use when
- The port is a throwaway or offline tool with no production callers.

Follow the persona hard rules: read the original and every given file before writing Rust; the original is the oracle; record its behaviour before porting; a mismatch is fixed in the port, never in the recording; return Err where the original fails, never panic; no network, std only unless the plan names a crate.

## Procedure
1. **Shadow mode:** callers keep getting the original's result; the Rust runs second on the same input; mismatches and Rust errors are logged, never returned. Mutated arguments: give each side its own copy.
2. **Watch the mismatch log** for a period the owner sets; each mismatch becomes a recorded case and a fix in the port.
3. **Switch per unit with a kill switch** (an environment variable or flag that sends the unit back to the original for one run or permanently).
4. **Cut over** when the mismatch log stays empty for the agreed period; keep the kill switch for one release.
5. **After upstream changes to the original** (before the original is retired): re-record, re-replay; new mismatches are upstream behaviour changes to port.
6. **Retire the original** only after the owner agrees; remove the bridge fallback and kill switch in a separate change.

## Worked example
A CLI's `parse_config` port ships in shadow for two weeks: 3 mismatches logged, all on configs with a UTF-8 BOM. Added a recorded case and fixed BOM handling; one more clean week; switched with `APP_PARSE_CONFIG=original` as the kill switch; removed the fallback one release later.

## Checklist
- [ ] Shadow mode returns the original's result; Rust errors never reach callers
- [ ] Mismatch log watched; each mismatch recorded and fixed
- [ ] Kill switch per unit
- [ ] Cutover after a clean period; fallback removed later

## Output
Rollout record: shadow period, mismatches and fixes, switch date, kill switch.

## Avoid
- Switching all callers at once with no way back.
