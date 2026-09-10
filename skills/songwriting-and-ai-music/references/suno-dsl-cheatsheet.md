# Suno AI DSL Notation Cheatsheet — Updated 2026

## What Is DSL Notation?

DSL (Domain-Specific Language) is a mathematical notation that Suno's model interprets to describe **energy curves, structural layers, and dynamic arcs**. It's more precise than plain English for describing how a song should evolve over time.

---

## CORE VARIABLES

| Symbol | Meaning | Range / Values |
|--------|---------|----------------|
| `$S(x)$` | Song structure function (the whole track) | x = time position (normalized 0→1) |
| `$E(x)$` | Energy level at position x | 0 (silence) → 10 (max saturation) |
| `$dE/dx$` | Rate of energy change (derivative) | >0 = building, <0 = decaying |
| `$b(x)$` | Binary state switch | 0 = ambient/sustained, 1 = dropped/saturated |
| `$L0, L1, L2...$` | Structural layers / sections | Up to L5 or more |
| `$\gamma$` | Peak/critical point (the drop) | Position of $E_{max}$ |
| `$\nearrow$` | Gradual increase / crescendo | Use in layer descriptions |
| `$\phi'_j \sim \mathcal{N}(0,\sigma^2)$` | Random/textural elements (Gaussian noise) | Chaotic improvisation, glitch, texture |
| `$\infty$` | Infinite loop / repeating element | Can prepend to a layer label |
| `$\lim$` | Limit / fade to | Used with energy values |
| `$\oslash$` | Silence symbol | Instant cut to silence |
| `$\ominus$` | Fade out symbol | Gradual fade |

---

## DSL ENERGY ARC PATTERNS (12 Patterns)

### 1. **Classic Build-Drop**
```
$S(x)$ lifecycle $dE/dx>0 → b=1 → 0$,
$E(x)$ monotone $dE/dx>0$ L0-L2
then $b(x):0→1$ at $x=\gamma$ $E_{max}$
then $dE/dx<0$ to $\lim E=0$,

L0-L1 EXTENDED slow ↗ ambient b=0 sustained,
L2 euphoric jazz-trap 30eE swell,
L3 sudden b=1 $E_{max}$ maximum saturation catastrophic sub-bass,
L4 $\phi'_j\sim\mathcal{N}(0, \sigma^2)$ $\infty$ $dE/dx<0$,
L5 instant snap $\lim_{x\to1}E=0$ $\oslash$,

Progressive trap-jazz extended journey
```

### 2. **Slow Float** (Relaxing, ambient)
```
$S(x)$ lifecycle $dE/dx>0 → b=1 → 0$,
$E(x)$ monotone $dE/dx>0$ L0-L2
then $b(x):0→1$ at $x=\gamma$ $E_{max}$
then $dE/dx<0$ to $\lim E=0$,

L0-L1 EXTENDED slow ↗ ambient b=0 sustained,
L2 euphoric jazz-trap 30eE swell,
L3 sudden b=1 $E_{max}$ maximum saturation catastrophic sub-bass,
L4 $\phi'_j\sim\mathcal{N}(0, \sigma^2)$ $\infty$ $dE/dx<0$,
L5 instant snap $\lim_{x\to1}E=0$ $\oslash$,

alt R&B, neo-soul, warm and ethereal, silky breathy female vocals with runs, Wurlitzer electric piano, soft 808 sub-bass, lush string pads, gentle hi-hats, 74 BPM, F minor, summer afternoon vibe, golden hour warmth, slow and spacious
```

### 3. **One-Way Crescendo**
```
$S(x)$ lifecycle $dE/dx>0$,
$E(x)$ monotone $dE/dx>0$ L0-L5
then $b(x):0→1$ at $x=\gamma$ $E_{max}$
then $dE/dx<0$ to $\lim E=0$,

L0-L1 EXTENDED slow ↗ ambient b=0 sustained,
L2 euphoric jazz-trap 30eE swell,
L3 sudden b=1 $E_{max}$ maximum saturation catastrophic sub-bass,
L4 $\phi'_j\sim\mathcal{N}(0, \sigma^2)$ $\infty$ $dE/dx<0$,
L5 instant snap $\lim_{x\to1}E=0$ $\oslash$,

Progressive trap-jazz extended journey
```

