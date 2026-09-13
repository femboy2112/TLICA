#!/usr/bin/env python3
"""Finite-model demonstration for "This Ontology Is Really Moreish".

WHAT THIS IS. A small, deterministic, standard-library illustration of the
manuscript's central mathematical claim (the "Greedy Integral Problem", MANUSCRIPT
sections 4 and 9):

    Maximizing the integrand u(x, a) locally at every step does NOT maximize the
    integral J = sum_t u(x_t, a_t) when the integrand is dynamically coupled
    through the state, x_{t+1} = F(x_t, a_t).

and the corrective claim (section 9): a feedback policy pi(x) that values future
*option value* (the size of the reachable action set) beats the greedy policy on
the integral, and does so precisely by refusing "gratuitous" actions for which
|A(x_{t+1})| << |A(x_t)|.

WHAT THIS IS NOT. This is a toy state machine, not evidence about any person and
not a validation of the phenomenological reading. It illustrates a control-theory
identity that is already a standard result (Bellman's principle of optimality:
the greedy/myopic policy is generally suboptimal under state coupling); the toy
just makes the manuscript's specific figures concrete and checkable. It is
explicitly NOT independent corroboration of the essay's psychological content.

THE INSTRUMENT RULE (calibration first). Before any headline reading counts, the
model is run on a case where the answer is KNOWN: a *decoupled* variant in which
actions do not change the future state. There, maximizing each moment
independently IS optimal, so greedy must exactly equal the optimum. The demo
asserts that it does. Only then is the coupled reading trusted. The optimal /
feedback policy is also computed two independent ways -- backward-induction
dynamic programming AND exhaustive search over all action sequences -- and the
two must agree.

THE TOY. State x = (d, t): d = number of open "doors" (a concrete stand-in for
|A(x)|, the size of Future-Me's reachable action set), t = step index. Three
actions:

    INDULGE  : reward = R_INDULGE (high, immediate); effect d -> d - 1   (needs d >= 1)
               -- the "present resonance" move; it pays now and closes a door.
    MAINTAIN : reward = d (a *sustainable* present that scales with open doors);
               effect d -> d                                             (always legal)
    OPEN     : reward = 0 (pay nothing now); effect d -> min(d + 1, DMAX) (needs d < DMAX)
               -- pure option preservation: buy nothing today, keep tomorrow wide.

GREEDY  = the myopic (horizon-1) policy: argmax_a u(d, a), ties broken by the
          fixed priority INDULGE > MAINTAIN > OPEN. This is Underground Super Hans
          + Pavlov's Veruca fused into a controller: take the most resonant state
          available *now*, discount the coupled future.
FEEDBACK= the full-lookahead optimal policy pi(x) = argmax_a [ u(d, a) + V(F(d, a)) ],
          V computed by backward induction. It is the manuscript's pi(x): it need
          not predict the future, only respond to the state with the future's
          option value already priced in.

Pure standard library. Run:  python3 greedy_vs_option_demo.py [--output results.json]
Exit status 0 iff every check passes.
"""
from __future__ import annotations

import argparse
import json
import sys
from functools import lru_cache

# ---- model parameters -------------------------------------------------------
DMAX = 5          # cap on open doors
D0 = 3            # initial open doors
T = 8             # horizon (number of steps)
R_INDULGE = 4     # immediate reward of the door-closing "present resonance" move

ACTIONS = ("INDULGE", "MAINTAIN", "OPEN")  # fixed priority order (greedy tie-break)


def legal(d: int) -> list[str]:
    """The reachable action set A(x) at state d, in priority order."""
    acts = []
    if d >= 1:
        acts.append("INDULGE")
    acts.append("MAINTAIN")
    if d < DMAX:
        acts.append("OPEN")
    return acts


def reward(d: int, a: str) -> int:
    if a == "INDULGE":
        return R_INDULGE
    if a == "MAINTAIN":
        return d
    if a == "OPEN":
        return 0
    raise ValueError(a)


def step(d: int, a: str, coupled: bool) -> int:
    """State transition d -> d'. When coupled is False, the door count is frozen
    (F(x, a) = x on the door coordinate) -- the decoupled calibration variant."""
    if not coupled:
        return d
    if a == "INDULGE":
        return d - 1
    if a == "MAINTAIN":
        return d
    if a == "OPEN":
        return min(d + 1, DMAX)
    raise ValueError(a)


# ---- policies ---------------------------------------------------------------
def run_greedy(coupled: bool) -> dict:
    """Myopic policy: pick the highest-immediate-reward legal action each step."""
    d, total, trace, shrinks = D0, 0, [], 0
    for _ in range(T):
        acts = legal(d)
        # argmax immediate reward, ties broken by fixed ACTIONS priority
        best = max(acts, key=lambda a: (reward(d, a), -ACTIONS.index(a)))
        d2 = step(d, best, coupled)
        # |A(x)| proxy is the open-door count d; a "shrinking move" is a
        # transition d' < d -- an action that gratuitously deletes an option
        # (the section-9 |A(x_{t+1})| << |A(x_t)| move). Same proxy the
        # terminal_d check uses, so the two are consistent.
        shrinks += 1 if d2 < d else 0
        total += reward(d, best)
        trace.append((d, best, reward(d, best), d2))
        d = d2
    return {"J": total, "terminal_d": d, "shrinking_moves": shrinks, "trace": trace}


