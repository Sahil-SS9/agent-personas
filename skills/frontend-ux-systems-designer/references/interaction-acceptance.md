Source ledger: ../../../sources.json
Retrieved: 2026-09-07T18:04:01.820110+00:00
Sharpens: component-compatibility-review, ui-integration-acceptance
Rights: original distillation; source-specific restrictions retained in ledger; no full-book or source-code reproduction.

# Interaction and AI-state acceptance

Sources: F02 (W3C modal pattern), F03 (Motion reduced-motion guidance), F05 (agent UI catalogue). A02 supports relevance of human-AI design, not effectiveness of this package. Operational approval rules below are original synthesis.

## Modal contract
On open, place focus appropriately inside the dialog. For long structured content, a static heading can be a better initial target than a distant button. Keep Tab and Shift+Tab within it. Escape and a visible close/cancel control should close it. Return focus to the invoker unless it disappeared or a documented next workflow target is more appropriate. Use an accessible title. Mark modal only when the actual background interaction is disabled; visual dimming alone is insufficient.

For an irreversible final action, consider initial focus on the least destructive choice. Do not use aria-describedby to flatten a long structured document into one unbroken announcement.

## Motion contract
Respect the operating system's reduced-motion preference. MotionConfig reducedMotion='user' disables transform/layout animation, not every possible animated effect. Check custom CSS, autoplay and canvas effects separately. Keep changes understandable without physical movement; use simpler transitions where appropriate.

Verify normal-motion and reduced-motion as two separate modes. Record actual changes across frames and response to user input; a static screenshot cannot establish choreography. Give continuous decoration a pause control, cap rendering work/pixel ratio, suspend hidden/offscreen loops and provide a static fallback if WebGL is unavailable. Text contrast must survive moving backgrounds and translucent overlays. Keep canvas decoration out of the accessibility tree unless it exposes equivalent semantic controls.

## Agent-state contract
Proposed is not running; running is not completed; completion requires an observed result. Show partial output and recovery choices honestly. Approval UI should show action, target, consequences and cancellation. Repeated clicks or retries must not silently duplicate a state-changing action. Backend enforcement belongs to implementation; the UI alone cannot authorise safely.

## Acceptance matrix
For each state record entry event, visible message, keyboard destination, screen-reader information, available action, cancellation semantics and exit condition. Verify success, timeout, partial failure, cancelled work, repeated action, navigation away and reconnect where applicable.

## Honest evidence
A design review can verify the matrix exists. Only an exercised implementation can verify focus, retry behaviour and performance. Automated checks supplement, not replace, keyboard and assistive-technology testing.
