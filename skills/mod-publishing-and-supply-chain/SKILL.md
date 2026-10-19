---
name: mod-publishing-and-supply-chain
description: "Publish mods cleanly (no game files, honest credits) and vet third-party mod and trainer downloads."
version: 0.1.0
author: Hermes
license: MIT
---

# Mod publishing and supply chain

## Part A: publishing your mod

### 1. Never ship
- game files or byte-identical copies, extracted assets, decompiled source;
- retail offsets or decompiler-generated names baked into shipped code;
- credentials, API keys, local paths from the build machine;
- leaked builds or code, or a mod that only works with them.

### 2. Do ship
Your own code and assets; patches and diffs; converters or installers that transform the user's own files on their machine ("bring your own game files").

### 3. Pre-publish check
Scan the package for files that match the game install, decompiler artefacts, secrets and absolute paths. Build from a clean tree and record output hashes.

### 4. Credits, licence and honesty
- Credit loaders, libraries, references and any generated-asset tools; check each tool's licence for commercial use.
- State plainly that AI was used and how. Communities react badly to undisclosed AI releases, and some ban AI projects; follow each community's rules.
- Write a README with exact game build, loader versions, install, uninstall and known issues.

### 5. Legal reality (not legal advice)
Read the publisher's mod policy. Takedowns happen even without assets (the re3/reVC takedown and lawsuit, 2021; a cease-and-desist to the H2M mod, 2024). Commercial use, monetisation and leaked material raise the risk sharply.

## Part B: vetting third-party downloads (loaders, tools, trainers, mods)

### 1. Get tools from official sources only
Official release pages of the project (e.g. the BepInEx, UE4SS or MO2 GitHub releases, Nexus, Thunderstore, the loader's own site). Check checksums or signatures where offered.

### 2. Malware-lure signals (treat as suspect, do not download)
- "Best <game> Trainer/Mod Menu <year>" names, keyword-stuffed READMEs, sections written for search engines;
- download buttons that leave GitHub (Pages sites, file hosts) instead of real releases;
- many similar repos created the same day with similar star counts and few or no forks;
- archives that ask you to disable antivirus, use a password, or run an installer as administrator;
- no source code matching the claimed features.

### 3. If something must be inspected
Analyse it in a disposable VM without credentials, never on the user's gaming PC, and report findings instead of running it.

## Proof
A publish-check result with no findings, a README with credits and AI disclosure, and for any third-party download its official source, version and checksum.
