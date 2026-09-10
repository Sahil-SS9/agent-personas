# Image-model acquisition reference: Krea 2, Ideogram 4, Qwen-Image-2512

Verified official sources and ComfyUI paths for the local Windows portable install.

## Official workflow templates

- Krea 2 Turbo T2I: `https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_krea2_turbo_t2i.json`
- Ideogram 4 T2I: `https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_ideogram4_t2i.json`
- Qwen-Image-2512: `https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_Image_2512.json`

Official documentation: `https://docs.comfy.org/tutorials/image/krea/krea-2`, `https://docs.comfy.org/tutorials/image/ideogram/ideogram-v4`, and `https://docs.comfy.org/tutorials/image/qwen/qwen-image-2512`.

## Exact HF manifest sizes

Repository `Comfy-Org/Krea-2`:

| File | Destination | Bytes | Approx. decimal GB |
|---|---|---:|---:|
| `diffusion_models/krea2_turbo_fp8_scaled.safetensors` | `models/diffusion_models/` | 13,141,730,784 | 13.14 |
| `text_encoders/qwen3vl_4b_fp8_scaled.safetensors` | `models/text_encoders/` | 5,242,467,968 | 5.24 |
| `vae/qwen_image_vae.safetensors` | `models/vae/` | 253,806,246 | 0.254 |

Optional Krea style LoRAs are in `loras/`, each approximately 469,291,992 bytes; style-reference LoRA is approximately 457,111,760 bytes.

Repository `Comfy-Org/Ideogram-4`:

| File | Destination | Bytes | Approx. decimal GB |
|---|---|---:|---:|
| `diffusion_models/ideogram4_int8_convrot.safetensors` | `models/diffusion_models/` | 9,583,465,712 | 9.58 |
| `diffusion_models/ideogram4_unconditional_int8_convrot.safetensors` | `models/diffusion_models/` | 9,583,465,712 | 9.58 |
| `diffusion_models/ideogram4_nvfp4_mixed.safetensors` | `models/diffusion_models/` | 5,490,550,037 | 5.49 |
| `diffusion_models/ideogram4_unconditional_nvfp4_mixed.safetensors` | `models/diffusion_models/` | 5,490,550,037 | 5.49 |
| `text_encoders/qwen3vl_8b_fp8_scaled.safetensors` | `models/text_encoders/` | 10,588,637,512 | 10.59 |
| `text_encoders/qwen3vl_8b_nvfp4.safetensors` | `models/text_encoders/` | 6,305,221,764 | 6.31 |
| `vae/flux2-vae.safetensors` | `models/vae/` | 336,211,292 | 0.336 |

The supplied workflow expects the INT8 pair plus Qwen3-VL 8B FP8 and `flux2-vae`; do not silently substitute NVFP4 files without the matching official workflow or node changes.

Repository `Comfy-Org/Qwen-Image_ComfyUI`:

| File | Destination | Bytes | Approx. decimal GB |
|---|---|---:|---:|
| `split_files/diffusion_models/qwen_image_2512_fp8_e4m3fn.safetensors` | `models/diffusion_models/` | 20,430,679,144 | 20.43 |
| `split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors` | `models/text_encoders/` | 9,384,670,680 | 9.38 |
| `split_files/diffusion_models/qwen_image_nvfp4.safetensors` | `models/diffusion_models/` | 19,769,139,136 | 19.77 |
| `split_files/text_encoders/qwen_2.5_vl_7b_nvfp4.safetensors` | `models/text_encoders/` | 6,114,433,446 | 6.11 |
| `split_files/vae/qwen_image_vae.safetensors` | `models/vae/` | 253,806,246 | 0.254 |

The Qwen official page lists `Qwen-Image-Lightning-4steps-V1.0.safetensors` as an optional accelerator LoRA; resolve its current size before downloading.

## Acquisition and verification procedure

1. Query `https://huggingface.co/api/models/<org>/<repo>/tree/main?recursive=true` and record exact `path` and `size`.
2. Calculate disk budget and preserve headroom.
3. Download large artifacts separately with native Windows destinations and `curl -L --fail --retry 5 -C -`.
4. On Windows/MSYS, use separate background processes for large files; do not combine multiple background subshells with a final `wait` pattern.
5. Download workflow JSON separately and verify it parses.
6. Treat a download as complete only after exit code 0 and byte count matches the manifest.
7. Validate the workflow against the live ComfyUI model/node inventory after refresh or restart.

## Hardware note

For a 12 GB RTX 4070 Ti class card, Krea 2 Turbo FP8 is the first candidate, but its diffusion model plus Qwen3-VL encoder may still require offloading. Ideogram NVFP4 is smaller than INT8, while the supplied graph expects INT8 filenames. Qwen-Image-2512 FP8 is an offload-heavy experiment; do not call it a comfortable native-12-GB fit without a smoke test.

## Provenance

Report source repository, exact destination, byte count, and verification status. Distinguish files found, downloaded, loaded by ComfyUI, and exercised in a generation run.
