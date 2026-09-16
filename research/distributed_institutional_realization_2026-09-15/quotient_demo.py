#!/usr/bin/env python3
"""
quotient_demo.py — Probe A of the Distributed Institutional Realization v0.2 program.

Executes the institutional-macrostate *quotient* construction of the v0.2 manuscript
(Sections 5-7, Probe A in Section 18.1) as a small, deterministic, standard-library
finite model. Its single job is to make the load-bearing v0.2 formal claim CONCRETE
and CHECKABLE rather than merely asserted:

    the institutional macrostate  I^T(X) = [X]_{~_T}  is a genuine QUOTIENT of the
    micro-realization X = (P, R, D) by response-signature equivalence, strictly
    coarser than X, and the response map factors uniquely through it:

        X --q_T--> I^T --Respbar_T--> Y      with  Resp_T(X;s,u) = Respbar_T([X];s,u).

The model instantiates a tiny "who may approve request-type k" institution:

    P : indexed agents, each with a ROLE (carrier identity varies freely);
    R : typed  (role) --can-approve--> (request-type)  authority relations;
    D : an authoritative record set (here: the authority table itself).

The task family T declares:
    S_T : two situational conditions (normal / audit-mode);
    U_T : the full set of (request-type) queries;
    Y_T : {GRANT-by-<role>, DENY}.
Resp_T reads ONLY the role-typed authority relations and the situation — never the
carrier identity of any specific person. The response SIGNATURE is Resp_T over the
whole admissible (s, u) domain.

WHAT THIS DEMONSTRATES (all Disclosed inside the declared formal model):
  * two DISTINCT micro-realizations (different people, different headcount) that share
    a response signature land in the SAME class  -> carrier substitution preserves I^T;
  * cutting one load-bearing authority relation moves X to a DIFFERENT class;
  * Respbar_T is single-valued on each class and reproduces Resp_T exactly
    (Proposition 1, the factorization, verified on every (X, s, u) cell);
  * the quotient is STRICTLY coarser than identity on micro-realizations
    (more micro-realizations than classes) -> I^T carries strictly less than X;
  * APPROXIMATE equivalence within a tolerance need NOT be transitive -- exhibited by
    an explicit counterexample -- which is exactly why the manuscript refuses to write
    [X]_{~_{T,eps}} without checking (Section 6.2).

WHAT THIS IS **NOT**:
  * NOT a model of any real government, court, or firm;
  * NOT empirical evidence that useful institutional quotient macrostates exist in the
    world (that is C-006's remaining UNVERIFIED empirical debt);
  * NOT a novelty claim against distributed systems / social ontology / role theory
    (C-025 remains UNVERIFIED).
It is a finite constructive witness that the v0.2 quotient/factorization construction
is coherent and does what the manuscript says it does.

Run:  python3 quotient_demo.py [--output results.json]
Deterministic, no third-party dependencies, no randomness, no I/O beyond the optional
results file.
"""

from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import dataclass, field
from typing import Optional


# --------------------------------------------------------------------------------------
# Micro-realization  X = (P, R, D)
# --------------------------------------------------------------------------------------

@dataclass(frozen=True)
class Agent:
    """An indexed participant. `person_id` is the carrier identity; `role` is the type."""
    person_id: str
    role: str


@dataclass
class MicroRealization:
    """X_t = (P, R, D) for one declared institution, scoped to the approval task family.

    P : the indexed agents (carriers + their roles).
    R : typed authority relations, here  role -> set(request_types the role may approve),
        optionally gated on a situation label ("*" = every situation).
    D : the authoritative record set. In this toy the record IS the authority table, so
        we keep an explicit copy to show artifacts are part of the micro-realization even
        though the response reads them through R.
    """
    name: str
    P: tuple[Agent, ...]
    # R[role] = tuple of (request_type, situation_guard) the role may approve.
    R: dict[str, tuple[tuple[str, str], ...]]
    D: tuple[str, ...] = field(default=())

    def carriers(self) -> frozenset[str]:
        return frozenset(a.person_id for a in self.P)

    def roles_present(self) -> frozenset[str]:
        return frozenset(a.role for a in self.P)

    def structural_key(self) -> tuple:
        """A hashable fingerprint of the FULL micro-realization (identity level).

        Two micro-realizations with different people, headcounts, record labels, or
        authority tables get different keys. This is deliberately finer than ~_T; the
        whole point is that ~_T collapses many of these into one class.
        """
        p = tuple(sorted((a.person_id, a.role) for a in self.P))
        r = tuple(sorted((role, tuple(sorted(v))) for role, v in self.R.items()))
        return (p, r, tuple(sorted(self.D)))


