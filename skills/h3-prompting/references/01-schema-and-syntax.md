# H3 Prompting — Schema and Syntax Reference

Reference for writing prompts for the MiniMax Hailuo H3 video model. Everything here is
about the *text* of the prompt, not about workflow settings.

## Provenance markers

Every claim below carries one of these tags.

| Tag | Meaning |
|---|---|
| `[OFFICIAL]` | Stated in MiniMax's own prompt-writing guides (`VIDEO_PROMPT_WRITING_GUIDE_base_en.md`, `VIDEO_PROMPT_WRITING_GUIDE_ref_en.md`) or the model's own docs. |
| `[OBSERVED]` | Someone ran it and reported the result. Almost always single-author, single-seed, self-rated. |
| `[INFERRED]` | Derived from official structure or measured across a corpus of working prompts. Nobody tested that violating it degrades output. |
| `[ASSERTED]` | Stated as fact by community prompting kits with no evidence at all. Treat as suspect. |

Read `[ASSERTED]` as "someone's taste, written in the voice of a specification."

---

## 1. Mode names

| Label | Input | Schema |
|---|---|---|
| T2VA | text only | three-field |
| I2VA | first-frame image | three-field |
| FL2VA | first + last frame images | three-field |
| L2VA | last frame image only | three-field |
| Ref2VA (full-reference mode) | reference images / videos / audio | six-field |

`[OFFICIAL]` The base guide uses the labels T2VA / I2VA / FL2VA / L2VA.
`[OBSERVED]` Some runtime UIs display shorter labels (T2V, I2V, R2V) for the same modes.
`[INFERRED]` "Ref2VA" is a community shorthand; the official reference guide calls it
**Full-Reference Mode**. Either name is fine in conversation; neither appears inside the prompt.

---

## 2. The two schemas

### 2.1 Three-field schema — T2VA, I2VA, FL2VA, L2VA

`[OFFICIAL]` Exactly three fields, exactly these spellings, exactly this order:

```text
integrated_multimodal_description:
...

overall_soundscape:
...

non_diegetic_music:
...
```

1. `integrated_multimodal_description`
2. `overall_soundscape`
3. `non_diegetic_music`

`[OFFICIAL]` The field value goes on the **line after** the label. That is the form the
official template shows.

> **Honest note on this point.** Both the official base guide and community kits also
> print inline examples that read `integrated_multimodal_description: [Shot 1] ...` with the
> value on the same line as the label. `[OBSERVED]` The community kits are internally
> inconsistent about this — some example files use inline, others use newline, and both are
> presented as correct. `[INFERRED]` No test shows either form failing. Use the newline form
> because that is what the templates show; do not treat a same-line prompt as broken.

`[OFFICIAL]` Field content rules:

| Field | Contains | Length |
|---|---|---|
| `integrated_multimodal_description` | The shot timeline. Visuals, action, camera, dialogue and singing, diegetic music/media audio, sounds synchronised to specific visual events. | No stated limit |
| `overall_soundscape` | Ambience, physical action and object sounds, non-verbal human sounds. One paragraph. | 1–4 English sentences |
| `non_diegetic_music` | Audience-only score: instrumentation, tempo, rhythm, dynamic change. | 1–3 English sentences |

`[OFFICIAL]` `N/A` is the value for `overall_soundscape` only when total silence is explicitly
requested, and for `non_diegetic_music` whenever no audience-only score is intended.

`[OFFICIAL]` Do not repeat dialogue, singing, or diegetic music in `overall_soundscape`.
`[OFFICIAL]` Avoid abstract score descriptions such as "emotional music"; describe the actual
sound instead.

### 2.2 Six-field schema — Ref2VA / Full-Reference Mode

`[OFFICIAL]` Exactly six sections, exactly these spellings, exactly this order:

```text
subject_definitions:
...

summary:
...

retention_analysis:
...

detailed_description:
...

overall_soundscape:
...

non_diegetic_music:
...
```

