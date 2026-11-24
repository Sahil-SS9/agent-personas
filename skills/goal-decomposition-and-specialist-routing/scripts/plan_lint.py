#!/usr/bin/env python3
"""Lint a dispatch plan against its task graph, roster and limits before launch.

  plan_lint.py --tasks TASKS.json --plan PLAN.json [--roster ROSTER.json] [--limits LIMITS.json]

TASKS.json: [{"id", "depends_on": [...], "needs"?: capability, "tokens"?: n, "output_tokens"?: n}]
PLAN.json:  {"agents": [{"id", "specialist"}], "tasks": [{"id", "agent", "objective", "output",
             "boundaries", "done_check", "inputs": [{"from_task", "via"}], "verifier"}], "waves": [[ids]]}
ROSTER.json: [{"name", "capabilities": [...]}]     LIMITS.json: {"agent_budget", "context_limit_tokens"}

Reports each problem as {"task", "type", "detail"}; exit 1 if any. Types:
missing_task, unknown_task, duplicate_assignment, unknown_agent, wrong_specialist, over_budget,
missing_transfer, extra_transfer, chat_history_handoff, context_overflow, dependency_order,
missing_from_waves, cycle, empty_brief_field, self_verified, no_verifier.
"""
import argparse, json, re, sys

HISTORY = re.compile(r"\b(chat|conversation|history|transcript|everything so far)\b", re.I)


def lint(tasks, plan, roster=None, limits=None):
    issues = []
    add = lambda t, ty, d="": issues.append({"task": t, "type": ty, "detail": d})
    by = {t["id"]: t for t in tasks}
    # cycle check on the goal graph
    state = {}
    def visit(n, stack):
        if state.get(n) == 1:
            add(n, "cycle", " -> ".join(stack + [n])); return
        if state.get(n) == 2 or n not in by:
            return
        state[n] = 1
        for d in by[n].get("depends_on", []):
            visit(d, stack + [n])
        state[n] = 2
    for n in by:
        visit(n, [])
    agents = {a["id"]: a.get("specialist") for a in plan.get("agents", [])}
    caps = {r["name"]: set(r.get("capabilities", [])) for r in (roster or [])}
    seen, assign = set(), {}
    for t in plan.get("tasks", []):
        tid = t.get("id")
        if tid not in by:
            add(tid, "unknown_task"); continue
        if tid in seen:
            add(tid, "duplicate_assignment")
        seen.add(tid); assign[tid] = t.get("agent")
        if t.get("agent") not in agents:
            add(tid, "unknown_agent", str(t.get("agent")))
        elif roster and by[tid].get("needs") and by[tid]["needs"] not in caps.get(agents[t["agent"]], set()):
            add(tid, "wrong_specialist", f"{agents[t['agent']]} lacks {by[tid]['needs']}")
        for k in ("objective", "output", "boundaries", "done_check"):
            if not str(t.get(k) or "").strip():
                add(tid, "empty_brief_field", k)
    for tid in by:
        if tid not in seen:
            add(tid, "missing_task")
    used = {assign[t] for t in assign}
    if limits and len(used) > limits.get("agent_budget", 10**9):
        add("PLAN", "over_budget", f"{len(used)} agents > {limits['agent_budget']}")
    load = {a: 0 for a in used}
    for t in plan.get("tasks", []):
        tid, ag = t.get("id"), t.get("agent")
        if tid not in by or ag not in load:
            continue
        load[ag] += by[tid].get("tokens", 0)
        deps = set(by[tid].get("depends_on", []))
        declared = set()
        for inp in t.get("inputs") or []:
            src, via = inp.get("from_task"), str(inp.get("via") or "")
            declared.add(src)
            if src not in deps or assign.get(src) == ag:
                add(tid, "extra_transfer", str(src))
            elif not via or HISTORY.search(via):
                add(tid, "chat_history_handoff", via or "(empty)")
            else:
                load[ag] += by.get(src, {}).get("output_tokens", 0)
        for d in deps:
            if d in assign and assign[d] != ag and d not in declared:
                add(tid, "missing_transfer", f"needs {d} from {assign[d]}")
        if len(used) >= 2:
            v = t.get("verifier")
            if not v:
                add(tid, "no_verifier")
            elif v == ag:
                add(tid, "self_verified")
    if limits:
        lim = limits.get("context_limit_tokens", 10**12)
        for ag, n in load.items():
            if n > lim:
                for t in plan.get("tasks", []):
                    if t.get("agent") == ag:
                        add(t.get("id"), "context_overflow", f"{ag} needs {n} > {lim}")
    pos = {}
    for wi, w in enumerate(plan.get("waves") or []):
        for tid in w:
            pos.setdefault(tid, wi)
    for tid in by:
        if tid not in pos:
            add(tid, "missing_from_waves")
        else:
            for d in by[tid].get("depends_on", []):
                if d in pos and pos[d] >= pos[tid]:
                    add(tid, "dependency_order", f"{d} is not in an earlier wave")
    return issues


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tasks", required=True); ap.add_argument("--plan", required=True)
    ap.add_argument("--roster"); ap.add_argument("--limits")
    a = ap.parse_args(argv)
    try:
        load = lambda p: json.load(open(p)) if p else None
        issues = lint(load(a.tasks), load(a.plan), load(a.roster), load(a.limits))
    except (OSError, ValueError, KeyError, TypeError) as e:
        print(f"cannot lint: {e}", file=sys.stderr); return 2
    print(json.dumps(issues, indent=1))
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
