# H3 Prompting — Failure Modes

The diagnostic reference. Open this when a generation came back wrong.

123 entries in nine chapters, plus a contradictions register and an appendix of issues that are
**not** prompt problems. Each entry is ID / SYMPTOM / CAUSE / FIX / EVIDENCE, and the fix is
written as prompt language you can copy rather than as advice.

---

## Start here — symptom router

Find what you actually saw. The IDs point into the chapters below.

### The cutting is wrong

| What you saw | Look at |
|---|---|
| It cut to another angle I never asked for | CUT-03, CUT-04, CAM-06 |
| Too many cuts; every shot is over before it lands | CUT-05 |
| A cut lands mid-sentence and the line restarts | CUT-06, AUD-22 |
| My loop doesn't loop — it ends on a freeze or a fade | CUT-07 |
| Cut times came out wrong or out of order | CUT-01, CUT-02, STR-04 |

### The camera is wrong

| What you saw | Look at |
|---|---|
| The camera drifted when I wanted it still | CAM-05 |
| I asked for a push and got a crop (or the reverse) | CAM-02 |
| My camera instruction was ignored completely | CAM-01 |
| The camera roams and I can't see the action I wrote | CAM-06 |
| A movement toward or away from camera is invisible | CAM-05, and see `02-camera-and-motion.md` §8 on travel axis |

### The motion is wrong

| What you saw | Look at |
|---|---|
| The action never finishes — it starts and then just holds | MOT-01 |
| Fast action smears into mush | MOT-09, and `02-camera-and-motion.md` §7 |
| I asked for stepped/limited animation and got smooth interpolation | MOT-02, MOT-04, MOT-06, MOT-08, MOT-11 |
| Ghost copies, onion skins, or multiple characters appeared | MOT-07 |
| Poses teleport with no path between them | MOT-12 |
| The background slides under the character | MOT-18 |
| Holding harder made it worse, not better | NEG-02, MOT-06 |

### The characters are wrong

| What you saw | Look at |
|---|---|
| The face degrades as the clip runs | SUB-01 |
| Likeness holds in closeup but collapses in wide shots | SUB-02 |
| Wrong character speaks the line | SUB-06, AUD-04 |
| A trait from one reference ended up on a different character | REF-19, NEG-05 |
| Wrong number of objects or people | SUB-10 |
| My emotional direction produced nothing visible | SUB-04 |

### The references aren't working

| What you saw | Look at |
|---|---|
| It ignored my reference image and redrew the scene | REF-18, REF-24, and `03-reference-inputs.md` §3 |
| It ignored my start frame | Appendix A1 — this is an engine bug, not a prompt problem |
| Adding more references didn't improve likeness | REF-20 |
| A reference's background or lighting came along with the identity | LOOK-08, LOOK-03, NEG-10 |
| One reference was silently dropped | REF-17 |
| Motion transfer isn't precise | REF-21 |
| The label roles came out wrong | REF-01 … REF-13 |

### The audio is wrong

| What you saw | Look at |
|---|---|
| There is speech I never wrote; gibberish | AUD-13, and `04-audio-and-dialogue.md` §4 |
| Subtitles are burned into the picture | `04-audio-and-dialogue.md` §3 — remove quotes inside `<d>` |
| Music appeared though I asked for none | AUD-02, AUD-10 |
| A character who should be silent keeps talking | AUD-14 |
| The line is delivered too fast to follow | AUD-22, CUT-06 |
| Two voices blended or swapped | AUD-18 |
| My voice reference dragged its original words in | AUD-08 |
| The character mouths the voiceover | AUD-05 |

### The look is wrong

| What you saw | Look at |
|---|---|
| It looks like TV or social media, not like film | LOOK-04, LOOK-05, CUT-05 |
| Skin is plastic; I can't get a rough or amateur look | LOOK-07 |
| The style is incoherent — several looks at once | LOOK-01 |
| My style words did nothing | LOOK-02, LOOK-04, SUB-05 |
| A subject looks pasted in rather than lit by the scene | LOOK-08, and `03-reference-inputs.md` |

### It ignored what I told it

| What you saw | Look at |
|---|---|
| My "do not" was ignored | NEG-01, NEG-03, NEG-04 |
| An instruction leaked into a shot where it didn't belong | NEG-05, NEG-06, NEG-07 |
| Actions or lines were silently dropped | STR-11, and `05-length-and-structure.md` |
| It behaved as if there were no references at all | REF-18, STR-11 — suspect prompt length first |

---
## How to read EVIDENCE

| Grade | Means |
|---|---|
| **OFFICIAL** | Stated in MiniMax's own `VIDEO_PROMPT_WRITING_GUIDE_base_en` / `_ref_en` (or the H3 README / API docs). kit2 verified both guides char-for-char against HuggingFace; kit1 restates the same rules. |
| **OBSERVED** | Someone ran it and reported the outcome. Observer and test count named. Includes named-implementer reports of shipped behaviour (Kijai), which are labelled as such. Almost all of these are single-seed, single-author, qualitatively self-rated — Kijai's own warning applies: *"many prompts/seeds are needed to compare methods rather than a single sample."* |
| **INFERRED** | A plausible rule derived from official structure or from measuring the gold corpus. Nobody tested that violating it degrades output. |
| **ASSERTED** | The kits state it as fact with no evidence. **Treat as suspect.** Everything in the kits' craft layer is here: pack IDs `V01–V24` / `M01–M08` / `F01–F08` / `A01–A08`, the 30 style anchors, "one action beat per 1–3 seconds", "exactly one pack per category", "bind 1–3 sound events", "one or two smear breakdowns", the keyword→pack routing tables, the style evidence-priority ordering, the 0–25 scoring rubric, and the 5-level cadence ladder as a *procedure*. None of it is H3 interface vocabulary — nothing in H3 recognises "V19" or "M08". |

Primary observers referenced throughout:
**The Shadow (NYC)** — 20-test T2VA batch, 2026-08-07, 5 s / 16:9 / 0.5 MP / seed locked / generic subjects, plus an earlier Aug 4 set (864×480, Int8, ComfyUI default T2V, no refs) and ~11 loop attempts. Single author, no blind evaluation, no repeat runs, no rubric; ratings are the words "strong"/"very strong"/"excellent".
**kit2 file 15 lab** — controlled T2VA cadence tests at 24 fps, static camera, simple backgrounds; **n is never reported**.
**Kijai** — ComfyUI implementer; describes shipped behaviour, not controlled tests.
**Banodoco Hivemind** — named practitioners, uncontrolled single reports.

---

# 1. STRUCTURE & LENGTH

