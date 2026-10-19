---
name: mashup-and-cross-game-bridges
description: "Design cross-game mashups: choose the route, write the bridge contract and build the smallest proven slice."
version: 0.1.0
author: Hermes
license: MIT
---

# Mashup and cross-game bridges

"Minecraft in Skyrim" clips look alike but hide very different builds. Mashups fail by drifting, not by lacking code: choose the route deliberately and prove each step.

## 1. Ask what the user wants from the guest game
Its real behaviour (physics, inventory, combat), or only its look or one mechanic? This decides whether the guest must run at all.

## 2. Choose the lightest route
| Route | What runs | Every player needs |
|---|---|---|
| Content port | host only; guest behaviour re-created as host content | the host |
| Asset or map conversion | host only; converted offline from the user's files | the host plus their own copy of the guest |
| Rebuilt guest rules inside the host | real host plus a re-implemented guest mechanic or simulation | the host (plus guest data if used) |
| Live passthrough (state exchange) | both real games, swapping positions, collision, hits | both games and both loaders |
| Frame compositing | both games; guest picture drawn into the host frame | both games |
| Native geometry transfer | both games; host draws guest meshes in its own pass | both games |
| Engine recreation | one rebuilt engine reading the user's own files | the original's files |
Most shipped mashups combine compositing with state exchange. Find the nearest prior project (the awesome-game-mashups catalogue is a good index) and treat its README as a creator report until you run it.

## 3. Write the bridge contract before code (`docs/CONTRACT.md`)
- Who owns the player and how control is handed back (a hotkey, menus, cutscenes).
- Units and axes, with one mapping function both sides share (e.g. 1 metre = 1 block; axis flips; yaw conventions).
- Each channel: content, rate, and what happens when it is full, late or the other side dies.
- Transport on 127.0.0.1 only: shared-memory ring buffer, UDP or named pipes for state; JSON lines or HTTP for control; shared GPU handles or CPU readback for frames.
- Protocol version and byte order; startup and shutdown order; a watchdog.

## 4. Build in this order
1. One cube from process A drawn in B at the right place.
2. Positions every frame, with timestamps and frame-rate tolerance.
3. Collision back-channel (host geometry near the player sent to the guest as solids).
4. Combat and events, mapped per direction (guest hit becomes host damage and vice versa).
5. Only then real content, menus and polish.
Build against a fake host or fake guest with known geometry first; then the real games.

## 5. Guardrails
- Offline or user-run servers only; a hooked online-capable game stays offline for the whole session and never runs with its anti-cheat on.
- Everything guest-side comes from the user's own install; publish code and converters, never assets.
- Say plainly what was AI-assisted and what was verified in a real run versus read in a README.

## 6. Proof
A measurement scene that shows latency and alignment (something drawn by one side only), the contract file, and a real-run clip naming game builds, OS and GPU.
