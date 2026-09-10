---
name: h3-prompt-director
description: "Use for H3 prompts needing style packs or gold examples."
version: 1.0.0
license: MIT
---
# H3 Prompt Director — craft kit (v2, 2026-08-13)

The "shareable pack" layer for MiniMax H3 prompting. The sibling skill **h3-prompting**
carries the official schema/grammar with provenance tags; this kit carries the *craft*:
style packs, gold examples, temporal-animation technique, and the QA suite. Use both together.

## File map (all under `references/`, prefixed to keep order)

| File | When to open |
|---|---|
| `00_README-pack.md` | Pack manifest + SHA256 file |
| `01_CUSTOM_GPT_INSTRUCTIONS.md` | The CustomGPT system prompt itself (mode rules, exact output contracts, silent validator) |
| `02_H3_MODES_AND_COMFYUI.md` | Mode decision table, reference limits, weight families, ref_image_size match/max |
| `03_H3_PROMPT_GRAMMAR.md` | Canonical structure, exact alignment lines, camera vocabulary, density control, style-pressure grammar |
| `04_H3_EXAMPLES.md` | Worked examples for all five modes + voiceover-across-cut |
| `05_QA_TEST_SUITE.md` | 29 pass/fail tests to self-check a prompt before delivery |
| `06_OFFICIAL_GUIDE_CLEAN_COPY.md` | Clean copy of the official T2VA/I2VA/FL2VA/L2VA guide |
| `07_REF2VA_FULL_REFERENCE_GUIDE.md` | Six-section contract, label semantics, retention markers, empirical addenda |
| `08_H3_AESTHETIC_MOTION_AUDIO_LIBRARY.md` | V01-V24 visual packs, M01-M08 motion, F01-F08 finish, A01-A08 audio |
| `09_H3_STYLE_REFERENCE_ANCHORS.md` | 30 named-style anchors mapped to injectable traits (UPA, Ghibli, Akira, LAIKA…) |
| `10_H3_STYLE_PICKER_RULESET.md` | The automatic style picker: hard rules, gates per mode, keyword routing, style-strength score G/S/P/M/T |
| `11_T2VA_GOLD_EXAMPLES.md` | T01-T05 |
| `12_KEYFRAME_GOLD_EXAMPLES.md` | I01-I05, F01-F04, L01-L04 with exact alignment lines |
| `13_REF2VA_GOLD_EXAMPLES.md` | R01-R11: identity+voice, multi-picture, camera-video, video edit+audio reuse, continuation, style transfer, material process |
| `14_EDGE_CASE_GOLD_EXAMPLES.md` | Ambiguous single image, dialogue across cut, reused-song lyric, conflicting style sources |
| `15_H3_TEMPORAL_ANIMATION_TECHNIQUES.md` | Cadence ladder (on twos/fours/eights), smear vs blur, line boil, in-place walk protocol |
| `16_H3_REF2VA_STYLE_TRANSFER_LAB.md` | Reference-video style transfer decision tree, transfer hierarchy, content firewall |

## Quick core rules (from the kit)

- **Mode picks the schema:** T2VA/I2VA/FL2VA/L2VA → three fields
  (`integrated_multimodal_description` / `overall_soundscape` / `non_diegetic_music`),
  with exact alignment lines for the image modes. Ref2VA → six fields
  (`subject_definitions` / `summary` / `retention_analysis` / `detailed_description` / audio fields),
  no alignment line.
- **One pack per category max** (1 medium + 1 motion + 1 finish + 1 audio), unless explicit hybrid.
- **Style pressure stack:** prefer 4-6 correlated cues implying one visual system; score ≥3 of G/S/P/M/T.
- **Cadence is not a style pack** — route `on twos/fours/eights` through file 15, never claim literal frame repetition.
- **Ref2VA style transfer:** reference controls HOW, user controls WHAT; derived style = `<Subject N>` +
  `attribute_transfer`; add a content firewall to block source-character leakage.
- **Ref2VA detailed_description** 350-500 words; don't over-length it or references silently degrade.

## QA discipline

Run the relevant 05_qa-test-suite checks silently before delivering. For style stress tests,
separate the three questions (style / motion-grammar / cadence) or failure diagnosis becomes ambiguous.