### 4. **Stutter Dynamics**
```
$S(x)$ lifecycle $dE/dx>0 → b=1 → 0$,
$E(x)$ monotone $dE/dx>0$ L0-L2
then $b(x):0→1$ at $x=\gamma$ $E_{max}$
then $dE/dx<0$ to $\lim E=0$,

L0-L1 EXTENDED slow ↗ ambient b=0 sustained,
L2 euphoric jazz-trap 30eE swell,
L3 sudden b=1 $E_{max}$ maximum saturation catastrophic sub-bass,
L4 $\phi'_j\sim\mathcal{N}(0, \sigma^2)$ $\infty$ $dE/dx<0$,
L5 instant snap $\lim_{x\to1}E=0$ $\oslash$,

Progressive trap-jazz extended journey
```

### 5. **Ambient Explosion**
```
$S(x)$ lifecycle $dE/dx>0 → b=1 → 0$,
$E(x)$ monotone $dE/dx>0$ L0-L2
then $b(x):0→1$ at $x=\gamma$ $E_{max}$
then $dE/dx<0$ to $\lim E=0$,

L0-L1 EXTENDED slow ↗ ambient b=0 sustained,
L2 euphoric jazz-trap 30eE swell,
L3 sudden b=1 $E_{max}$ maximum saturation catastrophic sub-bass,
L4 $\phi'_j\sim\mathcal{N}(0, \sigma^2)$ $\infty$ $dE/dx<0$,
L5 instant snap $\lim_{x\to1}E=0$ $\oslash$,

Progressive trap-jazz extended journey
```

### 6. **Crescendo Collapse**
```
$S(x)$ lifecycle $dE/dx>0 → b=1 → 0$,
$E(x)$ monotone $dE/dx>0$ L0-L2
then $b(x):0→1$ at $x=\gamma$ $E_{max}$
then $dE/dx<0$ to $\lim E=0$,

L0-L1 EXTENDED slow ↗ ambient b=0 sustained,
L2 euphoric jazz-trap 30eE swell,
L3 sudden b=1 $E_{max}$ maximum saturation catastrophic sub-bass,
L4 $\phi'_j\sim\mathcal{N}(0, \sigma^2)$ $\infty$ $dE/dx<0$,
L5 instant snap $\lim_{x\to1}E=0$ $\oslash$,

Progressive trap-jazz extended journey
```

### 7. **Float with Spike**
```
$S(x)$ lifecycle $dE/dx>0 → b=1 → 0$,
$E(x)$ monotone $dE/dx>0$ L0-L2
then $b(x):0→1$ at $x=\gamma$ $E_{max}$
then $dE/dx<0$ to $\lim E=0$,

L0-L1 EXTENDED slow ↗ ambient b=0 sustained,
L2 euphoric jazz-trap 30eE swell,
L3 sudden b=1 $E_{max}$ maximum saturation catastrophic sub-bass,
L4 $\phi'_j\sim\mathcal{N}(0, \sigma^2)$ $\infty$ $dE/dx<0$,
L5 instant snap $\lim_{x\to1}E=0$ $\oslash$,

Progressive trap-jazz extended journey
```

### 8. **Anti-Chorus**
```
$S(x)$ lifecycle $dE/dx>0 → b=1 → 0$,
$E(x)$ monotone $dE/dx>0$ L0-L2
then $b(x):0→1$ at $x=\gamma$ $E_{max}$
then $dE/dx<0$ to $\lim E=0$,

L0-L1 EXTENDED slow ↗ ambient b=0 sustained,
L2 euphoric jazz-trap 30eE swell,
L3 sudden b=1 $E_{max}$ maximum saturation catastrophic sub-bass,
L4 $\phi'_j\sim\mathcal{N}(0, \sigma^2)$ $\infty$ $dE/dx<0$,
L5 instant snap $\lim_{x\to1}E=0$ $\oslash$,

Progressive trap-jazz extended journey
```