def optimal_dp(coupled: bool) -> dict:
    """Full-lookahead feedback policy via backward induction (Bellman)."""

    @lru_cache(maxsize=None)
    def V(d: int, t: int) -> int:
        if t == T:
            return 0
        return max(reward(d, a) + V(step(d, a, coupled), t + 1) for a in legal(d))

    d, total, trace, shrinks = D0, 0, [], 0
    for t in range(T):
        acts = legal(d)
        best = max(acts, key=lambda a: (reward(d, a) + V(step(d, a, coupled), t + 1),
                                        -ACTIONS.index(a)))
        d2 = step(d, best, coupled)
        shrinks += 1 if d2 < d else 0  # |A(x)| proxy = open-door count d
        total += reward(d, best)
        trace.append((d, best, reward(d, best), d2))
        d = d2
    return {"J": total, "terminal_d": d, "shrinking_moves": shrinks, "trace": trace,
            "V_root": V(D0, 0)}


def brute_force_max(coupled: bool) -> int:
    """Independent cross-check: exhaustive search over all action sequences.

    Enumerates every legal sequence and returns the maximum achievable integral.
    Must equal the DP root value; this is the 'second independent implementation'
    the instrument rule requires for a load-bearing number."""
    best = {"J": -1}

    def rec(d: int, t: int, acc: int):
        if t == T:
            if acc > best["J"]:
                best["J"] = acc
            return
        for a in legal(d):
            rec(step(d, a, coupled), t + 1, acc + reward(d, a))

    rec(D0, 0, 0)
    return best["J"]


# ---- checks -----------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=None, help="write results JSON to this path")
    args = ap.parse_args()

    coupled_greedy = run_greedy(coupled=True)
    coupled_opt = optimal_dp(coupled=True)
    coupled_brute = brute_force_max(coupled=True)

    decoupled_greedy = run_greedy(coupled=False)
    decoupled_opt = optimal_dp(coupled=False)
    decoupled_brute = brute_force_max(coupled=False)

    checks = []

    def check(name: str, ok: bool, detail: str):
        checks.append({"name": name, "passed": bool(ok), "detail": detail})

    # Calibration (instrument rule): decoupled => greedy is optimal.
    check("calibration_decoupled_greedy_equals_optimal",
          decoupled_greedy["J"] == decoupled_opt["J"] == decoupled_brute,
          f"decoupled: greedy J={decoupled_greedy['J']}, DP J={decoupled_opt['J']}, "
          f"brute J={decoupled_brute} (all must be equal)")

    # Cross-check: DP optimum equals exhaustive-search optimum (both variants).
    check("dp_matches_brute_force_coupled",
          coupled_opt["J"] == coupled_opt["V_root"] == coupled_brute,
          f"coupled: DP J={coupled_opt['J']}, V_root={coupled_opt['V_root']}, "
          f"brute J={coupled_brute}")
    check("dp_matches_brute_force_decoupled",
          decoupled_opt["J"] == decoupled_brute,
          f"decoupled: DP J={decoupled_opt['J']}, brute J={decoupled_brute}")

    # Headline 1: under coupling, greedy is strictly suboptimal on the integral.
    check("coupled_greedy_strictly_suboptimal",
          coupled_greedy["J"] < coupled_opt["J"],
          f"coupled: greedy J={coupled_greedy['J']} < optimal J={coupled_opt['J']}")

    # Headline 2: greedy gratuitously shrinks the reachable action set; the
    # feedback policy preserves it (terminal |A(x)| proxy = terminal door count).
    check("greedy_collapses_reachable_set",
          coupled_greedy["terminal_d"] < coupled_opt["terminal_d"],
          f"coupled: greedy terminal d={coupled_greedy['terminal_d']} < "
          f"feedback terminal d={coupled_opt['terminal_d']}")
    check("greedy_takes_more_shrinking_moves",
          coupled_greedy["shrinking_moves"] > coupled_opt["shrinking_moves"],
          f"coupled: greedy |A|-shrinking moves={coupled_greedy['shrinking_moves']} > "
          f"feedback={coupled_opt['shrinking_moves']}")

    passed = sum(c["passed"] for c in checks)
    results = {
        "model": {"DMAX": DMAX, "D0": D0, "T": T, "R_INDULGE": R_INDULGE,
                  "actions": list(ACTIONS)},
        "coupled": {"greedy": coupled_greedy, "feedback_optimal": coupled_opt,
                    "brute_force_J": coupled_brute},
        "decoupled_calibration": {"greedy": decoupled_greedy,
                                  "feedback_optimal": decoupled_opt,
                                  "brute_force_J": decoupled_brute},
        "checks": checks,
        "summary": {"passed": passed, "total": len(checks),
                    "all_passed": passed == len(checks)},
    }

    for c in checks:
        print(f"[{'PASS' if c['passed'] else 'FAIL'}] {c['name']}: {c['detail']}")
    print(f"\n{passed}/{len(checks)} checks passed.")

    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            json.dump(results, fh, indent=2)
        print(f"wrote {args.output}")

    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