# --------------------------------------------------------------------------------------
# Task family T:  S_T, U_T, Y_T, and Resp_T
# --------------------------------------------------------------------------------------

SITUATIONS: tuple[str, ...] = ("normal", "audit")          # S_T
REQUEST_TYPES: tuple[str, ...] = ("A", "B", "C")           # U_T (the interventions)


def resp_T(X: MicroRealization, situation: str, request_type: str) -> str:
    """Resp_T(X; s, u) in Y_T = {"GRANT:<role>", "DENY"}.

    Reads ONLY role-typed authority (R) and the situation. Carrier identity (person_id)
    is never consulted -- the institution's approval behavior is role-relative here BY
    CONSTRUCTION, which is exactly why the badge-door and this demo are constructive
    witnesses rather than empirical proofs of role-primacy (v0.2 Section 17).

    A request is granted iff SOME role that is (a) present among the agents and
    (b) authorized for this request-type under this situation exists. The granting role
    returned is the lexicographically-first such role, so the output is a well-defined
    function of (R, P-roles, situation), independent of carriers.
    """
    present = X.roles_present()
    granting_roles = []
    for role in present:
        for (rt, guard) in X.R.get(role, ()):  # authority the role carries
            if rt == request_type and guard in ("*", situation):
                granting_roles.append(role)
                break
    if granting_roles:
        return "GRANT:" + sorted(granting_roles)[0]
    return "DENY"


def signature(X: MicroRealization) -> tuple[tuple[tuple[str, str], str], ...]:
    """Sigma_T(X): the complete response signature over the admissible (s, u) domain.

    Returned as a sorted tuple of ((situation, request_type), response) so it is
    hashable and usable as the canonical class label q_T(X).
    """
    cells = []
    for s in SITUATIONS:
        for u in REQUEST_TYPES:
            cells.append(((s, u), resp_T(X, s, u)))
    return tuple(sorted(cells))


def q_T(X: MicroRealization) -> tuple:
    """The quotient projection  q_T : X |-> [X]_{~_T}.  The class label IS the signature."""
    return signature(X)


def equiv_T(X: MicroRealization, Y: MicroRealization) -> bool:
    """X ~_T Y  iff response signatures agree on every admissible (s, u)."""
    return signature(X) == signature(Y)


# --------------------------------------------------------------------------------------
# Respbar_T : the induced response on the QUOTIENT (Proposition 1)
# --------------------------------------------------------------------------------------

def build_respbar(micro_realizations: list[MicroRealization]) -> dict:
    """Construct Respbar_T on the quotient from a representative of each class.

    Respbar_T is defined by picking ANY representative of a class and reading its
    Resp_T. Proposition 1 says this is independent of the representative; `well_defined`
    below checks that empirically against EVERY member, not just the representative.
    """
    table: dict[tuple, dict[tuple[str, str], str]] = {}
    for X in micro_realizations:
        cls = q_T(X)
        if cls not in table:
            # cls already tabulates (s,u) -> response, since the label is the signature.
            table[cls] = {su: y for (su, y) in cls}
    return table


def respbar_T(table: dict, cls: tuple, situation: str, request_type: str) -> str:
    return table[cls][(situation, request_type)]


# --------------------------------------------------------------------------------------
# The worked institution: distinct micro-realizations, some sharing a macrostate
# --------------------------------------------------------------------------------------

