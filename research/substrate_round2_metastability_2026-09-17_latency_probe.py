#!/usr/bin/env python3
"""
Round 2 latency probe -- confirms the "straw that broke the camel's back" latency
is DERIVED from the frozen baseline dynamics (foundation/3_formal_apparatus.md, v5.5.0).

Frozen equations used (verbatim structure):
  baseline law:   db/dt = gamma*(f - b)                 [line 519-521; rho CANCELS]
  felt salience:  V = tau*||Delta||_rho, Delta = f - b  [line 507]
  one content-axis: V = tau*sqrt(rho)*|Delta|.

Two claims to confirm numerically (both fall out of ONE fact: rho weights V but
cancels from the motion of b):
  C1 (latency) While the self tracks its target (Delta ~ 0) and the coupling rho
     decays slowly, felt salience V stays ~ 0 REGARDLESS of rho. The weakening of
     the attractor is unregistered -- the self coasts its inertial path.
  C2 (readout) An IDENTICAL perturbation ("the straw") applied early (rho high) vs
     late (rho low) yields peak felt responses whose ratio is sqrt(rho_e/rho_l):
     the perturbation is the "test" that finally reads out the current coupling.
     Same straw, different back.
     NOTE: C2 is a CONSISTENCY CHECK, not an independent witness for the sqrt(rho)
     law. V is defined below as tau*sqrt(rho)*|Delta| (posit P1), so the sqrt-ratio
     is arithmetic GIVEN that the perturbation displaces b by the same |Delta| early
     and late -- which is the non-trivial part it confirms: because rho cancels from
     db/dt, the pulse's effect on b is rho-independent, so the dynamics contributes
     no rho-dependence beyond P1's weighting. The sqrt(rho) law itself rests on P1.
     C1 (latency) is the genuinely independent numerical result.

The behavioral departure (held vs. leaves) is then gated by the POSITED slack/pressure
mechanism (Section 8.11); this probe confirms only the DERIVED substrate of it -- the
latency and the coupling-readout -- not the posited gate.

Pure stdlib; no external deps, no network. Instrument calibrated on a known analytic
case before any experimental reading is reported.
"""
import math

GAMMA = 1.0   # relaxation rate
TAU   = 1.0   # temperature (felt-salience per unit differential)


def run(f_of_t, rho_of_t, b0, t0, t1, dt, pulse=None):
    """Euler-integrate db/dt = GAMMA*(f-b); track peak felt V and peak |Delta|.
    pulse=(t_p, mag): an instantaneous displacement of b at t_p (a 'smack')."""
    n = int(round((t1 - t0) / dt))
    b = b0
    pulsed = False
    v_max = 0.0
    d_max = 0.0
    b_calib_err = 0.0
    for i in range(n + 1):
        t = t0 + i * dt
        f = f_of_t(t)
        rho = rho_of_t(t)
        if pulse is not None and not pulsed and t >= pulse[0]:
            b += pulse[1]           # the perturbation displaces the state from f
            pulsed = True
        delta = f - b
        v = TAU * math.sqrt(max(rho, 0.0)) * abs(delta)
        v_max = max(v_max, v)
        d_max = max(d_max, abs(delta))
        b += dt * GAMMA * (f - b)   # rho-independent, exactly as the frozen law
    return v_max, d_max


def calibrate():
    """Known case: constant f, constant rho => b(t) = f + (b0-f) e^{-GAMMA t}."""
    f0, b0, dt = 1.0, 0.0, 1e-4
    err = 0.0
    b = b0
    for i in range(int(10.0 / dt) + 1):
        t = i * dt
        analytic = f0 + (b0 - f0) * math.exp(-GAMMA * t)
        err = max(err, abs(b - analytic))
        b += dt * GAMMA * (f0 - b)
    return err


if __name__ == "__main__":
    cal = calibrate()
    print("CALIBRATION  max|numeric - analytic| = %.2e   (Euler O(dt), expect ~1e-4)" % cal)
    assert cal < 1e-3, "integrator failed calibration"

    # Coupling rho decays SLOWLY from 1.0 to 0.05 over T (eps << GAMMA).
    T = 200.0
    k = math.log(1 / 0.05) / T
    rho = lambda t: math.exp(-k * t)
    # A gentle slow drift for the tracked target, so the self has a realistic inertial path.
    fdrift = lambda t: 1.0 + 0.02 * math.sin(2 * math.pi * t / T)

    # C1: pure tracking, NO pulse -- watch felt V across the whole coupling collapse.
    v1, d1 = run(fdrift, rho, 1.0, 0.0, T, 1e-2)
    print("C1 latency   rho %.3f -> %.3f ;  tracking |Delta|max = %.2e ;  felt V max over full decay = %.2e"
          % (rho(0.0), rho(T), d1, v1))

    # C2: identical perturbation ("straw") early (rho high) vs late (rho low).
    mag = 0.3
    ve, _ = run(fdrift, rho, 1.0, 0.0, T, 1e-2, pulse=(5.0, mag))
    vl, _ = run(fdrift, rho, 1.0, 0.0, T, 1e-2, pulse=(190.0, mag))
    print("C2 readout   same straw |%.2f| -> peak felt V  early(rho=%.3f)=%.3f   late(rho=%.3f)=%.3f"
          % (mag, rho(5.0), ve, rho(190.0), vl))
    print("             Ve/Vl = %.3f    predicted sqrt(rho_e/rho_l) = %.3f"
          % (ve / vl, math.sqrt(rho(5.0) / rho(190.0))))
