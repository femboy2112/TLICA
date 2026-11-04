#!/usr/bin/env python3
"""Synthetic smoke test before any heavy fly dependencies are installed.

This is NOT a fly simulation. It only proves that the event/provenance contract can
represent a sensory-contact event without inventing phi or rho.
"""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from events import (  # noqa: E402
    ClaimStatus,
    CoordinateState,
    CoordinateValue,
    ProbeSet,
    SourceMap,
    TLICAEvent,
    TransformStep,
)
from recorder import EventRecorder  # noqa: E402


def build_event() -> TLICAEvent:
    return TLICAEvent(
        run_id="synthetic-0001",
        step_index=7,
        world_time_s=0.105,
        brain_time_s=0.105,
        kind="sensory_drive",
        raw={
            "modality": "odor",
            "left_antenna_concentration": 0.8,
            "target_flywire_ids": [101, 102, 103],
        },
        sigma=SourceMap(
            world_source="synthetic odor source A",
            sensor="left antenna synthetic receptor bank",
            target="FlyWire ORN placeholder population",
            transform_chain=[
                TransformStep(
                    name="synthetic_linear_odor_encoder",
                    version="0.0.1",
                    parameters={"gain_hz_per_unit": 100.0},
                )
            ],
            ambiguities=["placeholder neuron IDs; not biological mapping"],
            calibration_status="synthetic-only",
        ),
        mu=ProbeSet(
            probes=["sensor_off", "source_swap", "direct_neural_injection"],
            unavailable=["validated_internal_verification_pathway"],
        ),
        kappa=CoordinateValue(
            state=CoordinateState.CALIBRATED_PROXY,
            value=0.8,
            basis="synthetic normalized present transduced drive",
        ),
        # These remain undefined on purpose.
        phi=CoordinateValue(state=CoordinateState.UNDEFINED),
        rho=CoordinateValue(state=CoordinateState.UNDEFINED),
        epistemic_status=ClaimStatus.OBSERVED,
        assumptions=["synthetic event only; no biological inference"],
        controls=["zero-input null", "matched-amplitude source swap"],
        upstream={"schema": "bootstrap-0.1"},
    )


def main() -> None:
    event = build_event()
    event.validate()

    with tempfile.TemporaryDirectory(prefix="tlica-fly-") as tmp:
        path = Path(tmp) / "events.jsonl"
        recorder = EventRecorder(path)
        recorder.append(event)
        payload = json.loads(path.read_text(encoding="utf-8"))

        assert payload["phi"]["state"] == "undefined"
        assert payload["rho"]["state"] == "undefined"
        assert payload["kappa"]["value"] == 0.8
        print(json.dumps(payload, indent=2, sort_keys=True))
        print(f"sha256={recorder.sha256()}")


if __name__ == "__main__":
    main()