1. `subject_definitions`
2. `summary`
3. `retention_analysis`
4. `detailed_description`
5. `overall_soundscape`
6. `non_diegetic_music`

`[OFFICIAL]` Value on the line after the label, same as above.

`[OFFICIAL]` The two schemas never mix. A Ref2VA prompt never contains
`integrated_multimodal_description`. A three-field prompt never contains
`subject_definitions` or `retention_analysis`.

`[OFFICIAL]` Ref2VA has **no** alignment-instruction line.

`[OFFICIAL]` `detailed_description` opens with one or two English sentences establishing overall
style, *before* `[Shot 1]`. Generation tasks normally run 350–500 English words.

`[OFFICIAL]` Section responsibilities:

| Section | Job |
|---|---|
| `subject_definitions` | One line per tracked item: its label, role, which attributes to follow, and provenance. |
| `summary` | One short paragraph, opening with the bracketed task-type prefix. No new labels introduced here. |
| `retention_analysis` | One line per label, giving its relationship marker and a short explanation. |
| `detailed_description` | The full target timeline: composition, appearance, positions, environment, lighting, actions, state changes, camera, sound, and where each reference takes effect. |
| `overall_soundscape` | As in the three-field schema. |
| `non_diegetic_music` | As in the three-field schema. |

`[OFFICIAL]` `detailed_description` must be explicit staging, not a plot summary and not a list
of references.

---

## 3. Alignment-instruction preambles

`[OFFICIAL]` I2VA, FL2VA and L2VA each begin with one exact sentence, placed **before** the
three fields. T2VA and Ref2VA have none.

