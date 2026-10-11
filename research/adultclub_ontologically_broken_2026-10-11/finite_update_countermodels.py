#!/usr/bin/env python3
"""Exact/elementary construction-level controls for an AdultClub/TLICA analogy.

Not a psychological experiment, RH result, or measured physical system.
Pure Python 3 standard library; deliberately small countermodels.
"""
from __future__ import annotations

import cmath
import json
import math


def potential(x: float, a: float = 0.0) -> float:
    """Tilted double-well potential; x is fast, a is a structural parameter."""
    return (x * x - 1.0) ** 2 + a * x


def slope(x: float, a: float) -> float:
    return 4.0 * x * (x * x - 1.0) + a


def curvature(x: float) -> float:
    return 12.0 * x * x - 4.0


def polynomial_roots(a: float) -> tuple[complex, complex]:
    """The zeros of F_a(z)=z**2-a; no relation to zeta zeros."""
    root = cmath.sqrt(a)
    return (-root, root)


def charpoly2(matrix: tuple[tuple[int, int], tuple[int, int]]) -> tuple[int, int, int]:
    """Coefficients of det(zI-A) in descending powers of z."""
    (aa, bb), (cc, dd) = matrix
    return (1, -(aa + dd), aa * dd - bb * cc)


def multiply2(left: tuple[tuple[int, int], tuple[int, int]],
              right: tuple[tuple[int, int], tuple[int, int]]) -> tuple[tuple[int, int], tuple[int, int]]:
    return tuple(tuple(sum(left[i][k] * right[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))  # type: ignore[return-value]


def apply2(matrix: tuple[tuple[int, int], tuple[int, int]],
           vec: tuple[int, int]) -> tuple[int, int]:
    return (sum(matrix[0][k] * vec[k] for k in range(2)),
            sum(matrix[1][k] * vec[k] for k in range(2)))


def checks() -> dict[str, object]:
    results: dict[str, bool] = {}
    def check(name: str, proposition: bool) -> None:
        results[name] = bool(proposition)
        if not proposition:
            raise AssertionError(name)

    check("fixed_geometry_barrier_is_one", math.isclose(potential(0), 1.0) and
          math.isclose(potential(-1), 0.0) and math.isclose(potential(1), 0.0))
    check("energetic_crossing_can_leave_geometry_fixed", 1.5 > potential(0) and
          0.5 < potential(0))
    xcrit = 1.0 / math.sqrt(3.0)
    acrit = 8.0 / (3.0 * math.sqrt(3.0))
    check("double_well_fold_is_stationary_and_flat", math.isclose(slope(xcrit, acrit), 0.0, abs_tol=1e-12) and
          math.isclose(curvature(xcrit), 0.0, abs_tol=1e-12))
    check("eight_small_updates_pass_fold", 7 * 0.2 < acrit < 8 * 0.2)
    z_on = polynomial_roots(-1)
    z_off = polynomial_roots(1)
    z_merge = polynomial_roots(0)
    check("zeros_can_be_on_reference_axis", all(math.isclose(v.real, 0.0) for v in z_on))
    check("zeros_can_leave_reference_axis", all(math.isclose(abs(v.real), 1.0) for v in z_off))
    check("zeros_can_merge", z_merge == (0j, 0j))
    zero = ((0, 0), (0, 0))
    nilpotent = ((0, 1), (0, 0))
    check("different_dynamics_identical_zero_multiset", charpoly2(zero) == charpoly2(nilpotent) == (1, 0, 0))
    check("nilpotent_square_vanishes", multiply2(nilpotent, nilpotent) == zero)
    # exp(0)e_2=e_2, whereas exp(N)e_2=(I+N)e_2=(1,1), since N^2=0.
    identity = ((1, 0), (0, 1))
    exp_nilpotent = ((identity[0][0] + nilpotent[0][0], nilpotent[0][1]),
                     (nilpotent[1][0], identity[1][1] + nilpotent[1][1]))
    response0 = apply2(identity, (0, 1))
    response1 = apply2(exp_nilpotent, (0, 1))
    check("equal_zeros_do_not_fix_response", response0 == (0, 1) and
          response1 == (1, 1) and response0 != response1)
    return {"result": "PASS", "checks": len(results), "test_names": list(results),
            "critical_tilt": acrit,
            "epistemic_scope": "construction-level finite mathematical controls only"}


if __name__ == "__main__":
    print(json.dumps(checks(), sort_keys=True, indent=2))
