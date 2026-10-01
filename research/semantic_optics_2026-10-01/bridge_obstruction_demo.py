#!/usr/bin/env python3
"""
Finite obstruction witness for a naive TLICA-semantics -> extensional-optics equivalence.

The construction intentionally separates:

- two internally distinct observer-state objects (different source/probe semantics),
- identical extensional controller behavior on every exposed view.

The source semantic category is taken to be discrete on those two states: if TLICA
treats the internal distinction as real and supplies no isomorphism between them,
there are no cross-state morphisms.

The naive target forgets the internal semantics and retains only the controller
truth table. Since both states induce the same controller, both map to one target
object c. The target therefore has id_c in Hom(c,c), while the source has empty
Hom(A,B). The forgetful functor cannot be full, hence cannot be an equivalence.

This is a conditional obstruction, not a proof that TLICA must preserve the
chosen distinction. It establishes the theorem debt cleanly:

  either quotient A and B as semantically redundant,
  or enrich the target so the distinction is represented.
"""

from __future__ import annotations

import argparse
import json


VIEWS = ("ambiguous", "clear")

THETA_A = {
    "name": "source-resolved",
    "source_map": {
        "ambiguous": "sensor-A",
        "clear": "sensor-A",
    },
    "probe_profile": ["p", "q"],
    "controller": {
        "ambiguous": "seek_context",
        "clear": "accept",
    },
}

THETA_B = {
    "name": "source-unresolved",
    "source_map": {
        "ambiguous": "unknown",
        "clear": "unknown",
    },
    "probe_profile": ["p"],
    "controller": {
        "ambiguous": "seek_context",
        "clear": "accept",
    },
}


def controller_signature(theta):
    return tuple((v, theta["controller"][v]) for v in VIEWS)


def run():
    sig_a = controller_signature(THETA_A)
    sig_b = controller_signature(THETA_B)

    same_extensional = sig_a == sig_b
    internal_distinct = (
        THETA_A["source_map"] != THETA_B["source_map"]
        or THETA_A["probe_profile"] != THETA_B["probe_profile"]
    )

    # Source category T: discrete category on two semantic states A, B.
    source_homs = {
        "A->A": ["id_A"],
        "B->B": ["id_B"],
        "A->B": [],
        "B->A": [],
    }

    # Naive target O: both states are forgotten to the same extensional controller c.
    target_homs = {
        "c->c": ["id_c"],
    }

    # U(A)=U(B)=c. Fullness on A->B would require every target morphism
    # U(A)->U(B) = c->c to have a source preimage A->B. It does not.
    full_on_A_B = len(source_homs["A->B"]) == len(target_homs["c->c"])

    checks = {
        "internal_states_distinct": internal_distinct,
        "extensional_controller_signatures_identical": same_extensional,
        "source_cross_hom_empty": source_homs["A->B"] == [],
        "target_hom_after_object_collapse_nonempty": target_homs["c->c"] == ["id_c"],
        "naive_forgetful_functor_not_full": not full_on_A_B,
        "naive_equivalence_obstructed": (
            internal_distinct and same_extensional and not full_on_A_B
        ),
    }

    return {
        "scope": "conditional finite category obstruction only",
        "assumption": (
            "Theta_A and Theta_B are treated as non-isomorphic semantic objects "
            "rather than quotiented as redundant."
        ),
        "theta_A": THETA_A,
        "theta_B": THETA_B,
        "extensional_signatures": {
            "A": list(sig_a),
            "B": list(sig_b),
        },
        "source_category_homs": source_homs,
        "naive_target_homs": target_homs,
        "object_map": {
            "A": "c",
            "B": "c",
        },
        "fullness_cell": {
            "source_Hom_A_B_cardinality": len(source_homs["A->B"]),
            "target_Hom_UA_UB_cardinality": len(target_homs["c->c"]),
            "full": full_on_A_B,
        },
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_pass": all(checks.values()),
        "verdict": (
            "Naively forgetting source/probe semantics to the extensional controller "
            "cannot yield an equivalence under the stated non-isomorphism assumption. "
            "Either quotient the semantic distinction or represent it in the target."
        ),
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
