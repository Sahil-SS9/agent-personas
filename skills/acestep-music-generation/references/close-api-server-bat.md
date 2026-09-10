# close_api_server.bat — Companion Script

**Location:** `C:\Users\Hermes\Suno\ACE-Step-1.5\close_api_server.bat`

**Purpose:** One-double-click tool to kill whatever zombie process is holding port 8001 (the ACE-Step API server).

## What it does

1. Checks if anything is LISTENING on port 8001
2. If yes, tries graceful shutdown via HTTP POST to `/shutdown`
3. If that fails (no /shutdown endpoint), force-kills via `Stop-Process -Force`
4. Verifies the port is freed
5. Reports status

## Usage

- **Double-click** the file in Explorer
- **From terminal:** `cd C:\Users\Hermes\Suno\ACE-Step-1.5 && start close_api_server.bat`

## Exit codes

- `0` — port was freed (either it was already free, or killing succeeded)
- `255` — batch parser error (see pitfalls below)

## Batch-file pitfalls on this system

Creating `.bat` files from Hermes on this Windows 10 system via git-bash/MSYS has specific quirks:

### Line ending sensitivity

When created via `write_file` tool, the file uses LF-only (`\n`) line endings. This is usually fine for simple batch files.

When created via Python `open(path, 'w', newline='')` with explicit `\r\n`, the file has CRLF — but this triggered `. was unexpected at this time.` in `for /f` loops that use pipes (`^|`). The root cause was never fully isolated but correlates with:

- CRLF files created from scratch (not based on a working template)
- `for /f` loops containing `^|` pipe escapes
- Running via `cmd //c` through git-bash (not native cmd.exe)

**Safe approach found:** Start from a working `.bat` file created by `write_file`, append new content via Python bytes manipulation, preserving the original's byte-level structure.

### `timeout /t` vs git-bash `timeout`

`cmd //c close_api_server.bat` runs through git-bash, which has its own `timeout` binary (from coreutils). The command `timeout /t 2 /nobreak` gets intercepted by git-bash's `timeout`, which interprets `/t` as a signal-argument option, producing:
```
timeout: invalid time interval '/t'
```

**Impact:** Harmless for `close_api_server.bat` — the script continues past the error and completes normally. The `timeout` calls are just pauses for OS to release the port. They fail silently but the script still works.

**Fix for truly reliable pauses:** Use `ping -n 2 127.0.0.1 >nul` instead of `timeout /t 1 /nobreak >nul`.

### Powershell from batch

The graceful-shutdown PowerShell command uses escaped quotes heavily:
```batch
powershell -Command "& {try {Invoke-WebRequest -Uri \"http://127.0.0.1:8001/shutdown\" ...}}"
```

Keep the PowerShell command on a single line in the batch file. Multi-line PowerShell inside batch `"` quoting is fragile and varies by Windows version.

## Verification

The ad-hoc verification script is at:
`C:\Users\Hermes\AppData\Local\Temp\hermes-verify-close-api-server.py`

It tests:
- File existence and content
- Server running on port 8001 pre-kill
- Batch execution succeeds
- Port 8001 freed post-kill
