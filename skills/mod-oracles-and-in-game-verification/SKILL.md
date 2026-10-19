---
name: mod-oracles-and-in-game-verification
description: "Prove a mod works with a mechanical oracle, keep evidence levels honest and stop drifting builds."
version: 0.1.0
author: Hermes
license: MIT
---

# Mod oracles and in-game verification

Agents fail at modding by building confidently on a wrong guess. The fix is an oracle: something mechanical that says right or wrong, run after every change. The running game is the oracle; a reading of the code is not.

## 1. Pick the cheapest oracle that catches the next likely mistake
| Oracle | Catches |
|---|---|
| Game or loader log (BepInEx `LogOutput.log`, `UE4SS.log`, Unity `Player.log`, SKSE log, `client.log`, `latest.log`) | load errors, exceptions, missing assets |
| Scripted scene plus a screenshot you actually inspect | "does it show up", scale, facing, pivot, layering |
| Test command or GameTest | feature behaviour, repeatably |
| Round trip (decode, encode, decode) | wrong file-format understanding |
| Trace replay (real state in, compare next state) | a port that behaves differently from the game |
| Headless simulation bench | rules and data regressions in seconds |
| Fake host or fake guest | bridge and integration bugs before the real games run |
| Measurement scene | latency, camera lag, audio offset |
| Publish check | shipping game files, decompiled code or secrets |

## 2. Make the loop one command
Automate launch, menus, scene, check and log capture so one command answers "did it work". Use windowed mode at a fixed size so screenshots and clicks stay stable. Ask before driving the user's mouse and keyboard.

## 3. Prove the oracle can fail
Run it once against a deliberately broken build or mutated input. An oracle that stays green on a broken build is not checking anything.

## 4. Circuit breaker
After about three identical failures, stop. Write down what is known in MODLOG.md, then change approach or ask the user. Do not repeat the same attempt.

## 5. Keep evidence levels apart
Label every claim, in notes and to the user:
- creator report (README, post, video);
- design or proposal;
- source inspection (code read, nothing run);
- synthetic test (fake host, unit test);
- real run (the real game ran this build and someone looked; name game build, OS and GPU).
Only a real run supports "it works", and only for the scenarios actually played. A passing test that checks little, a design doc or one clean install on one machine is not proof.

## 6. Report
What was verified and how, what the oracle did not cover, known failures with reproduction steps, and the restore path.
