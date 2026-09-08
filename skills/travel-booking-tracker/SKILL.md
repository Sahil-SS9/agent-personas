---
name: "travel-booking-tracker"
description: "Track reservations, payment deadlines and pre-departure confirmations in one place."
license: "MIT"
---
# Travel Booking Tracker

## Use when
- Bookings are being made and deadlines must not slip
- Producing the pre-departure confirmation sweep

## Instructions

1. Maintain one tracker table for the trip. Columns:
   item | provider | confirmation ref | amount | paid? |
   cancellation deadline | check-in/booking window | status.
2. Record EVERY advance booking: flights, rooms, tours, transfers,
   restaurant reservations with booking windows, travel insurance.
3. Compute every cancellation deadline against actual dates — never leave
   it as "free cancellation" without the date.
4. Pre-departure sweep at T-7 days and T-1 day: reconfirm each reservation,
   re-fetch any price-dependent items, flag anything unconfirmed.
5. On any change or cancellation, update the tracker the same session and
   note the reason (audit trail).

## Stop conditions
- Never make bookings or payments. Tracking and reminders only.

## Escalation
- Missed cancellation deadline discovered: surface immediately with the
  financial exposure stated plainly.