| ID | SYMPTOM | CAUSE | FIX | EVIDENCE |
|---|---|---|---|---|
| STR-01 | Six-section Ref2VA prompt opens `integrated_multimodal_description:`; or a three-field prompt contains `subject_definitions:` | Field sets of the two grammars treated as interchangeable | Ref2VA starts `subject_definitions:` and never contains `integrated_multimodal_description`. Keyframe modes use exactly `integrated_multimodal_description`, `overall_soundscape`, `non_diegetic_music` | OFFICIAL |
| STR-02 | Sections present but reordered, renamed, or one missing | Free-form assembly | Fixed order, no substitutes: `subject_definitions` → `summary` → `retention_analysis` → `detailed_description` → `overall_soundscape` → `non_diegetic_music` | OFFICIAL |
| STR-03 | Alignment line missing, invented, or emitted for T2VA/Ref2VA | Header treated as optional boilerplate | Emit the mode's exact string, then **one blank line**. I2VA: `For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.` FL2VA: `How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot N) aligns with the S.SS-second mark of the target video.` L2VA: `How the reference pictures align with the target video — <Picture 1> (from [Shot N]) aligns with the S.SS-second mark of the target video.` T2VA and Ref2VA: none | OFFICIAL |
| STR-04 | `S.SS`, `N`, or `[Shot N]` survive into the delivered prompt; duration written `8` or `8.0` | Template not resolved | Write the effective duration to exactly two decimals — `8.00-second mark` — and substitute the real final shot index everywhere | OFFICIAL |
| STR-05 | Alignment line says `[Shot 1]` on a two-shot L2VA/FL2VA clip | Header hard-coded to shot 1 | The anchored picture belongs to the **last** shot: `<Picture 1> (from [Shot 2]) aligns with the 7.00-second mark`. Cross-check the shot index against the actual final `[Shot N]` marker | OFFICIAL |
| STR-06 | Output contains `integrated\_multimodal\_description` or `\<Subject 1>` | Markdown escaping applied to canonical syntax | Emit one fenced `text` block; canonical tokens stay literal with no backslashes | INFERRED (from the official exact-field-name rule) |
| STR-07 | Hosted API rejects the request on prompt length | Prompt over 7000 characters | Compress decorative detail, repeated provenance, and duplicated sound descriptions first. Never delete a reference label, task-type prefix, exact dialogue, or endpoint constraint to save characters | OFFICIAL (7000-char hosted limit) |
| STR-08 | Bloated prompt with no added control | Padding mistaken for specificity | Target ~100 words / ~1 kB for three-field modes and ~355 words / ~3.3 kB for Ref2VA. Ceilings in the entire gold corpus: 389 words in the description field, 4169 characters overall | INFERRED (measured across 39 gold prompts; no test shows longer prompts degrade) |
| STR-09 | `detailed_description` reads as a plot summary or a list of references | Ref2VA description written as narration rather than staging | Give every shot composition, appearance, position, environment, lighting, action, state change, camera, sound, and *where each reference takes effect*. Generation tasks normally run 350–500 English words | OFFICIAL |
| STR-10 | Ref2VA jumps straight to `[Shot 1]` with no look established | Style opener omitted | One or two sentences before `[Shot 1]`: `The target video uses photoreal live-action restaurant cinematography with warm overhead practicals, controlled stainless-steel reflections, and restrained handheld movement.` | OFFICIAL |
| STR-11 | Requested actions or dialogue silently dropped from the render | Prompt overloaded with unrelated beats for the runtime | One location, one causal action chain, one purposeful camera move for short clips. seitanism: *"an overloaded prompt with too many actions can also cause dialogue to just be dropped"* | OBSERVED (seitanism, 1 report) — the numeric *"one dominant action beat per roughly 1–3 seconds"* is **ASSERTED** |
| STR-12 | Prompt arrives wrapped in rationale, mode analysis, a settings table, or an offer to render | Compiler emits commentary with the deliverable | Return only the prompt. The single permitted exception is one concise clarification question, alone | ASSERTED (kit product rule; a compiler behaviour, not an H3 behaviour) |
| STR-13 | `<STYLE CLAUSE>`, `<SUBJECT>`, or similar placeholders reach the model | Skeleton delivered unfilled | Run a placeholder sweep before delivery; no angle-bracket token may survive except `<Picture N>`, `<Video N>`, `<Audio N>`, `<Subject N>`, `<d>`, `<scenetrans>`, `<cutoff>` | INFERRED |

---

# 2. SHOTS & CUTTING

| ID | SYMPTOM | CAUSE | FIX | EVIDENCE |
|---|---|---|---|---|
| CUT-01 | `[Shot 1] At 00:00.000, ...` | Timestamp applied uniformly | Shot 1 carries **no** timestamp. Timestamps begin at Shot 2 | OFFICIAL |
| CUT-02 | Cut times repeat, decrease, or exceed the clip length | Times authored per shot without a global check | Strictly increasing, all inside the duration, in playback order: `[Shot 2] At 00:04.500, the shot cuts to ...` | OFFICIAL |
| CUT-03 | Clip is chopped into cuts that only change distance or angle | Cut used as pacing decoration | A cut must add new subject, space, state, viewpoint, or time. For a modest distance or angle change write a camera move inside the existing shot instead | OFFICIAL |
| CUT-04 | An in-shot timed event gets promoted to a new `[Shot N]` | Timestamp read as a cut marker | A timestamp can mark an event without creating a shot: `At 00:06.500, the table lamp clicks on` stays inside Shot 1 with no new marker | ASSERTED (kit2 example decision note) |
| CUT-05 | A 5-second clip carries three cuts; each shot is under 2 seconds | Shot count scaled to ambition, not runtime | ≤5 s ⇒ 1 shot. 6 s ⇒ 1 shot unless the brief forces a cut. 8 s ⇒ 2 shots. Never more than 2. Earliest cut anywhere in the corpus is 3.0 s; cuts sit at 40–67 % of runtime, median 56 % | INFERRED (measured over 34 gold prompts with stated durations; kit1 explicitly denies that "~5 s = one shot" is a law) |
| CUT-06 | A spoken line is truncated or restarts at a cut | Audio continuity not declared across the boundary | Put `<scenetrans>` at the end of the pre-cut fragment **and** the start of the post-cut fragment, and state continuity on both sides: `<d>[English] I thought the road <scenetrans></d> Her voice continues seamlessly across the cut.` … `<d>[English] <scenetrans>would take us home.</d>` | OFFICIAL (least-corroborated official item — kit2 could not surface `<scenetrans>`/`<cutoff>` in the retrieved base guide) |
| CUT-07 | Loop request ends on a freeze, fade, dead stop, or a terminal musical cadence | Ordinary final-landing logic applied to a cyclic brief | Match the closing state to the opening: pose, screen position, object orientation, camera position and motion phase, direction, velocity, hair/cloth phase, particles, lighting, sound and music phase. No pause, fade, or terminal cadence. Never promise a seamless loop | OBSERVED (The Shadow, ~11 loop attempts, self-described *"hit or miss"*, no per-loop ratings) — the 13-dimension matching list is **ASSERTED** |
| CUT-08 | A direct video edit gets invented cut timestamps that fight the source | Edit treated as fresh authoring | The source owns its cuts: `[Shot 2] At the original source cut time, preserve the source close-up ...` | ASSERTED (kit2 gold example) |

---

# 3. CAMERA

| ID | SYMPTOM | CAUSE | FIX | EVIDENCE |
|---|---|---|---|---|
| CAM-01 | Camera written as detached tags — `[pan]`, `[zoom]`, `[static]`, `Camera: push in, slow, small amplitude.` | Bracket shorthand copied from the high-level API examples | Write camera behaviour as prose inside the shot: `The camera pushes in with small amplitude at slow speed toward the key in her palm.` See C2 | OFFICIAL (prompt-writing guide) |
| CAM-02 | "Zoom in" produces a dolly, or vice versa | Optical and physical moves conflated | `Zoom In` / `Zoom Out` change focal length with the body fixed. `Push In` / `Pull Out` physically move the camera. Same distinction for `Truck` (lateral translation) vs `Pan` (fixed pivot), and `Pedestal` vs `Tilt` | OFFICIAL |
| CAM-03 | Every move carries `with medium amplitude at normal speed` | Modifiers applied mechanically | State amplitude and speed only when they matter. Normal speed and medium amplitude are implicit. Canonical modifiers are exactly `with small amplitude`, `with large amplitude`, `at slow speed`, `at fast speed` | OFFICIAL |
| CAM-04 | `The camera slowly pushes in, moving gradually closer at a slow pace` | One control restated three ways | `The camera pushes in slowly.` | INFERRED |
| CAM-05 | Camera drifts in a shot that was meant to be locked | Static left implied by omission | Assert it: `The camera holds a static shot.` — the gold corpus states static positively in 9 of 9 locked shots and never leaves it to omission | INFERRED (corpus measurement) |
| CAM-06 | Orbiting/roaming camera hides the body mechanics the shot exists to show | Decorative cinematography added unrequested | One camera move per shot, described once at the start and referenced again only at the ending. For mechanics, timing, pose, or locomotion work prefer a locked camera or a simple track | OBSERVED (The Shadow deliberately locked the camera across several principle tests so mechanics could be evaluated) — "exactly one move per shot" is INFERRED from the corpus |

---

# 4. MOTION & PHYSICS