# Authority table shared by the "canonical" institution: manager approves A (any time)
# and C only under audit; clerk approves B (any time). This is the record D / relations R.
AUTH_CANON: dict[str, tuple[tuple[str, str], ...]] = {
    "manager": (("A", "*"), ("C", "audit")),
    "clerk": (("B", "*"),),
}


def build_micro_realizations() -> dict[str, MicroRealization]:
    """Return the named micro-realizations used across the checks.

    X1, X2, X2p : DISTINCT micro-realizations (different carriers/headcount/record
                  labels) that share the AUTH_CANON authority-by-role -> same signature.
    X3          : X1 with the load-bearing manager->A edge CUT -> different signature.
    X4          : X1 with a *carrier permutation only* (rename people) -> same class.
    X5          : a different macrostate again (clerk also gets C in normal mode).
    """
    X1 = MicroRealization(
        name="X1",
        P=(Agent("alice", "manager"), Agent("bob", "clerk")),
        R=dict(AUTH_CANON),
        D=("charter-v1", "authtable-canon"),
    )
    # Different people, an EXTRA clerk, a different record label -> genuinely != X1,
    # but identical authority-by-role, so identical response signature.
    X2 = MicroRealization(
        name="X2",
        P=(Agent("carol", "manager"), Agent("dave", "clerk"), Agent("erin", "clerk")),
        R=dict(AUTH_CANON),
        D=("charter-v7", "authtable-canon", "annex-3"),
    )
    # Yet another distinct realization in the same class (two managers, one clerk).
    X2p = MicroRealization(
        name="X2p",
        P=(Agent("fran", "manager"), Agent("gus", "manager"), Agent("hana", "clerk")),
        R=dict(AUTH_CANON),
        D=("charter-v2",),
    )
    # Load-bearing relation destruction: same PEOPLE as X1, manager loses the A edge.
    auth_cut = {
        "manager": (("C", "audit"),),   # manager->A removed
        "clerk": (("B", "*"),),
    }
    X3 = MicroRealization(
        name="X3",
        P=(Agent("alice", "manager"), Agent("bob", "clerk")),
        R=auth_cut,
        D=("charter-v1", "authtable-cut"),
    )
    # Pure carrier permutation of X1 (rename alice->zed, bob->yara); same roles/authority.
    X4 = MicroRealization(
        name="X4",
        P=(Agent("zed", "manager"), Agent("yara", "clerk")),
        R=dict(AUTH_CANON),
        D=("charter-v1", "authtable-canon"),
    )
    # A third distinct macrostate: clerk additionally approves C in normal mode.
    auth_wide = {
        "manager": (("A", "*"), ("C", "audit")),
        "clerk": (("B", "*"), ("C", "normal")),
    }
    X5 = MicroRealization(
        name="X5",
        P=(Agent("ivy", "manager"), Agent("jon", "clerk")),
        R=auth_wide,
        D=("charter-v9",),
    )
    return {"X1": X1, "X2": X2, "X2p": X2p, "X3": X3, "X4": X4, "X5": X5}


# --------------------------------------------------------------------------------------
# Approximate-equivalence non-transitivity counterexample (Section 6.2)
# --------------------------------------------------------------------------------------

def sig_distance(a: dict, b: dict) -> int:
    """A simple response-signature distance: number of (s,u) cells where outputs differ."""
    keys = set(a) | set(b)
    return sum(1 for k in keys if a.get(k) != b.get(k))


def approx_nontransitivity_witness() -> dict:
    """Exhibit three signatures with a1 ~eps a2, a2 ~eps a3, but a1 NOT ~eps a3.

    Uses tolerance eps = 1 cell of disagreement. a1 and a3 differ in 2 cells while each
    differs from a2 in only 1, so ~_{T,eps=1} is NOT transitive: a concrete reason the
    manuscript refuses the notation [X]_{~_{T,eps}} without a transitivity check.
    """
    eps = 1
    # Three signatures over a 2-cell domain, encoded as {cell: output}.
    a1 = {"c1": "x", "c2": "x"}
    a2 = {"c1": "x", "c2": "y"}   # differs from a1 in c2 (1)
    a3 = {"c1": "z", "c2": "y"}   # differs from a2 in c1 (1); from a1 in c1,c2 (2)
    d12, d23, d13 = sig_distance(a1, a2), sig_distance(a2, a3), sig_distance(a1, a3)
    return {
        "eps": eps,
        "d(a1,a2)": d12,
        "d(a2,a3)": d23,
        "d(a1,a3)": d13,
        "a1~a2": d12 <= eps,
        "a2~a3": d23 <= eps,
        "a1~a3": d13 <= eps,
        "transitivity_holds": (d12 <= eps and d23 <= eps) <= (d13 <= eps),
    }


