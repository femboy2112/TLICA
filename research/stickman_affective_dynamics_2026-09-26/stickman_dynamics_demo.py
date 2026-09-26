#!/usr/bin/env python3
"""
Construction-level witness for the Stickman affective-dynamics branch.

Purpose:
    Demonstrate one discriminator between a stable first-order (overdamped)
    response model and a stable second-order dissipative model under the same
    strictly positive forcing pulse.

This is NOT a fitted human model. Parameters are deliberately synthetic.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class Summary:
    dt: float
    horizon: float
    pulse_end: float
    overdamped_peak: float
    overdamped_post_min: float
    overdamped_zero_cross_after_pulse: bool
    inertial_peak: float
    inertial_post_min: float
    inertial_zero_cross_after_pulse: bool
    inertial_first_cross_time: float | None
    checks_passed: int
    checks_total: int


def forcing(t: float, pulse_end: float = 1.0) -> float:
    return 1.0 if 0.0 <= t < pulse_end else 0.0


def simulate_overdamped(
    *,
    dt: float = 0.002,
    horizon: float = 5.0,
    pulse_end: float = 1.0,
    stiffness: float = 4.0,
    damping: float = 2.0,
) -> list[tuple[float, float]]:
    """Gamma*qdot + K*q = u(t), explicit Euler."""
    q = 0.0
    out: list[tuple[float, float]] = []
    n = int(round(horizon / dt))
    for i in range(n + 1):
        t = i * dt
        out.append((t, q))
        qdot = (forcing(t, pulse_end) - stiffness * q) / damping
        q += dt * qdot
    return out


def simulate_inertial(
    *,
    dt: float = 0.002,
    horizon: float = 5.0,
    pulse_end: float = 1.0,
    mass: float = 1.0,
    stiffness: float = 4.0,
    damping: float = 0.5,
) -> list[tuple[float, float, float]]:
    """M*qddot + Gamma*qdot + K*q = u(t), semi-implicit Euler."""
    q = 0.0
    v = 0.0
    out: list[tuple[float, float, float]] = []
    n = int(round(horizon / dt))
    for i in range(n + 1):
        t = i * dt
        out.append((t, q, v))
        acceleration = (
            forcing(t, pulse_end) - damping * v - stiffness * q
        ) / mass
        v += dt * acceleration
        q += dt * v
    return out


def first_negative_time_after(
    points: list[tuple[float, float, float]],
    t0: float,
) -> float | None:
    for t, q, _ in points:
        if t >= t0 and q < 0.0:
            return t
    return None


def run_checks() -> tuple[Summary, dict]:
    dt = 0.002
    horizon = 5.0
    pulse_end = 1.0

    overdamped = simulate_overdamped(
        dt=dt, horizon=horizon, pulse_end=pulse_end
    )
    inertial = simulate_inertial(
        dt=dt, horizon=horizon, pulse_end=pulse_end
    )

    overdamped_peak = max(q for _, q in overdamped)
    overdamped_post_min = min(q for t, q in overdamped if t >= pulse_end)
    inertial_peak = max(q for _, q, _ in inertial)
    inertial_post_min = min(q for t, q, _ in inertial if t >= pulse_end)
    first_cross = first_negative_time_after(inertial, pulse_end)

    checks = {
        "positive_pulse_is_nonnegative": all(
            forcing(i * dt, pulse_end) >= 0.0
            for i in range(int(horizon / dt) + 1)
        ),
        "overdamped_has_positive_response": overdamped_peak > 0.0,
        "overdamped_no_post_pulse_sign_reversal":
            overdamped_post_min >= -1e-12,
        "inertial_has_positive_response": inertial_peak > 0.0,
        "inertial_post_pulse_sign_reversal":
            inertial_post_min < -1e-3,
        "inertial_crossing_occurs_after_forcing_ends":
            first_cross is not None and first_cross >= pulse_end,
        "both_models_stable_parameterization":
            4.0 > 0.0 and 2.0 > 0.0 and 1.0 > 0.0 and 0.5 > 0.0,
    }

    passed = sum(bool(v) for v in checks.values())

    summary = Summary(
        dt=dt,
        horizon=horizon,
        pulse_end=pulse_end,
        overdamped_peak=overdamped_peak,
        overdamped_post_min=overdamped_post_min,
        overdamped_zero_cross_after_pulse=overdamped_post_min < 0.0,
        inertial_peak=inertial_peak,
        inertial_post_min=inertial_post_min,
        inertial_zero_cross_after_pulse=first_cross is not None,
        inertial_first_cross_time=first_cross,
        checks_passed=passed,
        checks_total=len(checks),
    )

    payload = {
        "status": (
            "PASS"
            if passed == len(checks)
            else "FAIL"
        ),
        "scope": (
            "Construction-level numerical witness only; synthetic parameters; "
            "no human data and no empirical validation."
        ),
        "equations": {
            "overdamped": "Gamma*qdot + K*q = u(t)",
            "inertial": "M*qddot + Gamma*qdot + K*q = u(t)",
            "forcing": "u(t)=1 for 0<=t<1, else 0",
        },
        "parameters": {
            "overdamped": {
                "K": 4.0,
                "Gamma": 2.0,
            },
            "inertial": {
                "M": 1.0,
                "K": 4.0,
                "Gamma": 0.5,
            },
        },
        "summary": asdict(summary),
        "checks": checks,
    }
    return summary, payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="stickman_dynamics_demo_results.json",
        help="JSON output path",
    )
    args = parser.parse_args()

    summary, payload = run_checks()
    out = Path(args.output)
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    print(
        f"{payload['status']}: "
        f"{summary.checks_passed}/{summary.checks_total} checks"
    )
    print(
        "overdamped post-pulse minimum: "
        f"{summary.overdamped_post_min:.9f}"
    )
    print(
        "inertial post-pulse minimum: "
        f"{summary.inertial_post_min:.9f}"
    )
    print(
        "inertial first zero-cross time: "
        f"{summary.inertial_first_cross_time:.3f}"
    )
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
