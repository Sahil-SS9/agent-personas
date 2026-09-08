---
name: "competitor-news-monitor"
description: "Watch named companies for material news; cited digests."
license: "MIT"
---
# Competitor News Monitor

## When to use
Watch named companies for material news; cited digests.

## Method
1. Define competitors, topics, materiality criteria and reporting interval with the user. Monitoring setup is separate from authority to create schedules.
2. Search first-party announcements and corroborating coverage. Capture event date, source date and what actually changed.
3. Deduplicate coverage of the same event and distinguish new information from repeated commentary or sponsored claims.
4. Report why each event matters to the user, the supporting source and uncertainty. Do not invent activity when collection fails or there is no qualifying news.
5. Keep an explicit last-successful-run marker; failed collection must not advance it as if complete. Publish or notify only to approved destinations.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