# --------------------------------------------------------------------------------------
# Self-checks
# --------------------------------------------------------------------------------------

def self_check(mr: dict[str, MicroRealization]) -> list[dict]:
    checks: list[dict] = []

    def record(name: str, passed: bool, detail: str) -> None:
        checks.append({"check": name, "pass": bool(passed), "detail": detail})

    X1, X2, X2p, X3, X4, X5 = (mr[k] for k in ("X1", "X2", "X2p", "X3", "X4", "X5"))
    everything = [X1, X2, X2p, X3, X4, X5]

    # 1. X1 and X2 are DISTINCT micro-realizations (different carriers/records).
    record(
        "micro_realizations_distinct",
        X1.structural_key() != X2.structural_key()
        and X1.carriers() != X2.carriers(),
        "X1 and X2 differ as micro-realizations (people, headcount, records).",
    )

    # 2. ... yet share the same response signature over the full (s,u) domain.
    record(
        "distinct_micro_same_signature",
        equiv_T(X1, X2) and equiv_T(X1, X2p),
        "Sigma_T(X1) == Sigma_T(X2) == Sigma_T(X2p) across all situations x requests.",
    )

    # 3. ... therefore they land in the SAME quotient class (carrier substitution ok).
    record(
        "same_class",
        q_T(X1) == q_T(X2) == q_T(X2p),
        "[X1]_T = [X2]_T = [X2p]_T: distinct realizations, one institutional macrostate.",
    )

    # 4. Cutting a load-bearing relation changes the signature.
    record(
        "relation_cut_changes_signature",
        not equiv_T(X1, X3),
        "Removing manager->A moves X3 out: Sigma_T(X3) != Sigma_T(X1).",
    )

    # 5. ... therefore X3 is in a DIFFERENT class than X1.
    record(
        "relation_cut_different_class",
        q_T(X3) != q_T(X1),
        "[X3]_T != [X1]_T even though X3 keeps X1's exact people.",
    )

    # 6. Pure carrier permutation preserves the class.
    record(
        "carrier_permutation_preserves_class",
        q_T(X4) == q_T(X1) and X4.carriers() != X1.carriers(),
        "Renaming every person (X4) keeps [X4]_T = [X1]_T.",
    )

    # 7. Respbar_T is single-valued on each class and reproduces Resp_T EXACTLY
    #    on every (X, s, u) cell -- Proposition 1, the factorization, executed.
    table = build_respbar(everything)
    factor_ok = True
    mismatches = 0
    for X in everything:
        cls = q_T(X)
        for s in SITUATIONS:
            for u in REQUEST_TYPES:
                if resp_T(X, s, u) != respbar_T(table, cls, s, u):
                    factor_ok = False
                    mismatches += 1
    record(
        "factorization_holds",
        factor_ok,
        "Resp_T(X;s,u) == Respbar_T(q_T(X);s,u) on all "
        f"{len(everything) * len(SITUATIONS) * len(REQUEST_TYPES)} cells "
        f"({mismatches} mismatches).",
    )

    # 8. Respbar well-definedness restated: all members of a class share the signature.
    classes: dict[tuple, list[str]] = {}
    for X in everything:
        classes.setdefault(q_T(X), []).append(X.name)
    well_defined = all(
        len({signature(mr[n]) for n in names}) == 1 for names in classes.values()
    )
    record(
        "respbar_well_defined",
        well_defined,
        "Every class's members share one signature; the induced map is single-valued.",
    )

    # 9. The quotient is STRICTLY coarser than identity: more realizations than classes.
    n_micro = len({X.structural_key() for X in everything})
    n_classes = len(classes)
    record(
        "quotient_strictly_coarser",
        n_micro > n_classes,
        f"{n_micro} distinct micro-realizations collapse to {n_classes} macrostates; "
        "I^T carries strictly less than X.",
    )

    # 10. The three macrostates are genuinely different (no accidental collapse).
    record(
        "three_distinct_macrostates",
        n_classes == 3,
        f"Exactly {n_classes} classes: {{X1,X2,X2p,X4}}, {{X3}}, {{X5}}.",
    )

    # 11. Approximate equivalence need NOT be transitive (Section 6.2 warning is real).
    w = approx_nontransitivity_witness()
    record(
        "approx_equiv_nontransitive",
        w["a1~a2"] and w["a2~a3"] and not w["a1~a3"],
        "eps=1: a1~a2 and a2~a3 but NOT a1~a3 -> tolerance relation fails transitivity.",
    )

    # 12. Carrier identity is never consulted by Resp_T (role-relative BY CONSTRUCTION).
    #     Swap only person_ids across two agents of DIFFERENT roles within X1 must not
    #     be what we test (that changes roles); instead confirm two realizations with
    #     disjoint carrier sets but equal role-authority are ~_T (already X1 vs X4/X2),
    #     and state the construction honestly.
    disjoint_same = X1.carriers().isdisjoint(X2.carriers()) and equiv_T(X1, X2)
    record(
        "response_is_carrier_blind",
        disjoint_same,
        "Disjoint carrier sets (X1 vs X2) with equal role-authority are ~_T: "
        "Resp_T reads roles+situation, never person identity (construction-level).",
    )

    return checks


