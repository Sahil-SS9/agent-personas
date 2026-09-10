# DSL Character Count Pitfall — Worked Example

Suno's Style field has a **hard 1,000 character limit** for the DSL block.

## Why this catches you

The DSL format is verbose by design — layer descriptions, notation, texture words, and the genre tag line all add up fast. A complex song with 6+ layers, especially with a one-way crescendo arc spanning a full journey (intimate→hype), can easily exceed 1,000 chars.

## Compression strategies when over limit

If your DSL block is over:

1. **Merge adjacent layers** — L0+L1 ambient intro can share one line; pre-chorus can be absorbed into the build line
2. **Cut texture words** — each layer line only needs 2-5 descriptive words, not a full sentence
3. **Condense the genre tag line** — trim to essentials (genre, BPM, key, vocal). "Trap-soul meets hype hip hop, journey from intimate to triumphant, high BPM, hard 808s, anthemic chorus, male vocals from sung-rap to rapid-fire, 145 BPM, triumphant key, freedom and arrival" → "Trap-soul meets hype hip hop, intimate to triumphant, 145 BPM, hard 808s, anthemic chorus, male vocals sung-rap to rapid-fire, freedom and arrival"
4. **Remove redundant DSL notation** — `$b=0$` doesn't need restating on every ambient layer line when the header already says `$b=0$ V1`
5. **Drop '$...$' LaTeX delimiters** — the notation works without them in raw text, saving 3-5 chars per symbol

## Example: Before and After

**Before (1,299 chars — 299 over):**
```
$S(x)$ lifecycle one-way $dE/dx>0$ arc across full runtime,
$b=0$ through V1, $b=0\to1$ hybrid transition in V2,
$b=1$ full saturation from V3 through chorus,
$E(x)$: $E=3$ intro, $E=5$ V1, $E=7$ V2, $E=9$ V3 through finale,

L0 atmospheric intro $E=2$, distant keys, airy filtered pads, anticipation,
L1 verse 1 $E=4$ trap-soul subby 808 glide, filtered male vocal, sung-rap intimate delivery, minimal hats, underwater warmth, $b=0$,
L2 pre-chorus $dE/dx>0$ building tension, hi-hats doubling, vocal rising, brightness increasing,
L3 chorus 1 $E=7$ melodic hook, layered harmonies, room opens, 808 fuller, bass present, $b$ transitioning,
L4 verse 2 $E=6$ hybrid, trap-soul foundation with double-time rhythmic pockets, vocal more present, energy spikes, $b=0.5$,
L5 chorus 2 $E=8$ higher energy, more percussion, fuller production,
L6 verse 3 $E=9$ full hype, chest-thumping kick, rapid-fire delivery, vocal present and aggressive, $b=1$,
L7 final chorus $E_{max}=10$ cathartic release, full production, victory lap,
L8 outro $dE/dx<0$ to $\lim E=2$ satisfied exhale, distant reverb, gratitude in the quiet

Trap-soul meets hype hip hop, journey from intimate to triumphant, high BPM, hard 808s, anthemic chorus, male vocals from sung-rap to rapid-fire, 145 BPM, triumphant key, freedom and arrival
```

**After (822 chars — 178 to spare):**
```
$S(x)$ one-way $dE/dx>0$ across full runtime,
$b=0$ V1, $b(0\to1)$ transition V2, $b=1$ V3 onward,
$E(x)$ rises $E=3\to5\to7\to10$,

L0 intro $E=2$, filtered pads, distant keys, anticipation,
L1 V1 $E=4$ trap-soul, filtered sung-rap, subby 808, underwater warmth, $b=0$,
L2 pre-chorus $dE/dx>0$ build, hi-hats double, brightness rising,
L3 chorus $E=7$ melodic hook, layered harmonies, room opens, 808 fuller,
L4 V2 $E=6$ hybrid, double-time pockets, energy spikes, $b$ transitioning,
L5 V3 $E=9$ full hype, rapid-fire, chest-thumping kick, $b=1$,
L6 final chorus $E_{max}=10$ cathartic victory, full production,
L7 outro $\lim E\to2$ satisfied exhale, distant reverb, gratitude,

Trap-soul meets hype hip hop, intimate to triumphant, 145 BPM, hard 808s, anthemic chorus, male vocals sung-rap to rapid-fire, freedom and arrival
```

**Where the savings came from:**
- 9 layers → 8 (removed separate pre-chorus line, absorbed into L2)
- Texture words cut from verbose ("atmospheric intro, distant keys, airy filtered pads") to terse ("intro, filtered pads, distant keys")
- Redundant `$b=0$`/`$b=1$` per-layer removed (covered by header arc)
- Genre tag sentence condensed from 34 words to 18