---
name: h3-prompting
description: "Use when working on h3 prompting tasks."
version: 1.0.0
license: MIT
---
# Prompting MiniMax Hailuo H3

H3 does not read prompts as description. It reads them as a **production plan in a defined schema**
that its own prompt-compiler stage emits. Write in that schema and the model is precise. Write
around it — in free prose, in cinematography jargon, in mood adjectives — and it becomes erratic in
ways that look like model weakness but are format mismatch.

This package is vendor-neutral Markdown. Any agent or person can read it. Everything carries a
provenance tag: `[OFFICIAL]`, `[OBSERVED]`, `[INFERRED]`, `[ASSERTED]`. Read
`references/08-evidence-and-sources.md` before treating anything here as settled — the model was
about twelve days public when this was compiled.

---

## Step 1 — Identify the mode. The mode picks the schema.

| You are supplying | Mode | Schema |
|---|---|---|
| Text only | T2VA | three-field |
| A first frame | I2VA | three-field + alignment line |
| A first and a last frame | FL2VA | three-field + alignment line |
| A last frame only | L2VA | three-field + alignment line |
| Reference images / video / audio (identity, location, style, voice) | Ref2VA — full-reference | **six-field** |

Getting this wrong is the most common structural failure. The two schemas share no fields.

**Three-field schema**, in this order:

```
integrated_multimodal_description:
overall_soundscape:
non_diegetic_music:
```

**Six-field schema**, in this order:

```
subject_definitions:
summary:
retention_analysis:
detailed_description:
overall_soundscape:
non_diegetic_music:
```

Exact spelling, exact order, no substitutions, nothing omitted. Full syntax in
`references/01-schema-and-syntax.md`.

---

## Step 2 — Set the budget before writing a word

This is where most prompts go wrong, and it goes wrong in the direction of *more*.

| | Three-field modes | Ref2VA |
|---|---|---|
| Main description field | ~100 words median, 133 max observed | 350–500 words `[OFFICIAL]`, 389 max observed |
| Whole prompt | ~1,000 chars median | ~3,300 chars median, 4,169 max observed |

**Across 39 worked examples, nothing exceeds 389 words or 4,169 characters, and nothing uses more
than two shots.** Cuts land at 40–67% of runtime, never before 3.0 seconds.

Read those numbers as *what published working prompts look like*, not as a limit the model enforces.
The hosted service is reported to have a hard input cap and will refuse a long prompt outright. The
local open weights enforce nothing: a 30,000-character prompt has generated successfully, and long
local prompts are reported to degrade adherence rather than to be ignored. **Locally, length is a
gradient, not a gate** — going long is a bet on diminishing control, not a formatting error, and
nobody has run the comparison that would locate a threshold.

Shot budget by duration `[INFERRED from the corpus]`:

| Duration | Shots |
|---|---|
| ≤5 s | 1 |
| 6–7 s | 1, occasionally 2 |
| 8–15 s | 1 or 2 |

If you are writing a fourth shot into a fifteen-second clip, you are outside everything that has
been shown to work. The cost is not just crowding: short shots read as social-media grammar, and
`[Shot N]` markers force cuts you may not want.

**Over-long prompts are reported to silently degrade Ref2VA toward text-to-video** — the references
stop taking effect while everything still appears to run. Two independent reporters, uncontrolled.
If references seem to be ignored, cut length before you reword anything.
`references/05-length-and-structure.md` sets out both sides of the length argument, including the
evidence that non-conflicting length may cost nothing.

---

## Step 3 — Write it

Work in this order. Each step answers a question the next one depends on.

1. **Roles before action.** In Ref2VA, define every attached asset in `subject_definitions` and say
   what job it does. A reference that is not named in the prompt text is ignored — the slots are
   inert on their own.
2. **The opening frame.** T2VA has nothing to establish the scene; say what is in frame before
   anything moves. Image modes must describe only what *changes*, never re-describe the supplied
   frame.
3. **Action as a chronological chain.** Not "she runs" but weight, then coat, then the rail. Use
   *first / then / as / finally*. **Name the terminal event** — multi-stage actions stall before
   their end unless the end is written.
4. **Physical consequence, stated.** "Realistic water" is a wish. "The boot displaces water outward
   in a circular splash, droplets falling back onto the pavement" is an instruction.
5. **One camera path per shot**, from the closed vocabulary only:
   `Zoom In/Out`, `Push In/Pull Out`, `Pan`, `Truck`, `Tilt`, `Pedestal`, `Arc Shot`,
   `Tracking Shot`, `Static Shot`, `Shake`, `POV`, `Roll` — plus `with small/large amplitude` and
   `at slow/fast speed`. Written as prose inside the shot, never as bracketed tags. Terms outside
   this list (dolly, crane, handheld, locked-off, focal lengths, over-the-shoulder) have no defined
   handling — express the intent as framing plus a supported term.
   `references/02-camera-and-motion.md`.
