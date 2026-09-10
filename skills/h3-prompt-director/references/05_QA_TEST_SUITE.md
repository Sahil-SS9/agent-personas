# H3 Custom GPT QA Test Suite

Run these in GPT Preview after configuration. A passing answer should satisfy the checks without needing a second user turn unless the test is intentionally ambiguous.

## Test 1 — direct T2VA

User:

`Create a 5-second cinematic prompt: a baker opens a tiny shop before dawn and says exactly “First batch.” No background music.`

Pass criteria:

- No alignment instruction.
- Exactly three fields.
- Dialogue is `<d>[English] First batch.</d>` with a stable speaker ID.
- Sound effects are in the integrated description and/or soundscape.
- `non_diegetic_music: N/A`.

## Test 2 — I2VA image preservation

User attaches one image and says:

`Use this as the first frame of a 6-second video. She slowly closes the book, looks toward the window, and whispers “Not tonight.”`

Pass criteria:

- Exact I2VA first line.
- The opening preserves visible identity, clothing, pose, objects, composition, and scene anchors without inventing unsupported specifics.
- The action develops forward from the image.
- Dialogue is exact.

## Test 3 — ambiguous single image

User attaches one image and says:

`Make a six-second H3 prompt using this.`

Pass criteria:

- GPT asks one concise question: first frame, last frame, or general reference.
- GPT does not silently assume I2VA.

## Test 4 — FL2VA continuity

User attaches two images and says:

`Picture 1 is first, Picture 2 is last. Connect them in one continuous 8-second shot with no music.`

Pass criteria:

- Exact FL2VA line with Shot 1 for both pictures and `8.00`.
- One shot, no cut timestamp.
- Describes intermediate state changes rather than two static captions.
- Lands exactly on Picture 2.

## Test 5 — L2VA multi-shot final number

User attaches one final image and says:

`End exactly on this frame at 7 seconds. Use two shots: first the glass starts sliding, then cut close as it falls and breaks.`

Pass criteria:

- Exact L2VA line says `[Shot 2]` and `7.00`.
- Shot 2 has a legal increasing cut time below 7 seconds.
- The last shot converges on the reference.

## Test 6 — Ref2VA role assignment

User:

`In ComfyUI I connected a portrait first, a motion video second, and a voice clip third. Use the portrait only for identity and clothes, the video only for camera motion, and the audio for the woman's voice. She says “Meet me upstairs.”`

Pass criteria:

- Uses `<Picture 1>`, `<Video 1>`, and `<Audio 1>`.
- Uses exactly six sections and no boundary-frame line.
- Defines one or more `<Subject N>` items from the sources.
- Summary begins with valid bracketed task types.
- Retention analysis uses fixed visual/audio markers.
- Voice identity points to `<Audio 1>`.
- Exact dialogue is preserved.

## Test 7 — visible text

User:

`A night bus passes a neon store sign that must read exactly 营业中. The sign flickers twice.`

Pass criteria:

- Visible string appears in English double quotes as `"营业中"`.
- It is not translated or respelled.

## Test 8 — off-screen voiceover

User:

`A man is visible but we hear his internal narration: “I missed the last train.” His mouth must not move.`

Pass criteria:

- Uses exact phrase `says in an off-screen voiceover`.
- `<d>` contains only language tag and exact words.
- Immediately states that his lips remain completely closed.

## Test 9 — speech crossing a cut

User:

`Two-shot, 6-second prompt. Her line “I thought the road would take us home.” begins before the cut and ends after it.`

Pass criteria:

- Uses `<scenetrans>` in both dialogue segments.
- Explicitly states audio continuity across the cut.
- Words remain complete, ordered, and unaltered.

## Test 10 — duration honesty

User:

`Make an FL2VA prompt for 5 seconds. I don't know what duration ComfyUI will snap to.`

Pass criteria:

- Uses `5.00` as the requested duration or asks for rendered duration only if exact endpoint precision is essential.
- Does not claim `5.00` is a calculated snapped duration.

## Test 11 — audio classification

User:

`A pianist performs in the room while rain hits the windows. Add no background score.`

Pass criteria:

- Piano performance appears as diegetic action/music in the integrated description.
- Rain and room sounds appear in the soundscape.
- `non_diegetic_music: N/A`.

## Test 12 — output cleanliness

User:

`Give me the final prompt only.`

Pass criteria:

- One fenced text block only.
- No preamble, rationale, settings table, or follow-up offer.

## Test 13 — named cultural reference

User:

`Make this feel like a late-1980s high-detail cyberpunk anime with a rain-soaked city and weighty motorcycle movement.`

Pass criteria:

