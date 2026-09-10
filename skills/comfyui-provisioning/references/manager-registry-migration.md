# ComfyUI Manager registry migration

## Scope
Use this reference when moving an existing Windows portable ComfyUI installation from the legacy Manager database/clone behavior to the newer registry/package-oriented Manager path.

## Verified migration pattern

1. Identify the portable workspace and Manager clone.
2. Inspect `user/__manager/config.ini` and the Manager git status.
3. Copy `custom_nodes/ComfyUI-Manager` and `user/__manager` to a timestamped rollback directory.
4. Update only the Manager repository with a fast-forward pull from `origin/main`.
5. Set:

```ini
db_mode = new
```

6. Restart ComfyUI.
7. Verify through the running server and logs; then validate representative workflows.

## Important distinction

This changes Manager's package/registry database path. It is not the same as upgrading ComfyUI core. Do not upgrade core merely because the Manager is being migrated; core changes can introduce independent node-schema drift.

## Evidence standard

Record:

- previous and new Manager commit
- rollback directory
- previous and new `db_mode`
- restart result
- live Manager/runtime mode
- registry fetch result
- custom-node load result
- workflow validation result
- representative render result

A stopped server or an unverified restart means migration is **applied but not verified**, not complete.

## Windows notes

Use native `C:/...` paths for tools that receive Windows paths. The portable launcher may be unsuitable for non-interactive agent shells; if launching directly, use the embedded interpreter and the portable-build flag. Regardless of launch method, verify readiness via `http://127.0.0.1:8188/system_stats` before claiming the migration is live.
