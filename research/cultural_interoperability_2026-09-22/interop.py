"""Finite, consent-gated interoperability instrument; not a model of human minds.

Python 3.10+, standard library only. All predicates and preference ranks are
supplied, not inferred. A certificate is conditional on this finite input.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Any

Tri = bool | None


def conjunction(values: list[Tri]) -> Tri:
    """Strong three-valued conjunction: a known failure defeats unknowns."""
    if any(v is False for v in values):
        return False
    return None if any(v is None for v in values) else True


def _ids(rows: list[dict[str, Any]], label: str) -> set[str]:
    if not isinstance(rows, list) or any(not isinstance(r, dict) for r in rows):
        raise ValueError(f"{label}: expected a list of records")
    names = [r.get("id") for r in rows]
    if any(not isinstance(n, str) or not n for n in names):
        raise ValueError(f"{label}: nonempty string ids required")
    if len(set(names)) != len(names):
        raise ValueError(f"{label}: duplicate ids")
    return set(names)


def validate(case: dict[str, Any]) -> None:
    """Reject missing entries; absence is not silent agreement or falsity."""
    if not isinstance(case, dict):
        raise ValueError("case must be an object")
    if case.get("schema_version") != "0.1" or case.get("kind") != "synthetic":
        raise ValueError("v0.1 accepts explicitly synthetic fixtures only")
    parties = case["parties"]
    if not isinstance(parties, list) or any(not isinstance(p, str) or not p for p in parties):
        raise ValueError("parties must be a list of nonempty strings")
    if not 1 <= len(parties) <= 4 or len(set(parties)) != len(parties):
        raise ValueError("need 1..4 unique parties")
    if any(not isinstance(p, str) or not p for p in parties):
        raise ValueError("invalid party id")
    sources, constraints, options = case["sources"], case["constraints"], case["options"]
    sids = _ids(sources, "sources")
    cids = _ids(constraints, "constraints")
    _ids(options, "options")
    if not 1 <= len(constraints) <= 8 or len(options) > 128:
        raise ValueError("prototype bounds: 1..8 constraints, at most 128 options")
    if not any(c.get("kind") == "standing" for c in constraints):
        raise ValueError("explicit standing/third-party gate required")
    if not any(c.get("kind") == "reality" for c in constraints):
        raise ValueError("explicit reality gate required")
    for party in parties:
        if not any(c.get("kind") == "party_floor" and c.get("owner") == party for c in constraints):
            raise ValueError("each party needs an explicit acceptability floor")
    for source in sources:
        if source.get("status") not in {"confirmed", "unverified", "disputed"}:
            raise ValueError("invalid source status")
        if not isinstance(source.get("family"), str) or not source["family"]:
            raise ValueError("source family required")
    for constraint in constraints:
        if constraint.get("kind") not in {"reality", "standing", "party_floor"}:
            raise ValueError("invalid constraint kind")
        refs = constraint.get("source_ids", [])
        if not isinstance(refs, list) or any(not isinstance(s, str) for s in refs):
            raise ValueError("source_ids must be a list of strings")
        if not refs or not set(refs) <= sids or len(set(refs)) != len(refs):
            raise ValueError("constraint needs explicit, unique, known source ids")
        if constraint["kind"] == "party_floor" and constraint.get("owner") not in parties:
            raise ValueError("party floor needs a named owner")
    for option in options:
        for field, expected in (("checks", cids), ("consent", set(parties)), ("ranks", set(parties))):
            if not isinstance(option[field], dict) or set(option[field]) != expected:
                raise ValueError(f"{option['id']}: incomplete or extra {field}")
        for value in list(option["checks"].values()) + list(option["consent"].values()):
            if value is not None and type(value) is not bool:
                raise ValueError("checks/consent must be literal true, false, or null")
        if any(type(r) is not int for r in option["ranks"].values()):
            raise ValueError("synthetic preference ranks must be integers, not booleans")


def gate_matrix(case: dict[str, Any], excluded_families: frozenset[str] = frozenset()) -> dict[str, dict[str, Tri]]:
    validate(case)
    sources = {s["id"]: s for s in case["sources"]}
    matrix = {}
    for option in case["options"]:
        row: dict[str, Tri] = {}
        for c in case["constraints"]:
            refs = [sources[s] for s in c["source_ids"]]
            # References are jointly load-bearing here, not independent votes.
            available = all(s["status"] == "confirmed" and s["family"] not in excluded_families for s in refs)
            row[f"constraint:{c['id']}"] = option["checks"][c["id"]] if available else None
        row.update({f"consent:{p}": option["consent"][p] for p in case["parties"]})
        matrix[option["id"]] = row
    return matrix


def _minimal_blockers(matrix: dict[str, dict[str, Tri]]) -> list[list[str]]:
    """All inclusion-minimal gate sets rejecting every option in this catalog.

    This diagnoses the supplied incompatibility. It does NOT authorize relaxing
    a gate, changing someone's preferences, or overriding withheld consent.
    """
    if not matrix:
        return []
    names = sorted(next(iter(matrix.values())))
    cores: list[set[str]] = []
    for size in range(1, len(names) + 1):
        for group in itertools.combinations(names, size):
            chosen = set(group)
            if any(core <= chosen for core in cores):
                continue
            if all(any(row[g] is False for g in chosen) for row in matrix.values()):
                cores.append(chosen)
    return [sorted(c) for c in cores]


def solve(case: dict[str, Any], excluded_families: frozenset[str] = frozenset()) -> dict[str, Any]:
    matrix = gate_matrix(case, excluded_families)
    states = {oid: conjunction(list(row.values())) for oid, row in matrix.items()}
    supported = sorted(oid for oid, value in states.items() if value is True)
    pending = sorted(oid for oid, value in states.items() if value is None)
    rejected = sorted(oid for oid, value in states.items() if value is False)
    by_id = {o["id"]: o for o in case["options"]}
    def dominates(a: str, b: str) -> bool:
        ar, br = by_id[a]["ranks"], by_id[b]["ranks"]
        return all(ar[p] >= br[p] for p in case["parties"]) and any(ar[p] > br[p] for p in case["parties"])
    frontier = [o for o in supported if not any(dominates(other, o) for other in supported)]
    status = ("EMPTY_CATALOG_PATHWAY_GAP" if not matrix else
              "SUPPORTED_OPTIONS" if supported else
              "UNRESOLVED" if pending else "NO_PERMISSIBLE_OPTION_IN_CATALOG")
    return {
        "case_id": case["id"], "status": status, "supported": supported,
        "supported_frontier": frontier, "pending": pending, "rejected": rejected,
        "frontier_scope": "supported options only; pending/unlisted options may change it",
        "minimal_blockers": _minimal_blockers(matrix) if status == "NO_PERMISSIBLE_OPTION_IN_CATALOG" else [],
        "gate_matrix": matrix,
        "excluded_families": sorted(excluded_families),
        "certificate_scope": "finite synthetic catalog and supplied gates/ranks; no human outcome certified",
    }


def transport_report(source: list[list[str]], target: list[list[str]], mapping: dict[str, str]) -> dict[str, Any]:
    """Check a declared injective node transport on directed, typed edges.

    Relations must already be normalized under a declared semantic contract.
    Graph agreement does not validate that contract or identify a person's mind.
    """
    for graph in (source, target):
        if any(len(edge) != 3 or any(not isinstance(x, str) or not x for x in edge) for edge in graph):
            raise ValueError("edges require nonempty source, relation, target strings")
    nodes = {edge[i] for edge in source for i in (0, 2)}
    if not nodes:
        raise ValueError("empty transport is not a fidelity witness")
    if set(mapping) != nodes or len(set(mapping.values())) != len(mapping):
        raise ValueError("declare an injective map on exactly all source nodes")
    targets = {edge[i] for edge in target for i in (0, 2)}
    if not set(mapping.values()) <= targets:
        raise ValueError("mapped nodes must exist in target")
    moved = {(mapping[a], r, mapping[b]) for a, r, b in source}
    actual = {tuple(edge) for edge in target}
    missing, extra = moved - actual, actual - moved
    return {"preserves_declared_edges": not missing, "exact_on_declared_graphs": not missing and not extra,
            "missing_edges": sorted(missing), "extra_edges": sorted(extra)}


def predictive_overlap(predictions: dict[str, str | None]) -> dict[str, Any]:
    """Unweighted finite rival split; unknown predictions remain unresolved."""
    if not predictions:
        raise ValueError("at least one rival required")
    groups: dict[str, list[str]] = {}
    unknown = []
    for rival, prediction in sorted(predictions.items()):
        if prediction is None:
            unknown.append(rival)
        elif isinstance(prediction, str) and prediction:
            groups.setdefault(prediction, []).append(rival)
        else:
            raise ValueError("prediction must be a nonempty outcome label or null")
    pairs = list(itertools.combinations(predictions, 2))
    split = sum(predictions[a] is not None and predictions[b] is not None and predictions[a] != predictions[b] for a, b in pairs)
    return {"classes": groups, "unknown_rivals": unknown, "split_pairs": split,
            "unresolved_pairs": len(pairs) - split, "total_pairs": len(pairs),
            "scope": "declared predictions, not observed outcomes or truth probabilities"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON list of synthetic cases")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        cases = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(cases, list):
            raise ValueError("input must be a case list")
        reports = [solve(case) for case in cases]
        text = json.dumps(reports, indent=2, ensure_ascii=False) + "\n"
        if args.output:
            args.output.write_text(text, encoding="utf-8")
        else:
            print(text, end="")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(2, f"input/output error: {exc}\n")


if __name__ == "__main__":
    main()
