#!/usr/bin/env python3
"""Classical stochastic Wick/causal diagram witness for a TLICA research analogue.

Finite Gaussian algebra and a stationary Gibbs integral ONLY.
No claim of literal quantum particles or a validated psychological mechanism.

Run: python -m unittest -v causal_diagram_witness
"""
from __future__ import annotations

import math
import unittest


def retarded(k: float, t: float, s: float) -> float:
    """Ornstein-Uhlenbeck retarded response with Ito endpoint."""
    if k <= 0:
        raise ValueError("k>0")
    return math.exp(-k * (t-s)) if t > s else 0.0


def covariance(k: float, diffusion: float, t: float, s: float) -> float:
    if k <= 0 or diffusion < 0:
        raise ValueError("k>0,diffusion>=0")
    return (diffusion/k)*math.exp(-k*abs(t-s))


def gaussian_third_moment(mean: float, var: float) -> float:
    if var < 0:
        raise ValueError("var>=0")
    return mean**3 + 3*mean*var


def gaussian_fourth_moment(mean: float, var: float) -> float:
    if var < 0:
        raise ValueError("var>=0")
    return mean**4 + 6*mean*mean*var + 3*var*var


def steady_mean_first_order(j: float, k: float, u: float, d: float) -> float:
    if k <= 0 or d < 0:
        raise ValueError("k>0,d>=0")
    m=j/k
    return m - u*(m**3+3*m*d/k)/(6*k)


def susceptibility_first_order(k: float, u: float, d: float) -> float:
    if k <= 0 or d < 0:
        raise ValueError("k>0,d>=0")
    return 1/k - u*d/(2*k**3)


def simpson_equilibrium_moments(j: float, k: float, u: float, d: float,
                                span: float=8.0, n: int=4000) -> tuple[float,float]:
    """Independent Gibbs numerical integral: P proportional exp(-U(q)/D)."""
    if k <= 0 or u < 0 or d <= 0 or n <= 0 or n%2:
        raise ValueError("positive k,d,n; nonnegative u; n even")
    step=2*span/n
    m0=m1=m2=0.0
    for i in range(n+1):
        q=-span+step*i
        e=-(k*q*q/2 + u*q**4/24 - j*q)/d
        w=(1 if i in (0,n) else (4 if i%2 else 2))*math.exp(e)
        m0+=w
        m1+=w*q
        m2+=w*q*q
    mean=m1/m0
    return mean,m2/m0-mean*mean


def first_order_dynamic_mean_at_time(j:float,k:float,d:float,
                                    dt:float,steps:int)->tuple[float,float]:
    """Exact u=0 coefficient of E[q_n] for a finite Gaussian Euler recursion."""
    if dt<=0 or k<=0 or d<0 or steps<0 or k*dt>=2:
        raise ValueError("stable linear discretization required")
    a=1-k*dt
    m=v=deriv=0.0
    for _ in range(steps):
        deriv=a*deriv - dt*gaussian_third_moment(m,v)/6
        m=a*m+dt*j
        v=a*a*v+2*d*dt
    return m,deriv


def orient_partial(candidate: tuple[float,...],baseline:tuple[float,...])->str:
    """Coordinatewise Pareto order: illustrative only, NOT canonical TLICA Pi."""
    if len(candidate)!=len(baseline):
        raise ValueError("mismatched dimensions")
    a=all(x>=y for x,y in zip(candidate,baseline))
    b=all(x<=y for x,y in zip(candidate,baseline))
    if a and b:
        return "equivalent"
    if a:
        return "plus"
    if b:
        return "minus"
    return "incomparable"


class CausalDiagramTests(unittest.TestCase):
    def test_causal_response_zero_when_source_in_future(self):
        self.assertEqual(retarded(1.5,1,2),0)
        self.assertEqual(retarded(1.5,1,1),0)
        self.assertGreater(retarded(1.5,2,1),0)

    def test_stationary_covariance_symmetric(self):
        self.assertAlmostEqual(covariance(2,0.7,1,4),covariance(2,0.7,4,1))

    def test_variance_is_d_over_k(self):
        self.assertAlmostEqual(covariance(2,0.7,0,0),0.35)

    def test_wick_third_factor_three(self):
        self.assertEqual(gaussian_third_moment(2,3),26)

    def test_wick_fourth_factor_three_and_six(self):
        self.assertEqual(gaussian_fourth_moment(1,2),1+12+12)

    def test_noise_loop_absent_when_diffusion_zero(self):
        self.assertAlmostEqual(susceptibility_first_order(2,0.8,0),0.5)

    def test_tadpole_negative_stiffening(self):
        self.assertLess(susceptibility_first_order(2,0.1,0.5),0.5)

    def test_tree_survives_zero_noise(self):
        j,k,u=0.75,2.0,0.4
        self.assertAlmostEqual(steady_mean_first_order(j,k,u,0),
                               j/k-u*(j/k)**3/(6*k))

    def test_stationary_perturbation_converges_to_quadrature(self):
        j,k,d=0.45,1.8,0.6
        errors=[]
        for u in (0.08,0.04,0.02):
            exact,_=simpson_equilibrium_moments(j,k,u,d)
            approx=steady_mean_first_order(j,k,u,d)
            errors.append(abs(exact-approx))
        self.assertGreater(errors[0],3.4*errors[1])
        self.assertGreater(errors[1],3.4*errors[2])

    def test_independent_static_linear_response_via_variance(self):
        k,d=1.8,0.6
        for u in (0.08,0.04):
            _,v=simpson_equilibrium_moments(0,k,u,d)
            self.assertLess(abs(v/d-susceptibility_first_order(k,u,d)),0.001)

    def test_dynamic_derivative_zero_drive(self):
        m,deriv=first_order_dynamic_mean_at_time(0,1.4,0.8,0.1,60)
        self.assertEqual(m,0)
        self.assertEqual(deriv,0)

    def test_dynamic_derivative_negative_for_positive_drive(self):
        m,deriv=first_order_dynamic_mean_at_time(0.4,1.4,0.8,0.1,60)
        self.assertGreater(m,0)
        self.assertLess(deriv,0)

    def test_discrete_tadpole_depends_on_variance(self):
        v0=first_order_dynamic_mean_at_time(0.4,1.4,0,0.1,60)[1]
        v1=first_order_dynamic_mean_at_time(0.4,1.4,0.8,0.1,60)[1]
        self.assertLess(v1,v0)

    def test_partial_preorder_preserves_incomparability(self):
        self.assertEqual(orient_partial((1,0),(0,1)),"incomparable")

    def test_partial_preorder_other_cases(self):
        self.assertEqual(orient_partial((2,1),(1,1)),"plus")
        self.assertEqual(orient_partial((0,1),(1,1)),"minus")
        self.assertEqual(orient_partial((1,1),(1,1)),"equivalent")

    def test_zero_nonlin_is_exact_linear_response(self):
        j,k,d=0.45,1.8,0.6
        mean,var=simpson_equilibrium_moments(j,k,0,d)
        self.assertAlmostEqual(mean,j/k,places=11)
        self.assertAlmostEqual(var,d/k,places=11)


if __name__=="__main__":
    unittest.main(verbosity=2)
