---
name: eikon-create
description: "Interactively generate source images (and optionally short videos) for a herm eikon avatar, iterate on them with the user, and land them under ~/.hermes/eikons/<name>/source/ so the Eikon Studio tab can tune and bake them. This is the agent-driven counterpart to Studio's one-shot Generate dialog."
version: 1.0.0
license: MIT
---
# /eikon-create — generate eikon source files interactively

You are producing **source files**, not the packed `.eikon`. Studio owns
crop, tone (contrast/invert/flip), rasterizer choice, and baking. Your
deliverable is one or more images/videos under

    ~/.hermes/eikons/<name>/source/

named so Studio resolves them: `base.*` for the default pose, `<state>.*`
for per-state overrides (`idle listening thinking speaking working
error`). Extensions: `png jpg jpeg webp gif bmp mp4 webm mov mkv`.

## What survives rasterization

Output is 48×24, one theme color, braille/block glyphs. The one-line
brief (say once, don't repeat):

> 48×24, one color. Best results: light subject on black background,
> high contrast, strong silhouette.

Outline carries everything — facial detail, fine texture, and tonal
gradients mostly vanish.

## What Studio fixes for you (don't regenerate for these)

Studio adjusts these live on any source without a new generation:

- **Aspect / framing** — Studio crops to a square window; zoom + pan
  pick which square. A 16:9 or portrait source is fine.
- **Contrast** — slider, mean-centered. Flat or over-bright sources
  are usually salvageable.
- **Invert** — light↔dark swap. A dark-subject-on-light source works
  with invert off.
- **Flip** — horizontal/vertical mirror.

So: regenerate for **subject, pose, silhouette, background clutter**.
Don't regenerate for **crop, exposure, polarity, orientation**.

## Flow

### 0. Name

If the user passed an argument (`/eikon-create <name>`), slug it
(lowercase, `[^a-z0-9-]` → `-`, collapse runs, trim). Otherwise ask
once. Make the folder immediately so Studio's Open picker lists it:

```bash
n="<slug>"; mkdir -p "${HERMES_HOME:-$HOME/.hermes}/eikons/$n/source"
```

### 1. Subject

Ask what the eikon is. One line is enough. If they drop an image
instead of describing one, skip to §3 adopt-only.

### 2. Generate base

Call `image_generate` with the subject on line 1 and the fixed suffix
on line 2 — same suffix Studio seeds:

```
<subject>, close-up portrait emphasizing the face/head, looking slightly left, stark black and white, bold silhouette, simple uncluttered shape
high contrast, light subject on dark, black background
```

Keep this general: replace `face/head` with the subject's most readable
feature if it is not a character or creature. Prefer square if the tool
takes `aspect_ratio`; if it doesn't, don't worry — Studio crops. Show
the result inline with `![base](https://example.invalid/placeholder)`
and a 48-wide terminal preview:

```bash
chafa --size=48x24 --symbols=braille --colors=none --format=symbols --stretch "<path>" 2>/dev/null || true
```

Ask: **keep, regenerate, or adjust?** On adjust, fold their note into
the subject line (leave the suffix alone). Loop. **Always overwrite the
same `<state>.<ext>` in `source/` on every iteration** — Studio reads
that path live, so a new candidate that lives only in cache is invisible
to the user. If two rounds fail on background clutter, silently append
`, isolated on pure black, no floor, no environment` and try again.

### 3. Adopt

```bash
src="<path-or-downloaded-tmp>"
dst="${HERMES_HOME:-$HOME/.hermes}/eikons/$n/source/base.${src##*.}"
cp "$src" "$dst" && ls -l "$dst"
```

URL return → `curl -fsSL -o /tmp/<n>-base.png "<url>"` first. Ambiguous
extension → `.png`.

### 4. Per-state sources (optional)

Base covers all six states by default. If the user wants distinct
ones, repeat §2–3 per state, saving as `<state>.<ext>`. Nudge the
subject line with pose intent:

| state | pose nudge |
|---|---|
| listening | head turned slightly toward viewer |
| thinking | head tilted back, contemplative |
| speaking | mouth open mid-word |
| working | head bowed forward |
| error | recoiling, startled |

### 5. Video (optional, only if asked)

Use `video_generate` if available. What matters for an eikon source:

- **Duration** — 2–4 s is the useful range. Longer just inflates the
  bake. If the provider picks duration itself, accept whatever lands.
- **Aspect** — prefer 1:1 if the provider exposes it; otherwise any,
  Studio crops.
- **Resolution** — low is fine; the target is 48×24. Don't ask for
  HD if the provider lets you pick.
- **Start/end frame** — if the provider accepts a start (and/or end)
  image, pass `base.*` so the clip anchors on the still pose and
  loops cleanly. If it only takes text, that's fine — Studio plays
  whatever frames it gets.
- **Loop** — nice-to-have, not required. If the provider has a loop
  or seamless flag, set it; if not, don't chase it with prompting.

Providers vary in which of these knobs exist. **Pass what the tool
accepts, skip what it doesn't, and don't apologize for the gaps.**
None of them block a usable eikon.

Adopt as `<state>.mp4` (or `base.mp4` for an animated idle).

### 6. Hand off

Once source files are in place:

> Open the **Eikon** tab → `eikon` row → **<name>**. Tune zoom /
> contrast / invert / symbols there, then **Ctrl+S** to bake.

Stop there. Studio writes `<name>.eikon` and `studio.json`.

## Don'ts

- Don't write `.eikon` or `studio.json`.
- Don't pick contrast, invert, zoom, or rasterizer values — name the
  knob, the user turns it in Studio.
- Don't regenerate for things Studio can fix (see table above).
- Don't enumerate provider capabilities to the user; just use what's
  there.
- Don't repeat the 48×24 brief.
