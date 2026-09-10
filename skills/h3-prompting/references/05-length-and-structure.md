# 05 — Length and Structure

How long an H3 prompt should be, how many shots it should contain, and what to cut when it is too long.

**Provenance tags used throughout**

| Tag | Meaning |
|---|---|
| `[OFFICIAL]` | Stated in MiniMax's own H3 prompt-writing guides / API docs. |
| `[OBSERVED]` | Someone ran it and reported the outcome, or it is a direct measurement of a corpus of worked prompts. |
| `[INFERRED]` | Derived from official structure or from corpus measurement. Nobody tested that violating it degrades output. |
| `[ASSERTED]` | Stated as fact by a source with no evidence behind it. Treat as suspect. |

The corpus referred to below is **39 complete worked prompts** (41 fenced prompt blocks, 2 of which are deliberate fragments) drawn from six curated example files covering all five prompting modes.

---

## 1. THE MEASURED DISTRIBUTION

Counting rules: **"main description field"** = the body of `integrated_multimodal_description:` for T2VA / I2VA / FL2VA / L2VA, and the body of `detailed_description:` for Ref2VA. Field labels excluded; `[Shot N]` markers, `<d>` tags and timestamps included. **"Whole-prompt characters"** = every character you would paste, including the alignment line and blank lines. `[OBSERVED]`

### 1.1 All 39 complete prompts

| Metric | Min | Median | Max | Mean |
|---|---|---|---|---|
| Main-description **words** | 44 | **110** | 389 | 157 |
| Whole-prompt **characters** | 580 | **1139** | 4169 | 1654 |

`[OBSERVED]` This distribution is **bimodal**, not unimodal — three-field prompts and six-field Ref2VA prompts are two different populations. Never quote the combined median as a target.

### 1.2 Three-field modes (T2VA / I2VA / FL2VA / L2VA), n=27

| Metric | Min | Median | Max | Mean |
|---|---|---|---|---|
| `integrated_multimodal_description` **words** | 59 | **100** | 133 | 102 |
| Whole-prompt **characters** | 580 | **1018** | 1343 | 1030 |

`[OBSERVED]` The band is extremely narrow: **24 of 27 fall between 90 and 125 words**.

### 1.3 Six-field Ref2VA, n=12

| Metric | Min | Median | Max | Mean |
|---|---|---|---|---|
| `detailed_description` **words** | 44 | **352** | 389 | 282 |
| Whole-prompt **characters** | 1005 | **3263** | 4169 | 3059 |

`[OBSERVED]` Two of the twelve are deliberately abbreviated demonstration specimens (44 words and 137 words). Excluding them, the real Ref2VA band is **220–389 words** (median ≈ 360) and **2506–4169 characters** (median ≈ 3400).

### 1.4 By mode

| Mode | n | Words min / med / max | Chars min / med / max | Words per second of video |
|---|---|---|---|---|
| T2VA | 10 | 59 / 99.5 / 133 | 580 / 909 / 1173 | ~15 |
| I2VA | 7 | 72 / 97 / 120 | 758 / 1003 / 1192 | ~16 |
| FL2VA | 5 | 105 / 117 / 120 | 1139 / 1246 / 1343 | ~15 |
| L2VA | 5 | 91 / 94 / 111 | 991 / 1052 / 1226 | ~18 |
| Ref2VA | 12 | 44 / 352 / 389 | 1005 / 3263 / 4169 | ~46 |

### 1.5 The two audio fields (all 39 prompts)

| Field | Min words | Median | Max |
|---|---|---|---|
| `overall_soundscape` | 10 | **25** | 34 |
| `non_diegetic_music` (including `N/A`) | 1 | 15 | 31 |
| `non_diegetic_music` (excluding the 14 `N/A`s) | 9 | **19** | 31 |

`[OBSERVED]` `overall_soundscape` is *always* 2 sentences (occasionally 1 or 3), never more. `non_diegetic_music` is 1–2 sentences. **14 of 39 (36 %)** write `non_diegetic_music: N/A`. `[OFFICIAL]` The guides allow `overall_soundscape` 1–4 sentences and `non_diegetic_music` 1–3.