- Translates the reference into concrete cel detail, lighting, atmosphere, motion weight, and camera traits.
- Does not rely on a title or studio name alone.
- Selects one coherent medium, motion, finish, and audio treatment at most.

## Test 14 — reference-image style override gate

User attaches a watercolor image and says:

`Animate this as the first frame. Preserve its painted look.`

Pass criteria:

- I2VA structure is correct.
- Watercolor/paper traits come from the image and remain consistent.
- No unrelated CG, film, comic, or stop-motion pack is added.

## Test 15 — explicit hybrid

User:

`Use gouache-painted environments with comic-ink characters.`

Pass criteria:

- Clearly assigns gouache to environments and comic ink to characters.
- Does not blend both into an incoherent adjective stack.
- Motion and finish remain compatible with the two assigned layers.

## Test 16 — H3 audio treatment

User:

`Create a luxury perfume macro commercial with close, clean handling sounds and no score.`

Pass criteria:

- Uses premium product/beauty traits and restrained product-precision motion.
- Synchronizes specific handling sounds with visible contacts.
- Keeps the soundscape clean and writes `non_diegetic_music: N/A`.

## Test 17 — action verb does not trigger media generation

User:

`Generate a cinematic 6-second video of a baker opening a shop at dawn.`

Pass criteria:

- Returns a T2VA prompt as text in the required three-field format.
- Does not create or return an image, video, thumbnail, or storyboard.
- Does not invoke a generation tool or say that generation has started.

## Test 18 — ambiguous attached image remains prompt-only

User attaches one image and says:

`Animate this.`

Pass criteria:

- Asks one concise question about whether the image is a first frame, last frame, or general reference.
- Does not generate or edit the attached image.
- After clarification, returns only the correct H3 text prompt.

## Test 19 — explicit image request is reframed as a prompt

User:

`Create an image of an astronaut in a neon diner, then animate it.`

Pass criteria:

- Explains concisely that this GPT writes H3 video prompts rather than generating the source image.
- Returns an H3 prompt if the scene can be expressed as T2VA, or asks for the source image if the user requires I2VA.
- Does not invoke image generation.

## Test 20 — animation on twos is treated as target behavior, not a guarantee

User:

`Give me a 5-second T2VA test of a woman walking in place, traditional 2D animation on twos at 24 fps. I want to compare adjacent frames afterward.`

Pass criteria:

- Returns exactly the three T2VA fields.
- Keeps one subject, static camera, simple background, and an in-place walk cycle.
- Describes the intended paired playback pattern explicitly, e.g. `A, A, B, B, C, C`.
- Separates 24 fps playback from approximately 12 authored states per second.
- Does not claim that H3 is guaranteed to produce exact duplicate frame pairs.
- Does not add hard cuts, multiple bodies, onion skins, or pose-chart imagery.

## Test 21 — cadence failure repair

User:

`I asked for animation on fours, but H3 made the walk smooth on every frame. Rewrite it to make the reduced in-betweens easier for H3 to understand.`

Pass criteria:

- Uses file 15's repair strategy rather than only repeating `on fours`.
- Simplifies the action to fixed-position or in-place motion before translational locomotion when appropriate.
- Uses observable temporal wording and an explicit repeated-state pattern.
- Avoids stacking `freeze`, `hold`, and `hard cut` language unless the user specifically wants a discontinuity diagnostic.
- Does not promise literal four-frame repetition.

## Test 22 — smear drawing versus motion blur

User:

`A woman snaps her head from right to left in a traditional hand-drawn cartoon. Push the smear-frame technique.`

Pass criteria:

- Describes one or two intentionally authored elongated breakdown/smear drawings during the fastest transition.
- Lands on a clean readable final pose.
- Does not substitute generic photographic motion blur for the smear drawing.
- Keeps exactly one visible character rather than duplicated heads or onion skins.

## Test 23 — hand-drawn moving texture

User:

`Make the paper, watercolor, and ink feel alive frame by frame, but don't have the background paint on and off.`

Pass criteria:

- Keeps major background shapes and color-region boundaries continuously present.
- Describes subtle cycling of pigment grain, watercolor density, paper tooth, edge irregularity, line boil, or registration variation.
- Treats the effect as moving texture rather than a transitional reveal or disappearance.



## Test 18 — Ref2VA single-video style transfer with content firewall

User connects one animation video through `ref_video_0` and says:

`Use this video's animation style for a completely new woman opening an umbrella. Keep my new subject and action; do not copy characters or story content from the reference.`

Pass criteria:

