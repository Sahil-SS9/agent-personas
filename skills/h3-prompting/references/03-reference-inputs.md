# 03 — Reference Inputs (Full-Reference / ref2va)

How to attach, label, and cite reference images, video and audio in a MiniMax Hailuo H3
Full-Reference prompt.

**Provenance markers used in this file**

| Marker | Meaning |
|---|---|
| `[OFFICIAL]` | Stated in MiniMax's own prompt-writing guides (`VIDEO_PROMPT_WRITING_GUIDE_base_en` / `_ref_en`), the H3 README, or the hosted API docs. |
| `[OBSERVED]` | Someone ran it and reported the result. Observer name and date given. Nearly all are single-author, single-seed, self-rated. |
| `[INFERRED]` | Derived from official structure or from measuring a corpus of working prompts. Nobody tested that violating it degrades output. |
| `[ASSERTED]` | Stated as fact somewhere with no evidence behind it. Treat as suspect. |

Community observations come from a public practitioner forum, mined 2026-08-12, covering
roughly 2026-08-01 to 2026-08-12 — the model's first ~12 days in public. Treat every
`[OBSERVED]` item as a report, not a measurement.

---

## 1. Hard input limits

| Limit | Value | Provenance |
|---|---|---|
| Reference images | **up to 9** | `[OFFICIAL]` (open-weight H3-Base-Ref2VA spec) |
| Reference video clips | **up to 3** | `[OFFICIAL]` |
| Reference audio clips | **up to 3** | `[OFFICIAL]` |
| **Total mixed input files** | **12** | `[OFFICIAL]` as published, but see §1.1 |
| Each reference video clip | **2–15 s** | `[OFFICIAL]` |
| Total reference video duration | **≤ 15 s** | `[OFFICIAL]` |
| Each reference audio clip | **2–15 s** | `[OFFICIAL]` |
| Total reference audio duration | **≤ 15 s** | `[OFFICIAL]` |
| Audio as sole input | **not allowed** — audio must accompany an image or video | `[OFFICIAL]` (open-weight surface only) |

Community restatement of the same numbers, independently: izashin, 2026-08-10 — "max 9
images, 3 video clips, 3 audio clips, 12 files total"; Illynir, 2026-08-10 — "Audio: ≤ 3
clips; audio must be accompanied by image or video input and cannot be used as the sole
input; each clip must be 2–15 seconds long; total duration ≤ 15 seconds". `[OBSERVED]`
(two practitioners repeating a published figure, not testing it).

### 1.1 The caps do not add up — the 12-file cap is what binds

**9 + 3 + 3 = 15, which is greater than the stated 12-file total.** The per-type numbers are
therefore ceilings, not an allowance you can spend simultaneously. **The 12-file cap binds.**
You cannot attach 9 images and 3 videos and 3 audio clips in one job.

Honest caveat: the per-type numbers and the 12-file total come from the same official
specification, and that specification never explains the arithmetic. The 12 figure carries no
worked example anywhere in the corpus. `[OFFICIAL]` for its presence, `[ASSERTED]` for its
interpretation.

Nobody has confirmed the boundary experimentally. Ryko, 2026-08-06, proposed the exact
stress test and got no answer: *"So the torture test would be: 3 videos with their associated
3 audio tracks, + 6 reference images for a total of 12?"* `[OBSERVED]` — question asked, never
answered. If you need to know the real ceiling, run that test yourself.

### 1.2 Practical planning consequence

Budget the 12 slots before writing the prompt:

| Job shape | Typical spend |
|---|---|
| One character, one voice | 1–3 images + 1 audio |
| Two characters in dialogue | 2–6 images + 2 audio |
| Character + environment + motion driver | 2 images + 1 image (env) + 1 video |
| Character swap on a source video | 1–3 images + 1 video (+ 1 audio) |

Never silently drop a reference to make the set fit. Keep the intended semantic map and say
that execution may require reducing or splitting the reference set. `[ASSERTED]` (a
compiler-hygiene rule, not an H3 behaviour).

---

## 2. The four label types

H3 labels **roles**, not files. A label names a job that some content does in the target
video.

| Label | Use it for | Do **not** use it for |
|---|---|---|
| `<Subject N>` | Reusable **visible content** actually used in the target: people, animals, objects, scenes, backgrounds, environments, clothing, props, interfaces, **styles**, actions, expressions, poses, visual effects. Represents content, not the source file. | Anything whose only job is to be a literal frame of the output. |
| `<Picture N>` | **Only** when the image itself is a concrete target-video anchor: first frame, keyframe, last frame, edited keyframe, composition anchor, storyboard / shot-planning anchor. | An image that merely supplies a face, a costume, a location look, or a style. |
| `<Video N>` | **Whole-video relationships**: direct editing source, continuation source, camera-movement reference, cut structure, rhythm, temporal structure. | A video you are only borrowing one character's face from — that is a `<Subject N>` sourced from the video. |
| `<Audio N>` | Any intentional audio relationship: direct signal reuse, partial reuse, voice timbre, delivery, music style, dialogue/lyric content, sound-effect texture, beat/rhythm, audio continuity. | Sound that merely happens to exist inside a supplied video file. |

