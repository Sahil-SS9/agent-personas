# 09 — Video References for Style and Motion Transfer

How to use a **video** reference as a style, motion, performance, editing-rhythm or
material-technique prior in a MiniMax Hailuo H3 Full-Reference (`ref2va`) prompt, while keeping
your own subject, action, setting and story under prompt control.

This file assumes `03-reference-inputs.md`. That file covers input caps, the four label types,
the one-label rule, the "an uncited reference is an ignored reference" rule, character sheets,
and the retention-marker enum. None of it is repeated here.

**Provenance markers used in this file**

| Marker | Meaning |
|---|---|
| `[OFFICIAL]` | Stated in MiniMax's own prompt-writing guides (`VIDEO_PROMPT_WRITING_GUIDE_ref_en`), the model card, or the hosted API docs. |
| `[OBSERVED]` | Someone ran it and reported the result. Reporter and date given where they exist. |
| `[INFERRED]` | Derived from official structure, or measured across a corpus of working prompts. Nobody tested that violating it degrades output. |
| `[ASSERTED]` | Stated as fact with no evidence of any kind. Taste in the register of a specification. |

---

## 0. READ THIS FIRST — what the source evidence actually is

Almost everything in this file that is not label syntax comes from **one community kit's
style-transfer chapter**: a single-author compilation, undated as to its runs, describing tests
the author ran on themselves.

That chapter calls itself "Empirical", and its evidence section opens:

> "Controlled H3 Ref2VA tests across sparse line animation, graphic black/white animation,
> painterly animation, wet oil-paint-on-glass references, and acting references showed the
> following tendencies."

**It is not a controlled test.** The chapter reports:

| Reported | Present? |
|---|---|
| Sample size (n) | No |
| Number of seeds per condition | No |
| Control condition | No |
| Blind or third-party evaluation | No |
| Scoring scale | No |
| Observer name | No |
| Dates | No |
| Any inspectable output | No |

Five reference *categories* are named. Nothing else is quantified. Everything derived from that
chapter is graded `[OBSERVED]` here — **n unknown, single author, self-rated, unrepeated** — and
never higher, regardless of how confidently the source states it. Its taxonomies (the five
analysis families, the role patterns, the decision tree) have no test behind them at all and are
graded `[ASSERTED]`.

The kit's own closing rule is the honest part, and it is worth carrying forward verbatim
`[ASSERTED]` (self-imposed hygiene, not a finding):

- describe these as practical tendencies, not guarantees;
- do not claim H3 has an internal "style embedding" or IP-Adapter mechanism;
- use "adapter-like" only as an analogy;
- never claim exact cadence, redraw frequency, or physical production behaviour without
  inspecting the output.

---

## 1. The central principle — the reference controls HOW, the prompt controls WHAT

> **The video reference supplies the animation language. The prompt supplies the content that
> language is applied to.**

`[ASSERTED]` as a principle. `[OFFICIAL]` as a mechanism — the official label semantics already
force this split, because a video you are only borrowing a look or a movement from is a
`<Subject N>` *sourced from* `<Video N>`, not a `<Video N>` in its own right.

### What it means operationally

The split is not a mood. It is a division of the prompt into two territories, and every
sentence you write belongs to exactly one of them.

| Territory | Owned by | Contains |
|---|---|---|
| **HOW** | the reference, declared as `<Subject N>` sourced from `<Video N>` | Line behaviour, palette relationships, fill density, texture, graphic density, background treatment, pose rhythm, holds, anticipation, deformation, overshoot, follow-through, acting hierarchy |
| **WHAT** | the prompt text | Subject, identity, anatomy, costume, props, setting, composition, action, dialogue, story, camera (unless explicitly delegated) |

Four operational consequences `[INFERRED]` (from the official one-label and role-scoping rules):

1. **The video does not get a free-standing `<Video N>` entry just for being a video.** It gets
   one only if a *whole-video* relationship is genuinely in play — cuts, rhythm, camera path,
   temporal structure, continuation, editing. `[OFFICIAL]`
2. **Every HOW attribute you want must be named.** The reference is not scanned for you. State
   the specific surface and motion traits you are asking to carry across.
3. **Every WHAT attribute must be stated positively in the description body**, or the reference's
   own content is the only candidate the model has. This is the firewall's other half (§5).
