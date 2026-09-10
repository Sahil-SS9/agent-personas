# H3 Prompting — Audio and Dialogue Reference

H3 generates stereo audio in the same pass as the picture. It will generate audio whether or not
you asked for any. Silence is an instruction, not a default.

Provenance markers: `[OFFICIAL]` (MiniMax's own prompt-writing guides), `[OBSERVED]` (someone ran
it and reported, named where known), `[INFERRED]` (derived from structure), `[ASSERTED]` (community
kits state it as fact with no evidence).

---

## 1. Three layers, three homes

`[OFFICIAL]` Audio content is split across three places, and putting content in the wrong one is a
silent failure.

| Content | Goes in | Length |
|---|---|---|
| Dialogue, singing, and sound events synchronised to a specific shot | the main description field (`integrated_multimodal_description` or `detailed_description`) | as needed |
| Ambience, room tone, physical action sounds, non-verbal human sounds (footsteps, fabric, breathing, impacts, traffic, rain) | `overall_soundscape` | 1–4 sentences |
| Music the characters cannot hear — audience-only score | `non_diegetic_music` | 1–3 sentences |

`[OFFICIAL]` Music a character *can* hear — a radio, a phone, a television, a band in the room —
is diegetic and belongs in the main description field, **not** in `non_diegetic_music`.

`[OFFICIAL]` Do not repeat dialogue or lyrics into `overall_soundscape` or `non_diegetic_music`.
Complete spoken content lives only inside `<d>` in the description field.

`[OBSERVED]` MiniMax's own README example violates this rule — it repeats dialogue and background
music into `overall_soundscape`. **The written guide wins.** The README example is not a template.

`[OFFICIAL]` `non_diegetic_music` describes instrumentation, tempo, rhythm and dynamic change.
Avoid abstract mood language and emotional explanation — "melancholy", "tense", "uplifting" carry
no instruction. Write what an orchestrator would write.

---

## 2. Dialogue syntax

`[OFFICIAL]` The form is:

```
<speaker description> (S1) says, <delivery description>, <d>[English] The spoken words.</d>
```

Rules:

| Rule | Detail |
|---|---|
| Speaker IDs | `(S1)`, `(S2)`, … assigned in order of actual vocal events in the target video |
| Stability | A speaker keeps the same ID across all shots |
| Non-speakers | Characters who never vocalise get no ID |
| Simultaneous speech | Compound ID: `(S1,S2)` |
| First appearance | Give identifying context: character type, age, gender, on/off-screen, vocal quality, accent |
| Outside the tag | Speaker identity, ID, action and delivery |
| Inside the tag | Only the language tag and the spoken words, verbatim |

`[OFFICIAL]` In full-reference mode, when a referenced subject speaks, keep both labels:
`<Subject 2> (S1) turns toward her and says, <d>[English] ...</d>`. The subject label identifies
who it is; the speaker ID identifies the voice.

`[OFFICIAL]` `(Sx)` must **never** appear in `retention_analysis`.

---

## 3. THE QUOTE RULE

`[OBSERVED]` **Quotation marks inside a `<d>` tag produce burned-in on-screen subtitles.** Quotes
are the model's convention for text that should be rendered *in the picture*.

This is among the best-evidenced rules in the whole corpus: reported directly by one practitioner
("quotes are instructions to the model for printed words", 2026-08-11) and independently confirmed
by another's side-by-side failing/working pair (2026-08-07).

Fails — produces subtitles burned into the frame:

```
She says, "Could you keep it down?"
```

Works:

```
The woman with a calm dry voice (S1) says, <d>[English] Could you keep it down?</d>
```

`[OFFICIAL]` The one place quotation marks are correct is **on-screen text you actually want
rendered** — signs, banners, labels, neon. Those go in English double quotes, verbatim,
untranslated: `A red neon sign reading "營業中" glows above the doorway.`

---

## 4. THE SILENCE RULE

`[OBSERVED]` **H3 invents gibberish speech when speech is not addressed at all.** This is the
single most-reported failure in the community corpus — roughly fifteen independent reporters. The
formulation people converged on: the model produces gibberish if you do not prompt for speech *or
for the lack of it*.

`[OBSERVED]` Writing `N/A` in `non_diegetic_music` has itself been reported to provoke invented
audio. An affirmative description of silence is safer than an empty marker.

`[OFFICIAL]` The base guide does sanction `N/A` for both audio fields when music or sound is
absent — so this is a case where community observation contradicts the guide. The affirmative form
costs nothing and satisfies both.

Weak:

```
non_diegetic_music: N/A
```

Better:

```
non_diegetic_music: None. No score and no music of any kind at any point in the clip.
```

And if nobody speaks, say so in the description field: `No one speaks at any point.`

---

## 5. Voiceover, cuts, and truncation

`[OFFICIAL]` For voiceover use the exact phrase **"says in an off-screen voiceover"**. After every
voiceover `<d>` block, state the on-screen character's lips: *"while his lips remain completely
closed."* Omitting this produces a character mouthing the narration.

