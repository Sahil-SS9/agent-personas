# H3 Prompting — Worked Examples and Templates

Reference specimens, the model-adjacent rewriter template, and the recurring phrasings that
appear across the corpus of working prompts. Copy from these rather than inventing structure.

---

## 1. Verbatim reference specimens

### 1.1 Ref2VA specimen A — R01, "Portrait identity plus voice reference"
*Chosen because it is the archetype of the most common real Ref2VA job: one identity picture + one
voice-timbre audio + a required verbatim line, two shots, complete six-section grammar. 371 words / 3311 chars.*

**Brief:** Picture 1 is a chef portrait; Audio 1 is her voice. Create a restaurant-kitchen scene where she says exactly, "Service begins now."
**Mode:** Ref2VA · 8.00 seconds
**Style recipe:** V19 live action + M01 acting + A01 realism

```text
subject_definitions:
<Subject 1> is the chef whose facial identity, short dark curls, white jacket, blue neckerchief, and small silver earrings come from <Picture 1>.
<Audio 1> is the voice-timbre and measured-delivery reference for <Subject 1> (S1).

summary:
[reference generation + audio reference] The target video shows <Subject 1> preparing the kitchen for dinner service while <Audio 1> guides her spoken voice without copying its original signal or words.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - facial identity, hair, uniform, neckerchief, and earrings remain consistent throughout.
<Audio 1>: reference - its timbre and measured delivery guide <Subject 1> (S1), while the requested target line is newly performed.

detailed_description:
The target video uses photoreal live-action restaurant cinematography with warm overhead practicals, controlled stainless-steel reflections, and restrained handheld movement.
[Shot 1] A medium-wide shot frames <Subject 1> at the center pass of a working restaurant kitchen. Her facial identity, short dark curls, white chef's jacket, blue neckerchief, and silver earrings remain consistent with <Picture 1>. She checks three plated dishes from left to right, wipes one small sauce mark from the nearest rim, and turns her head toward the line cooks off-screen. The camera tracks slowly beside the pass, preserving her profile and the orderly row of heat lamps. Steam rises behind her while cooks move as soft background shapes without blocking her face. She rotates the center plate by a few degrees, compares its garnish height with the plate beside it, and uses the back of a spoon to restore one precise sauce edge. A cook crosses behind her carrying a pan; its brief reflection passes through the steel backsplash without changing the key light on her face. <Subject 1> (S1), using the stable voice timbre and measured delivery referenced from <Audio 1>, places both hands on the counter and says: <d>[English] Service begins now.</d> She closes her lips and gives one concise nod. Her left hand moves to the folded service cloth while her right hand reaches toward the bell, establishing the next action before the cut. [Shot 2] At 00:05.000, the shot cuts to a close view of her right hand ringing the service bell once. The bell cap depresses and returns, the cloth remains folded beneath her opposite hand, and the nearest plate stays aligned under the heat lamp. The camera tilts up to her face as she lifts the first plate, pivots toward the pickup side, and passes it out of frame. A server's hands receive the plate without covering its garnish. Her uniform, jewelry, and identity remain unchanged while the kitchen activity increases behind her. She immediately checks the second plate, lifts it with both hands, and pauses just long enough for steam to clear her face. The final composition holds her in three-quarter view beneath the warm lamps, shoulders squared, gaze directed toward the pickup area, and the second plate stable at counter height.

overall_soundscape:
Kitchen ventilation, low burner flame, restrained utensil contact, and distant staff movement continue throughout. A plate rim is wiped, the service bell rings once, and ceramic slides lightly across the pass.

non_diegetic_music:
N/A
```

**Decision note:** Audio is a timbre reference, not a copied signal; the supplied line replaces any source words.

---