4. **Do not describe both territories twice.** Re-describing what the reference already supplies
   is one of the documented ways to overload a reference prompt — see `03-reference-inputs.md`
   §7.3 and §4 on silent text-to-video fallback.

The task type is `reference generation` unless the source video is genuinely being edited or
continued. Presence of a video does not create a `video editing` task. `[OFFICIAL]`

---

## 2. The transfer hierarchy

### 2.1 Read the shape of this claim before reading the claim

The source does **not** publish a ranked ordering. It publishes **two unordered buckets** —
"Relatively strong transfer" and "Weaker or high-variance transfer" — as bullet lists, in the
order reproduced below. Any impression of a graded ranking within a bucket is an artefact of list
order, not a measurement. The source itself closes the section with: *"Treat these as model
tendencies, not guarantees."*

All of §2.2 and §2.3: `[OBSERVED]` — n unknown, single author, self-rated, uncontrolled.

### 2.2 Reported as transferring relatively well

In the source's own order:

| # | Property | Family |
|---|---|---|
| 1 | Broad palette and colour-density logic | Visual surface |
| 2 | Graphic density and shape simplification | Visual surface |
| 3 | Sparse versus dense rendering | Visual surface |
| 4 | High-contrast black/white mass relationships | Visual surface |
| 5 | Pose rhythm and readable holds | Motion grammar |
| 6 | Anticipation, acceleration, overshoot, follow-through, recovery | Motion grammar |
| 7 | Expressive transitional deformation, smear-like poses | Motion grammar |
| 8 | Nuanced acting hierarchy — **only when explicitly reinforced** | Acting grammar |
| 9 | Cut rhythm and shot-scale contrast — **only when explicitly described** | Temporal grammar |
| 10 | Graphic object-motion organisation | Motion grammar |

Note items 8 and 9. The source attaches an explicit condition to each: they transfer *when you
write them out*, not when you leave them to the reference. That is a meaningful demotion — those
two are closer to "the prompt can achieve this and the reference does not fight it" than to
"the reference transfers this".

### 2.3 Reported as weak or high-variance

In the source's own order:

| # | Property | Family |
|---|---|---|
| 1 | Exact frame-by-frame redraw cadence | Material process |
| 2 | Literal line-boil frequency during held poses | Material process |
| 3 | Exact exposure patterns | Temporal grammar |
| 4 | Physical wet-paint redistribution | Material process |
| 5 | Exact charcoal erase/rebuild or similar destructive process | Material process |
| 6 | Exact source editing rhythm when the prompt only says "let the reference decide" | Temporal grammar |
| 7 | Material-process fidelity under complex anatomy, props, dialogue, environments | Material process |

### 2.4 The one usable generalisation

`[INFERRED]` from the bucket contents: the boundary is not "visual versus temporal". It is
**abstract relationships versus exact reproduction of a physical production process**. Palette
relationships, density relationships and timing relationships cross. Frame-exact cadence,
redraw frequency, exposure patterns, and destructive material mechanics do not reliably cross.

### 2.5 Corroboration and contradiction from the wider corpus

| Point | Independent evidence |
|---|---|
| Motion from video is approximate, not frame-exact | `[OBSERVED]` — BNP4535353, 2026-08-10, reading the official guidance: motion copying supplies *"approximate trajectories"* and *"is not a universal solution"*. Kijai (implementer): *"more a reference than controlnet"*. Consistent with the source's item 2.3/1. |
| **Disputed** | `[OBSERVED]` — Ryko, 2026-08-06, reports video motion reference working exactly. Unreconciled. |
| Line boil is genuinely hard to control | `[OBSERVED]` positive for rough line boil (The Shadow); `[ASSERTED]` for the surrounding claims. See `07-failure-modes.md` MOT-15. |
| A style reference imports composition and identity unless scoped | `[INFERRED]` — `07-failure-modes.md` LOOK-03, derived from the official role-separation requirement. Motivates §5. |

---

## 3. The five analysis categories

`[ASSERTED]` in full. This is a taxonomy for classifying a reference before you write. No test
supports the division, and no test supports the claim that classifying improves output. It is
useful because it forces you to name what you want, which the "uncited reference is ignored" rule
`[OBSERVED]` says you must do anyway.

