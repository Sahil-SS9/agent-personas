---
name: eikon
description: "Guide the user through making or editing a herm sidebar avatar (eikon) using herm's built-in Eikon Studio tab. The agent's role is advisory (what makes a good source, which knob to reach for); source generation is /eikon-create and all rasterize/bake happens in-app."
version: 1.0.0
license: MIT
---
# Building an eikon in herm

An eikon is a 48×24 monochrome text avatar. It lives on disk as:

    ~/.hermes/eikons/<name>/
      <name>.eikon      packed NDJSON — written by Studio on Ctrl+S
      studio.json       Studio's workspace state
      source/           base.<ext>, <state>.<ext>

You do **not** write `.eikon` or `studio.json`. Studio does.

## Where the user does the work

Herm's built-in **Eikon** tab (Studio / Gallery). Tell the user: "open
the Eikon tab" or "Ctrl+K → Eikon". In Studio:

- `eikon` row → pick / New…
- `source` row → Local file… / Generate image… / Generate video…
- `input` section → contrast / invert / flip (pixel-domain, shared)
- `<rasterizer>` section → symbols / fill / dither (glyph-domain)
- Preview pane → wheel pans, Ctrl+wheel zooms, Shift+wheel pans X
- **Ctrl+S** bakes all six states and sets it active

## What makes a good source

One line, once: **48×24, one color. Light subject on black, high
contrast, strong silhouette.** Fine detail disappears; outline is
everything.

## When to do what

| user says | you do |
|---|---|
| "make me an eikon of X" | Load `eikon-create` and follow it. |
| drops an image path | `cp` it to `~/.hermes/eikons/<name>/source/base.<ext>` → "Eikon tab, pick <name>". |
| "edit my <name> eikon" | "Eikon tab → `eikon` row → <name>." |
| "too dark / washed out" | "invert toggle, then contrast slider — under `input`." |
| "off-center / too small" | "Ctrl+wheel to zoom, wheel/drag to pan on the preview." |
| "make it move" | `eikon-create` §5 (video), or Studio's `source` → Generate video…. |

## Quick poster

To show a candidate in chat without Studio:

```bash
chafa --size=48x24 --symbols=braille --colors=none --format=symbols --stretch "<path>"
```

Preview-only; Studio's output will differ (it tone-maps first).

## Don'ts

- Don't hand-write `.eikon` NDJSON.
- Don't pick knob values for the user. Name the knob.
- Don't repeat the 48×24 brief.
