#!/usr/bin/env python3
"""
Finite reparametrisation bridge for Semantic Optics.

This construction targets the exact theorem fork exposed by the Yoneda work.

Source semantic reparametrisations:
    Two independent updates are tracked with acquisition order.
    H = {N, S, P, SP, PS}
    s = acquire/resolve source information
    p = acquire/open a discriminating probe
    SP and PS remain distinct historical states.

Coarse categorical-cybernetic parameterisation:
    Forget acquisition order.
    Q = {N, S, P, B}
    where B means both capacities are present.
    The induced source/probe update functions commute extensionally.

The bridge q from history-sensitive reparametrisations to coarse
reparametrisations is checked exhaustively as a monoid homomorphism (equivalently
a functor between one-object categories).

Results establish, in this finite fixture:
  * q is full/surjective on morphisms and bijective on objects;
  * q is not faithful because p∘s and s∘p remain distinct upstairs but collapse;
  * quotienting the source by exactly that kernel congruence yields a monoid
    isomorphic to the coarse target;
  * retaining history in the target yields a faithful concrete representation;
  * the regular Yoneda representation separates all source morphisms;
  * a coarse controller cannot see update order, while one added history-sensitive
    probe ("lamp") can.

This is a construction-level witness only. It does not establish that TLICA
must treat source/probe acquisition order as semantically real in humans.
"""

from __future__ import annotations

from itertools import product
from typing import Dict, Iterable, Tuple
import argparse
import json


Transformation = Tuple[str, ...]


def compose(f: Transformation, g: Transformation, states: Tuple[str, ...]) -> Transformation:
    """Return f ∘ g."""
    idx = {x: i for i, x in enumerate(states)}
    return tuple(f[idx[y]] for y in g)


def closure(states: Tuple[str, ...], generators: Iterable[Transformation]) -> set[Transformation]:
    elems = {tuple(states), *generators}
    changed = True
    while changed:
        changed = False
        current = list(elems)
        for f in current:
            for g in current:
                h = compose(f, g, states)
                if h not in elems:
                    elems.add(h)
                    changed = True
    return elems


def apply(f: Transformation, states: Tuple[str, ...], x: str) -> str:
    return f[states.index(x)]


H = ("N", "S", "P", "SP", "PS")
Q = ("N", "S", "P", "B")

# Independent semantic specification: preserve which capacity arrived first.
S_H: Transformation = ("S", "S", "PS", "SP", "PS")
P_H: Transformation = ("P", "SP", "P", "SP", "PS")

# Independent coarse specification: retain capacities but forget acquisition order.
S_Q: Transformation = ("S", "S", "B", "B")
P_Q: Transformation = ("P", "B", "P", "B")

ID_H = tuple(H)
ID_Q = tuple(Q)

H_MONOID = closure(H, (S_H, P_H))
Q_MONOID = closure(Q, (S_Q, P_Q))

H_NAMED: Dict[str, Transformation] = {
    "id": ID_H,
    "s": S_H,
    "p": P_H,
    "p_after_s": compose(P_H, S_H, H),
    "s_after_p": compose(S_H, P_H, H),
}
Q_NAMED: Dict[str, Transformation] = {
    "id": ID_Q,
    "s": S_Q,
    "p": P_Q,
    "both": compose(P_Q, S_Q, Q),
}

assert set(H_NAMED.values()) == H_MONOID
assert set(Q_NAMED.values()) == Q_MONOID

H_INV = {v: k for k, v in H_NAMED.items()}
Q_INV = {v: k for k, v in Q_NAMED.items()}

PI = {
    "N": "N",
    "S": "S",
    "P": "P",
    "SP": "B",
    "PS": "B",
}

QMAP = {
    "id": "id",
    "s": "s",
    "p": "p",
    "p_after_s": "both",
    "s_after_p": "both",
}


def h_comp(a: str, b: str) -> str:
    """Named a ∘ b."""
    return H_INV[compose(H_NAMED[a], H_NAMED[b], H)]


def q_comp(a: str, b: str) -> str:
    """Named a ∘ b."""
    return Q_INV[compose(Q_NAMED[a], Q_NAMED[b], Q)]