| Family | What it is | Look for | You want this when |
|---|---|---|---|
| **A. Visual surface** | How each frame is rendered, independent of time | Line thickness, roughness, boil, redraw instability; flat vs modelled shapes; palette relationships and saturation; negative space; fill density; pigment/material texture; shadow and highlight treatment; background rendering density; edge softness, breakup, dissolution | A still frame of the reference already shows you the thing you want |
| **B. Motion grammar** | How a body or shape travels between poses | Held poses vs continuous interpolation; anticipation; acceleration/deceleration; pose spacing; arcs; squash/stretch; smear-like transitional drawings; overshoot; follow-through; secondary motion; recovery rhythm | Freezing the reference destroys what you liked; scrubbing it slowly keeps it |
| **C. Acting grammar** | How intention is staged through the body | Eyes leading head; head leading torso; thought pauses; expression timing; posture and balance changes; gesture economy; weight transfer; reaction hierarchy | The appeal survives redrawing the character in a different style |
| **D. Temporal / compositional grammar** | How shots are cut and framed against each other | Direct cuts; shot-length contrast; extreme scale changes; viewpoint changes; graphic reframing; repeated compositional motifs; action topology such as hold → anticipation → burst → landing → settle | The appeal disappears if you watch a single uncut shot in isolation |
| **E. Material process** | How the image is physically constructed, frame to frame | Continual redraw; wet paint pushed and repainted; charcoal erased/rebuilt; sand redistributed; clay resculpted; collage physically repositioned | You care about the *making*, not just the look |

### 3.1 The distinction that matters most

**Material appearance and material process are different targets.** `[ASSERTED]` as stated;
`[OBSERVED]` that the second is much harder (§2.3, items 1, 2, 4, 5, 7).

| Target | Phrasing | Difficulty |
|---|---|---|
| Surface style | *"looks like wet oil paint"* | Reported to transfer `[OBSERVED]` |
| Material process | *"each new state is physically rebuilt by redistributing wet paint"* | Reported high-variance `[OBSERVED]` |

Ask for the first unless the user specifically wants the second. Do not promise the second.

### 3.2 Complexity budget for material process

`[OBSERVED]` (same single source, described there as an "observed pattern"). Reported as a
monotone ladder of increasing difficulty:

```
simple abstract forms          → material transformation can show
recognisable objects           → object permanence starts fighting it
articulated human figures      → stable anatomy strongly fights it
+ detailed environments, props, dialogue, identity constraints → fidelity drops further
```

If material-process fidelity is the priority, the source's mitigations `[ASSERTED]`: reduce
simultaneous semantic demands; one subject, one causal action; locked or simple camera; choose an
action compatible with the transformation; drop unnecessary dialogue and environment detail;
explain the physical mechanism explicitly.

---

## 4. Reference-role patterns

All five patterns: `[ASSERTED]` as recipes. The label semantics they are built from:
`[OFFICIAL]`.

| Intent | `subject_definitions` shape | Retention markers |
|---|---|---|
| **Style only** | `<Subject 1>` sourced from `<Video 1>` controls line, palette, fill, texture, graphic density, background treatment, surface behaviour. No standalone `<Video 1>` entry. | `<Subject 1>: attribute_transfer` |
| **Motion / performance only** | `<Subject 1>` sourced from `<Video 1>` controls visible pose and performance traits. State explicitly that source rendering is *not* required. Keep `<Video 1>` only if whole-video timing is also in play. | `<Subject 1>: attribute_transfer` |
| **Style + motion** (the default reading of "animate this in the reference's style") | `<Subject 1>` sourced from `<Video 1>` controls visual surface **and** visible motion/performance grammar. Add a standalone `<Video 1>` only when whole-video rhythm, cuts or camera matter. | `<Subject 1>: attribute_transfer` (+ `<Video 1>` line if present) |
| **Editing / temporal structure** | Keep a standalone `<Video 1>` as the source for cut rhythm, shot-scale relationships, viewpoint contrast, temporal structure. | See §4.2 — the marker here is contested |
| **Material process** | `<Subject 1>` sourced from `<Video 1>`, plus an explicit description of the visible physical mechanism. Keep scene complexity conservative. | `<Subject 1>: attribute_transfer` |

