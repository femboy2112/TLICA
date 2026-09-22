"""Deliberately break three safeguards; require the unchanged tests to catch each.

A killed mutant validates a test's sensitivity, not the sociological theory.
"""
from __future__ import annotations
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MUTATIONS = {
    "unknown_as_true": ('return None if any(v is None for v in values) else True', 'return True'),
    "consent_erased": ('row.update({f"consent:{p}": option["consent"][p] for p in case["parties"]})', 'row.update({f"consent:{p}": True for p in case["parties"]})'),
    "provenance_ignored": ('option["checks"][c["id"]] if available else None', 'option["checks"][c["id"]]'),
}


def main() -> int:
    reports = []
    for name, (old, new) in MUTATIONS.items():
        with tempfile.TemporaryDirectory(prefix="cultural-interop-mutation-") as temp:
            folder = Path(temp)
            for file in ("interop.py", "fixtures.py", "test_interop.py"):
                shutil.copyfile(ROOT / file, folder / file)
            path = folder / "interop.py"
            text = path.read_text(encoding="utf-8")
            if text.count(old) != 1:
                raise RuntimeError(f"mutation anchor moved: {name}")
            path.write_text(text.replace(old, new), encoding="utf-8")
            run = subprocess.run([sys.executable, "-m", "unittest", "-v", "test_interop"], cwd=folder, capture_output=True, text=True, timeout=30)
            log = run.stdout + run.stderr
            # A parser error is not a successful semantic kill.
            killed = run.returncode != 0 and "FAIL:" in log and "SyntaxError" not in log
            (ROOT / "checks" / f"mutation_{name}.txt").write_text(log, encoding="utf-8")
            reports.append({"mutation": name, "exit_code": run.returncode, "killed_by_assertion": killed})
    output = {"mutations": reports, "all_killed": all(r["killed_by_assertion"] for r in reports)}
    (ROOT / "checks" / "mutations.json").write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))
    return 0 if output["all_killed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
