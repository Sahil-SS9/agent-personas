# Post-install verification & smoke test (validated 2026-08-04)

Server starting is NOT proof the nodes loaded. Packs with missing optional
deps skip themselves with a logged ImportError. Verify in this order:

## 1. Startup log triage
Grep the server log for `ImportError` and `could not be imported`.
- Graceful skips are fine (node just unavailable). Example: KJNodes'
  PatchTritonVAE requires `triton` — on Windows that's the `triton-windows`
  fork; without it the node skips but the pack loads.
- A pack whose ENTIRE `__init__.py` raised = missing deps → install with the
  portable python and restart.

## 2. Node registration check
```bash
curl -s http://127.0.0.1:8188/object_info | python -c "
import json,sys; d=json.load(sys.stdin)
print('nodes:', len(d))
print([k for k in d if 'minimax' in k.lower()])"   # keyword of interest
```
Reference scale: fresh 0.30.0 portable + 17 popular packs ≈ **1,927 nodes**.
Expected H3 natives: EmptyMiniMaxH3LatentAV, MiniMaxH3{Image,Reference}ToVideo,
MiniMaxH3SigmaShift (+ KJNodes' MiniMaxH3MemoryEfficientSageAttentionPatch,
+ Tr1dae's MiniMaxH3LatentUpscaleCombined).

## 3. WIP-commit gotcha
A repo can ship a node file whose class is NOT registered (author committed
the file but hasn't added it to NODE_CONFIG — seen with KJNodes' TinyVAEDecoder,
committed hours earlier, unregistered). Before debugging a "missing node":
grep the pack's `__init__.py` for the class name. File present ≠ registered.
(Internal helpers like TinyVAEDecoder may also be used by other code paths —
check call sites before concluding it's dead code.)

## 4. Smoke-test generation (end-to-end proof)
Use `templates/smoke_test_workflow.json` (API format). Flow:
```python
import json, urllib.request, time
wf = json.load(open('smoke_test_workflow.json'))
req = urllib.request.Request('http://127.0.0.1:8188/prompt',
    data=json.dumps({'prompt': wf}).encode(),
    headers={'Content-Type': 'application/json'})
pid = json.loads(urllib.request.urlopen(req, timeout=30).read())['prompt_id']
for _ in range(90):
    time.sleep(3)
    h = json.loads(urllib.request.urlopen(f'http://127.0.0.1:8188/history/{pid}').read())
    if pid in h:
        print(h[pid]['status'], h[pid]['outputs'])
        break
```
Settings in the template are Illustrious-flavored (Hyphoria): euler_ancestral,
cfg 3.0, 28 steps, 832×1216. Swap `ckpt_name` for any installed checkpoint.
First-gen wall time on RTX 4070 Ti ≈ 1 min. Output lands in `ComfyUI/output/`.

## 5. Post-gen checks
- File exists and size > 0 (`ls -la output/`).
- If workflow load fails with `class_type not found` → the missing pack name is
  in the error; install it (Manager or git clone) and restart.

## 6. Full inventory sweep (the "confirm everything is here" review)
When the user asks to confirm all models/files arrived, never answer from
memory — run a per-folder census and deliver it as a table:

```bash
cd <install>/ComfyUI_windows_portable/ComfyUI
for d in models/checkpoints models/loras models/embeddings models/upscale_models \
         models/vae models/diffusion_models models/text_encoders models/LLM models/ultralytics; do
  n=$(find "$d" -type f \( -name "*.safetensors" -o -name "*.pt" -o -name "*.pth" -o -name "*.gguf" \) | wc -l)
  s=$(find "$d" -type f -exec stat -c%s {} \; | awk '{t+=$1} END {printf "%.1f", t/1073741824}')
  printf "%-28s %3d files  %8s GB\n" "$d" "$n" "$s"
done
ls -d custom_nodes/*/ | wc -l                        # node pack count
find user/default/workflows -name '*.json' | wc -l   # workflows in browser
df -h /c | tail -1                                   # free disk
curl -s -m 3 http://127.0.0.1:8188/system_stats >/dev/null && echo UP
```
Report: folder / files / size / what-it's-for, server status, remaining
checklist items. Reference scale (RTX 4070 Ti build, 2026-08): 21 packs ≈
1,939 nodes; full H3 stack ≈ 39 GB diffusion (int8+fp8 pruned pair) + 14.6 GB
text encoder + 9.5 GB GGUF prompt pair + 5.7 GB VAEs.