def semiconjugacy_holds(h_name: str) -> bool:
    fh = H_NAMED[h_name]
    fq = Q_NAMED[QMAP[h_name]]
    lhs = tuple(PI[apply(fh, H, x)] for x in H)
    rhs = tuple(apply(fq, Q, PI[x]) for x in H)
    return lhs == rhs


def regular_yoneda_signature(m_name: str) -> Tuple[str, ...]:
    """
    One-object Yoneda/Cayley signature:
        y(m): h |-> m ∘ h
    recorded on every source morphism h.
    """
    order = tuple(H_NAMED)
    return tuple(h_comp(m_name, h) for h in order)


def coarse_action_signature(m_name: str) -> Transformation:
    """Restricted/coarse parameter action after forgetting history."""
    return Q_NAMED[QMAP[m_name]]


EVIDENCE_COARSE = ("ambiguous", "clear")

COARSE_CONTROLLER = {
    ("N", "ambiguous"): "guess",
    ("S", "ambiguous"): "source_only",
    ("P", "ambiguous"): "probe",
    ("B", "ambiguous"): "verify",
    ("N", "clear"): "accept",
    ("S", "clear"): "accept",
    ("P", "clear"): "accept",
    ("B", "clear"): "accept",
}


def induced_coarse_controller_signature(m_name: str) -> Tuple[Tuple[str, str, str], ...]:
    """
    Apply a history-sensitive reparametrisation, forget history, then run the same
    coarse controller. This is the operational quotient seen by a coarse arena.
    """
    f = H_NAMED[m_name]
    out = []
    for h in H:
        h2 = apply(f, H, h)
        q = PI[h2]
        for e in EVIDENCE_COARSE:
            out.append((h, e, COARSE_CONTROLLER[(q, e)]))
    return tuple(out)


def order_lamp(state: str) -> str:
    if state == "SP":
        return "source-first"
    if state == "PS":
        return "probe-first"
    return "order-unresolved"


def induced_lamp_signature(m_name: str) -> Tuple[Tuple[str, str], ...]:
    f = H_NAMED[m_name]
    return tuple((h, order_lamp(apply(f, H, h))) for h in H)


def quotient_classes() -> Dict[str, Tuple[str, ...]]:
    groups: Dict[str, list[str]] = {}
    for h_name, q_name in QMAP.items():
        groups.setdefault(q_name, []).append(h_name)
    return {k: tuple(sorted(v)) for k, v in groups.items()}