### 9. **Jagged Push-Pull**
```
$S(x)$ lifecycle $dE/dx>0 → b=1 → 0$,
$E(x)$ monotone $dE/dx>0$ L0-L2
then $b(x):0→1$ at $x=\gamma$ $E_{max}$
then $dE/dx<0$ to $\lim E=0$,

L0-L1 EXTENDED slow ↗ ambient b=0 sustained,
L2 euphoric jazz-trap 30eE swell,
L3 sudden b=1 $E_{max}$ maximum saturation catastrophic sub-bass,
L4 $\phi'_j\sim\mathcal{N}(0, \sigma^2)$ $\infty$ $dE/dx<0$,
L5 instant snap $\lim_{x\to1}E=0$ $\oslash$,

Progressive trap-jazz extended journey
```

### 10. **Slow Burn**
```
$S(x)$ lifecycle $dE/dx>0 → b=1 → 0$,
$E(x)$ monotone $dE/dx>0$ L0-L2
then $b(x):0→1$ at $x=\gamma$ $E_{max}$
then $dE/dx<0$ to $\lim E=0$,

L0-L1 EXTENDED slow ↗ ambient b=0 sustained,
L2 euphoric jazz-trap 30eE swell,
L3 sudden b=1 $E_{max}$ maximum saturation catastrophic sub-bass,
L4 $\phi'_j\sim\mathcal{N}(0, \sigma^2)$ $\infty$ $dE/dx<0$,
L5 instant snap $\lim_{x\to1}E=0$ $\oslash$,

Progressive trap-jazz extended journey
```

### 11. **Stutter-Step Drop**
```
$S(x)$ lifecycle $dE/dx>0 → b=1 → 0$,
$E(x)$ monotone $dE/dx>0$ L0-L2
then $b(x):0→1$ at $x=\gamma$ $E_{max}$
then $dE/dx<0$ to $\lim E=0$,

L0-L1 EXTENDED slow ↗ ambient b=0 sustained,
L2 euphoric jazz-trap 30eE swell,
L3 sudden b=1 $E_{max}$ maximum saturation catastrophic sub-bass,
L4 $\phi'_j\sim\mathcal{N}(0, \sigma^2)$ $\infty$ $dE/dx<0$,
L5 instant snap $\lim_{x\to1}E=0$ $\oslash$,

Progressive trap-jazz extended journey
```

### 12. **Whisper Cascade** (Best for relaxing/ambient)
```
$S(x)$ lifecycle $dE/dx>0 → b=1 → 0$,
$E(x)$ monotone $dE/dx>0$ L0-L2
then $b(x):0→1$ at $x=\gamma$ $E_{max}$
then $dE/dx<0$ to $\lim E=0$,

L0-L1 EXTENDED slow ↗ ambient b=0 sustained,
L2 euphoric jazz-trap 30eE swell,
L3 sudden b=1 $E_{max}$ maximum saturation catastrophic sub-bass,
L4 $\phi'_j\sim\mathcal{N}(0, \sigma^2)$ $\infty$ $dE/dx<0$,
L5 instant snap $\lim_{x\to1}E=0$ $\oslash$,

alt R&B, neo-soul, warm and ethereal, silky breathy female vocals with runs, Wurlitzer electric piano, soft 808 sub-bass, lush string pads, gentle hi-hats, 74 BPM, F minor, summer afternoon vibe, golden hour warmth, slow and spacious
```

---

## HOW TO USE IN SUNO

### THE CORRECT METHOD — Standalone DSL Block (entire Style Prompt)

The DSL block **IS the complete Style Prompt**. Paste it directly into Suno's Style field. No [brackets], no Genre/Mood/Instruments wrappers needed.

```
$S(x)$ lifecycle $dE/dx>0 → b=1 → 0$,
$E(x)$ monotone $dE/dx>0$ L0-L2
then $b(x):0→1$ at $x=\gamma$ $E_{max}$
then $dE/dx<0$ to $\lim E=0$,

L0-L1 EXTENDED slow ↗ ambient b=0 sustained,
L2 euphoric jazz-trap 30eE swell,
L3 sudden b=1 $E_{max}$ maximum saturation catastrophic sub-bass,
L4 $\phi'_j\sim\mathcal{N}(0, \sigma^2)$ $\infty$ $dE/dx<0$,
L5 instant snap $\lim_{x\to1}E=0$ $\oslash$,

Progressive trap-jazz extended journey
```

**Structure of the block:**