**I2VA**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.
```

**FL2VA**

```text
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot N) aligns with the S.SS-second mark of the target video.
```

**L2VA**

```text
How the reference pictures align with the target video — <Picture 1> (from [Shot N]) aligns with the S.SS-second mark of the target video.
```

`[OFFICIAL]` `N` is replaced by the actual final shot index. `S.SS` is replaced by the effective
duration written to exactly two decimals (`8.00`, not `8` or `8.0`).
`[OFFICIAL]` The dash in the FL2VA and L2VA lines is a real em dash (`—`).
`[ASSERTED]` Community kits require exactly one blank line between the alignment line and the
first field. No evidence supports "exactly one"; a blank line is sensible formatting.

### 3.1 The bracketing asymmetry — real, not a typo

`[OFFICIAL]` I2VA and L2VA use angle-bracketed `<Picture 1>` and square-bracketed `[Shot N]`.
FL2VA uses **bare** `Picture 1` / `Picture 2` and **bare** `Shot 1` / `Shot N`.

This asymmetry is present in the official document. Reproduce it. Do not "fix" FL2VA by adding
brackets for consistency, and do not strip them from I2VA/L2VA.

`[OBSERVED]` Community kits reproduce the asymmetry faithfully across multiple files but never
explain it, and one kit's own regression suite checks only the two-decimal duration formatting,
not the bracketing — so nobody has tested whether the asymmetry matters to the model.
`[INFERRED]` Copy it anyway: exact reproduction of an official string costs nothing.

### 3.2 Which shot the anchored picture belongs to

`[OFFICIAL]` In L2VA and FL2VA the anchored last-frame picture belongs to the **final** shot,
not shot 1. On a two-shot L2VA clip the line reads `<Picture 1> (from [Shot 2]) aligns with the
7.00-second mark`. Cross-check `N` against the actual final `[Shot N]` marker in the timeline.

---

## 4. Tag tokens

All tokens are literal. `[INFERRED]` Never Markdown-escape them — `integrated\_multimodal\_description`
or `\<Subject 1>` are defects.

### `<Subject N>`

`[OFFICIAL]` Reusable *visible content* abstracted from reference assets: person, animal, object,
environment, clothing, prop, interface, visual effect, style, action, expression, or pose. It
represents content used in the output, **not the source file**.

`[OFFICIAL]` One subject may draw on several sources; one source may define several subjects.

```text
<Subject 1> is the chef whose identity and clothing come from <Picture 1> and whose walking motion comes from <Video 1>.
```

- **Use when:** something must be referred to again later by name.
- **Most common mistake:** `[OFFICIAL]` writing `<Subject 1> uses all references.` — a role that
  resolves no conflicts. Also: reusing one label for two different things across shots.

### `<Picture N>`

`[OFFICIAL]` Use a standalone picture label **only** when the image itself is a concrete first
frame, keyframe, last frame, edited keyframe, composition anchor, or storyboard/planning
reference. If an image only defines a character, costume, scene, or style, cite it *inside* the
relevant subject definition instead of giving it its own entry.

```text
<Picture 2> is the first frame of [Shot 1], showing a woman beside a café window.
```

- **Most common mistake:** promoting every attached image to a `<Picture N>` entry, which turns
  identity references into frame anchors.

### `<Video N>`

`[OFFICIAL]` Reserved for whole-video relationships: directly editing a source video, continuing
from it, or referencing its camera, cuts, rhythm, or temporal structure.

`[OFFICIAL]` A person, object, or action taken *from* a video stays a `<Subject N>`. The video
label does not replace subject labels.

- **Most common mistake:** classifying a task as video editing because a video file was attached.
  `[OFFICIAL]` Mere presence of a video does not create a task type.

### `<Audio N>`

`[OFFICIAL]` A standalone audio asset, or an enabled synchronised track from a reference video.
It may supply copied audio, music style, voice timbre or delivery, dialogue or lyrics, effects,
beat, rhythm, or continuity.

`[OFFICIAL]` Video and audio labels are numbered **independently**. A source video may be
`<Video 1>` while its enabled audio is `<Audio 2>`. A video file that contains sound does not
automatically create an audio label — the audio must actually be enabled and used.

`[OFFICIAL]` When bound to a defined speaking subject, reuse that subject's speaker ID:

```text
<Audio 1> is the voice-timbre reference for <Subject 1> (S1).
```

- **Most common mistake:** assuming `<Video 1>` and `<Audio 1>` share provenance because the
  numbers match.

`[OFFICIAL]` Labels are numbered in the order the assets are connected (first image →
`<Picture 1>`, second image → `<Picture 2>`, first video → `<Video 1>`, first audio → `<Audio 1>`),
not by semantic importance or filename.

### `(S1)`, `(S2)`, `(S1,S2)`

`[OFFICIAL]` Stable speaker IDs for subjects that speak, sing, or produce an off-screen human
voice. Assigned once, in the order of actual vocal events, and reused everywhere afterwards.
`[OFFICIAL]` Non-vocal characters get no ID. These are vocal-source IDs, not general character
numbering.

`[OFFICIAL]` Introduce the person and voice *outside* the dialogue tag on first appearance:

```text
The older woman with a low, textured voice (S1) says: <d>[English] Leave the light on.</d>
```

`[OFFICIAL]` `(S1,S2)` marks two already-numbered speakers vocalising together.

`[OFFICIAL]` A referenced subject that physically speaks carries both labels:
`<Subject 2> (S1) turns and says: ...`

`[OFFICIAL]` Verbal content heard only inside directly reused background music or a complete
copied soundtrack uses `<Audio N>` as the source **without inventing a speaker**. A voice
physically produced by a person, character, or narrator gets `(Sx)`.

- **Most common mistake:** `[OFFICIAL]` putting `(Sx)` into `retention_analysis` (see §7).
- `[OBSERVED]` Multiple practitioners report the model confusing who speaks when there is more
  than one speaker; one reports the opposite. Distinguishing speakers by age, gender, clothing
  and voice descriptor is the reported mitigation, not a cure.

### `<d>[Language] ... </d>`

`[OFFICIAL]` Encloses dialogue and lyrics. Inside `<d>` put **only** the language tag and the
actual spoken words. Speaker identity, delivery, and staging go outside the tag.

```text
<d>[English] I still remember that road.</d>
```

`[OFFICIAL]` Preserve the user's wording and punctuation exactly; do not translate or paraphrase.

`[OFFICIAL]` For voiceover the exact phrase is `says in an off-screen voiceover`, and after the
`</d>` you state that the on-screen character's lips remain completely closed:

```text
The man (S1) says in an off-screen voiceover: <d>[English] I still remember that road.</d> while his lips remain completely closed.
```

`[OFFICIAL]` For dialogue transcribed from reference audio, use `[unclear]` rather than guessing.

`[OFFICIAL]` Two punctuation rules that deliberately differ:
- **User-supplied dialogue, lyrics, on-screen text:** preserve punctuation verbatim, including
  `No... don't touch that!!!`.
