---
name: "image-generation-workflow"
description: "Generate and inspect images using an available authorised tool."
license: "MIT"
---
# Image Generation Workflow

## When to use
Generate and inspect images using an available authorised tool.

## Method
1. Confirm subject, composition, visual direction, intended use, image count, rights constraints and budget before generation.
2. Select an available authorised image tool and inspect its actual supported inputs, limits and output format. Do not assume a particular CLI or provider exists.
3. Generate a low-cost concept proof where appropriate, then refine from explicit user feedback. Record prompt, model/version and reproducibility settings that the provider exposes.
4. Inspect the actual returned files for content fidelity, artefacts, dimensions and format. A successful API response without a usable image is not completion.
5. Preserve approved originals and derived exports separately. Do not publish, buy assets or exceed generation budget without approval.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