### 1.6 The ceiling

`[OBSERVED]` **Nothing in the corpus of 39 worked examples exceeds 389 words in the description field or 4169 characters overall.** There is no such thing as a "long" gold prompt: the ceiling is roughly **4 kB**.

### 1.7 Headline targets

| Schema | Description-field words | Whole prompt |
|---|---|---|
| Three-field (T2VA / I2VA / FL2VA / L2VA) | **~100** | **~1 kB** |
| Six-field Ref2VA | **~355** | **~3.3 kB** |

`[INFERRED]` — measured across the corpus; no test shows that a longer prompt degrades output.

---

## 2. THE OFFICIAL WORD-COUNT FIGURE, AND ITS TENSION WITH PRACTICE

`[OFFICIAL]` For Ref2VA, the guide states that generation tasks normally run **350–500 English words** in `detailed_description`, and that the field must give every shot composition, appearance, position, environment, lighting, action, state change, camera, sound, and *where each reference takes effect* — it must not read as a plot summary or a list of references.

`[OFFICIAL]` **This is the only word-count figure MiniMax states anywhere.** There is no official word count for `integrated_multimodal_description`.

**The tension, stated plainly:**

| | Official figure | Measured corpus |
|---|---|---|
| Ref2VA `detailed_description` | 350–500 words | median 352; real band 220–389; max 389 |
| Three-field `integrated_multimodal_description` | *(no figure)* | median **100**; max 133 |

`[OBSERVED]` The measured Ref2VA prompts sit at the **bottom edge** of the official band and none reaches its upper half. The three-field prompts run **roughly one third** of the Ref2VA length. `[INFERRED]` Treat 350–500 as a Ref2VA-only figure and read it as "350 is enough"; do not import it into three-field prompts, where the worked examples never exceed 133 words.

### 2.1 Hosted service and local weights are different regimes

**This distinction governs everything below and is routinely collapsed. Do not collapse it.**

| | Hosted service / API | Local open weights |
|---|---|---|
| Length limit | A hard input cap is widely reported; the request is refused above it | **No enforced limit exists.** Nothing rejects a long prompt |
| Failure mode when long | Refusal — you know immediately | **Silent degradation** — it runs, and adherence thins |
| What length costs | Nothing until the cap, then everything | Inference time, and progressively weaker instruction following |

`[ASSERTED]` The figure usually quoted for the hosted cap is **7,000 characters**. It appears in
secondary write-ups and is repeated widely, but it is **not stated in any MiniMax document this
package could verify**. Treat the existence of a hosted cap as likely and its exact value as
unverified.

`[OBSERVED]` Locally there is no forced ceiling. A **30,000-character** prompt generated
successfully, roughly 3× slower. A practitioner running deliberately very long inputs locally
reports they were **not** wholly ignored — degraded adherence, not a cliff.

`[INFERRED]` So the honest statement is: **locally, length is a gradient, not a gate.** Shorter
prompts should give stronger adherence, and every measured working example is short — but nothing
in the corpus establishes a threshold, and nobody has run the controlled comparison that would find
one. A long local prompt is a bet on diminishing control, not a formatting error.

**Other stated caps:**

| Limit | Value | Provenance |
|---|---|---|
| Community prompt-enhancer system prompts | "Maximum length is 2,000 characters" | `[ASSERTED]` — appears in two community enhancer system prompts of unverified provenance; contradicted by working prompts above that length |
| Official prompt-rewriter LoRA template | **no length limit stated** — it constrains fields and shot pacing instead | `[OFFICIAL]` |
| Practical encoder ceiling | ~8k tokens is "already a lot" | `[OBSERVED]` (one practitioner) |

---

## 3. DENSITY: WORDS PER SECOND OF VIDEO

