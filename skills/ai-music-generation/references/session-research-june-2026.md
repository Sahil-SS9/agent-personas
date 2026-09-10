# AI Music Generation — Session Research (June 2026)

## Sources Consulted
- **Suno Explore**: suno.com/explore — Staff Picks, Best of v5.5, community engagement metrics
- **Suno Terms of Service**: suno.com/terms — Revised March 26, 2026
- **Suno Help Article #2410177**: "Can I distribute my songs to Spotify, etc?" — confirms commercial rights for Pro/Premier
- **ACE-Step 1.5**: github.com/ace-step/ACE-Step-1.5 — 11.3k ⭐, MIT, actively maintained
- **YuEGP**: github.com/deepbeepmeep/YuEGP — CC BY-NC, 7B+1B architecture
- **AudioCraft/MusicGen**: github.com/facebookresearch/audiocraft — MIT, stale

## Suno Commercial Rights (from help.suno.com)

Full text snippet:
> "Songs made while subscribed (to a Pro or Premier plan) are granted commercial use rights. This allows you to distribute songs to Spotify, Apple Music, etc, using the distributor of your choice. This also allows you to use the songs in content you post to YouTube, TikTok, etc. You do not have to attribute the songs to Suno."
> 
> "Songs made on the free plan (not subscribed) are only available for non-commercial use and cannot be monetized. These do not include the commercial use license, and starting a subscription after you made a great song will not give you a retroactive license for the song."
>
> "Pro Tip: As with any time you monetize your songs, you must be the exclusive rights holder of 100% of the material. Don't try to monetize a song if you're using someone else's lyrics!"

## ACE-Step 1.5 — Model Zoo Detail

### DiT Models (2B)
| Model | Pre-Train | SFT | RL | Steps | Quality | Fine-Tunability |
|---|---|---|---|---|---|---|
| acestep-v15-base | ✅ | ❌ | ❌ | 50 | Medium | Easy |
| acestep-v15-sft | ✅ | ✅ | ❌ | 50 | High | Easy |
| acestep-v15-turbo | ✅ | ✅ | ❌ | 8 | Very High | Medium |

### DiT Models (4B XL)
| Model | Pre-Train | SFT | RL | Steps | VRAM |
|---|---|---|---|---|---|
| acestep-v15-xl-base | ✅ | ❌ | ❌ | 50 | ~9GB bf16 |
| acestep-v15-xl-sft | ✅ | ✅ | ❌ | 50 | ~9GB bf16 |
| acestep-v15-xl-turbo | ✅ | ✅ | ❌ | 8 | ~9GB bf16 |

Total with LM + XL DiT: ~20GB+ (bf16), ~12GB+ (with offload + quantization)

### LM Models (based on Qwen3)
| Model | Params | Capability |
|---|---|---|
| acestep-5Hz-lm-0.6B | 0.6B | Medium |
| acestep-5Hz-lm-1.7B | 1.7B | Medium |
| acestep-5Hz-lm-4B | 4B | Strong (composition, melody) |

## YuE Detail
- **GitHub**: deepbeepmeep/YuEGP (GPU Poor fork)
- **Stage 1**: YuE-s1-7B-anneal-{en/jp-kr/zh}-{cot/icl} — 7B params
- **Stage 2**: YuE-s2-1B-general — 1B params
- **Upsampler**: YuE-upsampler
- **VRAM profiles**: Profile 1 (fast, 16GB), Profile 3 (8-bit quant, 12GB), Profile 4 (<10GB, sequential offloading), Profile 5 (minimum VRAM)
- **Speed**: ~4 min for 30s on RTX 4090 (Profile 1 + turbo-stage2)
- **Key requirement**: Flash Attention 2 recommended, transformers patch doubles speed
- **Windows**: patchtransformers.bat available, triton-windows wheels available
- **License**: CC BY-NC 4.0

## System Specs (User from Memory)
- Windows 10, git-bash shell
- CUDA GPU(s) with sufficient VRAM for 35B MoE models (16-24GB+ range)
- llama.cpp with llama-server already in use
- Hermes profile: xay