- **Verbal content transcribed from reference audio:** normalise to basic sentence punctuation
  and drop decorative or repeated punctuation, ending the sentence before `</d>`.

- **Most common mistake:** putting the speaker name, tone, or stage direction inside `<d>`.

### `<scenetrans>`

`[OFFICIAL]` When one line of dialogue or lyrics crosses a cut, place `<scenetrans>` at the
connecting point in **both** fragments and explicitly state that the audio continues across the
cut.

```text
<d>[English] I thought the road <scenetrans></d> Her voice continues seamlessly across the cut.
...
<d>[English] <scenetrans>would take us home.</d>
```

- **Most common mistake:** marking only one side of the cut, or omitting the plain-English
  continuity sentence.
- `[OBSERVED]` This is the least-corroborated official item in the set. One independent retrieval
  of the base guide surfaced the defining sentence; another retrieval by a community kit could
  not find `<scenetrans>` or `<cutoff>` at all. Treat as genuine but lightly attested.

### `<cutoff>`

`[OFFICIAL]` Used when spoken content is truncated by the end of the video.

- **Most common mistake:** using it for any trailing-off delivery rather than specifically for
  speech clipped by the clip boundary.

### Other literals

| Token | Rule | Provenance |
|---|---|---|
| `[unclear]` | Stands in for unintelligible reference-audio content. | `[OFFICIAL]` |
| `N/A` | Value for an empty `overall_soundscape` (explicit silence only) or `non_diegetic_music`. | `[OFFICIAL]` |
| `"..."` | English double quotation marks around visible on-screen text. | `[OFFICIAL]` |

`[INFERRED]` The complete set of angle-bracket tokens permitted in a delivered prompt is:
`<Subject N>`, `<Picture N>`, `<Video N>`, `<Audio N>`, `<d>`, `</d>`, `<scenetrans>`, `<cutoff>`.
Any other angle-bracket token is an unresolved placeholder.

---

## 5. Shot and timestamp format

`[OFFICIAL]` `[Shot 1]` carries **no** timestamp. `[Shot 1] At 00:00.000, ...` is wrong.

`[OFFICIAL]` Later shots take the form:

```text
[Shot N] At MM:SS.mmm, the camera cuts to ...
```

Worked examples: `[Shot 2] At 00:03.500, the shot cuts to ...` / `[Shot 2] At 00:02.500, ...`

`[OFFICIAL]` Timestamps must be strictly increasing, must not repeat or decrease, must fall
inside the requested duration, and must match actual playback order.

`[OFFICIAL]` A cut should add new information about subject, space, state, viewpoint, or time.
If only distance or a modest angle changes, use camera motion inside the existing shot instead.

`[ASSERTED]` A timestamp can mark an event *within* a shot without creating a new shot —
`At 00:06.500, the table lamp clicks on` stays inside Shot 1. This appears only as a community
kit's decision note; it is consistent with the format but untested.

`[INFERRED]` Measured across a corpus of 34 working prompts with stated durations: clips of
5 seconds or less used one shot; 8-second clips used two; no prompt used more than two. The
earliest cut anywhere in that corpus is at 3.0 s, and cuts sit at 40–67 % of runtime (median
56 %). This is a measurement of what people wrote, not evidence that more shots fail.

