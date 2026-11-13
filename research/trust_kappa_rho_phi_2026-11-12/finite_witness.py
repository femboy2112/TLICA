#!/usr/bin/env python3
"""Exact finite witnesses for FORMALISM_AND_PROBES.md; Python standard library.

These fixtures are designed mechanisms, not measurements of human psychology.
No float, probability estimate of truth, or numerical infinitesimal is used.
The phi signatures are declared evaluation fixtures, never fitted to accuracy.
The program writes only to stdout/stderr and exits nonzero on a failed check.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass, is_dataclass
from fractions import Fraction
from itertools import product
import json
from typing import Callable, Hashable, Iterable


@dataclass(frozen=True)
class PhiSignature:
    """A symbolic Tier-3 status/value descriptor, with delta left formal."""

    pathway_constructible: bool
    conditional_depth: int | None = None
    empirical_deficit: Fraction | None = None

    def __post_init__(self) -> None:
        if not self.pathway_constructible:
            if self.conditional_depth is not None or self.empirical_deficit is not None:
                raise ValueError("Undefined phi has neither depth nor deficit.")
        elif (
            self.conditional_depth is None
            or self.conditional_depth < 1
            or self.empirical_deficit is None
            or not Fraction(0) <= self.empirical_deficit < Fraction(1)
        ):
            raise ValueError("The declared fixture requires finite depth and deficit < 1.")

    def expression(self) -> str:
        if not self.pathway_constructible:
            return "undefined"
        return f"1 - {self.conditional_depth}*delta - {self.empirical_deficit}"


def fibre_collisions(
    states: Iterable[Hashable],
    representation: Callable[[Hashable], Hashable],
    target: Callable[[Hashable], Hashable],
) -> list[dict]:
    """Return witnesses that a target does not factor through a representation."""
    buckets: dict[Hashable, list[Hashable]] = {}
    collisions = []
    for state in states:
        key = representation(state)
        for earlier in buckets.get(key, []):
            if target(earlier) != target(state):
                collisions.append({"left": earlier, "right": state, "representation": key})
        buckets.setdefault(key, []).append(state)
    return collisions


def static_factorization_fixture(checks: dict[str, bool]) -> dict:
    # A single-mode flow of capacity 1 would give the shared rho projection 1/2.
    # Current contact and that projection do not encode the tool/probe inputs.
    records = {
        "no_pathway": {"contact": 1, "rho_projection": Fraction(1, 2), "depth": None, "scores": ()},
        "pathway_pass": {"contact": 1, "rho_projection": Fraction(1, 2), "depth": 2, "scores": (Fraction(1), Fraction(1))},
        "pathway_mixed": {"contact": 1, "rho_projection": Fraction(1, 2), "depth": 2, "scores": (Fraction(1), Fraction(1, 2))},
        "same_evaluation_new_history": {"contact": 1, "rho_projection": Fraction(1, 2), "depth": 2, "scores": (Fraction(1), Fraction(1))},
    }

    def target(key: str) -> PhiSignature:
        row = records[key]
        if row["depth"] is None:
            return PhiSignature(False)
        deficit = sum((1 - q for q in row["scores"]), Fraction()) / len(row["scores"])
        return PhiSignature(True, row["depth"], deficit)

    def lossy(key: str) -> tuple:
        row = records[key]
        return row["contact"], row["rho_projection"]

    def evaluation_inputs(key: str) -> tuple:
        row = records[key]
        return row["depth"], row["scores"]

    bad = fibre_collisions(records, lossy, target)
    good = fibre_collisions(records, evaluation_inputs, target)
    checks["TF-1.lossy_readouts_have_collision"] = bool(bad)
    checks["TF-1.declared_evaluation_inputs_suffice"] = not good
    checks["TF-1.null_constant_target_factors"] = not fibre_collisions(records, lossy, lambda _: "constant")
    checks["TF-1.mutation_erasing_probe_scores_detected"] = bool(
        fibre_collisions(records, lambda key: records[key]["depth"], target)
    )
    return {
        "claim": "TF-1",
        "scope": "Synthetic symbolic evaluation inputs; delta remains a formal symbol.",
        "records": [dict(history=key, **row, signature=target(key), expression=target(key).expression()) for key, row in records.items()],
        "lossy_projection_collisions": bad,
        "evaluation_input_collisions": good,
        "constructible_is_not_executed": "The declared signatures do not certify an executed real-world verification.",
    }


def dynamic_closure_fixture(checks: dict[str, bool]) -> dict:
    domain = tuple(product((0, 1), repeat=2))
    states = ((0, 0), (1, 0))  # Two initial histories: (hidden bit, revealed flag).

    def representation(state: tuple[int, int]) -> int:
        hidden, revealed = state
        return hidden if revealed else 0

    def step(state: tuple[int, int], action: str) -> tuple[int, int]:
        return (state[0], 1) if action == "reveal" else state

    current = fibre_collisions(states, representation, representation)
    next_collision = fibre_collisions(states, representation, lambda state: representation(step(state, "reveal")))
    repaired = fibre_collisions(states, lambda state: state, lambda state: step(state, "reveal"))
    idle = fibre_collisions(states, representation, lambda state: representation(step(state, "idle")))
    checks["TF-2.declared_domain_closed_under_actions"] = all(
        step(state, action) in domain for state in domain for action in ("reveal", "idle")
    )
    checks["TF-2.present_readout_factors"] = not current
    checks["TF-2.same_action_successor_collision_detected"] = bool(next_collision)
    checks["TF-2.retaining_hidden_state_repairs_this_fixture"] = not repaired
    checks["TF-2.null_idle_has_no_collision"] = not idle
    return {
        "claim": "TF-2",
        "declared_closed_domain": domain,
        "states": states,
        "current_readouts": [representation(state) for state in states],
        "action": "reveal",
        "next_readouts": [representation(step(state, "reveal")) for state in states],
        "successor_collisions": next_collision,
        "scope": "Two initial histories in a four-state closed domain refute static sufficiency implying transition closure.",
    }


WORLDS = tuple(product((0, 1), repeat=2))
ACTUAL = (0, 0)


def observe(world: tuple[int, int], probe: str, duplicate_second: bool = False) -> int:
    if probe == "context_0":
        return world[0]
    if probe == "context_1":
        return world[0] if duplicate_second else world[1]
    if probe == "constant":
        return 0
    raise ValueError(f"Unknown probe: {probe}")


def survivors(events: Iterable[tuple[str, int]], duplicate_second: bool = False) -> tuple:
    events = tuple(events)
    return tuple(world for world in WORLDS if all(observe(world, probe, duplicate_second) == value for probe, value in events))


def pair_count(states: Iterable) -> int:
    size = len(tuple(states))
    return size * (size - 1) // 2


def duplicate_fixture(checks: dict[str, bool]) -> dict:
    first = (("context_0", 0),)
    repeated = first * 32
    base = survivors(first)
    repeats = survivors(repeated)
    fresh = survivors(first + (("context_1", 0),))
    null = survivors((("constant", 0),))
    corrupted = survivors(first + (("context_0", 1),))
    checks["TF-3.identical_deterministic_constraints_idempotent"] = base == repeats
    checks["TF-3.positive_fresh_context_discriminates"] = len(fresh) < len(base)
    checks["TF-3.null_constant_probe_does_not_discriminate"] = null == WORLDS
    checks["TF-3.mutation_inconsistent_duplicate_is_detected"] = not corrupted
    return {
        "claim": "TF-3",
        "candidate_worlds": WORLDS,
        "first_events": first,
        "repeat_count": 32,
        "survivors_first": base,
        "survivors_repeated": repeats,
        "fresh_context_event": ("context_1", 0),
        "survivors_fresh_context": fresh,
        "corrupted_duplicate_survivors": corrupted,
        "scope": "Repeated identical deterministic constraint, not fresh noisy measurements or learner development.",
    }


def accuracy(rows: Iterable[dict], predictor: Callable[[dict], int]) -> Fraction:
    rows = tuple(rows)
    if not rows:
        raise ValueError("Accuracy is undefined on an empty evaluation set.")
    return Fraction(sum(predictor(row) == row["actual_persistence"] for row in rows), len(rows))


def require_disjoint(selected: Iterable[dict], heldout: Iterable[dict]) -> None:
    if {row["id"] for row in selected} & {row["id"] for row in heldout}:
        raise ValueError("Heldout items overlap the selected observation set.")


def selected_observation_fixture(checks: dict[str, bool]) -> dict:
    rows = [
        {
            "id": index,
            "context": "familiar" if index < 2 else "changed",
            "signal_prediction": 1,
            "actual_persistence": int(index < 2),
        }
        for index in range(8)
    ]
    selected = rows[:2]
    heldout = rows[2:]
    require_disjoint(selected, heldout)
    signal = lambda row: row["signal_prediction"]
    selected_rate = accuracy(selected, signal)
    heldout_rate = accuracy(heldout, signal)
    population_rate = accuracy(rows, signal)
    truthful = lambda row: row["actual_persistence"]
    reversed_truth = lambda row: 1 - row["actual_persistence"]
    null_rows = [dict(row, actual_persistence=1) for row in rows]
    leaked_holdout_detected = False
    try:
        require_disjoint(selected, selected)
    except ValueError:
        leaked_holdout_detected = True
    inverted_signal = lambda row: 1 - row["signal_prediction"]
    checks["TW-1.selected_success_is_one"] = selected_rate == 1
    checks["TW-1.holdout_success_is_zero"] = heldout_rate == 0
    checks["TW-1.full_population_success_is_one_quarter"] = population_rate == Fraction(1, 4)
    checks["TW-1.positive_truthful_predictor_passes_everywhere"] = accuracy(rows, truthful) == 1
    checks["TW-1.negative_reversed_predictor_fails_everywhere"] = accuracy(rows, reversed_truth) == 0
    checks["TW-1.null_context_invariant_population_has_no_gap"] = accuracy(null_rows[:2], signal) == accuracy(null_rows[2:], signal)
    checks["TW-1.mutation_holdout_leakage_detected"] = leaked_holdout_detected
    checks["TW-1.mutation_signal_inversion_reverses_gap"] = accuracy(selected, inverted_signal) - accuracy(heldout, inverted_signal) == -1
    return {
        "claim": "TW-1",
        "all_events": rows,
        "policy": "Observe familiar contexts only.",
        "selected_ids": [row["id"] for row in selected],
        "external_holdout_ids": [row["id"] for row in heldout],
        "selected_success_fraction": selected_rate,
        "external_holdout_success_fraction": heldout_rate,
        "specified_population_success_fraction": population_rate,
        "selected_minus_holdout": selected_rate - heldout_rate,
        "holdout_leakage_mutation_detected": leaked_holdout_detected,
        "scope": "Externally selected disjoint holdout; no IID sampling or human-psychology claim. Fractions are accuracy, never phi.",
    }


def factorial_cells(duplicate_second: bool = False, remove_selection_dependence: bool = False) -> list[dict]:
    initial_events = (("context_0", observe(ACTUAL, "context_0")),)
    initial = survivors(initial_events, duplicate_second)
    cells = []
    for access, integrated_selection in product((0, 1), repeat=2):
        available = ("context_0", "context_1") if access else ("context_0",)
        choose_novel = bool(access and (integrated_selection or remove_selection_dependence))
        selected = "context_1" if choose_novel else "context_0"
        if selected not in available:
            raise ValueError("Policy attempted an inaccessible observation.")
        value = observe(ACTUAL, selected, duplicate_second)
        after = survivors(initial_events + ((selected, value),), duplicate_second)
        cells.append({
            "contact_access": access,
            "integrated_selection": integrated_selection,
            "available_probes": available,
            "selected_probe": selected,
            "observed_value": value,
            "survivors_before": initial,
            "survivors_after": after,
            "unresolved_pairs_before": pair_count(initial),
            "unresolved_pairs_after": pair_count(after),
            "discrimination_gain": pair_count(initial) - pair_count(after),
        })
    return cells


def interaction(cells: Iterable[dict]) -> int:
    cells = tuple(cells)
    by_cell = {(row["contact_access"], row["integrated_selection"]): row["discrimination_gain"] for row in cells}
    if len(cells) != 4 or set(by_cell) != set(product((0, 1), repeat=2)):
        raise ValueError("A factorial contrast requires all four distinct cells.")
    return by_cell[(1, 1)] - by_cell[(1, 0)] - by_cell[(0, 1)] + by_cell[(0, 0)]


def factorial_fixture(checks: dict[str, bool]) -> dict:
    baseline = factorial_cells()
    null = factorial_cells(duplicate_second=True)
    mutation = factorial_cells(remove_selection_dependence=True)
    missing_cell_detected = False
    try:
        interaction(baseline[:3])
    except ValueError:
        missing_cell_detected = True
    checks["TW-2.all_four_baseline_cells_present"] = len(baseline) == 4
    checks["TW-2.complete_factorial_interaction_is_one"] = interaction(baseline) == 1
    checks["TW-2.null_duplicate_probe_abolishes_gain"] = all(row["discrimination_gain"] == 0 for row in null)
    checks["TW-2.mutation_removing_selection_dependence_abolishes_interaction"] = interaction(mutation) == 0
    checks["TW-2.mutation_missing_factorial_cell_detected"] = missing_cell_detected
    return {
        "claim": "TW-2",
        "baseline_all_four_cells": baseline,
        "baseline_interaction": interaction(baseline),
        "null_duplicate_probe_all_four_cells": null,
        "null_interaction": interaction(null),
        "mutation_policy_ignores_integration_all_four_cells": mutation,
        "mutation_interaction": interaction(mutation),
        "missing_cell_mutation_detected": missing_cell_detected,
        "scope": "Engineered contact access and specified model-linked selection rule, not measured kappa/rho or a universal product law; no learning is simulated.",
    }


def json_default(value):
    if isinstance(value, Fraction):
        return {"numerator": value.numerator, "denominator": value.denominator}
    if is_dataclass(value):
        return asdict(value)
    raise TypeError(f"Cannot encode {type(value).__name__}")


def build_report() -> dict:
    checks: dict[str, bool] = {}
    witnesses = [
        static_factorization_fixture(checks),
        dynamic_closure_fixture(checks),
        duplicate_fixture(checks),
        selected_observation_fixture(checks),
        factorial_fixture(checks),
    ]
    return {
        "schema": "tlica-trust-finite-witness-v1",
        "scope": "Exact finite construction; no empirical validation, no numeric delta, no estimated human phi.",
        "witnesses": witnesses,
        "checks": checks,
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "all_passed": all(checks.values()),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Print the full raw exact report as JSON.")
    args = parser.parse_args()
    report = build_report()
    if args.json:
        print(json.dumps(report, default=json_default, indent=2, sort_keys=True))
    else:
        print(report["scope"])
        for name, passed in report["checks"].items():
            print(f"{'PASS' if passed else 'FAIL'} {name}")
        print(f"{report['checks_passed']}/{report['checks_total']} checks passed")
    return 0 if report["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
