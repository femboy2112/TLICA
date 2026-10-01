#!/usr/bin/env python3
"""
Finite construction-level witness for the Semantic Optics research dossier.

This script demonstrates only three formal points:

1. A deterministic optic-shaped interface can expose a public view while retaining
   hidden residual context, then use that residual plus a response to update the world.

2. The same base interface can be closed with different observer/controller
   decorations and produce different world trajectories. Therefore the base optic
   alone does not determine the TLICA-decorated behavior in this construction.

3. A restricted Yoneda/nerve-style probe family can fail to distinguish two
   non-isomorphic objects in a finite poset category; adding a discriminator can
   split them, while the full representable profile distinguishes every object in
   the fixture.

This is NOT empirical evidence about people, TLICA, politics, cinema, or cognition.
It is a deterministic consistency witness for distinctions made in the dossier.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple, List
import argparse
import json

World = Tuple[str, str]


def optic_view(world: World) -> Tuple[str, str]:
    """l : S -> M x A. Returns (residual M, exposed view A)."""
    hidden, visible = world
    return hidden, visible


def optic_update(residual: str, response: str) -> World:
    """r : M x B -> S'. Retain hidden support and apply observer response."""
    return residual, response


@dataclass(frozen=True)
class Decoration:
    name: str
    basis: str
    decoder: Dict[str, str]
    policy: Dict[str, str]


def close_optic(world: World, decoration: Decoration) -> Dict[str, object]:
    """
    Close the same base optic with an observer-specific controller:
        c_theta = policy_theta o decoder_theta : A -> B
    and evaluate r o (id_M x c_theta) o l.
    """
    residual, view = optic_view(world)
    meaning = decoration.decoder[view]
    response = decoration.policy[meaning]
    new_world = optic_update(residual, response)
    return {
        "decoration": decoration.name,
        "basis": decoration.basis,
        "residual": residual,
        "view": view,
        "meaning": meaning,
        "response": response,
        "new_world": list(new_world),
    }


def make_poset_fixture():
    """
    Finite poset category with objects p,q,x,y and arrows:
        p <= x, p <= y, q <= x,
    plus identities.

    In a poset category Hom(a,b) is singleton iff a <= b, otherwise empty.
    """
    objects = ["p", "q", "x", "y"]
    leq = {(o, o) for o in objects}
    leq |= {("p", "x"), ("p", "y"), ("q", "x")}
    return objects, leq


def hom_cardinality(a: str, b: str, leq) -> int:
    return 1 if (a, b) in leq else 0


def yoneda_profile(target: str, probes: List[str], leq) -> List[int]:
    """Restricted representable profile P^op -> Set, recorded by hom-set cardinality."""
    return [hom_cardinality(p, target, leq) for p in probes]


def run() -> Dict[str, object]:
    world = ("hidden-causal-support", "ambiguous")

    neutral = Decoration(
        name="neutral",
        basis="neutral-basis",
        decoder={"ambiguous": "uncertain"},
        policy={"uncertain": "seek_context"},
    )
    suspicious = Decoration(
        name="suspicious",
        basis="suspicious-basis",
        decoder={"ambiguous": "threat"},
        policy={"threat": "escalate"},
    )

    neutral_run = close_optic(world, neutral)
    suspicious_run = close_optic(world, suspicious)

    objects, leq = make_poset_fixture()
    p_only = {
        "x": yoneda_profile("x", ["p"], leq),
        "y": yoneda_profile("y", ["p"], leq),
    }
    pq = {
        "x": yoneda_profile("x", ["p", "q"], leq),
        "y": yoneda_profile("y", ["p", "q"], leq),
    }
    full = {o: yoneda_profile(o, objects, leq) for o in objects}

    checks = {
        "same_base_world_and_view":
            neutral_run["view"] == suspicious_run["view"] == "ambiguous",
        "same_hidden_residual":
            neutral_run["residual"] == suspicious_run["residual"] == "hidden-causal-support",
        "different_decoder_outputs":
            neutral_run["meaning"] != suspicious_run["meaning"],
        "different_responses":
            neutral_run["response"] != suspicious_run["response"],
        "different_closed_world_updates":
            neutral_run["new_world"] != suspicious_run["new_world"],
        "restricted_probe_p_collapses_x_y":
            p_only["x"] == p_only["y"],
        "adding_q_splits_x_y":
            pq["x"] != pq["y"],
        "full_profiles_distinguish_all_fixture_objects":
            len({tuple(v) for v in full.values()}) == len(objects),
    }

    return {
        "scope": "construction-level deterministic witness only",
        "base_optic": {
            "forward": "l: (hidden, visible) -> (residual=hidden, view=visible)",
            "backward": "r: (residual, response) -> (hidden=residual, visible=response)",
            "world": list(world),
        },
        "decorated_closures": [neutral_run, suspicious_run],
        "restricted_yoneda_fixture": {
            "objects": objects,
            "nonidentity_order_relations": [["p", "x"], ["p", "y"], ["q", "x"]],
            "probe_family_p": p_only,
            "probe_family_pq": pq,
            "full_profiles": full,
        },
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_pass": all(checks.values()),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="")
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    print(text)
    raise SystemExit(0 if result["all_pass"] else 1)


if __name__ == "__main__":
    main()