| Schema | Words per second of output | Words per shot |
|---|---|---|
| Three-field (T2VA / I2VA / FL2VA / L2VA) | **~15–18** | 60–100 |
| Six-field Ref2VA | **~46** | 175–195 |

`[OBSERVED]` Ref2VA carries roughly a **3× density multiplier** over the three-field modes for the same runtime. Words-per-shot stays near-constant within each schema, so the honest formula is per-shot, not per-second.

**Working budget by duration** `[INFERRED]` (density × duration, clamped to the observed band):

| Duration | Three-field description words | Ref2VA `detailed_description` words |
|---|---|---|
| 4 s | 60–90 | 180–250 |
| 5 s | 75–105 | 230–300 |
| 6 s | 90–115 | 270–350 |
| 7 s | 100–125 | 320–380 |
| 8 s | 110–135 | 350–390 |
| 10 s | 120–150 | 380–450 |

`[OBSERVED]` Under-writing has a named failure of its own: supply enough text for 5 seconds and request 15, and the model invents filler to cover the gap. `[OFFICIAL]` The official rewriter template makes this a rule: *"Make the number, timing, and pacing of shots appropriate for the requested duration."*

`[OBSERVED]` Over-writing has the inverse failure: *"apparently if you put too many words in it gets fast"* — over-stuffing a fixed duration accelerates the action rather than extending it.

---

## 4. SHOT COUNT

### 4.1 Duration vs shot count, measured

All corpus examples with a stated duration (n=34): `[OBSERVED]`

| Duration | n | Shot counts observed | Mean shots | 1-shot | 2-shot |
|---|---|---|---|---|---|
| 4.00 s | 1 | 1 | 1.00 | 100 % | 0 % |
| 5.00 s | 3 | 1 | 1.00 | 100 % | 0 % |
| 6.00 s | 12 | 1–2 | 1.25 | 75 % | 25 % |
| 7.00 s | 4 | 1–2 | 1.50 | 50 % | 50 % |
| 8.00 s | 12 | 1–2 | 1.75 | 25 % | 75 % |
| 10.00 s | 2 | 1–2 | 1.50 | 50 % | 50 % |

### 4.2 The facts this encodes

- `[OBSERVED]` **No example anywhere uses more than 2 shots.** Max = 2, across all 39 prompts and all five modes.
- `[OBSERVED]` **Cuts land at 40–67 % of runtime, median ≈ 56 %, mean ≈ 55 %.** The 14 numerically timestamped cuts fall at: 3.0, 3.0, 3.2, 3.8, 3.8, 4.0, 4.0, 4.2, 4.5, 4.5, 4.5, 4.8, 5.0, 6.0 s.
- `[OBSERVED]` **No prompt cuts before 3.0 seconds.** Every cut leaves at least 2.2 s of runtime on each side.
- `[OBSERVED]` ≤5 s ⇒ always exactly 1 shot (4/4). 6 s ⇒ 1 shot in 9/12. 8 s ⇒ 2 shots in 9/12.
- `[OBSERVED]` 10 s is still ≤2 shots. **Longer duration buys beats, not cuts.**
- `[OBSERVED]` Modal cross-tab: I2VA is 1-shot in 7/7; FL2VA leans 1-shot; Ref2VA leans 2-shot (7/8).
- `[OFFICIAL]` Shot 1 carries **no** timestamp. Timestamps begin at Shot 2, strictly increasing, all inside the duration.
- `[OFFICIAL]` A cut must add new subject, space, state, viewpoint, or time. A modest change of distance or angle is a **camera move inside the existing shot**, not a cut.
- `[INFERRED]` A timestamp does not imply a cut: `At 00:06.500, the table lamp clicks on` sits inside Shot 1 with no new `[Shot N]` marker.

### 4.3 Recommended shot budget

`[INFERRED]` from the measurements above:

| Duration | Default shots | 2 shots only if | Earliest legal cut |
|---|---|---|---|
| ≤ 5 s | **1** | never — do not cut | — |
| 6 s | **1** | the brief forces it (dialogue must cross a cut; a source video already contains a cut) | 3.0 s |
| 7 s | 1 or **2** | a genuine beat change exists | 3.0 s |
| 8 s | **2** | 1 shot for continuous-transformation work | 3.2–4.5 s |
| 10 s | **2** | — | 4.0–6.0 s |
| 12–15 s | **2** | more only with an explicit reason; no worked example exists above 2 | 5.0–8.0 s |

Place the cut at **50–60 % of runtime**. Never before 3.0 s. Never leave a shot shorter than ~2.2 s.

`[OBSERVED]` **Dissent worth printing:** community practitioners routinely run far higher shot counts — 3 shots in ~4.5 s, 5 shots in exactly 5 s (one per second), 7 shots in 15 s, and one reported-working prompt with **14 shots in ~14 s**. `[OBSERVED]` Separately, one practitioner reports the model has its own preferred subdivision, consistently splitting a 15-second output into three 5-second shots even when given uneven timing cues. `[INFERRED]` These are single, uncontrolled reports of "it generated". The curated corpus is the only source where shot count was chosen deliberately and the result was judged good. Follow the corpus by default; treat >2 shots as an explicit, justified departure.

`[OBSERVED]` **Adding `[Shot 2]` is what creates the cut.** A practitioner who kept getting unwanted camera changes fixed it by using `[Shot 1]` only. If you want one continuous take, use one shot marker and say so in words.

---

## 5. WHY MORE IS NOT BETTER

The evidence is genuinely split. Both sides, honestly:

### 5.1 Pro-length `[OBSERVED]`

- *"I literally feel like I can make anything my mind can imagine, with a crazy long prompt and it nails what I was thinking."*
- *"There's incredibly detailled giant prompt that were used and the model follow perfectly here."*
- *"i had to use gazilion words to prompt it so that it works perfectly lol"*
- *"one sentence prompts do work, but expect it to wander off"* — i.e. length buys **control**, not capability.
- Rationale offered: the model was probably trained on long prompts.
- `[OBSERVED]` A **30,000-character prompt did generate successfully** — *"the videos were like 3x slower haha."* Length costs inference time, not validity. There is no evidence of a hard truncation point in the encoder.

### 5.2 Anti-length `[OBSERVED]`

- *"The ref images already serve as strong guide. U don't have to write long prompt every time."*
- *"you can define or undefine anything in the main prompt so isnt needed."*
- *"what i'm absolutely amazed by is how little you can type and get super cool effects."*
- *"too much text lol"*
- *"apparently if you put too many words in it gets fast"* — over-stuffing a fixed duration accelerates the action.
- **Full-reference degradation:** *"Whenever the prompt is to detailed it just seems to become t2v ignoring ref video."* Corroborated: *"It does seem to struggle with longer prompts, often ignoring specific instructions such as who speaks when, sound effects etc."* `[OBSERVED]` — 2 independent reporters, uncontrolled, single-seed. This is the single most consequential anti-length report: an over-long Ref2VA prompt is reported to **silently fall back toward text-to-video**, ignoring the references entirely, and to dilute instruction adherence.
- `[OBSERVED]` A related, better-corroborated failure: an overloaded prompt with too many actions for the runtime causes **requested dialogue to be silently dropped**.

### 5.3 The formulation the evidence best supports

> **The failure variable is conflicting or redundant instruction, not raw length.**

`[INFERRED]` This is the reading that reconciles both columns: nobody has shown that adding *non-conflicting, correctly-keyed* text degrades a result, and one 30k-character prompt survived; but every reported length failure is also a redundancy or contradiction failure — a re-defined attribute, a second camera instruction, an action count the runtime cannot hold, or a reference whose role is buried under description.

The two practitioner formulations that state it best, quoted verbatim `[OBSERVED]`:

> *"i think you must be careful to not re-define stuff when not needed. and pay attention to conflicting instructions, if you add too much it will be there."*

> *"the main takeaway for H3 is providing a structured prompt that the text encoder can understand rather than offering conflicting or confusing instructions."*

