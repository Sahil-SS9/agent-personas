---
name: devradio-station-adapter
description: "Use when reviewing Hermes Dev Radio itself. Maps the generic radio-review skills to this station's data, rules and engine limits, read-only."
license: MIT
---

# Dev Radio station adapter

Point the generic radio-review skills at this one station: where its facts live, which rules already exist, and what its voice engine can do. Read-only throughout.

## Procedure
1. Work from a dated copy of the station database (`var/canon.db` in the station repo), opened read-only. Never write to the database, and never touch the repo checkout: another agent may be committing there.
2. Count what a listener can hear. In the `segments` table, status `rendered` means voiced and airable. `gated` is written but not yet voiced. `blocked` and `purged` are not airable. Each row has `kind`, `programme`, `duration_s` and an `ir` JSON whose `lines` carry `speaker`, `text` and `tags`.
3. Review against the cast and the clock: `config/cast.yaml` (five fictional hosts, each with a role, running bits and a stock voice) and `config/programmes.yaml` (eight programmes: seven have a host pair and Night Shift has one host). Judge a line against the host who says it and a block against its programme.
4. Stay inside the rules the station already has. Hosts are fictional AI presenters. Stock voices only, never a real person's voice. No fake callers or guests. Fictional ads and skits only with the spoken fiction label. Hermes itself is never roasted. Every factual line cites its source. Transitions use the registered templates exactly. Variety comes from better writing and more registered templates, never from loosening the colour, fact-check, safety or redaction gates.
5. Respect the pause. The owner paused content production, voices, music and the bulk shelf on 27 October 2026 (decision D49). Check `STATUS.md` and `docs/decisions.md` for whether that still holds. Write findings as proposals for the owner, start no production and change no configuration.
6. Before recommending any change to how lines are delivered, read the engine sheet in `references/` for the engine in use, and ask only for what that sheet says it can do.

## Verification
Every count names the database copy and its date and uses only rendered rows. Findings name the host and the programme. No recommendation changes a gate, a voice rule or the pause. Nothing was written to the database or to the repo.

## Stop conditions
Stop and hand to the owner if asked to produce or publish content, change a gate, or touch another agent's checkout.

## References
- `references/engine-kokoro.md`
- `references/engine-expressive-generic.md`
