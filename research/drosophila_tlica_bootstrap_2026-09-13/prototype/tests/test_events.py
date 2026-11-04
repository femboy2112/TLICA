from __future__ import annotations

import sys
import unittest
from pathlib import Path

PROTOTYPE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROTOTYPE))

from events import (  # noqa: E402
    CoordinateState,
    CoordinateValue,
    ProbeSet,
    SourceMap,
    TLICAEvent,
)


class CoordinateTests(unittest.TestCase):
    def test_undefined_phi_cannot_have_value(self) -> None:
        value = CoordinateValue(CoordinateState.UNDEFINED, value=0.5)
        with self.assertRaises(ValueError):
            value.validate("phi")

    def test_defined_rho_requires_basis(self) -> None:
        value = CoordinateValue(CoordinateState.CANDIDATE, value=0.5)
        with self.assertRaises(ValueError):
            value.validate("rho")

    def test_calibrated_kappa_accepts_declared_basis(self) -> None:
        value = CoordinateValue(
            CoordinateState.CALIBRATED_PROXY,
            value=0.25,
            basis="normalized present sensor drive",
        )
        value.validate("kappa")


class EventTests(unittest.TestCase):
    def test_minimal_event_keeps_phi_and_rho_undefined(self) -> None:
        event = TLICAEvent(
            run_id="test-run",
            step_index=0,
            world_time_s=0.0,
            brain_time_s=0.0,
            kind="null",
            raw={},
            sigma=SourceMap(
                world_source="null",
                sensor="none",
                target="none",
            ),
            mu=ProbeSet(probes=["null"]),
        )
        payload = event.to_dict()
        self.assertEqual(payload["phi"]["state"], "undefined")
        self.assertEqual(payload["rho"]["state"], "undefined")

    def test_out_of_range_coordinate_fails(self) -> None:
        event = TLICAEvent(
            run_id="test-run",
            step_index=0,
            world_time_s=0.0,
            brain_time_s=0.0,
            kind="bad-kappa",
            raw={},
            sigma=SourceMap(world_source="x", sensor="x", target="x"),
            mu=ProbeSet(),
            kappa=CoordinateValue(
                CoordinateState.CALIBRATED_PROXY,
                value=1.2,
                basis="bad synthetic value",
            ),
        )
        with self.assertRaises(ValueError):
            event.validate()


if __name__ == "__main__":
    unittest.main()
