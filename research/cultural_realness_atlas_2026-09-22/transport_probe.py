#!/usr/bin/env python3
"""Validate declared partial transports of annotated facts; never infer culture.

Python 3.10+, standard library. No training, lyric parsing, or listener model.
Run without --input for synthetic calibration; see PROTOCOL_AND_ROADMAP.md.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
import platform
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

VERSION = "0.1.0"
BASE_COMMIT = "471c28566dbf08b54bbc64d2c83089806a772e9f"
Fact = tuple[str, str, str, int]


def text(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a nonempty string")
    return value


def keys(value: Any, expected: set[str], name: str) -> None:
    if not isinstance(value, dict) or set(value) != expected:
        raise ValueError(f"{name} requires exactly {sorted(expected)}")


@dataclass(frozen=True)
class Episode:
    identifier: str
    basis: str
    provenance: str
    nodes: Mapping[str, tuple[str, str]]  # id -> (kind, surface label)
    facts: tuple[Fact, ...]

    @classmethod
    def parse(cls, raw: Any) -> Episode:
        keys(raw, {"id", "basis", "provenance", "nodes", "facts"}, "episode")
        identifier = text(raw["id"], "id")
        basis = text(raw["basis"], "basis")
        provenance = text(raw["provenance"], "provenance")
        if not isinstance(raw["nodes"], list) or not isinstance(raw["facts"], list):
            raise ValueError("nodes and facts must be arrays")
        nodes: dict[str, tuple[str, str]] = {}
        for node in raw["nodes"]:
            keys(node, {"id", "kind", "label"}, "node")
            identifier_node = text(node["id"], "node id")
            if identifier_node in nodes:
                raise ValueError("duplicate node id")
            nodes[identifier_node] = (text(node["kind"], "kind"), text(node["label"], "label"))
        facts: list[Fact] = []
        seen: set[tuple[str, str, str]] = set()
        for row in raw["facts"]:
            if not isinstance(row, list) or len(row) != 4:
                raise ValueError("a fact is [source, relation, target, polarity]")
            u, relation, v = (text(row[i], "fact term") for i in range(3))
            polarity = row[3]
            if type(polarity) is not int or polarity not in (-1, 1):
                raise ValueError("polarity must be integer -1 or +1, not a boolean")
            if u not in nodes or v not in nodes:
                raise ValueError("dangling fact endpoint")
            key = (u, relation, v)
            if key in seen:
                raise ValueError("duplicate or conflicting fact; split disputed annotations into alternatives")
            seen.add(key)
            facts.append((u, relation, v, polarity))
        return cls(identifier, basis, provenance, nodes, tuple(facts))


def assess(source: Episode, target: Episode, mapping: Mapping[str, str]) -> dict[str, Any]:
    """Open-world comparison: missing observations are unknown, not negative facts."""
    if source.basis != target.basis:
        raise ValueError("different predicate bases require an explicitly reconciled annotation first")
    if not isinstance(mapping, dict):
        raise ValueError("map must be a JSON object")
    for u, v in mapping.items():
        text(u, "source map id")
        text(v, "target map id")
        if u not in source.nodes or v not in target.nodes:
            raise ValueError("unknown map endpoint")
        if source.nodes[u][0] != target.nodes[v][0]:
            raise ValueError("map does not preserve declared node kinds")
    if len(set(mapping.values())) != len(mapping):
        raise ValueError("map must be injective")
    target_index = {row[:3]: row[3] for row in target.facts}
    examined: set[tuple[str, str, str]] = set()
    counts = {"matched": 0, "contradicted": 0, "unknown": 0}
    comparisons = []
    reverse_only = 0
    for u, relation, v, polarity in source.facts:
        if u not in mapping or v not in mapping:
            continue
        key = (mapping[u], relation, mapping[v])
        examined.add(key)
        observed = target_index.get(key)
        verdict = "unknown" if observed is None else ("matched" if observed == polarity else "contradicted")
        counts[verdict] += 1
        reversed_observed = observed is None and (key[2], relation, key[0]) in target_index
        reverse_only += int(reversed_observed)
        comparisons.append({"source_fact": [u, relation, v, polarity],
                            "target_key": list(key), "observed_polarity": observed,
                            "verdict": verdict, "reverse_only_observed": reversed_observed})
    tested = sum(counts.values())
    status = ("insufficient_evidence" if tested == 0 else
              "contradicted_on_scope" if counts["contradicted"] else
              "unresolved_on_scope" if counts["unknown"] else "supported_on_scope")
    return {"source": source.identifier, "target": target.identifier, "status": status,
            "mapping": dict(mapping), "basis": source.basis,
            "node_coverage": {"source_mapped": len(mapping), "source_total": len(source.nodes),
                              "target_mapped": len(mapping), "target_total": len(target.nodes)},
            "fact_coverage": {"source_tested": tested, "source_total": len(source.facts),
                              "source_untested": len(source.facts) - tested,
                              "target_total": len(target.facts),
                              "target_unexamined": sum(row[:3] not in examined for row in target.facts)},
            "counts": counts, "reverse_only_count": reverse_only,
            "equal_surface_labels": sum(source.nodes[u][1] == target.nodes[v][1] for u, v in mapping.items()),
            "comparisons": comparisons,
            "boundary": "Supplied annotations and map only; no truth, human, historical, or causal-equivalence score."}


def compose_maps(first: Mapping[str, str], second: Mapping[str, str]) -> dict[str, str]:
    """Compose partial functions, retaining only the domain where both are defined."""
    return {u: second[v] for u, v in first.items() if v in second}


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_request(path: Path) -> dict[str, Any]:
    raw = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicate_keys)
    keys(raw, {"source", "target", "map"}, "request")
    return assess(Episode.parse(raw["source"]), Episode.parse(raw["target"]), raw["map"])


def fixture() -> dict[str, Any]:
    """Author-created work/care motif, NOT a description of either musical audience."""
    return {"id": "synthetic_work_care", "basis": "work-care-v0",
            "provenance": "Author-created calibration fixture; no people, songs, or field observations.",
            "nodes": [{"id": "a", "kind": "person", "label": "worker"},
                      {"id": "k", "kind": "person", "label": "sibling"},
                      {"id": "w", "kind": "activity", "label": "paid shift"},
                      {"id": "c", "kind": "activity", "label": "care visit"}],
            "facts": [["a", "undertakes", "w", 1], ["a", "cares_for", "k", 1],
                      ["k", "needs", "c", 1], ["w", "prevents", "c", 1]]}


def rename_ids(raw: dict[str, Any], mapping: Mapping[str, str]) -> dict[str, Any]:
    renamed = copy.deepcopy(raw)
    for node in renamed["nodes"]:
        node["id"] = mapping[node["id"]]
    renamed["facts"] = [[mapping[u], relation, mapping[v], sign] for u, relation, v, sign in raw["facts"]]
    return renamed


def calibration() -> dict[str, Any]:
    source_raw = fixture()
    source = Episode.parse(source_raw)
    identity = {node: node for node in source.nodes}
    cells = []
    for surface_same, structure_same in itertools.product((False, True), repeat=2):
        raw = fixture()
        raw["id"] = f"surface_{int(surface_same)}_structure_{int(structure_same)}"
        if not surface_same:
            for node, label in zip(raw["nodes"], ("wage earner", "cousin", "repair shift", "helping at home")):
                node["label"] = label
        if not structure_same:
            raw["facts"][-1][-1] = -1
        result = assess(source, Episode.parse(raw), identity)
        expected = "supported_on_scope" if structure_same else "contradicted_on_scope"
        if result["status"] != expected:
            raise AssertionError("factorial calibration failed")
        cells.append({"surface_same": surface_same, "structure_same": structure_same, "result": result})
    permutations = 0
    for perm in itertools.permutations(identity):
        mapping = dict(zip(identity, perm))
        report = assess(source, Episode.parse(rename_ids(source_raw, mapping)), mapping)
        if report["counts"] != {"matched": 4, "contradicted": 0, "unknown": 0}:
            raise AssertionError("renaming invariance failed")
        permutations += 1
    mutations = 0
    for index in range(len(source.facts)):
        raw = fixture()
        raw["facts"][index][-1] *= -1
        report = assess(source, Episode.parse(raw), identity)
        if report["counts"]["contradicted"] != 1:
            raise AssertionError("polarity mutation escaped detection")
        mutations += 1
    partial = assess(source, source, {"a": "a", "w": "w"})
    missing_raw = fixture()
    missing_raw["facts"].pop()
    missing = assess(source, Episode.parse(missing_raw), identity)
    # Identical observed action; different unobserved action. Construction, not a fitted causal model.
    outcomes_a = {"stay": "paid", "leave": "unpaid"}
    outcomes_b = {"stay": "paid", "leave": "dismissed"}
    return {"version": VERSION, "base_commit": BASE_COMMIT, "python": platform.python_version(),
            "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "scope": "Synthetic instrument calibration only. All cells authored; no empirical holdout.",
            "factorial_cells": cells, "renamings_checked": permutations,
            "single_fact_polarity_mutations_detected": mutations,
            "partial_scope": partial, "missing_observation": missing,
            "counterfactual_counterexample": {"model_a": outcomes_a, "model_b": outcomes_b,
                "observed_action": "stay", "observed_outcomes_equal": outcomes_a["stay"] == outcomes_b["stay"],
                "unobserved_action": "leave", "unobserved_outcomes_equal": outcomes_a["leave"] == outcomes_b["leave"]},
            "human_subjects": "NOT RUN", "music_corpus": "NOT ANALYZED", "full_repository_validation": "NOT RUN"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="JSON with source, target, map; otherwise run synthetic calibration")
    parser.add_argument("--output", type=Path, help="write JSON here instead of stdout")
    args = parser.parse_args()
    try:
        result = read_request(args.input) if args.input else calibration()
        output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            args.output.write_text(output, encoding="utf-8")
        else:
            print(output, end="")
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
