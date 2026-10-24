#!/usr/bin/env python3
"""Finite stochastic-imprinting witnesses; not a validated mental model.

Run: python -m unittest -v frame_scattering_imprinting_witness
"""
import itertools
import math
import unittest


def weight_update(w, alpha, beta):
    """TLICA 8.4 update in the parameter subdomain where projection is inert."""
    if not all(0 <= z <= 1 for z in (w, alpha, beta)):
        raise ValueError('parameters must be in [0,1]')
    return (1-beta)*w + alpha*(1-w)


def sampled_update(w, event, a, b):
    """A coincident ambient event reinforces; its absence lets an edge weaken."""
    return weight_update(w, a if event else 0, 0 if event else b)


def expected_next(w, p, a, b):
    return p*sampled_update(w, True, a, b)+(1-p)*sampled_update(w, False, a, b)


def mean_after(n, w0, p, a, b):
    if n < 0 or not all(0 <= z <= 1 for z in (w0, p, a, b)):
        raise ValueError('invalid parameters')
    r=p*a+(1-p)*b
    if r == 0:
        return w0
    equilibrium=p*a/r
    return equilibrium+(w0-equilibrium)*(1-r)**n


def enumerated_mean(n, w0, p, a, b):
    """Sum over all 2^n sample paths, independent of the mean-recursion proof."""
    out=0.0
    for path in itertools.product((False, True), repeat=n):
        prob=1.0
        w=w0
        for event in path:
            prob*=p if event else 1-p
            w=sampled_update(w,event,a,b)
        out += prob*w
    return out


def focus_conditioned_plus(base_plus, gate_plus, gate_minus):
    """Bayes' rule: frame-dependent selection skews recorded exposures."""
    z=base_plus*gate_plus+(1-base_plus)*gate_minus
    if z <= 0:
        raise ValueError('no accepted exposure')
    return base_plus*gate_plus/z


def gaussian_square_moment(mean, var):
    return mean*mean+var


def gaussian_fourth_moment(mean, var):
    return mean**4+6*mean*mean*var+3*var*var


def ou_variance(k, diffusion):
    if k <= 0 or diffusion < 0:
        raise ValueError('invalid OU parameters')
    return diffusion/k


def slow_weight_drift(w, epsilon, a, b, signal_square_mean):
    """Frozen slow weight response to fast signal square expectation, not exact joint evolution."""
    return epsilon*(a*(1-w)*signal_square_mean-b*w)


def averaged_equilibrium(a, b, signal_square_mean):
    z=a*signal_square_mean+b
    if z == 0:
        raise ValueError('no determined equilibrium')
    return a*signal_square_mean/z


class ImprintingWitness(unittest.TestCase):
    def test_update_bounds(self):
        for w in (0, .13, .7, 1):
            for alpha in (0, .2, 1):
                for beta in (0, .35, 1):
                    self.assertGreaterEqual(weight_update(w,alpha,beta),0)
                    self.assertLessEqual(weight_update(w,alpha,beta),1)

    def test_update_rejects_illegal_parameters(self):
        with self.assertRaises(ValueError):
            weight_update(1.1,.2,.3)

    def test_weak_edge_reinforcement_sensitivity(self):
        da=.01
        low=(weight_update(.05,.2+da,0)-weight_update(.05,.2,0))/da
        high=(weight_update(.95,.2+da,0)-weight_update(.95,.2,0))/da
        self.assertAlmostEqual(low,.95)
        self.assertAlmostEqual(high,.05)

    def test_forgetting_sensitivity(self):
        db=.01
        w=.8
        self.assertAlmostEqual((weight_update(w,0,.1+db)-weight_update(w,0,.1))/db,-w)

    def test_random_event_at_zero_grows_edge(self):
        self.assertAlmostEqual(sampled_update(0,True,.12,.01),.12)

    def test_absent_event_weakens_edge(self):
        self.assertAlmostEqual(sampled_update(.8,False,.12,.02),.784)

    def test_expected_recurrence(self):
        self.assertAlmostEqual(expected_next(.4,.2,.1,.02),(.4+.2*.1*(1-.4)-.8*.02*.4))

    def test_analytic_vs_full_enumeration(self):
        for n in range(1,8):
            self.assertAlmostEqual(mean_after(n,.2,.1,.1,.01),enumerated_mean(n,.2,.1,.1,.01))

    def test_long_run_fixed_point(self):
        p,a,b=.1,.1,.01
        val=mean_after(400,0,p,a,b)
        star=p*a/(p*a+(1-p)*b)
        self.assertAlmostEqual(val,star,delta=.001)

    def test_random_cooccurrence_with_no_ground_truth_can_imprint(self):
        # By construction the coincidence events are independent random draws.
        val=mean_after(200,0,.1,.1,.01)
        self.assertGreater(val,.5)

    def test_no_exposure_no_formation(self):
        self.assertEqual(mean_after(200,0,0,.1,.01),0)

    def test_world_symmetry_can_be_broken_by_focus_selection(self):
        self.assertAlmostEqual(focus_conditioned_plus(.5,.8,.2),.8)

    def test_equal_focus_selection_preserves_world_symmetry(self):
        self.assertAlmostEqual(focus_conditioned_plus(.5,.8,.8),.5)

    def test_zero_focus_access_throws(self):
        with self.assertRaises(ValueError):
            focus_conditioned_plus(.5,0,0)

    def test_gaussian_square_wick_contraction(self):
        self.assertEqual(gaussian_square_moment(0,.7),.7)
        self.assertAlmostEqual(gaussian_square_moment(2,.7),4.7)

    def test_fourth_wick_contractions(self):
        self.assertAlmostEqual(gaussian_fourth_moment(0,2),12)
        self.assertAlmostEqual(gaussian_fourth_moment(1,2),25)

    def test_fast_signal_variance(self):
        self.assertAlmostEqual(ou_variance(2,.8),.4)

    def test_noise_loop_drift_from_zero_mean_signal(self):
        v=ou_variance(2,.8)
        self.assertAlmostEqual(slow_weight_drift(0,.02,1,.1,v),.008)

    def test_noise_loop_vanishes_at_zero_diffusion(self):
        self.assertEqual(slow_weight_drift(0,.02,1,.1,ou_variance(2,0)),0)

    def test_averaged_stationary_edge(self):
        v=ou_variance(2,.8)
        star=averaged_equilibrium(.5,.2,v)
        self.assertAlmostEqual(star,.5)
        self.assertAlmostEqual(slow_weight_drift(star,.01,.5,.2,v),0)

    def test_strong_edge_less_formation_by_same_bath(self):
        v=.4
        self.assertGreater(slow_weight_drift(.1,.01,.5,0,v),
                           slow_weight_drift(.9,.01,.5,0,v))


if __name__ == '__main__':
    unittest.main(verbosity=2)