All four: `[OFFICIAL]`.

### 2.1 The official one-label rule

> An image whose only job is to define a character or a style **must be cited inside the
> `<Subject N>` definition**. It does not get its own standalone `<Picture N>` entry.

`[OFFICIAL]`. Standalone `<Picture N>` entries exist only for concrete frame anchors and
storyboards.

**Wrong** — one label per file:

```text
<Subject 1> is the chef.
<Picture 1> is a photo of the chef.
```

**Right** — the image is cited inside the subject:

```text
<Subject 1> is the chef whose face, hairstyle, and recognizable body identity come from <Picture 1>; her costume is newly specified by the target prompt.
```

`[OFFICIAL]` (pattern taken from the official `subject_definitions` example).

### 2.2 Subject granularity

- Several assets may define **one** subject: identity from `<Picture 1>`, costume from
  `<Picture 2>`, walking motion from `<Video 1>` → all one `<Subject 1>`. `[OFFICIAL]`
- One asset may define **several** subjects, when each must be tracked separately
  (character A, character B, the vehicle). `[OFFICIAL]`
- Create a label only for content you must **refer back to** later. Use the smallest label
  set that preserves the requested relationships. `[INFERRED]`

### 2.3 Numbering families are independent

`<Video 1>` and `<Audio 1>` are **not** assumed to be the same file. A source video may be
`<Video 1>` while its enabled audio is `<Audio 2>`. `[OFFICIAL]`

Do not create `<Audio N>` just because a supplied video has a soundtrack. Create it only when
the audio itself is copied, or supplies timbre, rhythm, texture, or continuity — and only when
that audio input is actually enabled in the workflow. `[OFFICIAL]`

---

## 3. THE CENTRAL RULE — an uncited reference is an ignored reference

> **A reference that is not named in the prompt text does nothing. Slots are inert on their
> own. Attaching a file is not an instruction.**

This is the most-repeated and best-corroborated reference finding in the corpus.

- **mdkb, 2026-08-08** — the clearest statement: *"when I just stuck matt damon and the pig
  video in and didnt do proper prompt as per the guides I got this. so proper prompting is
  EVERYTHING. interesting thing this shows is you could leave all slots plugged in with stuff
  loaded and **if it aint in the prompt it will ignore it completely**."* `[OBSERVED]`
- **mdkb, 2026-08-09** — *"I find you have to define every connection properly in the prompt,
  else it ignores it. matt damon taught me that."* `[OBSERVED]`
- **Kijai (ComfyUI implementer), 2026-08-03** — *"note that the reference mode NEEDS PROPER
  PROMPTING, it really fails easily otherwise"* `[OBSERVED]` (implementer statement about
  shipped behaviour, not a controlled test)
- **Lumifel, 2026-08-11** — *"the model has a strict template to follow, when you miss one of
  the section gibberish happen"* `[OBSERVED]`
- **traxxas25, 2026-08-06** — *"Im realizing now how important the prompt guidelines are"*
  `[OBSERVED]`
- **Beaon, 2026-08-06** — the failure state: *"It's re-drawing the scene and not using the
  reference image"* `[OBSERVED]`

Eight independent practitioners reported "ref2va ignores my reference video entirely"
(protector131090, Grimm1111, MysteryShack, xwsswww, Tori Mori, VK, and others, 2026-08-03 to
2026-08-12). Prompt-format sensitivity is the dominant diagnosed cause. `[OBSERVED]`

**Operational consequence.** Every attached file gets:

1. one line in `subject_definitions` naming its label, its role, and what to follow;
2. one line in `retention_analysis` giving its relationship marker;
3. at least one mention in the description body **at the point where it takes effect**.

Audio references specifically need the declaration **twice** — once in `subject_definitions`
binding them to a subject, once in `retention_analysis` as `reference` / `fully_copy` /
`partially_copy`. `[OBSERVED]` (foxydits, 2026-08-11, working two-speaker practice) +
`[OFFICIAL]` (the sections are required).