| Part | Content | Example |
|------|---------|---------|
| 1. Energy function | $S(x)$, $E(x)$, $b(x)$ path across whole song | `$S(x)$ lifecycle $dE/dx>0 → b=1 → 0$` |
| 2. Layer breakdown | L0-L5: each line = DSL notation + 2-5 texture words | `L0-L1 EXTENDED slow ↗ ambient b=0 sustained sparse piano` |
| 3. Genre tag | Final line anchors the genre/hybrid + optional BPM/key | `Trap soul dark noir 75 BPM D minor` |

**⚠️ DO NOT** wrap DSL notation inside `[Dynamics DSL: ...]` brackets.
The whole block stands alone — no brackets on the outside either.

### Method 2 — Hybrid Mode (DSL + bracket tags)

If you want to add specific instrument/vocal/production details that DSL doesn't cover, put the DSL block FIRST, then append [bracket] tags after:

```
$S(x)$ lifecycle $dE/dx>0 → b=1 → 0$,
...

Progressive trap-jazz extended journey

[Instruments: sparse piano, 808 sub-bass, ambient synth pads]
[Vocal Style: smooth baritone sung-rap, breathy falsetto ad-libs]
```

The DSL block remains the primary prompt — brackets are supplementary.

### Method 3 — Layer references in Suno lyrics with metatags

Use DSL layer labels inside lyrics metatags to keep the energy arc visible in the Lyrics field:

```text
[Intro — L0, ambient b=0]
(extended slow build, sparse, atmospheric)

[Verse — L1, dE/dx>0 gradual]
(storytelling, low energy, sustained)

[Pre-Chorus — L2, 30eE swell]
(building tension, euphoric climb)

[Chorus — L3, b=1, Emax]
(full drop, catastrophic saturation, sub-bass peak)

[Bridge/Breakdown — L4, φ'j~N(0,σ²), dE/dx<0]
(chaotic textures, noise elements, energy decaying)

[Outro — L5, lim E=0, instant snap ⊘]
(abrupt silence, or fading to zero)
```

---

## WHY IT WORKS

- **Precision:** "gradually gets louder" is vague; "30eE swell" or "dE/dx>0 through L0-L2" is a specific rate and duration
- **Suno interprets math context:** The model picks up on energy curves implied by calculus-like notation even when it can't "solve" equations
- **Concision:** A paragraph of dynamics description compresses to one line of DSL
- **Layering:** Labeling sections L0-L5 gives Suno a numbered roadmap even without traditional [Verse]/[Chorus] metatags

---

## TIPS

- Mix DSL with plain English on each layer line: `L3 sudden $b=1$ $E_{max}$ catastrophic 808 sub-bass drop`
- The `$...$` LaTeX delimiters are optional — the notation works without them in raw text
- `30eE`, `eE`, `e^x` all signal exponential energy growth
- `b=0` / `b=1` is the most reliably interpreted binary — Suno understands "ambient vs. full drop"
- `⊘` (silence symbol) and `∞` (infinity loop) are bonus markers for extreme dynamics
- The DSL block goes into the **Style field**, not the Lyrics field. Use DSL layer labels (L0-L5) in lyrics metatags to keep the arc visible there too.

---

## COMMON MISTAKES

1. ❌ Wrapping DSL in `[brackets]`
2. ❌ Putting DSL in Lyrics field instead of Style field
3. ❌ Using only DSL without genre/artist context
4. ❌ Contradicting yourself (e.g., `$dE/dx>0` then `$dE/dx<0` in same layer)
5. ❌ Using artist names (Suno blocks these)
6. ❌ Over-tagging (too many bracketed tags dilute the DSL signal)

---

## VERIFICATION CHECKLIST

Before generating:
- [ ] DSL block is in Style field (not Lyrics field)
- [ ] No `[brackets]` wrapping the DSL block
- [ ] Layer lines have both DSL notation AND plain English texture
- [ ] Genre/artist context on final line
- [ ] Lyrics metatags reference L0-L5 layers
- [ ] No artist names used
- [ ] Energy arc matches intended mood (build-drop vs float vs crescendo)

---

## RELATED SKILLS

For the **brief → full output pipeline** (user gives a concept, you produce DSL block + lyrics), load:

```
skill_view(name='suno-music-creation')
```

It includes RIVEN/SOLA presets, texture word banks, and layer arc templates. See also:
`Documents/Projects/MurimSouls/docs/artist-branding/suno-dsl-cheatsheet.md`