### 1.2 Ref2VA specimen B — R06, "Full-reference keyframe completion"
*Chosen because it is the only example that combines Ref2VA role separation with an exact final-frame
anchor, and it carries the strongest end-state grammar in the whole corpus (the "converge …
without a late blink or camera drift" close). 366 words / 3214 chars.*

**Brief:** Picture 1 provides a character identity; Picture 2 is the exact final frame of Shot 2. Create a seven-second bookstore scene.
**Mode:** Ref2VA · 7.00 seconds

```text
subject_definitions:
<Subject 1> is the bookseller whose facial identity, round glasses, grey cardigan, and braided hair come from <Picture 1>.
<Picture 2> is the last frame of [Shot 2], showing <Subject 1> on a ladder holding a blue book beneath the brass reading lamp.

summary:
[reference generation + keyframe completion] The target video follows <Subject 1> locating a book in a quiet shop and ends exactly on the concrete frame anchor <Picture 2>.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - identity, glasses, cardigan, and braided hair remain consistent.
<Picture 2> ([Shot 2] last frame): fully_preserved - final ladder position, blue book, body pose, brass lamp, lighting, camera angle, and composition are matched exactly.

detailed_description:
The target video uses warm live-action bookstore cinematography with soft practical light, wooden shelf texture, restrained depth of field, and quiet naturalistic acting.
[Shot 1] A medium-wide shot establishes <Subject 1> behind a wooden counter, preserving the facial identity, round glasses, grey cardigan, and braided hair from <Picture 1>. She reads a handwritten request card, looks toward the upper shelves, and traces one shelf row with her eyes before stepping around the counter. The camera pans right slowly as she passes a small stack of returns and pulls a rolling ladder along its rail. Its brass wheels turn visibly, cross two shelf divisions, and stop beneath a reading lamp. She checks the shelf number against the card, folds the card once, and places it in the cardigan pocket without changing the garment. Dust moves gently through the lamp beam. She steadies the ladder with one hand, tests the first rung with the front of her shoe, and places her weight onto it while the free hand reaches for the rail. [Shot 2] At 00:03.800, the shot cuts to the angle that will become <Picture 2>. <Subject 1> climbs two rungs through careful weight shifts, preserving the glasses, braid, cardigan folds, and exact identity. The ladder remains fixed on its rail while the camera begins a restrained push. She reaches toward a cluster of books, touches two spines with her index finger, and stops on the blue volume. The book resists slightly; she braces with the other hand and slides it halfway free. The neighboring books compress and return as the volume clears. A thin layer of dust releases from the top edge and drifts through the brass light. She holds the rail, turns the cover toward herself, confirms it against the card partly visible in her pocket, and adjusts the book into the exact hand position shown in <Picture 2>. During the final two seconds, her movement becomes progressively smaller. The camera completes its push while her foot placement, shoulder angle, braid position, glasses, blue book, brass lamp, shelf spacing, hand grip, lighting, focus, and every compositional boundary converge on <Picture 2>. The shot ends exactly on that frame without a late blink or camera drift.

overall_soundscape:
Quiet room tone, faint street noise through glass, rolling ladder wheels, wooden rung creaks, cardigan movement, and a book sliding against paper fill the shop.

non_diegetic_music:
N/A
```

**Decision note:** A standalone `<Picture 2>` is valid because it is a concrete final-frame anchor.

*(Runner-up specimens worth keeping in view: **R02** for style-as-`<Subject 2>` + `attribute_transfer`
with visible text; **R03** for `<Video 1>` used as a camera-motion-only reference; **R08** for
`partially_copy` audio.)*

---

### 1.3 T2VA specimen — T02, "Limited-animation comedy"
*Chosen because it is the only T2VA example that exercises every three-field mechanism at once:
style clause, held-pose animation grammar, a timestamped cut, tagged dialogue with a voice
descriptor, a non-`N/A` instrumental music field, and a settle-based ending. 133 words / 1173 chars —
the longest T2VA in the corpus, i.e. the practical upper bound for the format.*

**Brief:** Eight-second flat TV animation. An office worker hides a birthday cake when the boss enters; the coworker whispers, "Act normal."
**Mode:** T2VA · 8.00 seconds · two shots
**Style recipe:** V02 limited television animation + M03 snappy cartoon timing + F01 clean digital + A03 cartoon accents

```text
integrated_multimodal_description: [Shot 1] Limited 2D television animation with clean flat color, held key poses, selective eye and mouth movement, and stable sitcom staging, a medium-wide shot frames two office workers beside a desk with a brightly iced cake. The elevator bell sounds. One worker snaps upright, slides the cake into a lower cabinet with a fast anticipation and clean held settle, while the other keeps watch. The camera holds static as the cabinet door almost closes, then rebounds one inch. The young coworker with a quick, dry alto voice (S1) leans closer and whispers: <d>[English] Act normal.</d> [Shot 2] At 00:04.500, the shot cuts to the boss entering from the elevator while both workers hold exaggeratedly neutral poses. Only their pupils shift toward the cabinet as a single candle flame rises behind the desktop.

overall_soundscape: Low office ventilation and distant keyboard taps continue beneath the elevator bell. The cabinet slides, bumps softly, and squeaks once as it rebounds.

non_diegetic_music: Short muted clarinet and pizzicato-string notes at a moderate tempo punctuate the cabinet movement, then stop under the final held pose.
```

**Decision note:** Limited movement is concentrated in eyes, mouth, cabinet, and candle; the music is described instrumentally rather than as "comedic."

---


---

## 2. The lightx2v prompt-rewriter template

Shipped with the `MiniMax-H3-Prompt-Rewriter-LoRA`. `[OBSERVED]` This carries more weight than
any community system prompt, because it is the template the model's own rewriter was trained to
emit. Reproduced as posted to the Banodoco Hivemind, 2026-08-07.

### ARTEFACT 4 — lightx2v official "MiniMax-H3-Prompt-Rewriter-LoRA" prompt template
**Posted by: RuneX — 2026-08-07T09:34:13Z**
Source he cites: https://huggingface.co/lightx2v/MiniMax-H3-Prompt-Rewriter-LoRA/blob/main/prompt_template.py

RuneX's framing: "the lightx one also looked interesting (untested).  But looked short and structured:"

Verbatim template:

```
You are a professional prompt rewriter for joint audio-video generation.
Rewrite the user's original prompt into one coherent, production-ready multimodal description for the requested output aspect ratio and duration.
Return only these three fields, in this exact order:
integrated_multimodal_description: ...
overall_soundscape: ...
non_diegetic_music: ...
Requirements:
- Expand the visual narrative into clearly numbered shots such as [Shot 1], [Shot 2], and include timestamps for cuts after the first shot when useful.
- Make the number, timing, and pacing of shots appropriate for the requested duration.
- Compose the scene for the requested aspect ratio.
- Preserve the user's intent while adding concrete subjects, appearance, environment, lighting, composition, camera movement, physical motion, and temporal continuity.
- Keep characters, objects, wardrobe, locations, and spatial relationships consistent across shots.
- Describe synchronized diegetic audio in overall_soundscape and external score in non_diegetic_music.
- Do not add explanations, Markdown fences, safety commentary, or fields other than the three requested fields.
```

This is the most authoritative artefact in the corpus: it is the actual rewriter
template shipped with the model's own prompt-rewriter LoRA, not a community guess.
Note the differences from ARTEFACT 1/2: **three named fields in a fixed order**,
`[Shot N]` numbering, timestamps only for cuts *after* the first shot, and no
2,000-character cap.


---

## 3. Load-bearing idioms

Phrases that recur often enough, and carry enough semantic weight, that they should be treated as
fixed vocabulary rather than stylistic choices. Counts are (occurrences / blocks-containing) out of 41 blocks.

### 3.1 Camera
| Idiom | Count | Function |
|---|---|---|
| `with small amplitude at slow speed` | 11 / 11 | Default restraint modifier; suppresses over-large camera motion |
| `at slow speed` (any) | 12 / 12 | Speed is always stated, never implied |
| `The camera holds a static shot` / `holds static` / `remains static` | 9 / 9 | Static is asserted, never left to omission |
| `at constant speed` | 3 / 2 | For mechanical/object motion |
| `pushes in` / `pulls out` / `trucks` / `tracks` / `arcs clockwise` / `pans` / `tilts up` | 23 total | Closed verb set; `trucks` = lateral, `tracks` = with-subject |

### 3.2 Cuts and time
| Idiom | Count | Function |
|---|---|---|
| `[Shot 2] At 00:MM.mmm, the shot cuts to …` | 11 / 11 | The cut formula |
| `At 00:` (any) | 16 / 16 | 3-dp millisecond timestamps, always |
| `the camera cuts to` | 2 / 2 | Legacy variant, only in 04_H3_EXAMPLES |
| `the shot changes to` | 1 / 1 | Rare variant (R02) |

### 3.3 Holds, settles, secondary motion
| Idiom | Count | Function |
|---|---|---|
| `hold` / `holds` (held pose, holds static, holds the final pose) | 22 / 15 | Animation-grammar staple; "held key poses", "clean held settle", "a brief still hold" |
| `settle` / `settles` | 15 / 14 | Terminates every motion — nothing stops abruptly without a settle |
| `then settles` / `and settles` | frequent | Overlap/follow-through: `her cape settles one beat after her shoulders`; `braids continue rotating after the head stops, then fall back`; `The coat hem lags by one held frame and snaps gently into place` |
| `overshoots slightly, returns, and settles` | 1 | Explicit follow-through recipe |
| `rebounds one inch` / `compress and return` / `depresses and returns` | 3 | Physical-plausibility micro-beats |

### 3.4 Continuity and preservation
| Idiom | Count | Function |
|---|---|---|
| `remain consistent (with <Picture N>)` / `remain unchanged` / `remain fixed` / `are fully preserved` | ~15 | Preservation assertion; always attached to a named attribute list |
| `without changing …` | 10 / 10 | Bounded-edit guard: `without changing her seated position`, `without changing the watch design`, `without changing its tailored silhouette`, `without changing the original character design` |
| `without copying …` | 9 / 5 | Reference-vs-copy guard: `without copying the original signal or words`, `without copying any waveform, melody, or verbal content` |
| `fully_preserved` / `attribute_transfer` / `partially_preserved` / `fully_copy` / `partially_copy` / `reference` | 28 | The retention enum; never paraphrased |
| `frame by frame` | 1 | Only for direct video edits (R04) |

### 3.5 End states
| Idiom | Count | Function |
|---|---|---|
| `converge on <Picture N>` (+ `exactly` / `at the end`) | 8 / 8 | The anchored-ending formula |
| `During the final <two seconds / second / half-second>` | 6 / 6 | Opens the convergence window |
| `progressively` (slows / smaller / converge) | 5 / 5 | Deceleration into the anchor |
| `exactly` | 10 / 7 | Attached to text spelling, anchor matching, and duration |
| `The shot ends exactly on that frame without a late blink or camera drift.` | 1 | Strongest terminal guard in the corpus |
| `The final composition holds …` | 4 | Unanchored Ref2VA ending |

### 3.6 Dialogue
| Idiom | Count | Function |
|---|---|---|
| `<d>[English] … </d>` | every spoken line | Language always bracketed inside the tag |
| `with a <adj>, <adj> voice (S1)` | 9 / 9 | Speaker ID is introduced via voice description, never as a bare label |
| `and says:` | 8 / 8 | Colon before the tag |
| `She closes her lips` (and variants) | 8 / 8 | Mandatory post-line mouth-closure beat |
| `says in an off-screen voiceover: … while his lips remain completely closed.` | 2 / 2 | The VO pair — both halves required |
| `<scenetrans>` | 4 / 2 | Cross-cut dialogue; appears at the *end* of fragment 1 and *start* of fragment 2 |
| `Her voice continues seamlessly across the cut.` / `the same voice carries over uninterrupted from the previous shot` | 2 | Continuity is stated on **both** sides of the cut |

### 3.7 Negation and role-fencing
Negation is expressed as a **bounded qualifier attached to a positive action**, never as a
standalone "do not" or a negative-prompt list. 45 uses of `without …` in 20 blocks vs. only 2 uses
of `never` and 2 of `rather than`, 1 of `instead of`. Representative shapes:

- `…lifts it vertically with constant speed` + `without shifting the bottle`
- `maintaining the referenced distance and low angle **instead of** orbiting or zooming`
- `changes through distinct economical poses **rather than** fluid full animation`
- `Cross-hatching changes density according to the moving light but **never** changes the product construction.`
- `The mirror reflects the same … movement with correct spatial correspondence **rather than** generating a second independent performer.`
- The only imperative negation in the corpus is inside a direct-edit prompt:
  `do not rotate the logo independently of the cup.` (R04)

### 3.8 Audio-field idioms
- `non_diegetic_music: N/A` — 14 / 39 prompts. Score absence is stated, not omitted.
- Music is described **instrumentally and mechanically**, never emotionally: named instruments +
  tempo + a stop condition. `A 96 BPM pattern of dry electronic clicks and muted hand percussion
  marks each movement accent, ending on one short bass tone.` `A 120 BPM pattern …`, `A sparse 90
  BPM pattern …`, `A 110 BPM electronic pulse …` (BPM given in 4 blocks). The decision note on T02
  makes the rule explicit: "the music is described instrumentally rather than as 'comedic.'"
- Music always carries an **exit instruction**: `then stop under the final held pose`, `stops exactly
  when the title locks`, `ends immediately at the break`, `fading during the final second`,
  `stopping cleanly at the end`, `then hold without a final flourish`.
- `overall_soundscape` follows a two-move shape: **(1) continuous bed** (`continue throughout`,
  `continues underneath`, `establish the location`) then **(2) discrete contact events** in the
  order they occur on screen. Physical impacts live here; score accents live in `non_diegetic_music`.
  T05's note: "physical impact stays in soundscape while score accents remain audience-only."

### 3.9 Visible text
Rendered on-screen text is quoted with **straight double quotes inside the description**, spelling
and capitalisation preserved: `a metal sign reading "EAST TERMINAL"`, `reads "ROUTE 8" in clean
black letters`, `printed "NORTH" wordmark`, `The words "MOVE WITH PURPOSE" assemble left to right
with exact spelling, capitalization, type placement, and line breaks.` No text is invented that the
brief did not supply (T03/R07 decision notes both make this point).

### 3.10 Counting idiom
Quantities are given as literal small integers rather than vague plurals — this is pervasive:
`one neat row`, `two clear bounds`, `three plated dishes`, `exactly three crystals`, `two crisp key
poses`, `two shortening steps`, `Four dry interface-like clicks`, `three quarters of its rotation`,
`two rungs`, `one concise nod`, `one small click`, `rebounds one inch`, `by a few degrees`.

---

## 4. Quick compliance checklist

1. Pick the mode first; if a single image's role is ambiguous, **ask one question** before serialising
   (E01/G11) — do not silently assume I2VA.
2. Emit the mode's exact alignment line (T2VA and Ref2VA have none).
3. Never mix `integrated_multimodal_description` with the six-section Ref2VA format (E05).
4. Open with `[Shot 1] <style clause>, <shot size> shot frames/follows …` — or, in Ref2VA, put the
   style on its own `The target video uses …` line above `[Shot 1]`.
