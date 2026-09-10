#!/usr/bin/env python3
"""safetensors_check.py — validate safetensors structural integrity.

Usage:
  python3 safetensors_check.py file1.safetensors [file2 ...]

Checks the 8-byte header length, JSON header parse, tensor count, and that the
max data offset does not exceed the file size (detects truncation/corruption).
Structural OK does NOT prove weights are correct — pair with a smoke test.
"""
import json
import os
import struct
import sys


def check(path):
    try:
        size = os.path.getsize(path)
    except OSError as e:
        return f"MISSING/UNREADABLE: {e}"
    if size < 8:
        return "BAD: file smaller than safetensors header"
    try:
        with open(path, "rb") as f:
            (n,) = struct.unpack("<Q", f.read(8))
            if n > size - 8:
                return f"BAD: header length {n} exceeds file size {size}"
            hdr = json.loads(f.read(n))
        tensors = {k: v for k, v in hdr.items() if k != "__metadata__"}
        max_end = max((t["data_offsets"][1] for t in tensors.values()
                       if isinstance(t, dict) and "data_offsets" in t),
                      default=0)
        expected = 8 + n + max_end
        if expected > size:
            return (f"TRUNCATED: tensors end at {expected:,} "
                    f"but file is {size:,} bytes")
        return f"OK | tensors={len(tensors)} | header={n}B | filesize={size:,}"
    except Exception as e:
        return f"PARSE FAIL: {e}"


def main():
    if len(sys.argv) < 2:
        print("usage: safetensors_check.py file.safetensors [...]")
        sys.exit(1)
    for p in sys.argv[1:]:
        print(f"{os.path.basename(p)}: {check(p)}")


if __name__ == "__main__":
    main()