And the honest null result `[OBSERVED]`:

> *"Never can quite tell with prompting, sometimes super simple works, other times going overboard was what worked."*

**Operational consequence.** Do not audit a prompt by its character count. Audit it by asking, of every sentence: *does this define something not already defined, and does it contradict nothing already written?* If yes, it is free regardless of length. If no, it is a liability regardless of length.

---

## 6. A PRACTICAL BUDGET

### 6.1 What to spend words on, in priority order

`[INFERRED]` from corpus structure plus the official field requirements. Rank 1 is written first and cut last.

| Rank | Item | Typical cost | Why it ranks here |
|---|---|---|---|
| 1 | Exact anchors — dialogue text, visible text spelling, keyframe alignment line, requested duration | 10–30 w | `[OFFICIAL]` A style choice may never alter exact dialogue, visible text, keyframe alignment, identity anchors, product geometry, or declared reference roles |
| 2 | Reference role bindings (`subject_definitions`, `retention_analysis`) | 60–120 w | `[OBSERVED]` *"if it aint in the prompt it will ignore it completely"* — an unbound reference slot does nothing |
| 3 | The style/medium opening clause | 15–30 w | `[OBSERVED]` Starting with the medium ("Live-action video", "2D animation") is reported to make a large difference; `[OFFICIAL]` for Ref2VA's `The target video uses …` line |
| 4 | Shot 1 subject, framing, environment | 25–40 w | Establishes what everything else modifies |
| 5 | The causal action chain, phase by phase, including the **terminal event** | 30–60 w | `[OBSERVED]` H3 does not reliably infer the payoff from the setup |
| 6 | One camera move per shot, with amplitude and speed | 10–20 w | `[OFFICIAL]` amplitude and speed are separate documented axes |
| 7 | Identity re-assertion at each shot boundary | 15–25 w | `[OBSERVED]` mitigates face drift across a cut |
| 8 | The explicit end state (settle, or the convergence formula) | 20–45 w | `[OBSERVED]` every corpus prompt terminates with one; none simply stops |
| 9 | `overall_soundscape` — continuous bed, then discrete contact events | ~25 w | `[OBSERVED]` corpus median 25 words, always 2 sentences |
| 10 | `non_diegetic_music` — instrumentation, tempo, exit condition | ~19 w, or `N/A` | `[OBSERVED]` 36 % of the corpus writes `N/A` |
| 11 | Secondary motion, overlap, follow-through, micro-beats | 15–40 w | Quality layer; the first thing that is genuinely optional |
| 12 | Atmosphere and decorative texture | any | Pure decoration |

### 6.2 What to cut first when over budget

`[OFFICIAL]` for the ordering principle (compress decorative detail, repeated provenance, and duplicated sound descriptions first; never delete a reference label, task-type prefix, exact dialogue, or an endpoint constraint to save characters). `[INFERRED]` for the ranked list.

| Order | Cut this | Never cut this |
|---|---|---|
| 1 | Decorative atmosphere, mood adjectives, "cinematic / beautiful / stunning" | — |
| 2 | Repeated provenance — the same reference re-cited in every sentence | The **first** citation of each reference |
| 3 | Sound detail duplicated between the description and `overall_soundscape` | The bed-then-events shape |
| 4 | Restated camera intent (one control described three ways) | The single amplitude+speed clause |
| 5 | Secondary motion and micro-beats on non-focal objects | Follow-through on the focal action |
| 6 | Style restated in Shot 2 | Style in Shot 1 / the Ref2VA style line |
| 7 | A whole extra action beat — and shorten the action chain, not the anchors | The terminal event of the primary action |
| 8 | A second shot, folded back into one shot with an in-shot camera move | — |
| — | — | Exact dialogue, visible-text spelling, the alignment line, the task-type tag, reference labels and roles, the end-state sentence |

`[OBSERVED]` If cutting reaches rank 7, prefer removing an entire beat over thinning every beat: the named failure of too many beats for the runtime is dropped dialogue and accelerated action, not merely vagueness.