def run() -> dict:
    h_names = tuple(H_NAMED)
    q_names = tuple(Q_NAMED)

    homomorphism_cells = []
    homomorphism_ok = True
    for a, b in product(h_names, repeat=2):
        lhs = QMAP[h_comp(a, b)]
        rhs = q_comp(QMAP[a], QMAP[b])
        ok = lhs == rhs
        homomorphism_cells.append({
            "a": a,
            "b": b,
            "q(a_after_b)": lhs,
            "qa_after_qb": rhs,
            "ok": ok,
        })
        homomorphism_ok &= ok

    semiconjugacy = {name: semiconjugacy_holds(name) for name in h_names}

    classes = quotient_classes()
    quotient_well_defined = homomorphism_ok
    quotient_iso_bijection = set(classes) == set(q_names) and len(classes) == len(q_names)

    yoneda = {name: regular_yoneda_signature(name) for name in h_names}
    yoneda_faithful = len(set(yoneda.values())) == len(h_names)

    coarse_actions = {name: coarse_action_signature(name) for name in h_names}
    coarse_collapses_order = (
        coarse_actions["p_after_s"] == coarse_actions["s_after_p"]
    )

    coarse_controller = {
        name: induced_coarse_controller_signature(name) for name in h_names
    }
    coarse_controller_collapses_order = (
        coarse_controller["p_after_s"] == coarse_controller["s_after_p"]
    )

    lamp = {name: induced_lamp_signature(name) for name in h_names}
    lamp_splits_order = lamp["p_after_s"] != lamp["s_after_p"]

    history_target_faithful = len(set(H_NAMED.values())) == len(h_names)
    history_target_full = set(H_NAMED.values()) == H_MONOID
    history_target_essentially_surjective = True  # one-object categories
    history_target_equivalence = (
        history_target_faithful
        and history_target_full
        and history_target_essentially_surjective
    )

    coarse_full = set(QMAP.values()) == set(q_names)
    coarse_faithful = len(set(QMAP.values())) == len(h_names)
    coarse_essentially_surjective = True  # one-object categories
    coarse_equivalence = coarse_full and coarse_faithful and coarse_essentially_surjective

    checks = {
        "history_monoid_has_5_morphisms": len(H_MONOID) == 5,
        "coarse_monoid_has_4_morphisms": len(Q_MONOID) == 4,
        "forget_map_semiconjugates_all_generators_and_composites": all(semiconjugacy.values()),
        "forget_map_is_monoid_homomorphism_all_25_cells": homomorphism_ok and len(homomorphism_cells) == 25,
        "coarse_functor_full_surjective_on_morphisms": coarse_full,
        "coarse_functor_not_faithful": not coarse_faithful,
        "coarse_functor_not_equivalence": not coarse_equivalence,
        "kernel_has_exactly_one_nontrivial_collision": classes["both"] == ("p_after_s", "s_after_p"),
        "kernel_quotient_isomorphic_to_coarse_target": quotient_well_defined and quotient_iso_bijection,
        "history_enriched_target_full": history_target_full,
        "history_enriched_target_faithful": history_target_faithful,
        "history_enriched_target_equivalence": history_target_equivalence,
        "regular_yoneda_representation_faithful": yoneda_faithful,
        "coarse_parameter_action_collapses_update_order": coarse_collapses_order,
        "coarse_controller_collapses_update_order": coarse_controller_collapses_order,
        "one_history_sensitive_lamp_splits_update_order": lamp_splits_order,
        "full_yoneda_splits_the_coarse_collision": yoneda["p_after_s"] != yoneda["s_after_p"],
    }

    return {
        "scope": "finite one-object categories / reparametrisation monoids; construction-level only",
        "source_semantics": {
            "parameter_states": H,
            "morphisms": h_names,
            "meaning": "source/probe acquisition order retained",
        },
        "coarse_target": {
            "parameter_states": Q,
            "morphisms": q_names,
            "meaning": "same capacities, acquisition order forgotten",
        },
        "forgetful_functor": {
            "object_map": "* -> *",
            "morphism_map": QMAP,
            "full": coarse_full,
            "faithful": coarse_faithful,
            "essentially_surjective": coarse_essentially_surjective,
            "equivalence": coarse_equivalence,
            "kernel_classes": classes,
        },
        "history_enriched_target": {
            "full": history_target_full,
            "faithful": history_target_faithful,
            "essentially_surjective": history_target_essentially_surjective,
            "equivalence": history_target_equivalence,
        },
        "semiconjugacy": semiconjugacy,
        "homomorphism_cells": homomorphism_cells,
        "regular_yoneda_signatures": {k: list(v) for k, v in yoneda.items()},
        "coarse_order_pair": {
            "p_after_s_action": list(coarse_actions["p_after_s"]),
            "s_after_p_action": list(coarse_actions["s_after_p"]),
            "equal": coarse_collapses_order,
        },
        "coarse_controller_order_pair": {
            "equal": coarse_controller_collapses_order,
        },
        "history_lamp_order_pair": {
            "p_after_s": list(lamp["p_after_s"]),
            "s_after_p": list(lamp["s_after_p"]),
            "different": lamp_splits_order,
        },
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_pass": all(checks.values()),
        "verdict": (
            "The coarse reparametrisation target is the exact extensional quotient of "
            "the history-sensitive semantic monoid by the single collision "
            "p_after_s ~ s_after_p. It is full but not faithful, hence not equivalent. "
            "Retaining update history in the target restores a full, faithful, "
            "essentially-surjective concrete representation. Full Yoneda sees the "
            "distinction; the coarse arena does not until a history-sensitive lamp is added."
        ),
    }


def main() -> None:
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