### 4.1 Why `attribute_transfer` is the right marker for a style-only video reference

This is `[INFERRED]`, and it is derivable directly from the official marker definitions rather
than from anybody's testing. The source states it as policy with no argument `[ASSERTED]`; the
argument is:

| Marker | Official meaning | Fits a style-only video reference? |
|---|---|---|
| `fully_preserved` | The defined role is fully retained | **No.** You are not retaining the source video. Its subject, setting and action are all being discarded. |
| `partially_preserved` | The defined content **is** used, some defined traits change | **No.** The defined *content* is not used at all. Only an abstraction of it is. |
| `attribute_transfer` | A characteristic moves from one visible reference onto a **different identifiable target** | **Yes.** This is the exact description: a rendering characteristic moves off the source and onto your new subject. |
| `weak_reference` | Broad similarity only — style, category, composition, atmosphere | Only if you genuinely want loose influence. It under-claims a deliberate style transfer. |

All four definitions: `[OFFICIAL]`.

The practical consequence of getting this wrong is documented: leaving a style-carrying video on
`fully_preserved` is the source's stated cause of "correct motion, wrong subject" (§9). It tells
the model to keep the source's content, which is precisely what you are trying to shed.
`[ASSERTED]` as a diagnosis, `[INFERRED]` as marker logic.

Related official rule, worth restating because it removes a common anxiety: **newly added target
actions, backgrounds and plot events are not reference-fidelity losses.** `[OFFICIAL]` Retention
is role-relative. A style role stays intact even though everything visible in the frame is new.

### 4.2 An unresolved tension in the temporal-structure marker

The source's own skeleton writes:

```text
<Video 1>: attribute_transfer - transfer [only the whole-video temporal relationships actually used].
```

The **official guide's own example** for the same job writes:

```text
<Video 1> (cut and pacing structure): weak_reference - ...
```

`[OFFICIAL]` for the second. The two are not reconcilable from the definitions alone, and nobody
has tested which performs better. Default to the official example's `weak_reference` for pure
cut/pacing structure, and reserve `attribute_transfer` for cases where a concrete temporal
characteristic is genuinely being remapped onto identifiable new content. Flag the choice as
unsettled rather than defending it.

### 4.3 Explicit cut times beat delegation

`[OBSERVED]` (single source, n unknown): *"Explicit cut times in the target prompt are more
reliable than merely telling H3 to infer source editing rhythm."* Consistent with §2.3 item 6.
Write `[Shot 2] At 00:03.500, ...` rather than "match the reference's cutting".

### 4.4 Line format

Retention lines use **a hyphen with spaces**, not an em dash — 12 of 12 worked examples in the
corpus. `[INFERRED]` The source kit writes em dashes; do not copy that.

---

## 5. The content firewall

The problem: a style reference is a video of *something*, and that something has a face, a
costume, a set, and props. Without an explicit exclusion, that content is the most available
candidate for your scene.

`[INFERRED]` that the firewall is needed (`07-failure-modes.md` LOOK-03, from the official
role-separation requirement). `[OBSERVED]` that the negative-scoping *shape* works for other
attribute leaks — Grimm1111 and IrrationalSoup, 2026-08-09, converged on it independently for
image references and Grimm1111 reported reduced flicker. Nobody has tested it on a video style
reference specifically.

### 5.1 What to exclude

| Category | Items |
|---|---|
| Identity | Character identity, facial construction, body proportions, anatomy |
| Wardrobe | Hairstyle, costume |
| Objects | Props, product categories, logos, branding, packaging, vehicles |
| Space | Locations, background layouts |
| Framing | Exact compositions, exact poses |
| Performance content | Exact gestures, exact actions |
| Narrative | Dialogue, story events |

### 5.2 Copyable prompt language

The scoped definition line — this is the load-bearing sentence:

```text
<Subject 1> is the abstract animation style sourced from <Video 1>, including [specific non-identifying surface and performance traits]. It excludes source character identity, anatomy, clothing, props, branding, settings, exact compositions, exact poses, exact actions, dialogue, and story content.
```

The blunt restatement, for use in `detailed_description` when leakage is likely:

