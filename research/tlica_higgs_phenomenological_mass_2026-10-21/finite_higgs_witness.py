#!/usr/bin/env python3
"""Finite witness for TLICA-HIGGS research-tier analogy; not a mind experiment.

Uses dimensionless parameters; no empirical fit, psychological or physical
identification. Run: python -m unittest -v tlica_higgs_prototype
"""
from __future__ import annotations

import math
import unittest


def double_well(h: float, v: float, eta: float) -> float:
    """Toy order-parameter potential U(h)=eta/4*(h^2-v^2)^2."""
    if v < 0 or eta <= 0:
        raise ValueError("v >= 0 and eta > 0 required")
    return 0.25 * eta * (h * h - v * v) ** 2


def double_well_curvature(h: float, v: float, eta: float) -> float:
    """Second derivative U''(h)."""
    return eta * (3 * h * h - v * v)


def stiffness(m0: float, g: float, h: float) -> float:
    """K=m0^2+g^2*h^2, toy mass gap squared for one mode."""
    if m0 < 0:
        raise ValueError("m0 >= 0 required")
    return m0 * m0 + (g * h) ** 2


def static_susceptibility(m0: float, g: float, h: float) -> float:
    k = stiffness(m0, g, h)
    if k <= 0:
        raise ValueError("zero gap: no finite static susceptibility")
    return 1.0 / k


def equilibrium(force: float, m0: float, g: float, h: float) -> float:
    return force * static_susceptibility(m0, g, h)


def energy_rate(q: float, velocity: float, drive: float, drag: float,
                m0: float, g: float, h: float) -> float:
    """E'=velocity*(drive-drag*velocity) for q''+drag*q'+K*q=drive.

    Computes LHS via chain rule and acceleration, so identity is testable.
    """
    k = stiffness(m0, g, h)
    accel = drive - drag * velocity - k * q
    return velocity * accel + k * q * velocity


def predicted_dissipation(velocity: float, drive: float, drag: float) -> float:
    return velocity * drive - drag * velocity * velocity


def difference_matrix(couplings: tuple[float, ...],
                      backgrounds: tuple[float, ...],
                      base_background: float) -> tuple[tuple[float, ...], ...]:
    """Delta K_{r,c}=g_r^2*(h_c^2-h_base^2); rank <= 1."""
    return tuple(tuple(g * g * (h * h - base_background * base_background)
                       for h in backgrounds) for g in couplings)


def minors_2x2(matrix: tuple[tuple[float, ...], ...]) -> tuple[float, ...]:
    if not matrix:
        return ()
    n = len(matrix[0])
    if any(len(row) != n for row in matrix):
        raise ValueError("ragged matrix")
    out = []
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            for c in range(n):
                for d in range(c + 1, n):
                    out.append(matrix[i][c] * matrix[j][d]
                               - matrix[i][d] * matrix[j][c])
    return tuple(out)


def overdamped_fractional_time(k: float, drag: float, fraction: float) -> float:
    """gamma*q'+k*q=F, q(0)=0: time to fraction of q(infinity)."""
    if k <= 0 or drag <= 0 or not (0 < fraction < 1):
        raise ValueError("k,drag >0 and 0<fraction<1")
    return -drag * math.log(1.0 - fraction) / k


class HiggsFiniteTests(unittest.TestCase):
    def test_potential_minima(self):
        for h in (-2, 2):
            self.assertEqual(double_well(h, 2, 0.75), 0.0)
        self.assertGreater(double_well(0, 2, 0.75), 0.0)

    def test_curvature_symmetry_break(self):
        self.assertAlmostEqual(double_well_curvature(1, 1, 2), 4.0)
        self.assertAlmostEqual(double_well_curvature(-1, 1, 2), 4.0)
        self.assertLess(double_well_curvature(0, 1, 2), 0.0)

    def test_no_field_coupling(self):
        self.assertAlmostEqual(stiffness(0.8, 0.0, 50), 0.64)
        self.assertAlmostEqual(stiffness(0.8, 0.0, 0), 0.64)

    def test_no_background(self):
        self.assertAlmostEqual(stiffness(0.8, 100, 0), 0.64)

    def test_monotone_coupling_effect(self):
        self.assertGreater(stiffness(1, 2, 1), stiffness(1, 1, 1))
        self.assertGreater(stiffness(1, 1, 2), stiffness(1, 1, 1))

    def test_sign_of_background_unidentifiable(self):
        self.assertEqual(stiffness(1, 2, -3), stiffness(1, 2, 3))

    def test_step_response_equilibrium(self):
        self.assertAlmostEqual(equilibrium(1, 1, 0, 1), 1)
        self.assertAlmostEqual(equilibrium(1, 1, 1, 1), 0.5)
        self.assertAlmostEqual(equilibrium(1, 1, 2, 1), 0.2)

    def test_conservative_mass_not_dissipation(self):
        for g in (0, 1, 9):
            rate = energy_rate(q=3, velocity=2, drive=1, drag=0.5,
                               m0=0.75, g=g, h=2)
            self.assertAlmostEqual(rate, predicted_dissipation(2, 1, 0.5))

    def test_rank_one_differences(self):
        mat = difference_matrix((0, 0.4, 1.1), (0.5, 1.0, 1.5), 0.5)
        self.assertTrue(all(abs(v) < 1e-12 for v in minors_2x2(mat)))

    def test_mutated_cell_breaks_rank_one(self):
        mat = [list(row) for row in difference_matrix((0.4, 1.1), (1, 1.5), 0.5)]
        mat[0][0] += 0.15  # deliberate path-/referent-specific deviation
        minors = minors_2x2(tuple(tuple(row) for row in mat))
        self.assertTrue(any(abs(x) > 1e-5 for x in minors))

    def test_zero_coupling_zero_background_shift(self):
        mat = difference_matrix((0, 0.5), (1, 2), 0)
        self.assertEqual(mat[0], (0, 0))
        self.assertGreater(mat[1][1], mat[1][0])

    def test_cross_referent_change_ratios(self):
        mat = difference_matrix((0.5, 1), (1, 2), 0.25)
        for a,b in zip(mat[0],mat[1]):
            self.assertAlmostEqual(a / b, 0.25)

    def test_stiffness_is_not_drag(self):
        # With fixed drag, higher K reaches a fraction of its *own* steady-state faster.
        t1 = overdamped_fractional_time(1, 3, 0.95)
        t2 = overdamped_fractional_time(4, 3, 0.95)
        self.assertAlmostEqual(t1, 4 * t2)

    def test_single_context_cannot_identify_mechanism(self):
        self.assertAlmostEqual(stiffness(math.sqrt(2), 0, 1),
                               stiffness(1, 1, 1))


if __name__ == '__main__':
    unittest.main(verbosity=2)
