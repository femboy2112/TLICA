#!/usr/bin/env python3
"""Badge-controlled door: a finite-model demonstration for distributed institutional realization.

This is the toy world described in MANUSCRIPT_SEED.md Section 14 and
PROBE_AND_PRIOR_ART_PLAN.md Section 2, actually implemented and executed.

WHAT THIS IS. A deterministic, standard-library, finite state model of a
single institutional micro-fact: "the door opens for the agent standing at
it." The model carries indexed agents, artifacts (a badge, an access-control
database, a door controller), typed relations, and source-tagged records. It
lets us *run* the baseline authority path and the ablations, and read off the
realized institutional output (does the door open?) plus a provenance verdict
and a failure class.

WHAT THIS IS NOT. It does not prove the social theory, model any real
organisation, or measure any human being. Like the sibling demos in this
repository (children_of_our_enemies/toy_models.py, geometry_of_actualization/
support_demo.py), it demonstrates a *mathematical possibility and internal
consistency* of the scaffold and its discriminators -- nothing empirical.
Every number below is a property of this ~250-line model, not of the world.

THE ONE LOAD-BEARING RESULT. The realized output (door opens) is a function of
three structural conditions -- an intact authorization RELATION, a valid
SOURCE path for the authorizing record, and an ACTIVE (non-latent, in-window)
role rule -- and is *invariant* to how strongly the agent identity-correlates
with the institution. The full 2x2x2x2 factorial exhibits this directly: the
identity-placement axis has zero main effect and zero interaction on access.
That is claim C-022 (identity-correlation dissociates from causal
participation) shown in a finite model, not asserted.

Run:  python3 badge_door_demo.py [--output results.json]
Std library only. Deterministic: no randomness, no clock, no I/O beyond the
optional JSON dump. Python 3.8+.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field, asdict
from typing import Optional


# --------------------------------------------------------------------------
# Entities. Deliberately spare -- the manuscript's Agent/Artifact/Relation/
# Event, pruned to what the badge-door fact actually needs.
# --------------------------------------------------------------------------

@dataclass
class Agent:
    id: str
    role: str                 # occupied role, e.g. "employee", "admin"
    rho_institution: float    # identity-correlation with the institution in [0,1]
    # rho is carried ONLY to show it is inert for access; nothing reads it
    # in the decision path. That inertness is the point, not an oversight.


@dataclass
class DBRecord:
    """An authorization record in the access-control database (primal not-I)."""
    subject_role: str         # the role this record authorizes
    door: str                 # which door
    written_by: str           # agent id claimed as author
    source_valid: bool        # did it arrive via a recognised-admin source path?
    valid_from: int           # inclusive time-window start
    valid_until: int          # inclusive time-window end


@dataclass
class World:
    agents: dict = field(default_factory=dict)      # id -> Agent
    records: list = field(default_factory=list)      # list[DBRecord]
    controller_online: bool = True   # is the controller<->DB path live?
    admins: frozenset = frozenset({"admin"})         # recognised authority ids


# --------------------------------------------------------------------------
# The realization + action maps, expanded into an indexed path.
# door_opens(agent) traces:  role/DB state -> credential -> controller query
#                            -> source & window check -> actuator.
# Every arrow is an ordinary lookup; no downward causation.
# --------------------------------------------------------------------------

FAIL_NONE = "access_granted"
FAIL_CARRIER_NO_RELATION = "carrier_without_relation"     # badge shell, no auth edge
FAIL_RELATION = "relation/edge_failure"                    # no authorizing record
FAIL_COMMUNICATION = "communication/path_severed"          # controller cannot reach DB
FAIL_SOURCE = "source_compromise"                          # record via invalid source path
FAIL_ACTIVATION_WINDOW = "activation/time_window"          # rule latent or out of window
FAIL_RECORD_DIVERGENCE = "record_divergence"               # conflicting authoritative records


@dataclass
class Decision:
    door_opens: bool
    provenance_valid: bool
    failure_class: str
    path: list = field(default_factory=list)   # the traced indexed path


def decide(world: World, agent_id: str, door: str, now: int,
           check_source: bool = True) -> Decision:
    """Realize the institutional micro-fact for `agent_id` at `door` at time `now`."""
    path = []
    agent = world.agents.get(agent_id)
    if agent is None:
        # A physical badge shell with no indexed agent behind its role.
        return Decision(False, False, FAIL_CARRIER_NO_RELATION, ["badge_present:no_agent"])
    path.append(f"agent:{agent_id}:role={agent.role}")

    # Controller must be able to reach the authoritative store.
    if not world.controller_online:
        return Decision(False, False, FAIL_COMMUNICATION, path + ["controller_query:UNREACHABLE"])
    path.append("controller_query:DB")

    # Find records authorizing this agent's role at this door.
    matching = [r for r in world.records
                if r.subject_role == agent.role and r.door == door]
    if not matching:
        return Decision(False, False, FAIL_RELATION, path + ["db_lookup:NO_RECORD"])

    # Record divergence: two records that disagree on the in-window verdict
    # cannot be adjudicated -> fail closed.
    in_window_flags = {(r.valid_from <= now <= r.valid_until) for r in matching}
    if len(matching) > 1 and len(in_window_flags) > 1:
        return Decision(False, False, FAIL_RECORD_DIVERGENCE,
                        path + [f"db_lookup:{len(matching)}_conflicting_records"])

    # Take the record; a valid institution requires a recognised source path.
    record = matching[0]
    provenance_valid = (record.written_by in world.admins) and record.source_valid
    if check_source and not provenance_valid:
        return Decision(False, provenance_valid, FAIL_SOURCE,
                        path + [f"source_check:INVALID(by={record.written_by},"
                                f"valid={record.source_valid})"])
    path.append(f"source_check:ok(by={record.written_by})")

    # Activation gate: the credential's role rule must be in its time window.
    if not (record.valid_from <= now <= record.valid_until):
        return Decision(False, provenance_valid, FAIL_ACTIVATION_WINDOW,
                        path + [f"window_check:OUT([{record.valid_from},"
                                f"{record.valid_until}] vs {now})"])
    path.append("window_check:in")

    # Actuator.
    return Decision(True, provenance_valid, FAIL_NONE, path + ["actuator:UNLOCK"])


# --------------------------------------------------------------------------
# A well-formed baseline institution: employee authorized by admin, in window.
# --------------------------------------------------------------------------

NOW = 100
DOOR = "lab"


def baseline_world() -> World:
    w = World()
    w.agents["employee_1"] = Agent("employee_1", role="employee", rho_institution=0.5)
    w.agents["employee_2"] = Agent("employee_2", role="employee", rho_institution=0.5)
    w.agents["admin"] = Agent("admin", role="admin", rho_institution=0.9)
    w.records.append(DBRecord(subject_role="employee", door=DOOR, written_by="admin",
                              source_valid=True, valid_from=0, valid_until=1000))
    w.controller_online = True
    return w


# --------------------------------------------------------------------------
# The eight ablations of MANUSCRIPT_SEED Section 14 / PROBE plan Section 2.2.
# Each returns (label, Decision, expectation) so the run is self-checking.
# --------------------------------------------------------------------------

def run_ablations() -> list:
    out = []

    # 0. Baseline -- the well-formed path opens.
    w = baseline_world()
    out.append(("baseline", decide(w, "employee_1", DOOR, NOW), True))

    # 1. Duplicate badge shell only: a cloned physical badge with no agent/role
    #    relation behind it.
    w = baseline_world()
    out.append(("ablate_1_badge_shell_only", decide(w, "cloned_badge", DOOR, NOW), False))

    # 2. Delete the database authorization record.
    w = baseline_world()
    w.records.clear()
    out.append(("ablate_2_delete_db_record", decide(w, "employee_1", DOOR, NOW), False))

    # 3. Keep the record, sever the controller<->DB path.
    w = baseline_world()
    w.controller_online = False
    out.append(("ablate_3_sever_network", decide(w, "employee_1", DOOR, NOW), False))

    # 4. Forge the admin update: record present but written by an unrecognised
    #    source.
    w = baseline_world()
    w.records[0].written_by = "attacker"
    w.records[0].source_valid = False
    out.append(("ablate_4_forge_source", decide(w, "employee_1", DOOR, NOW), False))

    # 5. Replace the employee with a compatible role-holder: access follows the
    #    relational state, not the physical person (C-016 substitutability).
    w = baseline_world()
    out.append(("ablate_5_substitute_role_holder", decide(w, "employee_2", DOOR, NOW), True))

    # 6. Preserve the person, delete the authorization edge for their role
    #    (P2 contrast with ablation 5).
    w = baseline_world()
    w.records.clear()
    out.append(("ablate_6_person_kept_edge_cut", decide(w, "employee_1", DOOR, NOW), False))

    # 7. Corrupt the time window: credential expired.
    w = baseline_world()
    w.records[0].valid_until = 50   # NOW=100 is now out of window
    out.append(("ablate_7_time_window_expired", decide(w, "employee_1", DOOR, NOW), False))

    # 8. Conflicting replicated records: one in-window, one not.
    w = baseline_world()
    w.records.append(DBRecord(subject_role="employee", door=DOOR, written_by="admin",
                              source_valid=True, valid_from=0, valid_until=50))
    out.append(("ablate_8_record_divergence", decide(w, "employee_1", DOOR, NOW), False))

    return out


# --------------------------------------------------------------------------
# The 2x2x2x2 factorial: relation x source x activation x identity-placement.
# The point is the identity axis: it must not move the outcome.
# --------------------------------------------------------------------------

def factorial_cell(relation_intact: bool, source_valid: bool,
                   activation_active: bool, identity_high: bool) -> Decision:
    w = World()
    rho = 0.95 if identity_high else 0.05
    w.agents["e"] = Agent("e", role="employee", rho_institution=rho)
    if relation_intact:
        # activation modelled as the credential's window covering NOW (active)
        # vs. a latent/not-yet-live rule (window in the future).
        if activation_active:
            vf, vu = 0, 1000
        else:
            vf, vu = NOW + 500, NOW + 1000   # formed but latent: not yet in window
        w.records.append(DBRecord(subject_role="employee", door=DOOR,
                                  written_by=("admin" if source_valid else "attacker"),
                                  source_valid=source_valid, valid_from=vf, valid_until=vu))
    return decide(w, "e", DOOR, NOW)


def run_factorial() -> list:
    cells = []
    for relation_intact in (True, False):
        for source_valid in (True, False):
            for activation_active in (True, False):
                for identity_high in (True, False):
                    d = factorial_cell(relation_intact, source_valid,
                                       activation_active, identity_high)
                    cells.append({
                        "relation_intact": relation_intact,
                        "source_valid": source_valid,
                        "activation_active": activation_active,
                        "identity_high": identity_high,
                        "door_opens": d.door_opens,
                        "failure_class": d.failure_class,
                    })
    return cells


def identity_invariance(cells: list) -> dict:
    """For each (relation, source, activation), the two identity levels must agree."""
    groups = {}
    for c in cells:
        key = (c["relation_intact"], c["source_valid"], c["activation_active"])
        groups.setdefault(key, []).append(c["door_opens"])
    mismatches = {str(k): v for k, v in groups.items() if len(set(v)) != 1}
    opens = [c for c in cells if c["door_opens"]]
    return {
        "identity_axis_ever_changes_outcome": bool(mismatches),
        "mismatching_conditions": mismatches,
        "cells_that_open": len(opens),
        "cells_total": len(cells),
        "all_open_cells_have_relation_source_activation_all_true": all(
            c["relation_intact"] and c["source_valid"] and c["activation_active"]
            for c in opens),
    }


# --------------------------------------------------------------------------
# Self-checks. These are the executed assertions; a failure exits nonzero.
# --------------------------------------------------------------------------

def self_check(ablations: list, cells: list, inv: dict) -> list:
    checks = []

    def record(name: str, ok: bool):
        checks.append({"check": name, "pass": bool(ok)})

    # Every ablation matched its stated expectation.
    for label, decision, expected in ablations:
        record(f"ablation:{label}:opens=={expected}", decision.door_opens == expected)

    # Substitution (5) opens while person-kept-edge-cut (6) does not: the P2
    # relation-first-over-person contrast.
    d5 = dict((l, d) for l, d, _ in ablations)["ablate_5_substitute_role_holder"]
    d6 = dict((l, d) for l, d, _ in ablations)["ablate_6_person_kept_edge_cut"]
    record("P2:substitution_opens_and_edge_cut_closes", d5.door_opens and not d6.door_opens)

    # Forgery fails specifically on provenance, not on some other class.
    d4 = dict((l, d) for l, d, _ in ablations)["ablate_4_forge_source"]
    record("source:forge_fails_as_source_compromise",
           (not d4.door_opens) and d4.failure_class == FAIL_SOURCE and not d4.provenance_valid)

    # The load-bearing one: identity never moves the outcome.
    record("C-022:identity_axis_inert", not inv["identity_axis_ever_changes_outcome"])
    record("factorial:only_relation_source_activation_open_cells",
           inv["all_open_cells_have_relation_source_activation_all_true"])
    record("factorial:exactly_two_cells_open", inv["cells_that_open"] == 2)

    return checks


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", default=None, help="write results JSON to this path")
    args = ap.parse_args()

    ablations = run_ablations()
    cells = run_factorial()
    inv = identity_invariance(cells)
    checks = self_check(ablations, cells, inv)

    results = {
        "model": "badge-controlled door (finite, deterministic, std-lib only)",
        "scope": ("finite-model demonstration of internal consistency and "
                  "discriminators; NOT empirical validation of the social theory "
                  "and NOT a model of any real organisation or person"),
        "baseline_and_ablations": [
            {"label": label, "door_opens": d.door_opens,
             "provenance_valid": d.provenance_valid, "failure_class": d.failure_class,
             "expected_open": expected, "path": d.path}
            for label, d, expected in ablations
        ],
        "factorial_2x2x2x2": cells,
        "identity_invariance": inv,
        "self_checks": checks,
        "all_checks_pass": all(c["pass"] for c in checks),
        "num_checks": len(checks),
    }

    # Human-readable summary to stdout (captured into the tests file).
    print(f"badge-door demo: {len(ablations)} baseline/ablation traces, "
          f"{len(cells)}-cell factorial, {len(checks)} self-checks")
    for label, d, expected in ablations:
        mark = "OPEN " if d.door_opens else "shut "
        print(f"  {mark} {label:32s} [{d.failure_class}]")
    print(f"identity axis ever changes outcome: "
          f"{inv['identity_axis_ever_changes_outcome']}  "
          f"(cells open: {inv['cells_that_open']}/{inv['cells_total']})")
    for c in checks:
        print(f"  [{'PASS' if c['pass'] else 'FAIL'}] {c['check']}")
    print(f"ALL CHECKS PASS: {results['all_checks_pass']} ({results['num_checks']} checks)")

    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            json.dump(results, fh, indent=2, sort_keys=False)
        print(f"wrote {args.output}")

    return 0 if results["all_checks_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
