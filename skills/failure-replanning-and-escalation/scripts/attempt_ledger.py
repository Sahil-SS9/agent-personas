#!/usr/bin/env python3
"""Decide the next move for a task node from its attempt ledger and live status.

  attempt_ledger.py LEDGER.json [--max-dispatches N]
LEDGER.json: {"task", "dispatches": [{"brief_version", "specialist", "outcome": "failed|passed|running|killed_rescoped", "reason"}],
              "running"?: {"minutes", "tokens", "budget_minutes", "budget_tokens", "scope_drift": bool}}
--max-dispatches has NO default: use the owner's policy (state it in the plan).

Rules, in order:
  running and over budget (time or tokens) or drifting scope -> kill_and_respawn (narrower brief); a
      killed-and-rescoped dispatch does not count as a failed dispatch
  failed dispatches >= max -> escalate (with this ledger)
  last two failures used the same brief and specialist -> retry_new_brief (never resend the same brief)
  last failure -> retry_new_brief, or reroute_specialist if the reason names a capability gap
Prints JSON {"next_action", "failed_dispatches", "reason"}.
"""
import argparse, json, sys


def decide(led, max_d):
    ds = led.get("dispatches", [])
    failed = [d for d in ds if d.get("outcome") == "failed"]
    run = led.get("running")
    if run:
        over = (run.get("budget_minutes") and run.get("minutes", 0) > run["budget_minutes"]) or \
               (run.get("budget_tokens") and run.get("tokens", 0) > run["budget_tokens"])
        if over or run.get("scope_drift"):
            return {"next_action": "kill_and_respawn", "failed_dispatches": len(failed),
                    "reason": "over budget or drifting scope: stop it and re-dispatch with a narrower brief (re-scope, not a failure)"}
        return {"next_action": "wait", "failed_dispatches": len(failed), "reason": "within budget and scope"}
    if any(d.get("outcome") == "passed" for d in ds[-1:]):
        return {"next_action": "verify", "failed_dispatches": len(failed), "reason": "worker reports success: verify independently"}
    if len(failed) >= max_d:
        return {"next_action": "escalate", "failed_dispatches": len(failed), "reason": f"{len(failed)} failed dispatches reached the limit of {max_d}"}
    if not failed:
        return {"next_action": "dispatch", "failed_dispatches": 0, "reason": "no attempts yet"}
    last = failed[-1]
    if "capab" in str(last.get("reason", "")).lower() or "lacks" in str(last.get("reason", "")).lower():
        return {"next_action": "reroute_specialist", "failed_dispatches": len(failed), "reason": "failure names a capability gap"}
    return {"next_action": "retry_new_brief", "failed_dispatches": len(failed), "reason": "change the brief using the failure reason; never resend it unchanged"}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ledger"); ap.add_argument("--max-dispatches", type=int, required=True)
    a = ap.parse_args(argv)
    try:
        led = json.load(open(a.ledger))
    except (OSError, ValueError) as e:
        print(f"cannot read ledger: {e}", file=sys.stderr); return 2
    print(json.dumps(decide(led, a.max_dispatches), indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