| ID | SYMPTOM | CAUSE | FIX | EVIDENCE |
|---|---|---|---|---|
| MOT-01 | A multi-stage action is compressed into one verb — "does an ollie dynamically", "swings the sword dramatically" — and the render stalls before the payoff. The xerographic archer drew, aimed, and **never released** | H3 does not reliably infer the terminal event from the setup | Name the phases and the terminal event: `She draws to full tension, steadies for a brief beat, releases her fingers, the bowstring snaps forward, the arrow leaves the bow, and her bow arm absorbs the small recoil.` Structure = setup → commitment → **terminal event** → immediate reaction/follow-through | OBSERVED (The Shadow, paired tests: archer failed to release; skate ollie, which named anticipation/compression/takeoff/airborne/landing, completed cleanly) |
| MOT-02 | `on ones` requested; output shows paired `AA, BB, CC` cadence | Articulated 2D walks carry a paired-frame bias regardless of the requested direction | Keep the user's term and add the visible consequence: `target a newly advanced authored state on every successive frame: A, B, C, D; do not intentionally repeat paired states`. Never promise literal ON-1 | OBSERVED (The Shadow, 3 tests: dance-on-ones, walk-on-ones, digital ink-and-paint walk — all drifted to pairs; walk-on-twos landed) |
| MOT-03 | `on twos` requested; output is continuously interpolated (jump rope) | The paired bias is action-specific, not a model-wide law | Treat ON-2 as a scoped tendency for articulated 2D walking only. For other actions state the pattern explicitly rather than assuming the model will drift into it | OBSERVED (The Shadow, 1 direct counterexample) |
| MOT-04 | Exposure jargon is the only cadence instruction and nothing changes | H3 follows animation principles and production technique more reliably than exposure math | Always pair the term with observable behaviour: distinct held drawings, stepped pose changes, reduced in-between density, wider spacing during fast travel, deliberate holds | OBSERVED (The Shadow, cross-conclusion of the 20-test batch; his own caveat: *"not proof that exposure terms never work"*) |
| MOT-05 | "Body on 4s, face on 2s" comes back with one blended cadence | Independent regional exposure rates are not reliably controllable | Do not request separate per-region rates. Say which parts hold and which move: `The torso remains on the held key pose while only the eyes shift left, then the head snaps to the next held drawing.` | OBSERVED (The Shadow, 1 test) |
| MOT-06 | ON 4 / ON 8 collapse toward ON 2, or degrade into freeze frames, smooth travel between landmarks, hard substitution, and timing drift | Large scheduled pose intervals acquire editing semantics | Do **not** escalate `freeze` / `hold` / `unchanged`. Keep the same in-place action, re-test ON 1 as a control, simplify the subject, and treat literal four- or eight-frame repetition as unverified | OBSERVED (kit2 file 15 lab, Findings D and E; n unreported) |
| MOT-07 | Multiple copies of the character on screen — onion skins, ghost poses, contact sheets, motion trails | Sparse pose lists read as a pose chart rather than a timeline | Add verbatim: `Exactly one opaque character is visible at every instant. Previous and future poses never remain on screen. Do not show onion skins, ghost poses, sequential figures, contact sheets, or duplicated bodies.` Then simplify to an in-place action. Duplicated bodies are **not** evidence that ON-2 worked | OBSERVED (kit2 file 15 lab Finding B; n unreported) |
| MOT-08 | A walk that travels left-to-right is smoothly interpolated no matter what cadence is asked for | Translational locomotion encourages continuous in-betweening | Diagnose cadence with a march or walk **in place**, fixed screen position, static camera, plain background. Add travel only after the cadence is stable, and state that previous poses disappear rather than remaining as spatial copies | OBSERVED (kit2 file 15 lab Finding B; The Shadow v1.5 package; no counts or seeds) |
| MOT-09 | A requested character smear renders as a detached graphic speed streak or photographic motion blur | Smear interpreted as an effects overlay | Demand body deformation explicitly: `during the fastest transition, use one or two hand-drawn smear breakdowns with elongated limb and facial shapes and directional contour trails, then resolve immediately into a clean landing pose; the character's body itself stretches into the smear and is not replaced by detached speed lines or photographic blur`. Expect partial compliance | OBSERVED (The Shadow, action-smear test partially failed; the double-take smear embedded in a full anticipation→smear→landing→follow-through grammar was rated excellent) |
| MOT-10 | Reducing in-betweens also slows the action down | Fewer states misread as a slower performance | State it: `maintain the same overall action duration and rhythm while using fewer unique intermediate poses, so successive authored states cover larger motion increments` | INFERRED (listed in the kit2 lab's repair table with no reported run) |
| MOT-11 | Limited or graphic animation is forced into continuous in-betweening | "Good animation" equated with maximum interpolation | Ask for the medium's own temporal grammar — held poses, stepped pose-to-pose timing, discrete replacement, sparse in-betweens, no photographic motion blur — and never write "smooth" over it | OBSERVED (The Shadow: modernist limited animation rated "very strong", and understood *better* than literal frame-count instructions) |
| MOT-12 | Realistic live-action motion teleports between poses with no visible path | Stylised discontinuity leaking into a continuous medium | For realistic motion describe continuous physical development. Unintended discontinuity is a failure; intentional graphic replacement is not | ASSERTED (kit rule; reversed once inside the project, never tested either way) |
| MOT-13 | "Limited animation, but extremely fluid and continuously smooth" produces neither | Incompatible instructions stacked | Replace the contradiction with a parts breakdown of what holds and what moves | INFERRED |
| MOT-14 | Head and ponytail stop at the same instant; or every accessory lags by the identical amount | Overlap either omitted or applied mechanically | Sequence one cause: `Her torso stops first. The ponytail continues forward from inertia, overshoots, rebounds once, and settles after the body is already stable.` Different masses settle differently — do not run eyes→head→shoulders→hips through every gesture | OBSERVED (The Shadow, follow-through isolation test rated "excellent demonstration") |
| MOT-15 | Intentional line boil read as identity drift, or texture cycling makes held poses look temporally unique | Handmade frame variation not separated from pose state | For hand-drawn work keep silhouette and colour-region boundaries continuously present and spatially stable, and let only internal pigment, paper tooth, and edge irregularity cycle. For strict cadence tests suppress line boil and texture cycling | OBSERVED for the positive (The Shadow, rough line-boil test "very strong"); **ASSERTED** for the claim that boil disguises held states |
| MOT-16 | Infographic bars get weight transfer, planted feet, and hair follow-through | One motion grammar applied to every medium | Motion-graphics vocabulary: easing, stagger, alignment, overshoot, final lock. Titles: entry → overshoot → correction → stabilised legibility | ASSERTED |
| MOT-17 | Graph-editor and easing-curve vocabulary produces weak, indifferent results | Vector/curve terminology is not a reliable control surface | Describe visible acceleration and spacing instead: where the motion accelerates, where it decelerates, where spacing widens, where it tightens near a reversal | OBSERVED (The Shadow, slow-in/slow-out vector set: *"not sold on these results as much"*) |
| MOT-18 | The background plate slides sideways under a successful character animation | Background and camera behaviour never separately constrained | Constrain the plate explicitly: `The background remains fixed and does not slide or parallax while the character runs in place.` | OBSERVED (The Shadow, 1 test — noted inside an otherwise successful animal run) |
| MOT-19 | Hard A/B pose replacement reads as video editing rather than limited animation | Over-forced discontinuity | Use `Only Pose A and Pose B exist; the complete current state is replaced directly by the next state; no intermediate pose is permitted.` only for deliberate pop/replacement styling or boundary diagnostics — never as the default way to request classical limited animation | OBSERVED (kit2 file 15 lab Finding E) |
| MOT-20 | A rule is invented such as "more than N articulated joints forces twos" | One walk finding over-fitted into a threshold | No monotonic joint-count rule exists. Stick figures, mannequins, robots, and isolated mechanisms changed behaviour non-monotonically. Do not state a threshold to users | OBSERVED-negative (The Shadow simplification series; the run was inconclusive rather than positive, and is recorded as a finding anyway) |
| MOT-21 | Prompt or explanation claims "H3 walks on twos because it renders at 24 FPS" | Correlation converted into architecture | No evidence establishes causation. A moving-dot control changed on successive playback frames at 24 fps, so the container supports per-frame change | OBSERVED (1 informal control, carrying a large negative conclusion) |
| MOT-22 | Clay or stop-motion brief renders as polished live action | Medium named but not translated into motion | Prompt the movement as physical poses: stepped pose increments, compression, contact, airborne state, tactile material response, slight registration variation. Saying "stop-motion" is not enough | ASSERTED (repair is kit synthesis; The Shadow's breadth report — one archer concept steered across 12 media including clay, sand, and paint-on-glass — supports that media *are* steerable, not that this phrasing is what steers them) |

---

# 5. SUBJECTS & IDENTITY

| ID | SYMPTOM | CAUSE | FIX | EVIDENCE |
|---|---|---|---|---|
| SUB-01 | Face degrades or garbles as the clip runs | Identity not restated at the points where it can drift | Re-assert the attribute list at each shot boundary: `Her facial identity, short dark curls, white chef's jacket, blue neckerchief, and silver earrings remain consistent with <Picture 1>.` Note this is mitigation, not a cure — see C11/C12 | OBSERVED (Albert, WorldX, mamad8, BecauseReasons — 4 independent uncontrolled reports of unfixed drift) |
| SUB-02 | Likeness collapses in wide or full-body framing but holds in closeups | Reference resolution vs framing scale | Prefer framings at or near the reference's scale; BecauseReasons: *"Terrible likeness and facial garbling with anything other than a medium closeup"* | OBSERVED (1 reporter) |
| SUB-03 | Style language quietly changes the character's anatomy or wardrobe | Medium traits that imply body proportion applied over a fixed identity | Strip anatomy-altering style terms and restate identity and clothing anchors before adding any look treatment | ASSERTED (kit repair, both kits, no test) |
| SUB-04 | "She feels guilty and afraid" produces nothing visible | Invisible intention written into the timeline field | Every detail in the timeline field must correspond to something visible or audible: `She hesitates, glances toward the door, tightens her grip on the envelope, and shifts her weight backward.` | OFFICIAL |
| SUB-05 | "cinematic, dramatic, stunning, epic, dynamic" echoed back as the whole prompt | User's adjective stack mistaken for a specification | Translate to production choices: `Low-angle tracking shot, hard backlight through smoke, rapid footsteps, sharp impact sounds, and a short accelerating percussion build.` | INFERRED (from the official visible-or-audible rule) |
| SUB-06 | Wrong character speaks the line | Model confused by more than one speaker | Introduce each speaker by voice descriptor plus a stable ID before the tag: `The older woman with a low, textured voice (S1) says: <d>[English] Leave the light on.</d>` and distinguish speakers by age, gender, or clothing in the description | OBSERVED (BecauseReasons: *"Model gets very confused with more than 1 speaker"*; MetrCedar's descriptor fix; Ryko reports the opposite — see C14) |
| SUB-07 | A complex reference collapses into one vague subject, or one person is split into three | Wrong subject granularity | Several assets may define one subject and one asset may define several. Track separately only what must be referred to separately later | OFFICIAL |
| SUB-08 | `<Subject 1> uses all references.` | Role left unresolved | One line per tracked item naming label, role, attributes to follow, and provenance: `<Subject 1> is the chef whose identity and clothing come from <Picture 1> and whose walking motion comes from <Video 1>.` | OFFICIAL |
| SUB-09 | `<Subject 1>` means the woman in shot 1 and her dog in shot 2; or `<Video 2>` appears having never been defined | Labels reused, renumbered, or introduced late | A label keeps one meaning across all six sections. Every label is introduced in `subject_definitions` and nowhere else | OFFICIAL |
| SUB-10 | Vague plurals produce the wrong number of objects | Counts left implicit | Use literal small integers as the corpus does: `three plated dishes`, `two crisp key poses`, `one concise nod`, `rebounds one inch` | INFERRED (pervasive corpus idiom) |

---

# 6. REFERENCES (ref2va)

| ID | SYMPTOM | CAUSE | FIX | EVIDENCE |
|---|---|---|---|---|
| REF-01 | An identity photo is silently pinned to frame zero as an exact first frame | Exact-frame semantics inferred from the mere presence of an image | Presence of an image establishes nothing. If it only supplies a person, cite it inside the subject: `<Subject 1> is the woman whose face, hairstyle, and recognizable body identity come from <Picture 1>; her costume is newly specified by the target prompt.` and use `reference generation` | OFFICIAL (role must be declared) + OBSERVED (The Shadow's *"biggest surprise"* was using a starting frame as *"suggestion rather than exact"* via `weak_reference` semantics) |
| REF-02 | A supplied final image is placed in Shot 1 | Any picture treated as an opening anchor | L2VA's picture belongs to the **last** shot. Infer a plausible preceding state and converge into the supplied endpoint | OFFICIAL |
| REF-03 | One image, no stated role, compiled straight to I2VA | Ambiguity resolved by assumption | Ask exactly one question and nothing else: `Should this image be the exact first frame, the exact last frame, or a general identity/style reference?` | ASSERTED (kit procedure; the ambiguity is real, the one-question protocol is invented) |
| REF-04 | FL2VA prompt describes both pictures and nothing in between | No temporal bridge authored | Write the path: first-frame state → observable intermediate changes → narrowing differences → exact last-frame state, closing with `During the final two seconds, the camera, body pose, reflections, and every compositional edge progressively converge on Picture 2 exactly.` | INFERRED |
| REF-05 | Any supplied video makes the task `video editing` | File type read as operational role | Presence of video creates no task type. Camera, cut, or rhythm guidance is `reference generation`. `video editing` only when a source video is directly modified; `video continuation` only when the output resumes one | OFFICIAL |
| REF-06 | An `<Audio N>` label appears because the reference video happens to have sound | Audio intent inferred from file contents | Create `<Audio N>` only when the audio is actually copied, or supplies timbre, rhythm, texture, or continuity — and only when it is enabled in the workflow | OFFICIAL |
| REF-07 | `<Video 1>` and `<Audio 1>` assumed to be the same file | Index equality read as provenance | Numbering families are independent. A source video may be `<Video 1>` while its enabled audio is `<Audio 2>` | OFFICIAL |
| REF-08 | A standalone `<Picture 2>` entry exists for an image that only sources a subject's face | One-label-per-file thinking | Standalone picture labels only for concrete frame anchors — first frame, keyframe, last frame, edited keyframe, composition anchor, storyboard. Otherwise cite the image inside the subject definition | OFFICIAL |
| REF-09 | A label for every visible detail; retention analysis becomes unmanageable | No tracking-requirement test | Label only what must be independently referred to later. Smallest label set that preserves the requested relationships | INFERRED |
| REF-10 | Retention downgraded to `partially_preserved` because the target has a new background or action | Whole-source similarity judged instead of role-relative retention | Retention is relative to the role you defined. An identity-only role stays `fully_preserved` while costume, pose, and scene change. Newly added target actions and backgrounds are not fidelity losses | OFFICIAL |
| REF-11 | `weak_reference` used where the defined content is genuinely in use | Loose influence conflated with partial retention | `weak_reference` = broad style/category/composition/atmosphere similarity only. `partially_preserved` = the defined content **is** used with some specified traits changed | OFFICIAL |
| REF-12 | `attribute_transfer` applied while the original subject is itself preserved | Marker misuse | `attribute_transfer` only when a trait moves from one visible reference onto a *different* identifiable target | OFFICIAL |
| REF-13 | `(S1)` written into `retention_analysis` as if it were a marker | Speaker IDs treated as retention vocabulary | Speaker IDs never appear in `retention_analysis`. Only the eight fixed markers appear there | OFFICIAL |
| REF-14 | An exact first frame is treated as locking the whole clip, so a requested costume change is refused | Frame anchor read as a clip-wide constraint | An exact first frame constrains frame zero only; an exact last frame constrains the endpoint only. Clothing, scene, and camera may still develop between them | INFERRED |
| REF-15 | Reference images resized or reframed to match the target output | Dimension match assumed to be required | References need not match generation resolution or aspect ratio; they are downscaled internally. Do not alter a reference to "fit" | OBSERVED (Kijai, implementer report; corroborated by Ryko's `max` vs `match` node description) |
| REF-16 | Invented numeric weights — "identity weight 0.8, motion weight 1.2" | A per-reference strength control assumed to exist | No user-facing weighting mechanism exists; Kijai answered that it is *"something he is working on"*. Express priority semantically: `Preserve the woman's identity from <Picture 1> while using <Video 1> only for walking motion and camera rhythm.` | OBSERVED (Kijai, answering Piblarg directly, 2026-08-08) |
| REF-17 | A reference is silently dropped so the set fits the input caps | Execution limits applied as semantics | Preserve the intended semantic map and state that execution may require reducing or splitting references. Never discard a role silently | ASSERTED |
| REF-18 | The model redraws the scene and ignores the reference image entirely | Reference supplied but its job never stated in the prompt | Name the job of every asset. Beaon, copying the guide verbatim: *"It's re-drawing the scene and not using the reference image"*; embedding-shapes diagnoses *"it took a reference too literally instead of being inspired"* and checking you are on the ref2va model | OBSERVED (Beaon, embedding-shapes, traxxas25 — 3 practitioners, uncontrolled) |
| REF-19 | A trait from one reference mutates onto a different reference's subject | Cross-reference contamination, worse at higher step counts | Fence each reference negatively and positively: `<Picture 1> provides subject identity only. It does not provide lighting, exposure, color grading, background, camera angle, pose, framing, or scene composition.` | OBSERVED (JustRed, 2 reports; Grimm1111 reports the fencing wording reduced flicker) — the sampler component belongs in the appendix |
| REF-20 | Adding more reference images fails to improve likeness | More references assumed to be monotonically better | Reference count is not a likeness dial; Albert: *"my ref faces become distorted after generating no matter how many refs I put"*. Improve role clarity and framing scale first | OBSERVED (Albert, 1 report; contradicted by AvidGamer's successful 4-asset "frankenstein" build — see C11) |
| REF-21 | A video motion reference is described as pixel-precise or ControlNet-like | Reference precision over-promised | Write `follow the camera movement and rhythm of <Video 1>`, not "reproduce every camera-space pixel trajectory". BNP4535353, reading the official guidance: motion copying gives *"approximate trajectories"* and *"is not a universal solution"*. Kijai: *"more a reference than controlnet"* | OBSERVED (BNP4535353 report + Kijai implementer statement; disputed by Ryko — see C15) |
| REF-22 | Complex multi-role reference sets routed onto the FL2VA checkpoint because it accepts images | Checkpoint capability mistaken for semantic fit | Route reusable multi-role references to ref2va. Kijai: *"general references work worse on FL2VA."* Semantic mode is separate from checkpoint: a text-only brief on an FL2VA checkpoint is still T2VA structure | OBSERVED (Kijai, implementer observation, explicitly *"not a formal benchmark"*) |
| REF-23 | A universal ranking is asserted — "Ref2VA is always better" / "FL2VA is always better" | Semantics, model family, and empirical quality conflated | Encode no ranking. Choose by which relationships must be preserved | OBSERVED-disputed (Karsticles, xwsswww, N0NSens all report different winners — see C10) |
| REF-24 | An asset the user only *described* is treated as if the file were attached | No supplied-vs-described check | Do not create labels for assets that were not supplied | ASSERTED |

---

# 7. AUDIO & DIALOGUE

| ID | SYMPTOM | CAUSE | FIX | EVIDENCE |
|---|---|---|---|---|
| AUD-01 | Full dialogue or lyrics repeated inside `overall_soundscape` | Soundscape used as a second dialogue/music field | Complete spoken and sung content lives only inside `<d>` in the timeline field. `overall_soundscape` carries ambience, physical/object sound, and non-verbal human sound | OFFICIAL (see C1 — an official README example violates this) |
| AUD-02 | `overall_soundscape: N/A` because the brief never mentioned sound | Absence of a request read as silence | `overall_soundscape: N/A` is reserved for explicitly requested total silence. Otherwise describe the ambience actually present: `Refrigerator hum, rain against the window, and distant traffic continue throughout.` | OFFICIAL |
| AUD-03 | Radio or on-set music placed in `non_diegetic_music` | Diegetic and non-diegetic layers swapped | Music audible to characters belongs in the timeline field. `non_diegetic_music` is audience-only score; write `N/A` when there is none | OFFICIAL |
| AUD-04 | Speaker name written inside the dialogue tag | Tag used as a script line | Only the language marker and the exact words go inside: `<d>[English] Leave the light on.</d>`. Identity is established outside it | OFFICIAL |
| AUD-05 | Voiceover paraphrased, or the on-screen character's lips move | Exact official handling skipped | Use the exact phrase and the adjacent lip clause: `The man (S1) says in an off-screen voiceover: <d>[English] I still remember that road.</d> while his lips remain completely closed.` | OFFICIAL |
| AUD-06 | The user's `Don't move!!!` comes back as `Don't move!` or translated | Reference-audio normalisation applied to user-typed text | User-entered dialogue, lyrics, and visible text are preserved verbatim — wording, punctuation, language | OFFICIAL |
| AUD-07 | Reperformed reference-audio lines carry decorative punctuation, or unintelligible spans are guessed | The verbatim rule applied to the wrong provenance | For reference-audio verbal content: preserve source words and language, normalise to basic sentence punctuation, terminate with `.` `?` `!` before `</d>`, and write `[unclear]` rather than guessing | OFFICIAL |
| AUD-08 | A voice-timbre reference drags the source's original words into the target | Property-level reference becomes content reuse | Declare it twice and negate the copy: `<Audio 1> is the voice-timbre and delivery reference for <Subject 1> (S1); do not reuse its source words.` and `<Audio 1>: reference - its timbre and measured delivery guide <Subject 1> (S1), while the requested target line is newly performed.` Task type `audio reference`, never `audio reuse` | OFFICIAL + OBSERVED (Lumifel, screwfunk, obsxrver, Tori Mori all independently carry an explicit do-not-reuse-the-words clause) |
| AUD-09 | `(S1)` invented for a voice that exists only inside a copied soundtrack | Any audible voice assumed to need a speaker ID | Attribute it to the audio: `When <Audio 1> reaches the existing lyric <d>[English] Turn around.</d>, <Subject 1> shifts weight...` plus `<Subject 1> does not sing, speak, or lip-sync it.` Retention: `<Audio 1>: fully_copy` | OFFICIAL |
| AUD-10 | `non_diegetic_music: emotional, tense music` | Abstract mood in place of a score description | Instrumentation, tempo, rhythm, dynamic change, plus an exit: `Sparse piano notes at a slow tempo, joined by sustained low strings that rise gradually in volume, then stop under the final held pose.` | OFFICIAL |
| AUD-11 | Score continues past the end or stops arbitrarily | No exit condition given | Every music field in the gold corpus carries a stop condition — `then stop under the final held pose`, `stops exactly when the title locks`, `fading during the final second` | INFERRED (corpus measurement) |
| AUD-12 | Reference audio drowns the newly generated foreground dialogue and effects | Reference audio dominates by default | DawnII's fix: `<Audio 1>: partially_copy - the source audio is reused purely as the background music layer, leaving room for the model to generate and mix new foreground diegetic dialogue and sound effects on top.` | OBSERVED (DawnII, 1 report with a working fix) |
| AUD-13 | Low gibberish undertone between spoken lines | Voice conditioning fills silence | Reduce prompt load, keep speaker IDs and dialogue formatting strict, and describe the silent intervals as silent. Note the reporters' other suspected causes are engine-side (turbo LoRAs, very low step counts, step skipping) — see appendix | OBSERVED (ray_a and Nemlet17, 2 independent reports, unsolved; seitanism's causal list is unverified) |
| AUD-14 | A character who should be silent keeps talking | Prompting alone does not suppress speech | No prompt wording is reported to work. xwsswww: prompting failed repeatedly and empty audio in the node failed; **audio masking with empty audio worked**. This is effectively an engine-side fix | OBSERVED (xwsswww, multiple attempts; Ablejones corroborates partial masking) |
| AUD-15 | Audio-only Ref2VA request fails to run | Open-weight Ref2VA requires audio to accompany an image or video | Keep the `<Audio N>` semantics, and flag that the open-weight surface needs a visual input alongside it. The hosted API docs do not repeat the restriction — see C3 | OFFICIAL (open-weight spec) |
| AUD-16 | `<Audio 1>` used as a sound-effect source for a specific hit or impact | Audio reference treated as an SFX sampler | Describe the effect in words in the timeline instead. MetrCedar: *"use `<audio 1>` as the punch sound effect when the man punches the other guy — seems to not work"* | OBSERVED (MetrCedar, 1 report) |
| AUD-17 | A calm reference voice will not deliver an angry line | Affect is carried by the reference, not fully overridable by direction | Choose a reference whose affect matches the target delivery; treat emotional re-colouring as unreliable | OBSERVED (garbus, 1 report) |
| AUD-18 | Two speakers share one mixed audio file and the voices swap or blend | Speaker-to-audio binding is ambiguous inside a single file | Splice per-speaker audio and bind each file to one subject, or use foxydits' two-speaker method: one line in `subject_definitions` binding each `<Audio N>` to its `<Subject N>`, one line in `retention_analysis` marking it `reference` | OBSERVED (foxydits reports the two-speaker method working; NebSH raises the ambiguity; seitanism recommends splicing but *"hasn't really tested that"*) |
| AUD-19 | Audio reference declared once and its role never restated | Single declaration insufficient | Declare every audio reference **twice** — once in `subject_definitions` binding it to a subject, once in `retention_analysis` as `reference` vs `fully_copy` vs `partially_copy` | OBSERVED (foxydits, working practice) + OFFICIAL for the section requirement |
| AUD-20 | `overall_soundscape` runs to a paragraph of six sentences | Length guidance ignored | 1–4 English sentences in one paragraph; the gold corpus is always 2 sentences and ~25 words. `non_diegetic_music` is 1–3 sentences, ~19 words | OFFICIAL (sentence counts); INFERRED (word counts, corpus) |
| AUD-21 | Sound bed feels detached from the picture | No sound event tied to a visible action | Structure the field as continuous bed first, then discrete contact events in screen order: `Kitchen ventilation, low burner flame, and distant staff movement continue throughout. A plate rim is wiped, the service bell rings once, and ceramic slides lightly across the pass.` | INFERRED — the specific count *"bind 1–3 sound events"* is **ASSERTED** |
| AUD-22 | Speech is cut off by the end of the clip with no marker | Truncation unmarked | Use `<cutoff>` when the clip ends mid-utterance | OFFICIAL (weakly corroborated — see C24) |

---

# 8. LIGHTING & LOOK

| ID | SYMPTOM | CAUSE | FIX | EVIDENCE |
|---|---|---|---|---|
| LOOK-01 | "watercolor anime claymation photorealistic comic-book style" produces an incoherent look | Unrelated style systems stacked | One coherent visual language per shot. If a genuine hybrid is wanted, divide responsibilities rather than blending adjectives: `Use painterly gouache environments with comic-ink characters; character motion follows stepped limited timing while the camera moves smoothly through layered parallax depth.` | ASSERTED (the "exactly one medium pack" budget is a kit invention; no evidence H3 degrades at two and not three) |
| LOOK-02 | A film title or studio name used as the whole style instruction | Proper-name shorthand substituted for traits | Translate the name into concrete traits: medium, line quality, palette, lighting, motion weight, camera, finish, audio. Proper names are discovery aliases, not final prompt language. Avoid claims about lens, pipeline, fps, or proprietary technique | ASSERTED (the 30 named anchors and their trait strings are kit-authored mappings, self-flagged as *"creative shorthand, not claims of official affiliation"*) |
| LOOK-03 | A style reference silently imports the source's composition, identity, or object placement | Style role over-reaching its declaration | Scope it in the definition: `<Subject 2> is the mid-century flat graphic treatment from <Picture 3>, applied to rendering only and not to composition, identity, or object placement.` Tag it `attribute_transfer` | INFERRED (from the official role-separation requirement) |
| LOOK-04 | "smooth", "cinematic", "beautiful" carry the entire look | Empty quality words | Replace "smooth" with continuous / gradually accelerating / no held poses / uninterrupted camera move; pair "cinematic" with actual choices — `restrained cinematic lighting with soft side key, low-contrast fill, shallow depth of field, and a slow push-in` | INFERRED |
| LOOK-05 | Style declared as a separate `Style:` line, or restated in every shot | Look treated as metadata | Three-field modes: style is the opening clause inside `[Shot 1]`, a noun phrase with 3–4 comma-listed qualifiers, then the framing — `[Shot 1] Photoreal live-action cinematography with motivated tungsten light, fine film grain, and restrained depth of field, a medium-wide shot frames a middle-aged baker...`. Never repeated in Shot 2. Ref2VA: its own sentence before `[Shot 1]` | OFFICIAL (Ref2VA placement); INFERRED (three-field placement, 39/39 corpus) |
| LOOK-06 | An unrelated style treatment is layered over a supplied reference image | Look inferred instead of read from the anchor | Exact first/last frames and reference assets outrank inferred style. Derive the baseline look from the picture and add a different style only on an explicit transformation request | INFERRED |
| LOOK-07 | Skin renders plastic and over-polished; a rough amateur/handheld look cannot be reached | Model default bias toward polish | State the degradation positively — available light, natural exposure variation, imperfect foreground occlusion, consumer camcorder framing, auto-exposure pumping — rather than asking for "amateur" or "unpolished" | OBSERVED (ObsidianDreams, 2 separate reports; no fix reported to work) |
| LOOK-08 | A reference image's lighting, grade, or background arrives in the output along with the identity | Look attributes travel with an identity reference | Fence the picture explicitly (see NEG-05) | OBSERVED (Grimm1111, 1 practitioner, reported flicker reduction after fencing) |

---

# 9. NEGATION & INSTRUCTION BLEED

**Nothing in any source measures how H3 handles negation.** The corpus contains one pure-negation prompt (The Shadow's frozen-held-drawing test) and the ledger records that **no success report for it was ever found**. Everything below is either an official structural rule, a corpus measurement, or a practitioner's working habit.

| ID | SYMPTOM | CAUSE | FIX | EVIDENCE |
|---|---|---|---|---|
| NEG-01 | Trailing list of "no artifacts, no weird motion, no bad anatomy, no mistakes" | Negative prompting used as a habit | Use a negation only to block a *likely, named* failure. Good: `The held pose remains completely still with no breathing or cloth motion.` | ASSERTED |
| NEG-02 | Stronger `freeze` / `hold` / `unchanged` language makes the result worse — freeze frames, hard substitution, timing drift | Escalating suppression instead of restating the target state | Stop escalating. Return to the positive form — repeated-state pattern, in-place action, simpler subject — rather than piling on prohibitions | OBSERVED (kit2 file 15 lab Finding D; The Shadow v1.5 package; the 5-level ladder built on top of it is **ASSERTED**) |
| NEG-03 | Standalone "do not" sentences are ignored | Negation detached from any action | Attach the negation to a positive action as a bounded qualifier. The gold corpus uses `without ...` 45 times across 20 blocks and a bare imperative negation exactly once: `lifts it vertically with constant speed without shifting the bottle`, `maintaining the referenced distance and low angle instead of orbiting or zooming`, `changes through distinct economical poses rather than fluid full animation` | INFERRED (corpus measurement; no test) |
| NEG-04 | A prompt made entirely of prohibitions produces something unrelated | No positive state left to render | Always describe the state that *should* exist. The one pure-negation experiment in the corpus has no reported outcome | ASSERTED (never demonstrated to work or fail) |
| NEG-05 | An instruction scoped to one reference bleeds onto everything — the identity picture also supplies lighting, background, pose, framing | Role boundaries never written down | Write the exclusion into `subject_definitions`: `<Subject 1> is only the identity, face, hair, age, and distinguishing physical features of the woman in <Picture 1>. <Picture 1> provides subject identity only. It does not provide lighting, exposure, color grading, background, camera angle, pose, framing, or scene composition.` | OBSERVED (Grimm1111 and IrrationalSoup independently converged on this shape; Grimm1111 reports reduced flicker) |
| NEG-06 | An instruction scoped to one body region bleeds into another | Regional separation not maintained | Do not request separate per-region behaviour. Describe which parts hold and which move (see MOT-05) | OBSERVED (The Shadow, body/face cadence test — the only observed cross-region bleed) |
| NEG-07 | Camera treatment absorbs the character's timing (or vice versa) | Two motion systems described as one | Separate them explicitly: `The camera trucks left slowly and smoothly, deliberately separating camera movement from the character's held animation timing.` | ASSERTED (kit2 edge-case example) |
| NEG-08 | Audio continuity is assumed across a cut and breaks | Continuity not stated | State continuity on both sides of the cut alongside `<scenetrans>` (see CUT-06) | OFFICIAL |
| NEG-09 | Style overrides a fixed constraint — dialogue wording, visible text, keyframe alignment, product geometry | Look treated as top priority | A style choice may never alter exact dialogue, visible text, keyframe alignment, identity anchors, product geometry, or declared reference roles | ASSERTED (kit hard rule; the underlying precedence of exact anchors is OFFICIAL) |
| NEG-10 | A reference is followed too literally — the model copies the whole source image instead of taking guidance | Reference role stated as an object, not as a job | Say what to take and what not to: `<Video 1> supplies the camera path, framing, background, lighting, composition, and action timing. It does not supply the face or identity.` | OBSERVED (embedding-shapes diagnosis; IrrationalSoup's working prompt) |

---

# 10. CONTRADICTIONS

Where the sources disagree with each other or with the official guide. "Winner" = what a manual should print.

| # | Disagreement | Side A | Side B | Winner and why |
|---|---|---|---|---|
| C1 | Dialogue and diegetic music inside `overall_soundscape` | The written prompt guide forbids repeating dialogue, singing, or diegetic music there | An official H3-Context-IR README example does exactly that | **Written guide.** Both kits agree; the README example is evidence that official Context-IR output is not self-consistent, not a licence to copy it |
| C2 | Camera syntax | High-level API docs show `[pan]`, `[zoom]`, `[static]` shorthand | The prompt-writing guide requires natural language inside the shot | **Prompt guide** for structured prompts. The shorthand is API-convenience surface, not canonical grammar |
| C3 | Audio-only reference input | Open-weight Ref2VA: audio may not be the sole input | Hosted API docs do not repeat the restriction | **Neither — it is an execution-surface split.** Keep `<Audio N>` semantics identical and validate the target surface before claiming it will run |
| C4 | Bracketing in the FL2VA alignment line | kit1 flags the bare `Picture 1 (from Shot 1)` vs bracketed `<Picture 1> (from [Shot 1])` asymmetry as an unexplained internal inconsistency; the gold corpus notes bracketed is the majority form (11 blocks vs 5) | kit2 verified all three lines character-for-character against the official guide and calls the asymmetry deliberate | **kit2.** Reproduce each mode's official string exactly, including the asymmetry. Do not normalise it |
| C5 | Retention-line delimiter | kit1's efficiency file uses an em dash: `<Subject 1>: fully_preserved — identity retained` | kit2 template and 12/12 gold examples use space-hyphen-space: `fully_preserved - identity retained` | **Hyphen.** Weight of examples; kit1 never states its em dash is canonical |
| C6 | Ref2VA field value placement | kit1/kit2 file 04 inline the value on the label line | kit2 files 07/13/14 and 11 of 12 gold blocks put the label alone and the value on the next line | **Next line** for the six-section format; inline for the three-field format. Mixing the two in one few-shot set produces mixed output |
| C7 | Task-type joiner | kit1 specifies the literal joiner string `` + `` with surrounding spaces as an isolated token | Every worked example writes it inline inside the brackets: `[reference generation + audio reference]` | **Inline.** No example anywhere writes the joiner any other way |
| C8 | Scope of the ON-2 tendency | kit1: scoped strictly to articulated 2D walking | kit2 file 15 Finding F: appeared in simplified humanoids too, "in some articulated character tests" | **Scoped tendency, never a default.** The jump-rope counterexample (twos requested, continuous delivered) rules out any universal law in either direction |
| C9 | Empirical tendency vs explicit user intent | The evidence says a requested ON-1 walk will probably come back paired | kit1's regression suite treats substituting ON-2 for a user's ON-1 request as a regression | **User intent wins.** Preserve the requested term, add the visible-consequence description, and never silently convert the request |
| C10 | Ref2VA vs FL2VA quality | Karsticles: Ref2VA more reliably honours the 0:00 anchor. Kijai: general references work worse on FL2VA | xwsswww: FL2VA better and more detailed. N0NSens: FL2VA followed image/video references more closely in one mixed test | **No ranking.** Route on semantics. Part of the disagreement is probably a ComfyUI core bug, not model quality — see appendix A1: any reference silently wipes every keyframe |
| C11 | One collage/character sheet vs several separate references | chancelor: *"Minimax does an incredible job at retaining likeness through single collage reference images. Honestly better than any character LoRA i've made."* dk endorses stitching | Illynir: *"It's a bad idea to put all the distances on a single image... unless you use a very high resolution. You'll get better results if the three are kept separate"* | **Unresolved.** The untested reconciliation is reference resolution. Nobody ran a controlled comparison. Print both positions |
| C12 | Do character sheets deliver likeness at all | Yes: PoliteCat, Ryko, VK, chancelor | No: WorldX, Albert, mamad8 | **Unresolved**, and confounded by framing scale (BecauseReasons: likeness collapses outside medium closeup). Do not promise likeness retention |
| C13 | Is the official guide actually honoured by the model | traxxas25: *"Im realizing now how important the prompt guidelines are"* | Beaon, after copying the task-type table verbatim: *"This seems to be not true"* and *"Their guide has specific tags and formats to use. Seems they might not be honored in some cases."* foxydits notes the community has drifted off-spec entirely | **Follow the guide** — it is the only specification and the only thing that is falsifiable — but state plainly that adherence is partial and that off-spec minimal prompts also work (protector131090, N0NSens, DawnII all report working non-canonical prompts) |
| C14 | Are `(S1)` speaker IDs necessary | foxydits: *"I haven't noticed any difference using the (S1) nomenclature over just simply referring to <Subject #>"* | The official guide requires them; MetrCedar recommends them specifically to fix wrong-speaker output; foxydits himself hedges for 3–4 speakers | **Use them.** Zero cost, official, and the documented multi-speaker failures are exactly what they address |
| C15 | Video motion reference precision | BNP4535353, citing official guidance: *"approximate trajectories... not a universal solution"*; Kijai: *"more a reference than controlnet"* | Ryko: *"you can literally drop a .mp4 into r2v... then make the characters do anything you want"* | **Approximate.** Two sources including the implementer against one enthusiastic report |
| C16 | Image vs video reference for facial likeness | Moonbow: image is enough, video unnecessary | KakerMix: video is always better if you have the hardware | **Unresolved.** No test on either side |
| C17 | Multi-speaker audio — solved or not | Ryko, 2026-08-08: *"In MMH3, it's rock solid"* | BecauseReasons, 2026-08-04: *"Model gets very confused with more than 1 speaker"*; Quality_Control only got stability on 2026-08-10 and only via turbo LoRAs | **Unresolved, and date/engine dependent.** Report as fragile |
| C18 | Duration bounds | kit1/ledger: 4–15 s, hosted API integer seconds only | kit2: "up to ~15 s", no lower bound stated; ComfyUI snaps to a `17k+5` frame grid so effective duration is neither | **Surface-dependent.** Hosted: integers 4–15. ComfyUI: requested duration is not the rendered duration — never invent a snapped value |
| C19 | "~5 seconds = one shot" | kit2 density rule and the gold corpus (4/4 clips ≤5 s use one shot) | kit1 explicitly narrows it: *"Do not treat '~5 seconds = one shot' as an absolute law"* | **Default, not law.** Print it as the default with the escape hatch |
| C20 | Action density | kit2: *"one dominant action beat per roughly 1–3 seconds"* | kit1 gives no numeric density rule at all | **kit1.** The number is uncited and the word "roughly" carries it. Print the qualitative rule and drop the number |
| C21 | Can a supplied image be a weak suggestion | The Shadow's headline finding: a starting frame worked as *"suggestion rather than exact"* via `weak_reference` | I2VA exact-first-frame semantics require frame zero to match | **Both, in different modes.** The finding applies to Full-Reference `weak_reference` framing and must not be used to weaken I2VA |
| C22 | Pose teleportation | v2 rule: unexplained pose teleportation is always a failure | Reversed in v3: reject only *unintended* discontinuity, since graphic and discrete replacement can be intentional and works | **Reversed version.** But note the reversal rests on one prompt with no reported outcome |
| C23 | Prompt-only output | kit1 kernel: return only the compiled prompt | The comparison doc found this read too literally; softened so H3/ComfyUI questions get normal answers and ideation gets 2–3 options | **Softened version** |
| C24 | `<scenetrans>`, `<cutoff>`, the transition-phrase list, and `(S1,S2)` | Both kits present them as official | kit2's verification pass could not surface any of them in the retrieved official base guide | **Keep using them** — they are consistent with the tag family — but mark them as the lowest-confidence "official" items in the manual |
| C25 | ComfyUI tag numbering by connection order | Both kits state it as fact and one promoted it into an execution guide | kit1's own ledger says the action item was *"add after official-source verification"* and no verification was ever recorded | **Unverified.** If connection order is unknown and materially affects the prompt, ask once rather than inventing tag order |
| C26 | Weight families | kit2 file 02 says the implementation refers to `t2va`, `fl2va`, and `ref2va` conditioning | ComfyUI ships only `minimax_h3_fl2va_pruned_int8_convrot` and `minimax_h3_ref2va_pruned_int8_convrot` | **Two families.** `t2va` is guide vocabulary, not a shipped weight family |
| C27 | Resolution | MiniMax blog: up to 2K | ComfyUI native canvas: 768 px short edge, ~768×1344 | **Both, different paths.** 2K comes via the separate regenerate stage, not the base workflow |
| C28 | Ref2VA input caps | 9 images + 3 videos + 3 audio | "12 total mixed input files" — which is not the sum (15) | **Treat the 12-file cap as an independent, uncited claim.** Ryko's proposed torture test of exactly 12 was never answered |
| C29 | Checkpoint names vs prompt modes | The kits use T2VA/I2VA/FL2VA/L2VA as if they were four checkpoints | The spec concedes *"There are not necessarily four separate base checkpoints"*; H3-Base-FL2VA alone covers 0, 1, and 2 input images | **Semantic modes ≠ checkpoints.** Never let a checkpoint filename dictate prompt structure |
| C30 | Does a reference's white background leak into the output | chancelor's working recipe explicitly requests *"pure white background"* for the sheet and reports excellent results | Nobody reports either leakage or its absence | **Open question.** State it as untested rather than answering it |

---

# APPENDIX — ENGINE / WORKFLOW / SETTINGS ISSUES (not prompt problems)

Dropped from the catalogue above because no prompt wording fixes them. Kept because losing them would cost real debugging time. **None of these values or names may ever be written into an H3 prompt.**

| # | Issue | Detail |
|---|---|---|
| A1 | **References silently wipe keyframes in ComfyUI core** | Chandler ✨🎈, 2026-08-06: `model_base.py` assigns `cond_video_latents` twice — once from keyframes, then again from refs; second wins. *"any reference silently wipes every keyframe. Keyframes only work when there are no refs, i.e. fl2va only."* Also: the keyframe positional base ignores ref blocks packed before the target, and only first/last anchors are implemented. This likely explains part of the Ref2VA-vs-FL2VA disagreement (C10) |
| A2 | Wrong checkpoint silently degrades references | `..._ref2va_...` for reference work, `..._fl2va_...` for T2V/I2V/first-last. embedding-shapes, LukeG89, avataraim all report the confusion |
| A3 | Duration snapping | ComfyUI snaps to a `17k+5` frame grid at 24 fps; `effective seconds = frames ÷ 24`. Use the *requested* duration in the prompt and only claim a rendered duration once the frame count is known |
| A4 | Output geometry | Dimensions round to a multiple of 32; native base canvas ~768 px short edge, capped around 768×1344 |
| A5 | `ref_image_size` | `match` rescales references to output size (fast); `max` keeps them at up to a 2048 px short edge (better identity detail, slower, heavier). Ryko: *"max = use references at original size, match = rescale to output size"* |
| A6 | Reference count drives cost, not quality | KingGore2023: *"More refs more gen time."* Lodis, alexone, MetrCedar concur; jab reports OOM on `MiniMax H3 Reference to Video` |
| A7 | Sampler-dependent reference corruption | JustRed: multistep causes one reference's traits to mutate another, worse at higher steps; *"Doesn't seem to happen with er_sde"* |
| A8 | Step-count artifacts | Janosch Simon: euler beta 30 steps clean, fewer steps gave muddy backgrounds. Vérole runs lightx2v LoRA at 0.8 with 6 steps. seitanism links turbo LoRAs, very low steps, and step skipping to destroyed dialogue |
| A9 | Audio reference not enabled | foxydits: *"You didn't enable `<Audio 1>` in the Reference Control Panel toggle section."* A silent no-op that looks like a prompt failure |
| A10 | Forcing silence needs masking | xwsswww: prompting failed, empty audio in the node failed, **audio masking with empty audio worked**. Ablejones uses partial masking to blend source and reference |
| A11 | Multi-speaker stability via LoRAs | Quality_Control got stable multi-speaker ref2v output only after turbo LoRAs |
| A12 | Hosted API constraints | Durations are integer seconds; prompt ≤7000 characters; first/last-frame image width and height each in [256, 5760]; aspect ratio 2:5 to 5:2; `ratio` required for T2V and cannot be `adaptive`; JPG/JPEG/PNG/WEBP/HEIC/HEIF, H.264/H.265, WAV/MP3 |
| A13 | Web UI uses a different reference syntax | iGoon: prompts copied from the MiniMax chat UI reference assets as `@Image1` / `@Audio1`, not `<Picture 1>` / `<Audio 1>`. Kijai: *"the actual model should use `<Picture i>` tags"*; API-facing workflows differ because they may run a prompt-enhancer stage first |
| A14 | Never inject workflow values into the prompt | Model filenames, quantization, sampler, scheduler, steps, seeds, cache settings, attention implementation, VRAM/offload settings, `ref_image_size`, node names, tensor dimensions, frame counts. They are workflow parameters, not prompt facts |
| A15 | Deliberately excluded from the prompting knowledge base | turbo-LoRA strengths, 4-step vs 8-step tuning, sampler-specific audio fixes, cache-node compatibility, Sol-Attention thresholds, VRAM/offload advice, quantization selection, transient ComfyUI regressions, audio-VAE sampler bugs, workflow-specific lip-sync timing hacks |

---

# COUNTS

| Chapter | Entries |
|---|---|
| 1. Structure & Length | 13 |
| 2. Shots & Cutting | 8 |
| 3. Camera | 6 |
| 4. Motion & Physics | 22 |
| 5. Subjects & Identity | 10 |
| 6. References (ref2va) | 24 |
| 7. Audio & Dialogue | 22 |
| 8. Lighting & Look | 8 |
| 9. Negation & Instruction Bleed | 10 |
| **Catalogue total** | **123** |
| 10. Contradictions | 30 |
| Appendix (engine/settings) | 16 |

| Evidence grade | Entries |
|---|---|
| OFFICIAL | 44 |
| OBSERVED | 44 |
| INFERRED | 19 |
| ASSERTED | 16 |
| **Total** | **123** |

Grades count the primary grade of each entry. Twelve entries carry a split grade — an OFFICIAL or OBSERVED rule with an ASSERTED numeric or an ASSERTED procedure bolted on (CUT-07's 13-dimension loop list, STR-11's "one beat per 1–3 seconds", AUD-21's "1–3 sound events", NEG-02's 5-level ladder, MOT-15, MOT-22, CAM-06, CUT-05, AUD-19, AUD-20, LOOK-05, REF-19). Those are marked inline in the EVIDENCE column and counted under their primary grade.

Of the 44 OBSERVED entries, **31 rest on a single observer and a single unrepeated run.** Nine rest on The Shadow's 20-test batch, which was single-seed, single-author, self-rated on an undefined scale, with no blind evaluation. Six rest on the kit2 cadence lab, which never reports n. The rest are individual Hivemind reports. Nothing in any source has been replicated by a second party under controlled conditions.