---

## 7. INSTRUCTION BLEED

**The behaviour.** `[OBSERVED]` An action or attribute described anywhere in the prompt tends to migrate into shots, regions, subjects, and references where it was not requested.

Attested forms:

| Form | Report | Provenance |
|---|---|---|
| Reference-role bleed | An identity picture also supplies lighting, grade, background, pose, framing, composition | `[OBSERVED]` — 2 practitioners converged independently on the same fix |
| Cross-reference contamination | A trait from one reference mutates onto a different reference's subject | `[OBSERVED]` — 2 reports |
| Regional bleed | An instruction scoped to one body region affects another; "body on 4s, face on 2s" returns one blended cadence | `[OBSERVED]` — 1 test |
| Camera / performance bleed | The camera treatment absorbs the character's timing, or vice versa | `[ASSERTED]` |
| Over-literal reference | The model copies the whole source instead of taking guidance | `[OBSERVED]` |

**The rule this implies.** `[INFERRED]` The prompt is not read as a set of scoped blocks. An action that **must not happen in a given shot has to be excluded in that shot explicitly** — it is not enough that you only described it in the other shot.

**How to exclude, in the corpus's own grammar** `[OBSERVED]` — negation is written as a **bounded qualifier attached to a positive action**, never as a standalone "do not" and never as a trailing negative list:

```
lifts it vertically with constant speed without shifting the bottle
maintaining the referenced distance and low angle instead of orbiting or zooming
changes through distinct economical poses rather than fluid full animation
Cross-hatching changes density according to the moving light but never changes the product construction.
```

`[OBSERVED]` The corpus uses `without …` **45 times across 20 blocks**, against 2 uses of `never`, 2 of `rather than`, 1 of `instead of`, and exactly **one** bare imperative negation in 41 blocks.

**Fencing a reference** `[OBSERVED]` — the shape two practitioners arrived at independently, one reporting reduced flicker:

```
<Subject 1> is only the identity, face, hair, age, and distinguishing physical features of the woman in <Picture 1>. <Picture 1> provides subject identity only. It does not provide lighting, exposure, color grading, background, camera angle, pose, framing, or scene composition.
```

**Fencing a role positively and negatively** `[OBSERVED]`:

```
<Video 1> supplies the camera path, framing, background, lighting, composition, and action timing. It does not supply the face or identity.
```

**Excluding an action from one shot** `[INFERRED]` — the same grammar, applied per shot:

```
[Shot 2] At 00:04.500, the shot cuts to a close view of her hands. She continues folding the cloth without speaking and without turning toward the door.
```

**Caveats to print.** `[OBSERVED]` H3 has no negative prompt (it runs at CFG 1); in-prompt negation is the community's substitute, and **nothing in any source measures how H3 handles negation**. `[OBSERVED]` Escalating suppression language — stronger `freeze` / `hold` / `unchanged` — makes results *worse*, producing freeze frames, hard substitution and timing drift. `[ASSERTED]` Use a negation only to block a **likely, named** failure; never as a habitual trailing list.

---

## 8. HOLDS, PAUSES, AND "NO CUT HERE"

### 8.1 How to phrase a hold so it is not compressed away

`[OBSERVED]` A hold is compressed away for two distinct reasons, with two different fixes:

| Cause | Symptom | Fix |
|---|---|---|
| Too much competing instruction for the runtime | The whole clip speeds up; the pause vanishes | Remove a beat, not words from every beat |
| The hold is described as an absence | Nothing renders; the model in-betweens through it | Describe the hold as a **positive, visible state with a duration and a terminating event** |

`[OBSERVED]` **Do not escalate.** Stronger `freeze` / `hold` / `unchanged` wording is reported to degrade into freeze frames, hard substitution and timing drift. Return to the positive form instead.

**Working shapes, from the corpus** `[OBSERVED]` — `hold`/`holds` appears 22 times across 15 blocks; `settle`/`settles` 15 times across 14:

```
a brief still hold
steadies for a brief beat
pauses just long enough for steam to clear her face
the camera holds a static shot
held key poses, selective eye and mouth movement
a fast anticipation and clean held settle
both workers hold exaggeratedly neutral poses. Only their pupils shift toward the cabinet
The torso remains on the held key pose while only the eyes shift left, then the head snaps to the next held drawing.
her cape settles one beat after her shoulders
overshoots slightly, returns, and settles
The shot ends exactly on that frame without a late blink or camera drift.
```

**The four ingredients of a hold that survives** `[INFERRED]`:

1. **Name what is still** — the specific parts, not "she is still": *the torso remains on the held key pose*.
2. **Name what still moves** — a hold with zero motion reads as a freeze; give it one small residual (pupils, steam, dust, a flame). `[OBSERVED]` Every corpus hold has a moving element somewhere in frame.
3. **Give it a boundary** — either a duration phrase (`During the final two seconds`, `for a brief beat`, `one beat after`) or an explicit timestamp: `At 00:06.500, …`.
4. **Give it an exit** — the event that ends the hold. `[OBSERVED]` Nothing in the corpus stops abruptly without a settle or a terminating event.

**Timestamped in-shot beats** `[OBSERVED]` are the strongest available tool for pinning a pause inside a shot, and they do not create a cut (see 8.2):

```
At 00:00–00:03.0, ...   At 00:03.0–00:06.5, ...   At 00:06.5–00:08.5, ...
```

`[INFERRED]` Do not ask for fewer in-between poses as a way of asking for a pause — the reported side effect is that the whole action slows down. If you want fewer poses at the same tempo, say so: *maintain the same overall action duration and rhythm while using fewer unique intermediate poses.*

### 8.2 How to phrase "no cut here"

`[OBSERVED]` **The `[Shot N]` marker is the cut.** Adding `[Shot 2]` is what makes the model cut to another angle; a practitioner who kept getting unwanted camera changes fixed it by using `[Shot 1]` only.

`[INFERRED]` Three moves, in order of strength:

1. **Emit exactly one `[Shot 1]` marker.** No second marker means no cut. This is the primary control.
2. **Say it in words inside the shot** `[OBSERVED]` — the phrasing a practitioner reports working: *in one continuous, unbroken single shot*.
3. **Use time-beats, not shot markers, to structure the interior** `[OBSERVED]`:

```
integrated_multimodal_description: [Shot 1] <style clause>, <framing> <subject> <place>. At 00:00–00:03.0, ... At 00:03.0–00:06.5, ... At 00:06.5–00:08.5, ...
```

`[INFERRED]` A timestamp alone does not create a shot. An in-shot timed event is written without a `[Shot N]` marker:

```
At 00:06.500, the table lamp clicks on and the room warms one stop.
```

**Over-specifying a locked camera** `[OBSERVED]` — the form one practitioner used to fix drift, quoted verbatim:

> *"the camera is locked off with zero movement and zero speed for the entire video, with no pan, tilt, zoom, dolly, shake, or reframing… The camera does not move at any point."*

`[OBSERVED]` The corpus's lighter default is to assert static positively and once — `The camera holds a static shot` / `holds static` / `remains static`, used in 9 of 9 locked shots and never left to omission.

**Continuity across a cut you *do* want** `[OFFICIAL]` — when a spoken line crosses the boundary, put `<scenetrans>` at the end of the pre-cut fragment **and** the start of the post-cut fragment, and state continuity on both sides:

```
<d>[English] I thought the road <scenetrans></d> Her voice continues seamlessly across the cut.
... as the same voice carries over uninterrupted from the previous shot: <d>[English] <scenetrans>would take us home.</d>
```

`[INFERRED]` `<scenetrans>` and `<cutoff>` are the lowest-confidence items in the official tag family — one verification pass could not surface them in the retrieved base guide. They are consistent with the rest of the tag family; keep using them, but do not build a prompt whose only mechanism is `<scenetrans>`.