Counter-evidence, stated for honesty: several practitioners get results from off-spec minimal
prompts — protector131090, 2026-08-05: *"anyways this prompt works — `<Subject 1> is the person
from <Picture 1>. <Audio 1> provides the complete singing performance for <Subject 1> (S1).`"*;
N0NSens, 2026-08-05; DawnII, 2026-08-10. `[OBSERVED]`. Note that even these minimal prompts
**still name every attached asset**. The central rule survives; the surrounding scaffolding is
what is optional.

---

## 4. Silent degradation: over-long prompts fall back to text-to-video

**This is the highest-consequence reference failure, because it produces no error.** The job
runs, the video looks fine, and the references simply stopped applying.

> **Reported behaviour: when the prompt gets too long or too detailed, Full-Reference mode
> starts behaving like text-to-video and the attached references are ignored.**

- **VK, 2026-08-04** — *"Whenever the prompt is to detailed it just seems to become t2v
  ignoring ref video."* `[OBSERVED]`
- **BecauseReasons, 2026-08-03** — corroborating from the instruction-adherence side: *"It
  does seem to struggle with longer prompts, often ignoring specific instructions such as who
  speaks when, sound effects etc."* `[OBSERVED]`
- **seitanism, 2026-08-07** — the same shape for audio: *"an overloaded prompt with too many
  actions can also cause dialogue to just be dropped"* `[OBSERVED]`
- **Parker, 2026-08-08** — a distinct over-stuffing pathology: *"apparently if you put too many
  words in it gets fast"* `[OBSERVED]`

**Evidence strength: weak-to-moderate.** Two direct reporters for the t2v fallback, both
uncontrolled, neither naming a threshold. Nobody has produced a character count at which it
flips.

**Direct contradiction, stated plainly.** Several practitioners report that very long prompts
work perfectly:

- Lumifel, 2026-08-12 — *"8k token for a prompt is already a lot. But There's incredibly
  detailled giant prompt that were used and the model follow perfectly here."* `[OBSERVED]`
- Juampab12, 2026-08-12 — *"I did something like 30k character prompt and the videos were
  like 3x slower haha."* Still generated. `[OBSERVED]`
- DaxRedding, 2026-08-05 — *"with a crazy long prompt and it nails what I was thinking."*
  `[OBSERVED]`

**Reconciliation the evidence supports** (`[INFERRED]`): length is not the variable. **Density
of non-conflicting, correctly-keyed instruction per second of output** is. Contradictory or
redundant text is worse than no text. ErosDiffusion, 2026-08-09, states it best: *"i think you
must be careful to not re-define stuff when not needed. and pay attention to conflicting
instructions, if you add too much it will be there."* `[OBSERVED]`

### 4.1 Working numbers

| Quantity | Value | Provenance |
|---|---|---|
| Hosted API hard prompt cap | **7000 characters** | `[OFFICIAL]` |
| Full-Reference description body, healthy band | **220–389 words**, median ~355 | `[INFERRED]` (measured across 12 reference-mode reference prompts) |
| Whole Full-Reference prompt, healthy band | **~2.5–4.2 kB**, median ~3.3 kB | `[INFERRED]` (same corpus; nothing in it exceeds 4169 characters) |
| Official guidance for the description field | **350–500 English words**, "guidance, not a hard quota" | `[OFFICIAL]` |
| Reported working prompts in the wild | cluster **1500–2500 characters** | `[OBSERVED]` (community posts, 2026-08-05 to 2026-08-12) |

### 4.2 What to cut first, if you are over budget

Cut from the bottom of this list upward. `[INFERRED]` + `[ASSERTED]` (procedure).

1. Decorative adjectives and mood words that name nothing visible.
2. Repeated provenance ("from `<Picture 1>`" restated in every sentence).
3. Duplicated sound descriptions across the description body and the soundscape field.
4. Re-descriptions of what a reference already supplies (see §7.3).

**Never** cut to save characters: a reference label, a task-type prefix, exact dialogue, a
retention line, or an endpoint constraint. `[OFFICIAL]` (these are the load-bearing parts).

### 4.3 Diagnosing the fallback

If output looks like a competent text-to-video render of your prompt with none of your
reference identity in it, before rewriting wording, check in this order:

1. Is the reference model loaded at all? (Wrong checkpoint is a silent no-op — see §9.)
2. Is the reference input **enabled** in the workflow's toggle panel? `[OBSERVED]` (foxydits,
   2026-08-06: *"You didn't enable `<Audio 1>` in the Reference Control Panel toggle
   section."*)
3. Is every attached file named in the prompt text?
4. Only then: cut the prompt down and re-run.

---

## 5. Character sheets and stylesheets

A "character sheet" here means one image containing several views of the same character
(face close-up, front full body, rear/side full body), usually generated with a dedicated
image-model LoRA and composited on a plain background.

### 5.1 Evidence FOR sheets

| Observer | Date | Report |
|---|---|---|
| chancelor | 2026-08-11 | *"Minimax does an incredible job at retaining likeness through single collage reference images. Honestly better than any character LoRA i've made."* Also: *"I don't think character loras are necessary for ref2va. Krea stylesheets work incredibly well when referenced."* |
| PoliteCat | 2026-08-04 | *"I am endlessly amazed at how well this model does with a simple character sheet reference."* |
| Ryko | 2026-08-07 | *"So (of course) MMH3 makes short work of character sheets"* |
| VK | 2026-08-11 | *"Prompt with character sheet. Model is impressive."* |
| Janosch Simon | 2026-08-07 | Sheet + separate environment reference: *"the result mind blowing"* — at only 0.6 MP references |
| Vérole | 2026-08-09 | Sheet + ref2va at 6 steps, working |
| crinklypaper | 2026-08-07 | *"multiple character sheets and references with character swap exactly that"* |
| MACRO | 2026-08-09 | *"you can put your character sheet in ... and get consistent story boards with props or characters"* |

All `[OBSERVED]`, all single-author, none blind or repeated.

### 5.2 Evidence AGAINST sheets

| Observer | Date | Report |
|---|---|---|
| Illynir | 2026-08-09 | The strongest direct counter: *"It's a bad idea to put all the distances on a single image, like a character sheet, **unless you use a very high resolution**. You'll get better results if the three are kept separate in different ref image"* |
| WorldX | 2026-08-09 | *"my problem with the ref2va is that i use a character sheet a good one but it still doesnt produce the same likeness of the the character"* |
| shotgun messiah | 2026-08-08 | Prefers many separate images: a sheet *"would limit you to more inputs"* |
| Panthero | 2026-08-09 | Reports the separate-image approach working well: *"I use three separate images as references (front, back, face) in high res and the consistency is ver very good at 1MP."* |

All `[OBSERVED]`.

**Verdict: unresolved.** Nobody ran a controlled comparison. The untested reconciliation
nobody in the corpus stated explicitly is **resolution**: a sheet divides your effective pixels
across N panels, so a sheet at low resolution gives each view fewer pixels than a dedicated
image would. `[INFERRED]`. Practical reading: use a sheet if it is high resolution; use
separate images if it is not; do not promise likeness retention either way.

### 5.3 White cutout backgrounds — does the background leak?

**Untested. There is no evidence in either direction.** `[OBSERVED-absent]`

- chancelor's working sheet-generator prompt (2026-08-11) explicitly requests *"pure white
  background"* and he reports excellent likeness retention. He never addresses backgrounds in
  the **output**. This is weak indirect evidence against a harmful leak.
- Nobody in the corpus reports a reference's white background bleeding into a generated scene.
- Nobody reports that it does not.

Do not state that white backgrounds are safe, and do not state that they leak.

**What to write anyway, as cheap insurance.** The reference-fencing pattern below is
`[OBSERVED]` effective for *other* attribute leaks (Grimm1111 reported reduced flicker after
adding it, 2026-08-09), and costs about 25 words. Applying it to background specifically is
`[INFERRED]`.

```text
<Subject 1> is only the identity, face, hair, age, and distinguishing physical features of the woman in <Picture 1>.
<Picture 1> provides subject identity only. It does not provide lighting, exposure, color grading, background, camera angle, pose, framing, or scene composition.
```

Then state the target background positively in the description body, so there is something
for the model to render instead of the reference's background. `[INFERRED]`

### 5.4 How to build a sheet, per practitioners who reported success

chancelor's generator prompt, 2026-08-11, verbatim in the load-bearing parts — note the two
explicit design choices:

```text
... High quality photography in collage format. No visible text, labels, or separating lines, pure white background.