`[OFFICIAL]` When a line crosses a cut, place `<scenetrans>` at both connection points and state
the audio continuity explicitly, using one of: *"continues seamlessly across the cut"*,
*"continues uninterrupted into the next shot"*, *"carries over from the previous shot"*,
*"remains audible across the transition"*.

`[OFFICIAL]` Use `<cutoff>` when speech ends abruptly — cut short by the shot or by the end of the
clip.

---

## 6. Punctuation: two rules that conflict by design

`[OFFICIAL]` The two guides say opposite things, and both are correct within their scope. Resolve
by **input source**, not by picking a winner.

| Source of the words | Rule |
|---|---|
| Dialogue the user supplied | Preserve wording **and punctuation** verbatim. Keep `!!!` and `...` if the user wrote them. |
| Dialogue transcribed from a reference audio asset | Normalise to basic marks (`,` `.` `?` `!`). Strip repeated tildes, emoji, bullets, decorative punctuation. Write `[unclear]` for unintelligible spans rather than guessing. End statements, questions and exclamations with `.`, `?`, `!` respectively before `</d>`. |

`[OFFICIAL]` When only timbre, rhythm, emotion or delivery is being referenced from an audio
asset, do **not** carry the original words into the target video.

---

## 7. Voice references

`[OFFICIAL]` An `<Audio N>` used as a voice reference is bound to a target speaker by reusing that
speaker's global ID in the definition:

```
<Audio 1> is the voice-timbre reference for <Subject 1> (S1).
```

The ID comes from the target video's speaking order. It is never assigned independently in the
audio definition.

`[OFFICIAL]` In `retention_analysis`, a voice reference is `reference`, not `fully_copy`:

```
<Audio 1>: reference - the target speaker follows <Audio 1>'s voice timbre and measured delivery
without copying the original signal.
```

`[OBSERVED]` Voice-timbre reference for a **single** speaker works well and is widely reported as
one of the model's strengths.

`[OBSERVED]` **Binding two distinct voices to two subjects is an unsolved problem.** Multiple
practitioners are stuck on it. The reported symptoms are the classic voice-clone failure set: too
little dialogue per speaker collapses to a generic voice, and some clips simply refuse. If your
piece needs two distinct referenced voices, plan to generate separately and assemble in post.

`[OBSERVED]` Reference audio can overpower the foreground mix. Sound-effect references specifically
were reported not to work.

`[OFFICIAL]` An audio file must accompany at least one image or video — audio alone is not a valid
reference set.

---

## 8. Dialogue timing

`[OFFICIAL]` Dialogue-dense content should prioritise fitting the complete spoken timeline over
reaching any word count.

`[INFERRED]` A short line — four to six words — needs roughly 1.2 seconds of clip. Budget for it
before you budget anything else, because the model will not slow a shot down to accommodate a line
it cannot fit; it speeds the delivery up until the line stops sounding human.

`[OBSERVED]` Rushed delivery is a reported failure. The two fixes are: shorten the line, or extend
the clip.

`[ASSERTED]` The community kits publish precise words-per-second budgets. These are invented.
Time the line aloud instead.

---

## 9. Audio failure modes

| Symptom | Cause | Fix |
|---|---|---|
| Speech you never wrote; gibberish | Speech not addressed at all | State positively that no one speaks; or write the speech you do want |
| Subtitles burned into the picture | Quotation marks inside `<d>` | Remove the quotes; keep words bare inside the tag |
| Invented audio despite `N/A` | Empty marker read as unspecified rather than absent | Replace `N/A` with an affirmative sentence describing silence |
| Music appears though none was asked for | `non_diegetic_music` left unaddressed | Write the affirmative-silence sentence |
| Character mouths the narration | Voiceover phrase used without the lip note | Add *"while his lips remain completely closed"* |
| Line delivered too fast to parse | Line too long for the shot | Shorten the line or lengthen the clip |
| Wrong character speaks | Speaker IDs not stable or not assigned in vocal order | Assign `(Sx)` once in order of vocal events, reuse everywhere |
| Second speaker's voice collapses to generic | Two voice references, known unsolved | Generate separately, assemble in post |
| Reference audio drowns the scene | Reference level not controllable from the prompt | Engine-side; not a prompt fix |
| Sound effect reference has no effect | Reported not to work | Describe the effect in `overall_soundscape` instead |
| Dialogue appears in `overall_soundscape` and is doubled | Content placed in the wrong layer | Dialogue belongs only in the description field |

---

## 10. Open questions

- Whether the affirmative-silence phrasing outperforms `N/A` under controlled comparison. Nobody
  has run one; the evidence is anecdotal on both sides.
- Whether `<scenetrans>` has any effect when the audio would have continued anyway.
- The mechanism behind the two-voice binding failure — whether it is a prompt-format problem or a
  model limitation. Currently unknown.
