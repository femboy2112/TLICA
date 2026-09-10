#!/usr/bin/env python3
"""Exact switched-operator counterexample; synthetic mathematics, not political data.

Run: python3 toy_models.py --output validation.json
Uses only the standard library. No parameter is estimated from people or conflicts.
"""
from __future__ import annotations

import argparse
import json
import math
import platform
from fractions import Fraction as F
from pathlib import Path

Matrix = tuple[tuple[F, F], tuple[F, F]]
Vector = tuple[F, F]
I: Matrix = ((F(1), F(0)), (F(0), F(1)))
A: Matrix = ((F(1, 2), F(9, 10)), (F(0), F(1, 2)))
B: Matrix = ((F(1, 2), F(0)), (F(9, 10), F(1, 2)))


def mul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(2)), F(0))
                       for j in range(2)) for i in range(2))


def apply(a: Matrix, v: Vector) -> Vector:
    return tuple(sum((a[i][j] * v[j] for j in range(2)), F(0))
                 for i in range(2))


def power(a: Matrix, n: int) -> Matrix:
    if not isinstance(n, int) or n < 0:
        raise ValueError("exponent must be a nonnegative integer")
    result = I
    for _ in range(n):
        result = mul(a, result)
    return result


def trace(a: Matrix) -> F:
    return a[0][0] + a[1][1]


def det(a: Matrix) -> F:
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def run_checks() -> dict:
    checks: dict[str, bool] = {}

    def check(name: str, condition: bool) -> None:
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError(name)

    product = mul(B, A)
    expected = ((F(1, 4), F(9, 20)), (F(9, 20), F(53, 50)))
    mean = tuple(tuple((A[i][j] + B[i][j]) / 2 for j in range(2))
                 for i in range(2))
    check("exact_BA_product", product == expected)
    check("individual_characteristic_polynomials", all(
        trace(m) == 1 and det(m) == F(1, 4) for m in (A, B)))
    check("mean_eigenvalues_19_over_20_and_1_over_20",
          apply(mean, (F(1), F(1))) == (F(19, 20), F(19, 20))
          and apply(mean, (F(1), F(-1))) == (F(1, 20), F(-1, 20)))
    check("product_characteristic_polynomial",
          trace(product) == F(131, 100) and det(product) == F(1, 16))
    check("positive_growth_root_certificate",
          1 - trace(product) + det(product) == F(-99, 400))

    # Independent expression for A^n, but not an independent research witness.
    for n in (0, 1, 2, 20):
        d = F(1, 2) ** n
        off = F(0) if n == 0 else n * F(9, 10) * F(1, 2) ** (n - 1)
        check(f"closed_form_A_power_{n}", power(A, n) == ((d, off), (F(0), d)))

    # Null control: remove the off-diagonal couplings.
    null: Matrix = ((F(1, 2), F(0)), (F(0), F(1, 2)))
    check("null_control_exact_decay",
          apply(power(mul(null, null), 10), (F(1), F(1)))
          == (F(1, 4) ** 10, F(1, 4) ** 10))
    check("noncommutation_mutation_detected", mul(A, B) != mul(B, A))
    try:
        power(A, -1)
    except ValueError:
        rejected = True
    else:
        rejected = False
    check("malformed_exponent_rejected", rejected)

    v = (F(1), F(1))
    trajectory = []
    for cycle in range(21):
        trajectory.append({"cycle": cycle, "x_exact": [str(t) for t in v],
                           "x_decimal": [float(t) for t in v]})
        v = apply(product, v)
    check("finite_trajectory_growth_control",
          max(F(t) for t in trajectory[-1]["x_exact"]) > 10)

    return {
        "status": "PASS",
        "scope": "Exact synthetic linear-algebra checks only; no empirical validation.",
        "python": platform.python_version(),
        "checks_passed": len(checks),
        "checks": checks,
        "spectral_radii": {
            "A": 0.5, "B": 0.5, "mean": 0.95,
            "BA_exact": "(131 + 9*sqrt(181))/200",
            "BA_decimal": (131 + 9 * math.sqrt(181)) / 200,
        },
        "trajectory_BA_from_1_1": trajectory,
        "empirical_models": "UNVERIFIED; no participants, datasets, or fitted parameters",
        "full_repository_make_validate": "NOT RUN: full clone unavailable (container DNS failure)",
        "independence": "One assistant and one script; algebraic cross-checks are not independent witnesses",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="optional UTF-8 JSON output path")
    args = parser.parse_args()
    report = run_checks()
    text = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