`[OFFICIAL]` Ordinary transition phrasing: `the camera cuts to`, `the shot cuts to`,
`the shot transitions to`, `the shot changes to`, `the shot switches to`. Cross-dissolve, fade
and wipe only when explicitly requested or clearly required.
`[OBSERVED]` The transition-phrase list did not surface in one independent retrieval of the base
guide; it is likely genuine but unconfirmed at the string level.

---

## 6. Task-type prefixes (Ref2VA `summary` only)

`[OFFICIAL]` The `summary` paragraph begins with a square-bracketed task-type prefix. The six
canonical task types:

| Task type | Applies when |
|---|---|
| `keyframe completion` | An image is a concrete frame anchor (first frame, keyframe, last frame). |
| `reference generation` | Media guides identity, scene, style, action, camera, or storyboard — new footage is generated. |
| `video editing` | A source video is directly modified. |
| `video continuation` | The output extends or resumes a source video. |
| `audio reuse` | The same audio signal is copied, in whole or in part. |
| `audio reference` | The signal is not copied; its style, timbre, content, texture, beat, or continuity guides generation. |

`[OFFICIAL]` Combining rule: join multiple types with the literal joiner ` + ` — a space, a plus
sign, a space — and do not repeat a type.

```text
[reference generation + audio reference] ...
[video editing + reference generation + audio reuse] ...
```

`[OFFICIAL]` Mere presence of a video or audio file does not create a task type. Camera, cut, or
rhythm guidance taken from a video is normally `reference generation`, not `video editing`.

`[OFFICIAL]` Introduce no new labels in `summary` — use only labels already defined in
`subject_definitions`.

`[OFFICIAL]` For direct editing tasks, the summary continues immediately after the prefix with:
`The target video is an edited version of <Video 1>.`

### Decision table

| The brief says | Prefix contains |
|---|---|
| "use this image as the first/last frame" | `keyframe completion` |
| "make her look like this person" / "in this style" / "use this location" | `reference generation` |
| "change the jacket in this video" / "remove the sign from this clip" | `video editing` |
| "continue this clip" / "what happens next" | `video continuation` |
| "keep this soundtrack" / "use this exact audio" | `audio reuse` |
| "match this voice" / "same kind of music" / "this beat" | `audio reference` |
| An image anchor plus a separately tracked identity reference | `keyframe completion + reference generation` |
| A choreography video guiding new characters, plus its music copied | `reference generation + audio reuse` |

---

## 7. Retention relationship markers

`[OFFICIAL]` `retention_analysis` uses one line per label, with a marker drawn from one of two
**closed** sets. The sets do not overlap in usage: visible labels take visual markers, `<Audio N>`
takes audio markers. `weak_reference` is the only string that appears in both.

### Visual markers — for `<Subject N>`, `<Picture N>`, `<Video N>`

| Marker | Meaning |
|---|---|
| `fully_preserved` | The defined reference role is fully retained. |
| `partially_preserved` | Still used, but some defined traits change or are only partly retained. |
| `attribute_transfer` | Referenced traits are transferred to a different identifiable target. |
| `weak_reference` | Only broad similarity — style, category, composition, atmosphere. |

### Audio markers — for `<Audio N>`

| Marker | Meaning |
|---|---|
| `fully_copy` | The entire source audio becomes the entire final audio track. |
| `partially_copy` | Only part or some layers are copied, or copied audio is modified by additions, removals, or replacements. |
| `reference` | Signal not copied; attributes or content guide generation. |
| `weak_reference` | Only broad category or atmosphere similarity. |

### Entry format

`[OFFICIAL]` `label (scope): marker - explanation`. The scope parenthesis carries the shot list
or the aspect being retained.

```text
<Subject 1> (appears in [Shot 1], [Shot 3]): fully_preserved - the defined identity, hairstyle, and wardrobe remain consistent throughout.
<Picture 2> ([Shot 1] first frame): fully_preserved - the opening composition matches the supplied frame exactly.
<Video 1> (cut and pacing structure): weak_reference - only the general rhythm of cuts is echoed; no footage is reused.
<Audio 1> (ambience layer): partially_copy - the room tone is copied while new footstep sounds are added.
```

