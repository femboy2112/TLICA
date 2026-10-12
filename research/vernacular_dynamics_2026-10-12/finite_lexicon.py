"""Finite calibration for observer-relative vernacular labels.

All examples are INVENTED. No psychological inference is made about anyone.
No probabilities or empirical measurements are represented here.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Mapping


@dataclass(frozen=True)
class Rival:
    name: str
    predictions: Mapping[str, str | None]


def survivors(rivals: tuple[Rival, ...], evidence: Mapping[str, str]) -> tuple[Rival, ...]:
    """Keep predictions compatible with observations; None means unresolved."""
    return tuple(r for r in rivals if all(
        r.predictions.get(probe) in (None, observed)
        for probe, observed in evidence.items()
    ))


def split_count(rivals: tuple[Rival, ...], probe: str) -> tuple[int, int]:
    """Pair counts (distinguished, unresolved); missing predictions never split."""
    distinguished = 0
    unresolved = 0
    for a, b in combinations(rivals, 2):
        pa, pb = a.predictions.get(probe), b.predictions.get(probe)
        if pa is not None and pb is not None and pa != pb:
            distinguished += 1
        else:
            unresolved += 1
    return distinguished, unresolved


def exact_classes(rivals: tuple[Rival, ...], probes: tuple[str, ...]) -> tuple[tuple[str, ...], ...]:
    """Operational quotient only on complete predicted observations."""
    classes: dict[tuple[str, ...], list[str]] = {}
    for r in rivals:
        signature = tuple(r.predictions.get(p) for p in probes)
        if any(value is None for value in signature):
            raise ValueError("cannot identify an observational equivalence class from unknown predictions")
        classes.setdefault(signature, []).append(r.name)
    return tuple(tuple(names) for names in classes.values())


def synthetic_cases() -> dict[str, tuple[Rival, ...]]:
    return {
        "vibe": (
            Rival("mutual_rapport", {
                "surface_label": "good_vibe", "independent_report": "reciprocal"}),
            Rival("polite_masking", {
                "surface_label": "good_vibe", "independent_report": "not_reciprocal"}),
        ),
        "cope": (
            Rival("adaptive_coping", {
                "surface_token": "cope", "speech_role": "self_description",
                "credible_counterevidence": "revises_belief"}),
            Rival("defensive_reinterpretation", {
                "surface_token": "cope", "speech_role": "self_description",
                "credible_counterevidence": "protects_belief"}),
            Rival("dismissive_retort", {
                "surface_token": "cope", "speech_role": "accusation",
                "credible_counterevidence": None}),
        ),
        "lost_in_sauce": (
            Rival("absorbed_and_oriented", {
                "surface_label": "lost_in_sauce", "high_immersion": "yes",
                "checkpoint": "goal_recovered"}),
            Rival("absorbed_and_disoriented", {
                "surface_label": "lost_in_sauce", "high_immersion": "yes",
                "checkpoint": "goal_missed"}),
        ),
    }


def example_summary() -> dict[str, dict[str, object]]:
    cases = synthetic_cases()
    discriminators = {
        "vibe": "independent_report",
        "cope": "speech_role",
        "lost_in_sauce": "checkpoint",
    }
    return {
        term: {
            "candidate_count_from_token": len(survivors(candidates, {
                "surface_token" if term == "cope" else "surface_label":
                "cope" if term == "cope" else "good_vibe" if term == "vibe" else "lost_in_sauce"
            })),
            "probe": discriminators[term],
            "split_and_unresolved_pairs": split_count(candidates, discriminators[term]),
        }
        for term, candidates in cases.items()
    }


if __name__ == "__main__":
    import json
    print(json.dumps(example_summary(), indent=2))
