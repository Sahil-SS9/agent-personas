---
name: content-and-asset-pipeline
description: "Create new mod content and assets that match the game, using the end user's chosen local or paid tools."
version: 0.1.0
author: Hermes
license: MIT
---

# Content and asset pipeline

New items, weapons, enemies, units, levels, sound and music: make them fit the game, and make them the user's way.

## 1. Respect the user's asset preference (ask once, record it)
Ask before generating anything and record the answer in MODLOG.md:
- **Local only:** e.g. ComfyUI or other local image/3D/audio models, Blender, hand-made art. No network spend.
- **Paid services allowed:** e.g. hosted image, 3D, sound or video generation. Ask for the provider, the key's location (environment variable or keyring, never in the repo) and a spending limit, and whether each job needs approval.
- **Both:** local first, paid only for what local cannot do, under the same limits.
Never spend money or upload the user's files to a service without that recorded consent. If no preference is set, use placeholders and ask.

## 2. Study the game's own assets first
Measure before generating: resolution, pixel scale, palette, outline style, camera angle, facing directions, frame layout, polygon budget, texture format and naming. Content that ignores these looks wrong however good the art is.

## 3. Content design before art
Define the content in the game's terms: stats, tier, recipes, drop tables, AI behaviour, sounds and balance relative to existing content. Clone and modify an existing entity where the engine allows; it inherits animations and behaviour that are hard to author.

## 4. Generate or author
- Consistency across many angles or frames: make one concept, turn it into a 3D model, then render every required angle from the game's camera.
- Pixel art: generate on a flat or transparent background, cut out, then scale once with nearest-neighbour to the exact frame size.
- Sound: match sample rate, loudness and length to the game's existing effects.
- Record every generated asset (tool or model, prompt, seed, date, licence terms) in a manifest beside the mod.

## 5. Convert to what the engine loads
Examples: PNG into tModLoader; AssetBundles for Unity built with the same Unity major version; cooked `.uasset` in a matching Unreal editor; NIF/DDS for Bethesda; 16x16 PNG and JSON models for Minecraft. Check format, size and naming with a load test.

## 6. Other games' assets
Never copy assets from another game into a mod. For cross-game content, either recreate a look-alike, or ship a converter that runs on the user's own install and writes a private local pack. The mod must still work with placeholders when that pack is missing.

## 7. Proof
The asset appears in game at the right scale, facing, pivot and layer in a scripted scene screenshot that was actually inspected, plus a manifest entry for every generated file and a licence check for commercial use.
