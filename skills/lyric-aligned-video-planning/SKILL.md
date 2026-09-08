---
name: "lyric-aligned-video-planning"
description: "Plan music videos with WhisperX forced alignment driving shot changes at word level."
license: "MIT"
---
# Lyric-Aligned Video Planning

Model note: this workflow was proven on MiniMax H3 blocks at 24 fps; the
alignment pipeline itself is model-agnostic.

## Use when
- Making music videos where shots should land on lyric moments
- Coordinating H3 block generation across a full song timeline
- Any audio-synced video where timing precision matters

## Instructions

1. Forced-alignment pipeline: transcribe the track for initial timestamps;
   music causes transcript errors, so then supply the EXACT lyrics and let
   the aligner determine only WHEN each word is pronounced. (WhisperX is the
   proven tool for this; any forced aligner with word-level output works.)
2. Convert aligned word timestamps (accurate to tens of ms) into 24fps
   timecode — the frame grid everything else is planned on.
3. Build video prompts around the actual lyrics: each shot change triggers
   at a meaningful lyric boundary, not a fixed interval.
4. Manage block boundaries explicitly: if the backend stitches generated
   blocks with a frame-overlap window (e.g. H3's 22-frame overlap), plan
   motion that carries across boundaries so cuts never pop.
5. Keep a shot list keyed by timecode: start frame, end frame, lyric anchor,
   prompt variant, block index.

## Stop conditions
- Never cut blocks without accounting for inter-block frame overlap.
- Never align by ear/eyeball when forced alignment is available.

## Escalation
- Alignment quality below tolerance (drifting >100ms) escalates to audio
  review of the track mix before video production continues.