> **Contradiction, unresolved.** `[OFFICIAL]` The official examples use a plain hyphen-space
> delimiter (`marker - explanation`). `[ASSERTED]` One community kit's efficiency file uses an
> em dash (`marker — explanation`) while its own gold examples use the hyphen. No rule anywhere
> states which is canonical. Use the hyphen; it is what the official examples show.

`[OFFICIAL]` Rules:
- One line per label. A label keeps the role it was given in `subject_definitions`.
- **`(Sx)` must never appear in `retention_analysis`.** Speaker IDs are not retention labels.
- Newly added target actions, backgrounds, or plot events are **not** reference-fidelity losses —
  do not downgrade a marker because the output contains new material.

---

## 8. On-screen text convention

`[OFFICIAL]` Any visible banner, sign, label, subtitle, UI string, or neon message is written
inside **English double quotation marks**, verbatim, with spelling and punctuation preserved and
**not translated**.

```text
A red sign reading "营业中" glows above the doorway.
A door sticker reads "OPEN 24/7!!!".
```

`[OFFICIAL]` This holds even when the surrounding prompt is entirely English and the text is in
another script. Only dialogue inside `<d>` and visible text keep their original language;
everything else in the prompt is English.

---

## 9. Content rules that shape the description field

`[OFFICIAL]` Every detail in the timeline must correspond to something **visible or audible**.
"She feels guilty and afraid" specifies nothing. "She hesitates, glances toward the door,
tightens her grip on the envelope, and shifts her weight backward" does.

`[INFERRED]` Adjective stacks — "cinematic, dramatic, stunning, epic" — are not specifications.
Translate them into production choices: angle, lighting, sound, motion.

`[INFERRED]` Use literal small integers where count matters: `three plated dishes`, `two crisp
key poses`, `one concise nod`. This is a pervasive idiom in working prompts, not a stated rule.

`[OBSERVED]` Overloading a short clip with unrelated beats can cause requested content — including
dialogue — to be silently dropped. Prefer one location, one causal action chain, one purposeful
camera move for short clips. (Single practitioner report.)
`[ASSERTED]` The specific figure "one dominant action beat per roughly 1–3 seconds" is a community
kit heuristic with no cited basis.

`[OFFICIAL]` Length guidance that is actually stated: `overall_soundscape` 1–4 sentences,
`non_diegetic_music` 1–3 sentences, Ref2VA `detailed_description` 350–500 words for generation
tasks, Ref2VA style opener 1–2 sentences.
`[INFERRED]` Measured across a corpus of 39 working prompts: three-field prompts cluster around
100 words / ~1 kB, Ref2VA around 355 words / ~3.3 kB; the longest description field observed was
389 words and the longest whole prompt 4169 characters. No test shows longer prompts degrading.
`[OFFICIAL]` Hosted API requests are rejected above 7000 characters.

---

---

## 10. Runtime quirks that change the text you send

`[OBSERVED]` The prompt text is not always delivered to the model exactly as typed. Two known
cases, both runtime-specific rather than model behaviour:

| Runtime | Quirk | Consequence |
|---|---|---|
| One local front-end for open-weights H3 | **A blank line is treated as a prompt separator.** | The six sections must sit on consecutive lines with no blank line between them, or the prompt is split into several prompts. Blank lines typed into any field are stripped. |
| Local node-based runtimes | Reference slots are **0-indexed** in the interface while the prompt text is **1-indexed** (`<Picture 1>` is the first slot). | Off-by-one role assignment — the identity image gets the location's job. |

`[INFERRED]` Before blaming the model for ignoring structure, confirm what your runtime actually
sent. Where a runtime offers a preview of the final prompt string, read it.

`[OBSERVED]` Reference slot numbers follow **upload order**. Re-ordering uploads silently
re-assigns which asset is `<Picture 1>`, without changing your prompt text.


## COMMON SYNTAX ERRORS