6. **Audio, all three layers.** Dialogue and shot-synced events in the description field; ambience
   in `overall_soundscape`; audience-only score in `non_diegetic_music`.
7. **End state.** Say where things finish and what remains visible, in positive terms.

---

## The non-negotiables

Short list. Each of these breaks a generation on its own.

**No quotation marks inside `<d>` tags.** Quotes tell the model to render text *in the picture* —
you get burned-in subtitles. Write `(S1) says, <d>[English] Could you keep it down?</d>`, never
`She says, "Could you keep it down?"`. Best-evidenced rule in the corpus.

**Address silence explicitly.** H3 invents gibberish speech when speech is not mentioned at all —
the most-reported failure of all, ~15 independent reporters. If nobody talks, write that nobody
talks. And prefer an affirmative sentence of silence over `N/A` in the audio fields; the bare
marker has itself been reported to provoke invented audio.

**`[Shot N]` is a cut.** Adding a shot marker forces a camera change. For one continuous take, use
a single `[Shot 1]` and place time beats inside it. If you want a cut you must accept a full angle
change; if you want a size change only, use camera motion instead.

**Every reference needs a stated job.** Unnamed references are ignored. And do not re-describe in
the shot body what a reference already supplies.

**Open with the medium.** `[Shot 1] Live-action, cinematic, ...` — naming the medium in the first
clause is `[OBSERVED]` to fix several drift problems, including unrequested slow motion.

**Camera off the travel axis.** Movement toward or away from the camera is foreshortened to nothing,
so the model substitutes whatever motion *is* visible from that position — often the wrong one.
Either move the camera off the axis or state the visible consequence.

**Actions leak between shots.** An action described anywhere tends to migrate into shots that did
not ask for it. Exclude it explicitly where it must not happen.

**Instruction beats prohibition.** Prohibition lists are ignored. State the desired end state
positively; use a targeted negation only alongside the positive form, never instead of it. Note
honestly: nobody has measured how H3 handles negation — see the health warning.

---

## Step 4 — Diagnose

When a generation comes back wrong, go to `references/07-failure-modes.md` and use the symptom
router at the top. It maps plain-language symptoms — "it cut to another angle I didn't ask for",
"the small character looks pasted in", "there is speech I never wrote" — onto 123 catalogued
entries with causes and fixes.

Two diagnostic habits that save the most time:

**Change one thing per run.** H3 is sensitive enough that two simultaneous edits tell you nothing.

**Check whether it is a prompt problem at all.** Several widely-reported "prompt failures" are
runtime bugs — most notably a case where attaching any reference silently overwrites keyframes.
The appendix to the failure catalogue lists the known ones.

---

## Pre-flight checklist

- [ ] Correct schema for the mode; fields in exact order, none missing or renamed
- [ ] Alignment line present and exact for I2VA / FL2VA / L2VA; absent for T2VA and Ref2VA
- [ ] Shot count within budget; no `[Shot N]` you did not intend as a cut
- [ ] `[Shot 1]` carries no timestamp; later cuts strictly increasing, none before 3.0 s
- [ ] Main description field within the word budget for the mode
- [ ] Every reference has a stated role; nothing re-described that a reference supplies
- [ ] Retention markers from the closed sets only; no `(Sx)` in `retention_analysis`
- [ ] Camera terms from the closed vocabulary; one path per shot; written as prose
- [ ] No quotation marks inside `<d>`; on-screen text in quotes only where it should be rendered
- [ ] Speaker IDs assigned in order of vocal events and stable across shots
- [ ] Speech addressed — written, or explicitly absent
- [ ] Both audio fields filled affirmatively; no bare `N/A`
- [ ] Dialogue timed aloud against the shot it sits in
- [ ] Terminal events named for every multi-stage action
- [ ] End state specified

---

## Files

| File | Open it when |
|---|---|
| `references/01-schema-and-syntax.md` | Writing the prompt skeleton; checking a tag or marker |
| `references/02-camera-and-motion.md` | Specifying camera or physical motion |
| `references/03-reference-inputs.md` | Working with reference images, video, audio, character sheets |
| `references/04-audio-and-dialogue.md` | Anything with speech, sound or music |
| `references/05-length-and-structure.md` | Deciding how long, how many shots, what to cut |
| `references/06-worked-examples.md` | You want a specimen to copy, or the skeleton templates |
| `references/07-failure-modes.md` | Something came back wrong |
| `references/08-evidence-and-sources.md` | Deciding how much to trust a claim; extending the package |
| `references/09-video-style-transfer.md` | Using a video reference as a style, motion or performance source |
