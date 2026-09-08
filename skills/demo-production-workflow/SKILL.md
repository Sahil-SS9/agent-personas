---
name: "demo-production-workflow"
description: "Produce demos end to end — browser automation, screen recording, editing, walkthroughs, delivery."
license: "MIT"
---
# Demo Production Workflow

## Use when
- Creating recorded or interactive product demos at any scale
- Turning a screen recording into a polished walkthrough
- Deciding between live, recorded and interactive demo formats

## Instructions

1. FORMAT SELECTION by funnel stage: recorded video for awareness/comparison,
   interactive clickable demos for bottom-of-funnel evaluation, live sessions
   for enterprise deals (they answer questions; they do not scale). Mix all
   three deliberately.
2. CAPTURE via browser/desktop:
   - Drive the real product in a seeded environment (never live customer
     data); use browser automation for repeatable paths where useful, but
     record the human-paced take — automation pacing reads as fake.
   - Record at 1080p minimum; capture clean audio separately (bad audio
     kills credibility faster than bad video); keep takes short and re-record
     flubs rather than editing around them.
3. EDIT for legibility, not polish: zoom/callouts direct attention to the UI
   region that matters; captions on by default (most viewers are on mute);
   trim dead air aggressively; target length 30-60s awareness / 2-3min
   consideration; one workflow demonstrated deeply beats five features
   skimmed.
4. WALKTHROUGH creation: step-by-step guided variants (interactive
   walkthrough tools) share a script with the video — one source of truth;
   steps must survive UI changes or carry a dated screenshot refresh plan.
5. DELIVERY + measurement: single specific call-to-action per demo ("try the
   free 14-day", never "learn more"); engagement-tracked players where
   possible; A/B test one variable at a time; refresh cadence tied to UI
   release notes.

## Stop conditions
- Never publish a demo showing unreleased functionality without a roadmap
  label.
- Never ship audio below broadcast-reasonable quality.

## Escalation
- Product claims that cannot be demoed safely route to the QFS authoring
  skill as gaps, not improvised workarounds.