```text
Transfer HOW the reference is drawn and animated, not WHAT appears in it. The new subject, anatomy, clothing, props, setting, composition, action, dialogue, and story are controlled entirely by this prompt.
```

The image-reference fencing pattern, adapted — one line per reference `[OBSERVED]` for images,
`[INFERRED]` for video:

```text
<Video 1> provides animation language only. It does not provide subject identity, costume, props, background, location, composition, framing, action, or dialogue.
```

### 5.3 The other half of the firewall

**A firewall alone leaves a hole.** Exclusions tell the model what not to take; they do not tell
it what to render instead. State the target subject, setting and composition positively in the
description body so there is a candidate to fill the space. `[INFERRED]` — the same reasoning
`03-reference-inputs.md` §5.3 applies to reference backgrounds.

If character-design leakage still appears, add explicit user-defined identity anchors — compact
stature, round face, small nose, hair silhouette. `[ASSERTED]` The source attaches a caution
worth keeping: **do not over-specify rendering detail on the subject**, because heavy subject
styling competes with the style transfer you asked for. `[ASSERTED]`

---

## 6. Competing style vocabulary — and the contradiction you must know about

### 6.1 The source's rule

`[OBSERVED]` (single source, hedged with "sometimes", n unknown, no examples shown): naming a
medium in words while also supplying a style video *sometimes* pulled output toward a generic
learned style instead of the supplied reference.

Phrases the source names as risky when a style video is already attached:

```text
traditional cel animation
watercolor background
clean digital cartoon
cinematic painterly illustration
```

Its stated priority order `[ASSERTED]`:

1. reference role;
2. observable reference attributes;
3. only the minimum corrective language needed.

The mechanism it implies `[INFERRED]`: a named medium is a strong learned prior with its own
complete look attached. Supplied alongside a reference, you have two style sources describing the
same pixels, and the model has no way to know which wins. Both get diluted.

### 6.2 The contradiction

**Direct counter-evidence exists and points the other way.**

`[OBSERVED]` — DawnII, 2026-08-10, running a drift test: *"if I give it a picture of mona lisa,
over time it will drift to a more realistic version. If I instead prompt the mona lisa
specifically, it will keep the same style."* This is recorded in `03-reference-inputs.md` §8 as
the fix for the failure mode "style drifts toward photorealism over the clip", and the fix is
literally **name the style in words as well as by reference**.

| | Claim | Evidence |
|---|---|---|
| Source kit | Naming a style in words degrades a supplied style reference | `[OBSERVED]`, n unknown, unnamed author, no examples, hedged with "sometimes" |
| Corpus | Naming a style in words is what stops a supplied style reference drifting | `[OBSERVED]`, named observer, dated, described test, n=1 |

DawnII's reference was an **image**, not a video, which is the only material difference and is
not obviously load-bearing.

**Working position** `[INFERRED]`: the two are compatible if the variable is *conflict*, not
*presence*. Words that **describe what is visibly in the reference** reinforce it. Words that
**name a different medium than the reference shows** compete with it. Write the former, not the
latter. This reconciliation is untested by anyone.

---

## 7. Multi-reference strategy

`[ASSERTED]` for the pattern; `[OBSERVED]` for the corroborating corpus items cited.

**Role separation beats blending.** The source reports role-separated references behaving more
predictably than a vague "use all three for style" assignment. `[OBSERVED]`, n unknown.

```text
<Subject 1> from <Video 1> — surface, colour, line treatment
<Subject 2> from <Video 2> — visible performance and deformation
<Video 3>                  — whole-video cuts, composition, temporal structure
```

Use an equal broad blend **only** when the user explicitly wants a consensus style and the
references are compatible. `[ASSERTED]`

### 7.1 Style video plus identity images

The common real job: one style video, one or more identity images. Budget it first.

| Constraint | Value | Provenance |
|---|---|---|
| Reference video clips | up to 3 | `[OFFICIAL]` |
| Each clip | 2–15 s; total ≤ 15 s | `[OFFICIAL]` |
| Total mixed input files | 12 (this cap binds — see `03-reference-inputs.md` §1.1) | `[OFFICIAL]` for the number |

The shape:

