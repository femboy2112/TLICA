"""Invented calibration cases, not sampled communities, testimony, or lyrics."""
from __future__ import annotations

from copy import deepcopy
from typing import Any


def _case(identifier: str, description: str, parties: list[str] | None = None) -> dict[str, Any]:
    parties = parties or ["A", "B"]
    constraints = [
        {"id": "reality", "kind": "reality", "source_ids": ["stipulation"]},
        {"id": "standing", "kind": "standing", "source_ids": ["stipulation"]},
    ] + [{"id": f"floor_{p}", "kind": "party_floor", "owner": p, "source_ids": ["stipulation"]} for p in parties]
    return {"schema_version": "0.1", "kind": "synthetic", "id": identifier,
            "description": description, "parties": parties,
            "sources": [{"id": "stipulation", "family": "authored_fixture", "status": "confirmed"}],
            "constraints": constraints, "options": []}


def _option(case: dict[str, Any], identifier: str, ranks: list[int], *, fails: tuple[str, ...] = (), pending: tuple[str, ...] = (), consent: dict[str, bool | None] | None = None) -> None:
    checks = {c["id"]: True for c in case["constraints"]}
    checks.update({c: False for c in fails})
    checks.update({c: None for c in pending})
    consent_values: dict[str, bool | None] = {p: True for p in case["parties"]}
    consent_values.update(consent or {})
    case["options"].append({"id": identifier, "checks": checks, "consent": consent_values,
                            "ranks": dict(zip(case["parties"], ranks))})


def cases() -> list[dict[str, Any]]:
    workshop = _case("workshop", "A needs usable work time; B needs quiet time. Invented schedules, no real noise measurements.")
    _option(workshop, "all_evening", [5, 0], fails=("floor_B",))
    _option(workshop, "never_work", [0, 5], fails=("floor_A",))
    _option(workshop, "schedule_a", [4, 3])
    _option(workshop, "schedule_b", [3, 4])
    _option(workshop, "costly_schedule", [2, 2])
    _option(workshop, "unsafe_windfall", [100, 100], fails=("standing",))

    evidence = _case("unmeasured_insulation", "An option is promising but its claimed physical effectiveness has not been measured.")
    evidence["sources"].append({"id": "sound_test", "family": "unrun_measurement", "status": "unverified"})
    evidence["constraints"][0]["source_ids"] = ["sound_test"]
    _option(evidence, "insulation", [4, 4])

    conflict = _case("shared_map_real_conflict", "Both parties understand the same exclusive allocation; their stipulated floors still conflict.")
    _option(conflict, "allocate_a", [4, 0], fails=("floor_B",))
    _option(conflict, "allocate_b", [0, 4], fails=("floor_A",))

    withheld = _case("consent_withheld", "Modeled benefits do not substitute for permission to try an option.")
    _option(withheld, "trial", [5, 5], consent={"B": False})

    externality = _case("third_party_cost", "A and B both favor a plan, but a declared standing gate prohibits its burden on an absent affected person.")
    _option(externality, "shift_burden", [5, 5], fails=("standing",))

    music = _case("music_as_one_probe", "Shared listening versus separate headphones; invented preferences, no real artists or listeners modeled.")
    _option(music, "only_a_playlist", [4, 0], fails=("floor_B",))
    _option(music, "only_b_playlist", [0, 4], fails=("floor_A",))
    _option(music, "separate_headphones", [3, 3])

    triangle = _case("pairwise_not_global", "A accepts x/y; B accepts y/z; C accepts x/z. Each pair can agree, but all three cannot in this catalog.", ["A", "B", "C"])
    _option(triangle, "x", [3, 0, 3], fails=("floor_B",))
    _option(triangle, "y", [3, 3, 0], fails=("floor_C",))
    _option(triangle, "z", [0, 3, 3], fails=("floor_A",))

    empty = _case("no_candidate_yet", "No candidate was constructed; this is not a proof that no agreement exists.")
    return deepcopy([workshop, evidence, conflict, withheld, externality, music, triangle, empty])