- Uses Ref2VA six-section format.
- Defines reusable style/performance as `<Subject 1>` sourced from `<Video 1>`; keeps `<Video 1>` itself for whole-video timing/cuts/camera only if needed.
- Uses `reference generation`, not `video editing`, unless the user asked to edit the source.
- Uses `attribute_transfer` for the derived style/performance subject rather than preserving the whole source.
- States that reference controls visual/motion language while the new subject, action, setting, props, composition, dialogue, and story remain prompt-controlled.
- Blocks source character identity, anatomy, costume, props, setting, exact composition, exact poses/actions, dialogue, and narrative leakage.
- Does not add an unrelated named animation style that competes with the reference.

## Test 19 — Ref2VA multi-video role separation

User connects three videos in order and says:

`Video 1 has the line style I want, Video 2 has the acting and smears, Video 3 has the cut rhythm. Make a new character doing a completely new action.`

Pass criteria:

- Preserves connection order: Video 1 source, Video 2 source, Video 3 source.
- Defines line/surface and visible performance as derived `<Subject N>` items from their source videos; uses `<Video 3>` directly for whole-video cut/temporal grammar.
- Gives each reference a distinct role in `subject_definitions` and `retention_analysis`.
- Uses `attribute_transfer` for each abstract role.
- Does not blend all three vaguely as "the style."
- Preserves the user's new subject and action.
- Explicitly transfers cut/scale rhythm from Video 3 in the timeline when relevant.

## Test 20 — physical-process reference honesty

User connects a wet-paint-on-glass reference and says:

`Match the actual animation technique, not just an oil-painted look.`

Pass criteria:

- Distinguishes material surface from material process.
- Explicitly describes visible material behavior such as paint redistribution, dragged/smeared intermediate forms, repainted edges, pooling, or backlighting only when supported by the reference.
- Keeps semantic complexity conservative if process fidelity is prioritized.
- Does not promise exact frame-by-frame physical reconstruction.
- Does not claim H3 uses an IP-Adapter or style-embedding mechanism.

## Test 21 — reference video acting grammar

User connects one acting-animation reference and says:

`Use its acting nuance, but make a completely different elderly woman deciding whether to open a letter.`

Pass criteria:

- Uses the reference for acting hierarchy: thought pauses, eye/head order, gesture timing, weight/balance, holds, and recovery.
- Keeps the new character design and narrative independent.
- Does not copy exact source gestures or poses.
- Does not mistake acting reference for video editing.

## Test 22 — style-only versus motion-only distinction

User says:

`Use Video 1 only for the visual style. I want my own motion timing.`

Pass criteria:

- Defines a derived `<Subject N>` from Video 1 only for surface attributes such as line, palette, fill, texture, edge treatment, and background density.
- Does not let Video 1 control pose timing, cuts, or action rhythm unless the user asked for it.
- Keeps user motion instructions authoritative.

## Test 26 — weak still, maximum style freedom

User attaches one still and says:

`Use this only for the broad concept. I want maximum freedom. Make the whole video look like articulated cut paper.`

Pass criteria:

- Uses Ref2VA.
- Defines a `<Subject N>` sourced from `<Picture 1>`.
- Uses `weak_reference`.
- Preserves only the stated broad concept.
- Explicitly releases composition, palette, character design, and treatment.
- Does not use the picture as an opening-frame alignment anchor.
- Applies the cut-paper construction to subject and environment.

## Test 27 — style stress test versus cadence

User:

`Push a papercraft style as hard as possible and animate on eights.`

Pass criteria:

- Treats papercraft construction and cadence as separate controls.
- Strongly describes paper geometry, edges, layering, hinges, and parallax.
- Describes visibly stepped/held poses without guaranteeing exact duplicated frames.
- Does not claim literal on-eights cadence unless frame inspection/workflow evidence is supplied.

## Test 28 — whole-frame style pressure

User:

`Make the astronaut and unicorn look like clay, but keep Times Square realistic.`

Pass criteria:

- Preserves the user's explicit hybrid request.
- Does not automatically apply clay to the whole frame because the user asked for mixed media.
- Clearly states which layer is clay and which remains realistic.

User variant:

`Make the entire world clay.`

Pass criteria:

- Applies clay construction to astronaut, unicorn, crowds, vehicles, architecture, signs, pavement, and atmospheric details.
- Uses material-specific deformation and replacement-pose language rather than only saying `clay style`.

## Test 29 — repair a weak style label

User:

`Make it pixel art. Really push it.`

Pass criteria:

- Does not stop at `pixel art`.
- Adds visible large pixel clusters, stair-stepped edges, restricted indexed-looking palette, hard value ramps, blocky silhouettes, and no smooth antialiasing language.
- Keeps cadence claims separate from pixel construction.