# --------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Institutional-macrostate quotient demo (Probe A).")
    ap.add_argument("--output", default=None, help="write results JSON to this path")
    args = ap.parse_args()

    mr = build_micro_realizations()
    checks = self_check(mr)

    # Class map for the report.
    classes: dict[str, list[str]] = {}
    for name, X in mr.items():
        classes.setdefault(str(q_T(X)), []).append(name)
    class_report = [
        {"members": sorted(members), "signature": list(eval_sig)}
        for eval_sig, members in (
            (q_T(mr[members[0]]), members) for members in classes.values()
        )
    ]

    passed = sum(1 for c in checks if c["pass"])
    total = len(checks)

    results = {
        "demo": "distributed_institutional_realization / quotient_demo (Probe A, v0.2)",
        "situations_S_T": list(SITUATIONS),
        "request_types_U_T": list(REQUEST_TYPES),
        "micro_realizations": {
            name: {
                "carriers": sorted(X.carriers()),
                "roles": sorted(X.roles_present()),
                "signature": [[list(su), y] for (su, y) in signature(X)],
            }
            for name, X in mr.items()
        },
        "quotient_classes": class_report,
        "approx_nontransitivity_witness": approx_nontransitivity_witness(),
        "self_checks": checks,
        "self_checks_passed": passed,
        "self_checks_total": total,
        "all_passed": passed == total,
        "scope": (
            "Finite constructive witness of the v0.2 quotient/factorization construction. "
            "Disclosed inside the declared formal model. NOT empirical validation of any "
            "real institution (C-006 empirical usefulness UNVERIFIED); NOT a novelty claim "
            "(C-025 UNVERIFIED)."
        ),
    }

    print(f"quotient_demo: {passed}/{total} self-checks passed")
    for c in checks:
        mark = "ok " if c["pass"] else "FAIL"
        print(f"  [{mark}] {c['check']}: {c['detail']}")
    print()
    print("Quotient classes (distinct micro-realizations -> macrostates):")
    for cr in class_report:
        print(f"  {cr['members']}  ->  {cr['signature']}")

    if args.output:
        with open(args.output, "w") as fh:
            json.dump(results, fh, indent=2)
        print(f"\nwrote {args.output}")

    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
