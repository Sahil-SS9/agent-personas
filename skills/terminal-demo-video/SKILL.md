---
name: "terminal-demo-video"
description: "Record real CLI demo videos as MP4 for feature demos."
license: "MIT"
---
# Terminal Demo Video

## When to use
Record real CLI demo videos as MP4 for feature demos.

## Method
1. Choose a real command-line workflow and script its meaningful states: setup, command, observable result and cleanup. Use synthetic inputs without credentials.
2. Run the workflow successfully before recording. Fix terminal dimensions, font legibility, prompt noise and timing so viewers can follow the result.
3. Capture actual execution using an available authorised recorder; never fabricate command output. Keep captions distinguishable from terminal results.
4. Encode a playable deliverable and inspect duration, readable text, dropped frames and audio if present. A generated recording file is not proof of playback quality.
5. Preserve the source recording and describe any cuts. Do not expose home paths, tokens or unrelated session output.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
