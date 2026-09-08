---
name: "motion-notation-prompting"
description: "Use Laban effort notation in video prompts for smoother, more expressive movement."
license: "MIT"
---
# Motion Notation Prompting

## Use when
- Generated movement looks robotic, floaty or emotionally flat
- Fight/dance/performance scenes need choreography-grade direction
- A shot's motion quality matters more than its composition

## Instructions

1. Add a small Laban-effort section to the prompt describing movement
   QUALITY along the effort factors: space (direct/indirect), weight
   (strong/light), time (sudden/sustained), flow (bound/free). Example:
   "movement quality: sustained, light, indirect — flowing tai chi transitions".
2. Match effort vocabulary to character intent: combat = strong/bound/direct;
   grief = light/sustained/indirect; panic = sudden/bound.
3. Keep the section SMALL (one to two sentences) — it modulates existing
   action description rather than replacing it. Community testing (aimikoda,
   2026) reports smoother, more expressive results; treat as promising
   practice pending wider reproduction.

## Stop conditions
- Never let notation jargon replace concrete action description.
- Never stack conflicting efforts in one shot.

## Escalation
- If Laban modulation shows no effect on a given backend after controlled
  tries, record it in the divergence notes and skip for that model.