| # | Error | Correct form | Provenance |
|---|---|---|---|
| 1 | Ref2VA prompt opens with `integrated_multimodal_description:` | Ref2VA opens with `subject_definitions:` | `[OFFICIAL]` |
| 2 | Three-field prompt contains `subject_definitions:` or `retention_analysis:` | Three fields only | `[OFFICIAL]` |
| 3 | Fields reordered, renamed, abbreviated, or one omitted | Fixed order, exact spellings, no substitutes | `[OFFICIAL]` |
| 4 | Alignment line emitted for T2VA or Ref2VA | Only I2VA, FL2VA, L2VA carry one | `[OFFICIAL]` |
| 5 | Alignment line missing or paraphrased for I2VA/FL2VA/L2VA | Reproduce the exact sentence | `[OFFICIAL]` |
| 6 | FL2VA line "corrected" to `<Picture 1> (from [Shot 1])` | FL2VA uses bare `Picture 1 (from Shot 1)` | `[OFFICIAL]` |
| 7 | `S.SS` or `N` left unresolved in the delivered prompt | Substitute real values | `[OFFICIAL]` |
| 8 | Duration written `8` or `8.0` | `8.00` — exactly two decimals | `[OFFICIAL]` |
| 9 | Alignment line says `[Shot 1]` on a two-shot L2VA/FL2VA clip | The anchored picture belongs to the final shot | `[OFFICIAL]` |
| 10 | `[Shot 1] At 00:00.000, ...` | Shot 1 carries no timestamp | `[OFFICIAL]` |
| 11 | Cut times repeat, decrease, or exceed the clip duration | Strictly increasing, all inside duration | `[OFFICIAL]` |
| 12 | Speaker name or tone written inside `<d>` | Only `[Language]` plus the exact words | `[OFFICIAL]` |
| 13 | `<scenetrans>` on only one side of a cut | Both fragments, plus a continuity sentence | `[OFFICIAL]` |
| 14 | `(Sx)` appears in `retention_analysis` | Speaker IDs never enter retention analysis | `[OFFICIAL]` |
| 15 | An audio marker used on `<Subject N>`, or a visual marker on `<Audio N>` | Two closed sets, applied by label type | `[OFFICIAL]` |
| 16 | A retention marker invented (`mostly_preserved`, `style_only`) | Only the eight listed strings exist | `[OFFICIAL]` |
| 17 | On-screen text translated into English | Verbatim, original script, in double quotes | `[OFFICIAL]` |
| 18 | Task-type prefix joined with `,` or `and` | ` + ` with surrounding spaces | `[OFFICIAL]` |
| 19 | A task type repeated inside the prefix | Each type at most once | `[OFFICIAL]` |
| 20 | New labels introduced in `summary` | Introduce every label in `subject_definitions` | `[OFFICIAL]` |
| 21 | One label means different things in different sections | A label keeps one meaning across all sections | `[OFFICIAL]` |
| 22 | `<Video 2>` used without ever being defined | Every label defined before use | `[OFFICIAL]` |
| 23 | Dialogue or diegetic music repeated in `overall_soundscape` | Keep them in the description field | `[OFFICIAL]` |
| 24 | Diegetic (in-world) music placed in `non_diegetic_music` | `non_diegetic_music` is audience-only score | `[OFFICIAL]` |
| 25 | Markdown-escaped tokens: `integrated\_multimodal\_description`, `\<Subject 1>` | Emit tokens literally | `[INFERRED]` |
| 26 | Unresolved placeholders survive: `<STYLE CLAUSE>`, `<SUBJECT>` | Only the eight canonical angle-bracket tokens may appear | `[INFERRED]` |
| 27 | Invisible intent written into the timeline ("she feels guilty") | Visible or audible detail only | `[OFFICIAL]` |
| 28 | `<Picture N>` entry created for an image that only defines a character | Cite it inside the subject definition instead | `[OFFICIAL]` |
| 29 | Task type set to `video editing` because a video was attached | File presence does not determine task type | `[OFFICIAL]` |
| 30 | `<Video 1>` and `<Audio 1>` assumed to be the same asset | Video and audio numbering are independent | `[OFFICIAL]` |
