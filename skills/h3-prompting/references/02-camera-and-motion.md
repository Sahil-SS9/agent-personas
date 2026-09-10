# H3 Prompting — Camera and Motion Reference

How to express camera behaviour and physical motion so the model executes it.

Provenance markers used throughout: `[OFFICIAL]` (MiniMax's own prompt-writing guides),
`[OBSERVED]` (someone ran it and reported), `[INFERRED]` (derived from structure or measured
across working prompts), `[ASSERTED]` (community kits state it as fact with no evidence).

---

## 1. The camera vocabulary is a closed set

`[OFFICIAL]` The base guide publishes a fixed table of camera-motion expressions. These are the
terms the model has defined handling for. Anything outside this list is not a camera instruction —
it is prose the model will interpret loosely or ignore.

| Expression | Meaning |
|---|---|
| `Zoom In` / `Zoom Out` | Focal length changes; the camera body does **not** move |
| `Push In` / `Pull Out` | The camera body moves forward / backward |
| `Pan Left` / `Pan Right` | Camera pivots horizontally, in place |
| `Truck Left` / `Truck Right` | Camera translates horizontally through space |
| `Tilt Up` / `Tilt Down` | Camera pivots vertically, in place |
| `Pedestal Up` / `Pedestal Down` | Whole camera rises / lowers |
| `Arc Shot` | Camera moves along an arc around the subject |
| `Tracking Shot` | Camera follows a moving subject |
| `Static Shot` | Camera position and lens both hold still |
| `Shake Slightly` / `Shake Strongly` | Camera shake, two intensities |
| `POV` | The subject's point of view |
| `Roll Clockwise` / `Roll Counterclockwise` | Camera rolls about the lens axis |

### The Zoom / Push distinction matters

`[OFFICIAL]` `Zoom In` changes focal length from a fixed position — perspective stays put, the frame
crops in. `Push In` physically moves the camera — perspective changes, foreground and background
shift relative to each other. Writing "zoom" when you mean "push" gives you a flat crop instead of
a move through space. This is the single most common vocabulary error.

---

## 2. Amplitude and speed

`[OFFICIAL]` A complete camera expression is **type + amplitude + speed**. Amplitude and speed have
fixed phrasings:

| Slot | Exact phrasing |
|---|---|
| Amplitude | `with small amplitude` · `with large amplitude` |
| Speed | `at slow speed` · `at fast speed` |

`[OFFICIAL]` Defaults are medium amplitude and normal speed. **Omit the modifier when you mean the
default** — writing it out anyway adds noise without adding meaning.

Assembled:

```
The camera pushes in with small amplitude at slow speed toward the folded letter in her hands.
The camera pans right with large amplitude at fast speed, revealing the open doorway.
The camera holds a static shot as the runner exits the frame.
```

---

## 3. Camera goes in the prose, not in brackets

`[OFFICIAL]` Camera motion is written as natural English **inside the shot description**, integrated
into the action. It is not a separate labelled field and not a bracketed tag.

Correct:

```
[Shot 1] Live-action, cinematic, a medium-wide shot frames a baker opening the shutters.
The camera pushes in with small amplitude at slow speed as he places a loaf on the counter.
```

Wrong:

```
[Shot 1] [push in] [slow] A baker opens the shutters. Camera: push in, small amplitude.
```

`[OBSERVED]` Some higher-level API documentation shows bracket shorthand such as `[pan]`, `[zoom]`,
`[static]`. This conflicts with the prompt-writing guide. **The prompt-writing guide wins** — it
describes the format the model's own prompt compiler emits.

---

## 4. Framing is free description. Motion is a closed set.

These are two different slots and confusing them causes avoidable trouble.

### 4.1 Framing — ordinary description, use freely

`[OFFICIAL]` The guide's own worked examples open shots with plain framing language:
*"a medium-wide shot frames a baker opening the shutters"*. Framing is not a controlled vocabulary.
Shot sizes and angles are normal English and are safe to write.

Safe as ordinary description: extreme close-up, close-up, medium close-up, medium shot,
medium-wide, wide, extreme wide, establishing shot, two-shot, over-the-shoulder shot, low-angle,
high-angle, overhead, worm's-eye, Dutch-angle, point-of-view, profile, silhouette, insert, cutaway,
master, reflection shot, through-the-window shot.

`[OBSERVED]` An independent third-party prompt-builder offers exactly this list as free-text
framing while locking *motion* to the official set — the same split, arrived at separately.

### 4.2 Motion — closed set, substitute anything outside it

`[INFERRED]` These are standard motion words with no defined handling. Not forbidden — the model
will do *something* — but you cannot rely on them.

| Term people reach for | What to write instead |
|---|---|
| locked off, on sticks | `Static Shot` |
| dolly in / dolly out | `Push In` / `Pull Out` |
| dolly left / right, crab | `Truck Left` / `Truck Right` |
| crane up / down, jib | `Pedestal Up` / `Pedestal Down` |
| handheld | `Shake Slightly` |
| whip pan | `Pan Left/Right ... at fast speed` |
| orbit, circle round | `Arc Shot` |
| roll, canted move | `Roll Clockwise` / `Roll Counterclockwise` |
| macro, probe lens, snorkel | describe what fills the frame and how close it is |
| 35mm, 85mm, wide lens, long lens | describe framing, not the glass |
| dolly zoom, rack focus, crash zoom | no equivalent — describe the visible result |

`[INFERRED]` The reliable substitute for an unsupported motion term is **framing description plus a
supported motion term**. The model responds to what is in frame, in what size, from what position.
It does not respond to the name of a technique.

Example, rewriting "high three-quarter over-the-shoulder, 35mm, locked off":

```
An over-the-shoulder shot from above: his shoulder and the back of his head fill the right of frame
in dark foreground; beyond him the desktop runs diagonally away and the open drawer sits below the
desk edge. The camera holds a static shot.
```

### 4.3 Rig and extended-motion terms — caution

`[ASSERTED]` At least one third-party prompt-builder extends the motion list beyond the official
twelve — adding `Full 360 Orbit`, `Spiral Around Subject`, `Dolly Zoom`, `Crash Zoom In`,
`Snap Zoom Out`, `Whip Pan`, `Rack Focus`, `Trail Behind Subject`, `Lead Subject Backwards`,
`Locked Off` — and offers a separate rig clause (`on a tripod`, `handheld`, `on a steadicam`,
`on a gimbal`, `on a dolly track`, `on a crane`, `on a drone`, and so on). It also extends the
official five cut phrasings to sixteen, adding `hard-cuts to`, `smash-cuts to`, `match-cuts to`,
`jump-cuts to`, `cross-dissolves to`, `irises to`.

**None of these extensions appear in any MiniMax document**, and the tool describes its
vocabularies as coming "from the spec". Nobody has tested whether they do anything. Treat them as
plausible English the model may or may not parse — not as vocabulary. If you use one, expect the
same reliability as any other unsupported term.

---

## 5. One camera path per shot

`[OFFICIAL]` Cuts should introduce new information about subject, space, state, viewpoint or time.
For distance or angle adjustments alone, prefer camera motion over a cut.

`[OBSERVED]` Combining several motion types in one shot degrades all of them. Community reports
converge on one dominant path per shot: choose the move, state its amplitude and speed, and stop.

`[INFERRED]` If you need two distinct camera behaviours, that is two shots — and see
`05-length-and-structure.md` on why you probably cannot afford two shots.

---

## 6. Holding the camera still

`[OFFICIAL]` `Static Shot` is the instruction. It is a positive term, not the absence of one.

`[INFERRED]` Omitting all camera language does **not** produce a static shot; it produces whatever
the model feels like, which is usually a slow drift. If you want stillness, say `The camera holds a
static shot.`

`[OBSERVED]` Very small moves — "an extremely subtle push-in", "a barely perceptible drift" — are
below the model's resolution. What comes back is either nothing or an unmotivated wander that reads
as handheld. Either commit to `Push In ... with small amplitude at slow speed` or commit to
`Static Shot`. There is no reliable middle.

---

## 7. Motion of subjects

`[OFFICIAL]` Every detail should correspond to something visible or audible. Write actions, not
states.

`[OBSERVED]` **Multi-stage actions stall before their terminal event.** A test in which an archer
was asked to draw and release produced a prolonged aiming hold and no release; a skateboard ollie
that named every physical phase completed cleanly. The rule that follows — *name the terminal
event explicitly* — is the most generalisable finding in the corpus, and it applies far beyond
animation. If the action has an end state, write the end state.

`[OBSERVED]` Fast motion smears, and this is structural: one latent token spans four pixel frames,
so a burst of motion needs poses the token cannot hold. More sampling steps do not fix it, because
the missing poses were never generated. Slow the described action down or accept the smear.

`[INFERRED]` Physical consequence must be stated, not implied. "Realistic water" is a wish;
"the boot displaces water outward in a circular splash, droplets falling back onto the pavement" is
an instruction.

---

## 8. Camera and motion failure modes

| Symptom | Cause | Fix |
|---|---|---|
| Camera drifts when you asked for stillness | No camera term given, or a sub-threshold move requested | Write `The camera holds a static shot.` |
| Move reads as a crop, not a move | `Zoom In` used where `Push In` was meant | Swap the term |
| Requested move barely happens | Amplitude/speed modifiers omitted where non-default was intended | Add `with large amplitude` / `at fast speed` |
| Move happens but wrong direction | Direction is only implied by context | Name the direction with the term: `Truck Left`, `Pan Right` |
| Several moves requested, all mushy | More than one dominant path in one shot | One motion type per shot |
| Camera behaviour ignored entirely | Written as a bracketed tag or a separate line | Integrate into the shot prose as a sentence |
| Motion in a specialised term ignored | Term is outside the closed vocabulary | Substitute from the table in §4 |
| Movement of an object toward or away from camera is invisible | The camera sits on the object's travel axis, so the move is foreshortened to nothing | Reposition the camera off that axis so the travel crosses the frame, or state the visible consequence (what the moving edge sweeps across) |
| Action never finishes | Terminal event not named | State the end state explicitly |
| Fast action smears | Structural, one token spans four frames | Slow the action; do not add steps |

---

## 9. Open questions

- Whether the amplitude/speed modifiers have graduated effect or act as binary switches. Nobody
  has measured it.
- Whether `Arc Shot` accepts a direction qualifier. Not documented either way.
- Whether camera terms placed at the start of a shot behave differently from the same terms placed
  after the action. Untested.