```text
<Subject 1> is the woman whose face, hairstyle, and recognizable body identity come from <Picture 1>; her costume is newly specified by this prompt.
<Subject 2> is the abstract animation style sourced from <Video 1>, including [surface and performance traits]. It excludes source character identity, anatomy, clothing, props, settings, exact compositions, exact poses, exact actions, dialogue, and story content.
```

```text
<Subject 1>: fully_preserved - the defined identity and appearance are preserved.
<Subject 2>: attribute_transfer - the reference-derived visual and performance language is applied to <Subject 1> and to the newly specified scene.
```

Note `<Subject 1>` stays `fully_preserved`. An identity role is fully preserved even when
costume, pose, background and rendering all change. `[OFFICIAL]`

### 7.2 More references is not a fidelity dial

`[ASSERTED]` by the source: *"Never assume more references increase fidelity. Strong
multi-reference pressure can increase source-content leakage."*

Independently corroborated for the general case `[OBSERVED]`: Albert, 2026-08-09 — *"my ref faces
become distorted after generating no matter how many refs I put"*; KingGore2023 and Lodis on cost
scaling with reference count. `03-reference-inputs.md` §6 states the working guidance: **role
clarity beats reference count.**

### 7.3 Cross-check against the length ceiling

A firewall plus per-reference fencing plus explicit attribute reinforcement is a lot of text.
`03-reference-inputs.md` §4 documents reports of Full-Reference silently degrading to
text-to-video behaviour when a prompt gets over-stuffed, and the best-supported reconciliation is
that **density of non-conflicting instruction**, not raw length, is the variable. `[INFERRED]`
Write the firewall once, in `subject_definitions`. Do not restate it every shot.

---

## 8. Temporal correspondence

`[ASSERTED]` — no test reported, and the source presents it as craft.

When a reference has distinctive motion grammar, giving the *new* action an analogous **abstract
temporal topology** is claimed to improve transfer without copying content:

```text
held setup → small anticipation → sudden acceleration → extreme transitional state → clean landing → secondary settling
```

The target action may be completely unrelated to the source action. Preserve the relationships,
not the poses or the beats. Note the interaction with an unrelated `[OBSERVED]` finding in
`02-camera-and-motion.md` §7: multi-stage actions stall before their terminal event unless the
end state is named. If you write a topology, write its final state explicitly.

---

## 9. Failure diagnosis

All symptom/cause pairs `[ASSERTED]` unless a provenance column says otherwise. These are the
source's diagnoses of its own outputs, with no reported failure rates.

| Symptom | Diagnosis | Fix | Provenance |
|---|---|---|---|
| **Looks stylistically generic** — like a learned house style, not your reference | A named medium in the prompt is out-competing the reference | Remove competing named-medium language; make the video-derived `<Subject N>` the dominant style prior; reinforce the most visible surface traits | `[OBSERVED]` for the mechanism, n unknown — **and see §6.2, the corpus reports the opposite fix** |
| **Right look, wrong motion** | Motion grammar was never written out; only surface traits were | Add motion grammar explicitly (family B); match the reference's abstract action topology (§8); if cuts matter, write target cut times | `[ASSERTED]` |
| **Right motion, wrong subject** — the source's character or set has arrived | The firewall is missing, or the video is marked `fully_preserved` | Strengthen the content firewall (§5); state user-defined identity anchors; change the video's marker from `fully_preserved` to `attribute_transfer` unless literal source content is intended | `[INFERRED]` for the marker logic; `[OBSERVED]` for negative scoping working on image references (Grimm1111, IrrationalSoup, 2026-08-09) |
| **Looks handmade but has no actual redraw or material process** | Process fidelity is high-variance and you are trying to reach it with vocabulary | Stop adding synonyms; treat exact process as high variance; reduce semantic complexity if process fidelity is essential (§3.2) | `[OBSERVED]` for the difficulty, n unknown |
| **Multi-reference result drifts back toward looking like the sources** | Too many references, each with a vague role | Reduce reference count; give each reference one narrow role; exclude source subject/prop/location semantics explicitly | `[ASSERTED]`, corroborated in shape by `03-reference-inputs.md` §6.1 on cross-reference contamination `[OBSERVED]` |
| **The reference appears to do nothing at all** | Not a style-transfer failure | Check the reference is cited by name in the prompt, the input is enabled, and the reference checkpoint is loaded — `03-reference-inputs.md` §3 and §4.3 | `[OBSERVED]`, many independent reporters — the best-corroborated reference finding in the corpus |

