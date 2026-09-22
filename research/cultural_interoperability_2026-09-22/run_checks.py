"""Run the package checks and preserve deterministic synthetic reports."""
from __future__ import annotations
import hashlib
import io
import json
import platform
import unittest
from pathlib import Path

from fixtures import cases
from interop import predictive_overlap, solve

ROOT = Path(__file__).resolve().parent


def main() -> int:
    stream = io.StringIO()
    suite = unittest.defaultTestLoader.discover(str(ROOT), pattern="test_interop.py")
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    inputs = cases()
    encoded = json.dumps(inputs, sort_keys=True, separators=(",", ":")).encode()
    report = {
        "kind": "synthetic_instrument_calibration", "python": platform.python_version(),
        "tests_run": result.testsRun, "failures": len(result.failures), "errors": len(result.errors),
        "passed": result.wasSuccessful(), "input_sha256": hashlib.sha256(encoded).hexdigest(),
        "source_sha256": {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in ("interop.py", "fixtures.py", "test_interop.py", "run_checks.py")},
        "cases": [solve(case) for case in inputs],
        "leave_one_family_out": {case["id"]: [{"family": family, "status": solve(case, frozenset({family}))["status"], "supported": solve(case, frozenset({family}))["supported"]} for family in sorted({s["family"] for s in case["sources"]})] for case in inputs},
        "probe_calibration": {
            "null": predictive_overlap({"m1": "same", "m2": "same", "m3": "same", "m4": None}),
            "split": predictive_overlap({"m1": "a", "m2": "b", "m3": "b", "m4": None}),
        },
        "limitations": ["No humans, audio, lyrics, census, interviews, or real negotiation outcomes analyzed.",
                        "All fixture evidence is stipulated. Two code routes share authoring provenance.",
                        "Full repository make validate NOT RUN: complete checkout unavailable."]
    }
    (ROOT / "checks").mkdir(exist_ok=True)
    (ROOT / "checks" / "results.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (ROOT / "checks" / "tests.txt").write_text(stream.getvalue(), encoding="utf-8")
    print(stream.getvalue(), end="")
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
