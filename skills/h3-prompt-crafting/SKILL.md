---
name: "h3-prompt-crafting"
description: "Write video-generation prompts as structured schemas; diagnose failures per field. Includes MiniMax H3 notes."
license: "MIT"
---
# Schema-First Video Prompting

## Use when
- Generating video from text, frames or reference media on ANY
  instruction-style video model (schema-based models: MiniMax H3; cinematic-
  grammar models: Seedance/Kling/Veo class; descriptive models: older SD-video)

- A generation came back wrong and needs diagnosis
- Converting a shot idea or storyboard beat into H3's prompt schema

## Instructions

1. Identify what you are SUPPLYING and pick the input mode the backend
   defines for it — text only / first frame / first+last frame / last frame /
   reference media (identity, location, style, voice). Universal rule:
   wrong input-mode = erratic output that looks like model weakness but is
   format mismatch.
2. Write to the schema the mode demands — subject definitions, action beats,
   camera vocabulary from the CLOSED set, dialogue/audio syntax where native
   audio applies. Free prose, mood adjectives and cinematography jargon are
   the main failure cause.
3. Diagnose failures against the failure catalogue before re-rolling:
   classify what came back wrong (subject drift, motion artefact, camera
   violation), identify which schema field caused it, fix THAT field.
4. Respect length and shot budgets; plan shot changes at deliberate beats.
5. Provenance honesty: distinguish [OFFICIAL]/[OBSERVED]/[INFERRED] guidance
   when advising on this fast-moving model.

## Stop conditions
- Never free-prose an H3 prompt when the schema field exists.
- Never re-roll more than twice without classifying the failure mode first.

## Escalation
- Persistent schema-compliant failures escalate as candidate model issues
  with prompts + outputs attached, not silent retry loops.

## Model notes — MiniMax H3 (worked example)
Mode names: T2VA (text), I2VA (first frame), FL2VA (first+last), L2VA (last
only), Ref2VA (full-reference, six-field schema). Fields:
integrated_multimodal_description / overall_soundscape /
non_diegetic_music. Camera vocabulary is a CLOSED set (Zoom In/Out,
Push In/Pull Out, Pan L/R, Truck L/R, Tilt Up/Down, Pedestal Up/Down,
Arc Shot...) — anything outside it is loose prose. Failure catalogue:
123 entries across nine symptom chapters.