Note the last row. Before diagnosing anything in this file, rule that one out. "Reference ignored
entirely" is the single most-reported reference failure and it has nothing to do with style.

---

## 10. Prompt skeleton

Copy and fill. Bracketed spans are yours to replace. The six-section structure and the
`summary` prefix syntax are `[OFFICIAL]`; the wording inside is the source kit's `[ASSERTED]`.

```text
subject_definitions:
<Subject 1> is the abstract animation style sourced from <Video 1>, including [specific non-identifying surface and performance traits you can actually see]. It excludes source character identity, anatomy, clothing, props, branding, settings, exact compositions, exact poses, exact actions, dialogue, and narrative content.
<Subject 2> is [the user's subject], whose [identity attributes] come from <Picture 1>.
<Video 1> is the whole-video temporal reference for [only if genuinely needed: pose rhythm, cut timing, camera path, shot-scale relationships].

summary:
[reference generation] The target video applies <Subject 1>'s abstract animation language to a new prompt-defined subject, action, and setting. [One or two sentences of the actual scene.]

retention_analysis:
<Subject 1>: attribute_transfer - the reference-derived [visual / performance] language is applied to the prompt-defined subject and scene, which remain independently controlled.
<Subject 2>: fully_preserved - the defined identity and appearance are preserved.
<Video 1> (cut and pacing structure): weak_reference - only the declared temporal relationships are referenced.

detailed_description:
[One or two sentences establishing overall style, referencing <Subject 1>.] Use <Subject 1> continuously as the dominant source for how the animation looks and performs; this prompt controls what is depicted. [Shot 1] [Composition, subject position, appearance, environment, lighting, action, state change, camera, current sound — written out. Reinforce only the reference attributes that matter, and only where they take effect.]

overall_soundscape:
[Ambience and physical sound.]

non_diegetic_music:
[Audience-only score, or an affirmative statement of its absence.]
```

Drop the `<Video 1>` line and its retention line entirely if no whole-video temporal relationship
is in play. An unused label is prompt weight with no job. `[INFERRED]`

Target the official `detailed_description` band of 350–500 English words. `[OFFICIAL]`

---

## 11. Open questions

These are genuinely open. None has been tested by anybody whose work is visible here.

| Question | Why it matters | What would settle it |
|---|---|---|
| Does naming a style in words help or hurt when a style **video** is attached? | §6 gives a rule and §6.2 gives a named, dated counter-observation for images. The entire "competing vocabulary" section rests on the unresolved answer. | Matched pairs, same video reference and seed: reference-only vs reference + congruent medium name vs reference + incongruent medium name. Score style adherence blind, n ≥ 10. |
| Is the transfer hierarchy in §2 real, or is it one author's five reference clips? | Six of this file's sections are downstream of it. | Re-run the five categories with n ≥ 5 seeds each, a control prompt with no reference, and third-party blind rating. |
| `attribute_transfer` or `weak_reference` for cut and pacing structure? | The source kit and the official example disagree (§4.2). | Same reference, same scene, same seed, both markers. Compare cut timing against the source. |
| Does the content firewall actually reduce leakage from a **video** reference? | The negative-scoping evidence is entirely from image references. The video case is assumed, not shown. | Matched pairs with and without the exclusion clause. Count frames containing source-derived props, sets or character features. |
| Does explicit cut timing really beat delegating rhythm to the reference? | §4.3 is a bare assertion with a plausible mechanism and no numbers. | Same reference, explicit `[Shot N] At MM:SS.mmm` vs "match the reference's cutting". Measure cut-point error. |
| Is the material-process complexity ladder (§3.2) monotone, and where does it break? | It is the only quantitative-shaped claim in the source, and it has no quantities. | Fixed material reference; vary scene complexity across the five stated rungs; score visible process retention. |
| Does a style `<Subject N>` derived from a video behave differently from one derived from an image? | Determines whether this file needs to exist separately from `03-reference-inputs.md` at all. | Same style, supplied once as a still and once as a clip. Compare adherence and drift over clip length. |
