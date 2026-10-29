---
name: devradio-writer-adapter
description: "Use when writing scripts for Hermes Dev Radio itself. Private: maps the general writing skills to this station's script format, gates, cast and standing rules."
license: MIT
---

# Dev Radio writer adapter

Point the general writing skills at this one station: the shape a script must take, what its gates cut, and the rules it already has. Private to this station; the general skills stay free of its details.

## Procedure
1. Write to the station's draft format. A script is a list of lines, each with a speaker (host_a or host_b), text up to 1200 characters, source_event_ids and tags, and nothing else. At most 40 lines. A line with no source must be tagged banter, and a banter line inside an explainer fails the whole segment, so write no banter in explainers. Transitions are registered templates, not free prose.
2. Leave gate-owned tags alone. Do not set colour or unverified: the gate ignores a writer's copy.
3. Every line is a cited claim or colour, and a claim is never dressed up as colour. A line can never be colour if it carries a number, a code, path or link, a name the evidence does not contain, a universal claim such as "everyone" or "nobody", an answer to the question just asked, or more than 40 words. A model decides the rest. Colour runs longer than two lines are cut, only one colour line survives at the very end, and colour is capped by share of lines and of words. A segment with fewer than two cited claim lines is blocked.
4. Keep to the standing rules. Never roast Hermes (D4, D30). No fake callers or guests (D26). Stock voices only (K4). Every factual line cites its source (D27). Original fiction only with the spoken label (D48). Transitions use the registered templates (FR18.5).
5. The hosts are fictional AI presenters: no first-person history, and the cast file's banned phrases never appear.
6. Respect the pause. The owner paused content production, voices and music on 27 October 2026 (D49). Scripts are drafts for the owner: render nothing, change no configuration, and let cue changes wait for the owner.
7. Run the checks tool against a committed station revision, read-only. It covers only the rules a machine can see offline. The fact-check and safety checkers need a model and stay with the station.
8. Hand back the scripts, a list of every claim with its citation, and which brief items you acted on and which you could not. The Programme Director critiques; a human listens.

## Verification
Every factual line has a source id from the allowed set. The checks output is quoted with the station revision it ran against. Nothing was rendered, published or written to the station. No recommendation loosens a gate, a voice rule or the pause.

## Stop conditions
Stop and hand to the owner if asked to loosen a gate, add a caller or guest, roast Hermes, render or publish, or touch another agent's checkout.

## References
- `references/checks-tool.md`