[Panel 1] - top half - Closeup of girl's face
[Panel 2] - bottom half left - Front full body view
[Panel 3] - bottom half right - Rear full body view
```

`[OBSERVED]` (chancelor, 2026-08-11, reported working).

Two things are worth carrying forward:

1. **"No visible text, labels, or separating lines."** Independently supported by a separate
   finding: ND, 2026-08-10, reports that a 2× latent refinement pass *"may hallucinate
   lettering, thin lines, or other artifacts — especially when the reference image contains
   logos, text, panel borders, or multiple character views"*. `[OBSERVED]`. A sheet with
   labelled panels and borders is exactly that input.
2. **A clean, uniform background.** Rationale is unstated by its users; see §5.3.

Sheet panels do **not** appear to need individual description in the H3 prompt. Ryko asked
directly on 2026-08-07 — *"Did you have to describe the areas of the character sheet?"* — and
got no answer in the corpus. chancelor's panel labels live in the **image generator's** prompt,
not in the H3 prompt. `[OBSERVED-absent]` — treat as unknown, and default to not describing
panels.

### 5.5 Identity rigs that people reported working

- **blake37, 2026-08-08** — *"Bigger than your output works well. Also consider 2 references
  with the face being bigger since that is what most people will look at for identity."*
  `[OBSERVED]`
- **Panthero, 2026-08-09** — front + back + face, high res, 1 MP output. `[OBSERVED]`
- **JonkoXL, 2026-08-09** — *"also probably use closeup refs regardsless of whether the
  generation has them far away"* `[OBSERVED]`
- **AvidGamer, 2026-08-07** — the clearest positive multi-role report: *"Face from Image 1,
  Body type from Image 2, 'part' reference in Image 3. Voice in Audio 1. With the proper
  wording and prompting it puts it all together seamlessly and really quite accurately."*
  `[OBSERVED]`

---

## 6. How many references before quality degrades

**No numeric threshold exists in any source.** The question was asked at least four times in
the corpus (protector131090 2026-08-02; xwsswww 2026-08-03; Ruairi Robinson 2026-08-03; The
Shadow 2026-08-04) and never answered. `[OBSERVED-absent]`

What *is* established:

| Claim | Evidence |
|---|---|
| Reference count drives **cost**, not quality | `[OBSERVED]` — KingGore2023, 2026-08-04: *"More refs more gen time."* Lodis, 2026-08-06: *"reference model can get real heavy if you give it tons of refs"*. jab, 2026-08-10, reports out-of-memory on the reference node. |
| More references is **not** a likeness dial | `[OBSERVED]` — Albert, 2026-08-09: *"my ref faces become distorted after generating no matter how many refs I put"* |
| 3–4 well-role-separated assets work well | `[OBSERVED]` — AvidGamer (4 assets, 2026-08-07); DiXiao (3 images + voice, 2026-08-06); Relven and Richard Servello (2026-08-09) both post working 4-asset templates: `<Picture 1>` man, `<Picture 2>` girl, `<Picture 3>` environment, `<Video 1>` motion |

**Working guidance** `[INFERRED]`: role clarity beats reference count. If likeness is failing,
fix framing scale and role fencing before adding a fifth image.

### 6.1 Cross-reference contamination

A trait belonging to one reference mutates onto a different reference's subject.

- **JustRed, 2026-08-06** — *"when you give it a reference it sometimes mutates a part that is
  the reference related to another reference, focusing too hard on it."* `[OBSERVED]`
- **JustRed, 2026-08-06** — *"unironically the higher I go in steps the harder it deforms one
  small part of the reference / as if its some localized noise issue"*. He reports the effect
  is sampler-dependent and absent with one particular sampler. `[OBSERVED]` — that part is an
  **engine** finding, not a prompt finding; see the appendix.

**Prompt-side mitigation** — fence each reference both positively and negatively, one line per
reference. Grimm1111, 2026-08-09, reported reduced flicker after adding exactly this;
IrrationalSoup, 2026-08-09, converged on the same shape independently. `[OBSERVED]` (2
practitioners, uncontrolled).

```text
<Subject 1> is only the identity, face, hair, age, and distinguishing physical features of the woman in <Picture 1>.
<Subject 2> is only the identity, face, hair, age, and distinguishing physical features of the man in <Picture 2>.
<Picture 1> provides subject identity only. It does not provide lighting, exposure, color grading, background, camera angle, pose, framing, or scene composition.
<Picture 2> provides subject identity only. It does not provide lighting, exposure, color grading, background, camera angle, pose, framing, or scene composition.
```

Related: character **swaps** fail when source and target are similar. protector131090,
2026-08-12: *"if characters have anything similar (like they both women) it wont work properly.
but if its a woman for man or for anime panda - it works like magic"*. Dever, 2026-08-12:
*"it's easier for the model to understand/isolate the 'to' and 'from' when they're wildly
different. if similar you need to be more precise in your prompt (what to keep, what to
change)."* `[OBSERVED]` (2 practitioners, same day, mutually corroborating).

---

## 7. Writing `subject_definitions`

### 7.1 What each entry must contain

One line per tracked item. Each line names four things: **the label**, **the role**, **the
attributes to follow**, **the provenance**. `[OFFICIAL]`

```text
<Subject 1> is the chef whose identity and clothing come from <Picture 1> and whose walking motion comes from <Video 1>.
```

Multi-source single subject `[OFFICIAL]`:

```text
<Subject 1> is the woman whose identity comes from <Picture 1>, whose costume comes from <Picture 2>, and whose walking motion comes from <Video 1>.
```

Role-limited form, which is stronger in practice `[OFFICIAL]` (guide example) + `[OBSERVED]`
(the community independently converged on it):

```text
<Subject 1> is the woman whose face, hairstyle, and recognizable body identity come from <Picture 1>; her costume is newly specified by the target prompt.
```

Style as a subject, scoped `[INFERRED]` (from the official role-separation requirement):

```text
<Subject 2> is the mid-century flat graphic treatment from <Picture 3>, applied to rendering only and not to composition, identity, or object placement.
```

### 7.2 What to leave out

| Leave out | Why |
|---|---|
| `<Subject 1> uses all references.` | Role left unresolved — the definition does no work. `[OFFICIAL]` |
| A standalone `<Picture N>` entry for an image that only sources a face or a style | Violates the one-label rule, §2.1. `[OFFICIAL]` |
| A label for every visible detail | Retention analysis becomes unmanageable; prompt length wasted. `[INFERRED]` |
| Numeric weights — "identity weight 0.8, motion weight 1.2" | **No user-facing per-reference weighting mechanism exists.** Kijai, answering the question directly on 2026-08-08, said it is *"something he is working on"*. Express priority semantically instead. `[OBSERVED]` (implementer statement) |
| Speaker IDs `(S1)` inside `retention_analysis` | Speaker IDs are not retention vocabulary. `[OFFICIAL]` |
| Labels for assets the user only **described** but did not attach | `[ASSERTED]` (hygiene rule) |
| New labels introduced anywhere outside `subject_definitions` | A label keeps one meaning across the whole prompt and is introduced exactly once. `[OFFICIAL]` |

Semantic priority instead of weights `[OBSERVED]` (Kijai's own suggested phrasing):

```text
Preserve the woman's identity from <Picture 1> while using <Video 1> only for walking motion and camera rhythm.
```

### 7.3 Do not re-describe in the shot body what a reference already supplies

If `<Picture 1>` supplies the face, do not spend 40 words in the description body describing
the face. Refer to the subject and spend the words on what the reference does **not** supply:
action, staging, camera, lighting, state change.

- **KingGore2023, 2026-08-09** — *"The ref images already serve as strong guide. U don't have
  to write long prompt every time."* `[OBSERVED]`
- **mdkb, 2026-08-12** — *"give it ref images of characters then you wont need to. its nails
  mine very well."* `[OBSERVED]`
- **ErosDiffusion, 2026-08-09** — *"i think you must be careful to not re-define stuff when not
  needed. and pay attention to conflicting instructions, if you add too much it will be
  there."* `[OBSERVED]`

**Contradicting evidence — read this before applying the rule absolutely.** Other
practitioners report that describing the referenced content in words *helps*:

- **DawnII, 2026-08-10** — *"make sure to add descriptors about the subject in `<Picture 1>`
  for best results. sometimes describing the replaced character can help, especially if
  multiple characters on screen at once."* `[OBSERVED]`
- **DawnII, 2026-08-10** (drift test) — *"if I give it a picture of mona lisa, over time it
  will drift to a more realistic version. If I instead prompt the mona lisa specifically, it
  will keep the same style."* `[OBSERVED]`
- **JonkoXL, 2026-08-10** — *"if i dont autistically describe the first frame for Fl2a First
  frame it also usually ignores it"* `[OBSERVED]` (first-frame mode, not reference mode)

**Resolution that fits both sets of reports** `[INFERRED]`:

- Do **not** duplicate the reference's *definition* — one definition, in `subject_definitions`,
  and nowhere else.
- **Do** re-assert a short identity anchor at points where drift can occur (each shot
  boundary), as a list rather than a re-description:

```text
Her facial identity, short dark curls, white chef's jacket, blue neckerchief, and silver earrings remain consistent with <Picture 1>.
```

`[OBSERVED]` as mitigation, not a cure — four independent practitioners report unfixed drift
anyway (Albert, WorldX, mamad8, BecauseReasons, 2026-08-04 to 2026-08-09).

### 7.4 Retention markers

Every label gets exactly one line in `retention_analysis`, with one marker. `[OFFICIAL]`

Visible references (`<Subject N>`, `<Picture N>`, `<Video N>`) — use **only**:

| Marker | Meaning |
|---|---|
| `fully_preserved` | The defined role is fully retained. |
| `partially_preserved` | The defined content **is** used, but some defined characteristics change. |
| `attribute_transfer` | A characteristic moves from one visible reference onto a **different** identifiable target. |
| `weak_reference` | Only broad similarity — style, category, composition, atmosphere. |

Audio references (`<Audio N>`) — use **only**: `fully_copy`, `partially_copy`, `reference`,
`weak_reference`. All `[OFFICIAL]`. See file 04 for the audio semantics.

Two rules people get wrong:

- **Retention is role-relative.** An identity-only role stays `fully_preserved` even though the
  costume, pose, background and action all change in the target. New target actions and
  backgrounds are not fidelity losses. `[OFFICIAL]`
- **`weak_reference` ≠ `partially_preserved`.** `weak_reference` is loose stylistic influence
  only; `partially_preserved` means the defined content is genuinely in use. `[OFFICIAL]`

Line format — a hyphen with spaces, not an em dash. `[INFERRED]` (12 of 12 worked examples):

```text
<Subject 1>: fully_preserved - the defined identity and appearance are preserved.
<Video 1> (motion structure): attribute_transfer - source physical movements are mapped to the target.
<Audio 1>: reference - its vocal timbre guides <Subject 1> (S1) without copying the original signal.
```

---

## 8. Likeness and identity failure modes

| Symptom | Cause | Fix | Provenance |
|---|---|---|---|
| Face degrades or garbles as the clip runs | Identity not restated where it can drift | Re-assert the attribute list at each shot boundary (§7.3). Mitigation, not a cure | `[OBSERVED]` — Albert, WorldX, mamad8, BecauseReasons, 4 independent reports of unfixed drift |
| Likeness holds in close-up, collapses in wide/full-body | Reference resolution versus framing scale | Frame at or near the reference's scale; supply a close-up reference even for distant shots | `[OBSERVED]` — BecauseReasons, 2026-08-04: *"Terrible likeness and facial garbling with anything other than a medium closeup."* + JonkoXL, 2026-08-09 |
| Drift accumulates with clip length | Not diagnosed | Shorter clips; less aggressive quantization | `[OBSERVED]` — Visionmaster2 2026-08-04 (*"about 36 frames, then the drift becomes even worse"*); embedding-shapes 2026-08-07; GalaxyTimeMachine 2026-08-10 |
| Style drifts toward photorealism over the clip | Style carried only by the image | Name the style in words as well as by reference | `[OBSERVED]` — DawnII, 2026-08-10, Mona Lisa test |
| Colour shifts to generic skin/lighting when an image reference is used | Not diagnosed | None reported | `[OBSERVED]` — Karsticles, 2026-08-12, 1 report, unsolved |
| Identity comes out "overcooked" or too weak | Model-side, per the authors | None reported | `[OBSERVED]` — DaxRedding, 2026-08-11, attributing the statement to the model's developers; second-hand |
| A reference's lighting/grade/background arrives with the identity | Look attributes travel with an identity reference | Fence the picture (§6.1) | `[OBSERVED]` — Grimm1111, 2026-08-09, reported flicker reduction |
| The model copies the whole source image instead of taking guidance | Role stated as an object, not as a job | Say what to take **and** what not to take | `[OBSERVED]` — embedding-shapes diagnosis 2026-08-09; IrrationalSoup working prompt 2026-08-09 |
| An identity photo is silently pinned as an exact first frame | Frame semantics inferred from mere presence of an image | Presence of an image establishes nothing. Cite it inside the subject and use the `reference generation` task type | `[OFFICIAL]` |
| A video motion reference is described as pixel-precise | Precision over-promised | Write *"follow the camera movement and rhythm of `<Video 1>`"* | `[OBSERVED]` — BNP4535353, 2026-08-10, reading official guidance: motion copying gives *"approximate trajectories"* and *"is not a universal solution"*; Kijai: *"more a reference than controlnet"*. Disputed by Ryko, 2026-08-06, who reports it working exactly |

The "does not supply" pattern, verbatim from IrrationalSoup, 2026-08-09 `[OBSERVED]`:

```text
<Subject 1> is the woman whose complete visual identity (face, facial structure, eyes, skin tone, hair style and color, body proportions, and overall appearance) comes exclusively from <Picture 1>. Her body motion, posture, gestures, head movements, timing, and physical performance come from the original woman in <Video 1>. <Video 1> supplies the camera path, framing, background, environment, lighting, composition, action timing, and the original subject's body motion. It does not supply the face or identity.
```

---

## 9. Platform differences

### 9.1 Hosted site versus local

| Difference | Detail | Provenance |
|---|---|---|
| **Reference tag syntax differs** | Prompts copied from the hosted chat UI address assets as `@Image1` / `@Audio1`. The model's own documented syntax is `<Picture 1>` / `<Audio 1>`. Do not paste hosted-UI prompts into a local workflow unchanged. | `[OBSERVED]` — iGoon, 2026-08-03: *"if you copy prompts from the minimax chat ui the prompts reference like @Image1 @Audio1"*. Kijai: *"the actual model should use `<Picture i>` tags"* |
| **The hosted path may run a prompt-enhancer stage first** | Which is why hosted-facing prompt styles differ from what the model itself expects | `[OBSERVED]` — Kijai; corroborated by blake37, 2026-08-08: *"We just don't have a local prompt enhancer that's as strong as the API stuff."* |
| **Motion transfer reported to work on the hosted API and fail locally** | Unresolved. Tested against full-precision local weights and still failed for the reporter | `[OBSERVED]` — protector131090, 2026-08-10: *"I tried the full BF16 model, and no—it does not work like the API... The API can easily transfer motion and lip-sync, while locally i can't even get it working properly"* — 1 reporter, unresolved |
| Hosted API constraints | Prompt ≤ 7000 characters; durations are integer seconds; first/last-frame image width and height each in [256, 5760]; aspect ratio 2:5 to 5:2 | `[OFFICIAL]` |
| Audio-only input | Disallowed on the open-weight surface; the hosted API docs do not repeat the restriction | `[OFFICIAL]` on both sides — an execution-surface split, not a contradiction to resolve. Validate the target surface before promising it will run |

**A correction to a claim in circulation.** A widely-repeated attribution of a
"hosted site versus local ComfyUI reference behaviour" comparison to a specific practitioner on
2026-08-03 **could not be located** in the corpus. An author-scoped search of that practitioner's
entire message history in the relevant channels returned nothing of the sort. Treat any
attributed website-versus-local claim as **unverified** unless you can see the source.
`[OBSERVED-absent]`

### 9.2 Local reference behaviour worth knowing

| Item | Detail | Provenance |
|---|---|---|
| **Wrong checkpoint silently degrades references** | Reference work needs the reference-model weights (`ref2va`), not the first/last-frame weights (`fl2va`). Loading the wrong one produces weak-or-absent reference behaviour with no error | `[OBSERVED]` — embedding-shapes 2026-08-09, LukeG89 2026-08-09, avataraim 2026-08-05 |
| **Reference sizing option** | `max` uses references at (up to) original size — better identity detail, slower, heavier. `match` rescales references toward output size — faster | `[OBSERVED]` — Ryko, 2026-08-06: *"max = use references at original size, match = rescale to output size"* |
| **References need not match output resolution or aspect ratio** | They are downscaled internally. Do not crop or letterbox a reference to "fit" the output | `[OBSERVED]` — implementer report; corroborated by the `max`/`match` option existing at all |
| **Some workflows expose slot names, not tags** | e.g. `ref_image_0`, `ref_video_0` in the node UI, while the prompt still uses `<Picture 1>` | `[OBSERVED]` — NebSH 2026-08-03; xwsswww 2026-08-10 |
| **Reference inputs have an enable toggle** | A disabled input is a silent no-op that looks exactly like a prompt failure | `[OBSERVED]` — foxydits, 2026-08-06 |

### 9.3 THE 0-INDEX / 1-INDEX TRAP

> **The local node UI numbers reference inputs from 0. The prompt syntax numbers them from 1.**

- **hicho, 2026-08-07** — *"comfyui input dont match with what we use in the prompt, all input
  start with image 0, video 0, audio 0 while we refrence them in prompt by 1, 2 etc."*
  `[OBSERVED]`
- Confirmed by usage in the wild: some practitioners write `image 0` / `<Picture 0>` in the
  prompt to match the UI (djbfilmz, 2026-08-12; Jemmo, 2026-08-05), while the documented syntax
  is 1-based. `[OBSERVED]`

**Consequence:** the image plugged into the slot labelled `0` is `<Picture 1>` in the prompt.
Off-by-one here silently binds the wrong role to the wrong file — an identity image gets treated
as an environment, and the output looks like the model "ignored" your reference.

**Tag order follows connection order** — first connected image → `<Picture 1>`, second →
`<Picture 2>`, first connected video → `<Video 1>`, first connected audio → `<Audio 1>`.
`[ASSERTED]` — this is stated as fact in several derived documents and **was never verified
against an official source**. If connection order is unknown and materially affects the prompt,
ask rather than guess. Never number tags by semantic importance or by filename.

**Also unresolved:** several practitioners mix conventions inside one prompt
(`<image 1>` alongside `@Video1`). embedding-shapes, 2026-08-10: *"you're mixing to different
formats even ... needs to be the same everywhere, and the right syntax"* and *"it's very 'prompt
sensitive', especially around references"*. `[OBSERVED]`. Pick one convention — the documented
`<Picture N>` / `<Video N>` / `<Audio N>` / `<Subject N>` family — and use it everywhere.

---

## Appendix — engine issue, not a prompt issue

**Attaching any reference silently overwrites keyframes (local ComfyUI core).**

This is a code-level defect. **No prompt wording fixes it.** It is documented here so readers
stop trying to solve it by rephrasing.

Reported by **Chandler, 2026-08-06**, verbatim `[OBSERVED]` (implementer-grade source reading,
not a controlled test):

> "H3 keyframe completion is blocked by three things in ComfyUI core, and only the third
> actually gates the task.
> 1. `model_base.py` assigns `cond_video_latents` twice — once from keyframes, then again from
>    refs. **Second wins, so any reference silently wipes every keyframe. Keyframes only work
>    when there are no refs, i.e. fl2va only.**
> 2. `ldm/minimax/model.py` sets the keyframe's positional base to `float(text_len)` ('right
>    after text'), ignoring that ref blocks are packed before the target and advance their own
>    cursor. With refs present the anchor lands on rows the refs occupy.
> 3. The one that matters: only first/last keyframe anchors are supported. Keyframe completion
>    means several frames at arbitrary positions with the model filling between them. Core
>    implements exactly two."

**Practical consequences:**

- If you supply a first frame **and** a reference image in the same local job, expect the first
  frame to be discarded. Five independent practitioners reported "it ignores my start frame"
  during the same period; this bug plausibly accounts for a large share of them. `[OBSERVED]`
- Karsticles, 2026-08-08, found the workaround empirically without knowing the cause:
  *"Sometimes FL2VA ignores my 0:00, and REF2VA never does."* — when the opening frame must be
  honoured, route the job to the reference model. `[OBSERVED]`
- A related node-level defect was reported separately: a motion-context node overwriting the
  supplied **last** frame. `[OBSERVED]` — seitanism 2026-08-08, Simon 2026-08-09

Other engine-side items that masquerade as reference-prompt failures, listed so you can rule
them out: sampler-dependent reference corruption at high step counts (JustRed, 2026-08-06);
out-of-memory on the reference node with large references (jab, 2026-08-10); acceleration LoRAs
degrading prompt adherence generally (embedding-shapes, 2026-08-10: *"people need to stop
cranking up all optimizations to 11 :D Prompt adherence gets lower with seemingly all the tricks
we have available."*). **None of these values, node names, sampler names or filenames may ever
be written into an H3 prompt.**
