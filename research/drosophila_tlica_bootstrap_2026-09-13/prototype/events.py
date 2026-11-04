"""Dependency-free event schema for the Drosophila × TLICA bootstrap.

This module is deliberately conservative:
- phi defaults to undefined;
- rho defaults to undefined;
- sigma is structured provenance, not a scalar;
- mu is an explicit probe set;
- no consciousness/truth/selfhood aggregate score exists.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class ClaimStatus(str, Enum):
    DISCLOSED = "disclosed"
    CORROBORATED = "corroborated"
    OBSERVED = "observed"
    CONJECTURED = "conjectured"
    UNVERIFIED = "unverified"
    DARK = "dark"
    REFUTED = "refuted"


class CoordinateState(str, Enum):
    UNDEFINED = "undefined"
    CANDIDATE = "candidate"
    CALIBRATED_PROXY = "calibrated_proxy"
    DIRECT = "direct"


@dataclass(frozen=True)
class TransformStep:
    name: str
    version: str
    parameters: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class SourceMap:
    """Raw/path-adjusted provenance for sigma/source-map analysis."""

    world_source: str
    sensor: str
    target: str
    transform_chain: List[TransformStep] = field(default_factory=list)
    ambiguities: List[str] = field(default_factory=list)
    calibration_status: str = "unverified"


@dataclass(frozen=True)
class ProbeSet:
    """Explicitly available probes; this is mu metadata, not a truth score."""

    probes: List[str] = field(default_factory=list)
    unavailable: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class CoordinateValue:
    state: CoordinateState
    value: Optional[float] = None
    basis: Optional[str] = None

    def validate(self, name: str) -> None:
        if self.state == CoordinateState.UNDEFINED:
            if self.value is not None:
                raise ValueError(f"{name}: undefined coordinate cannot carry a value")
            return

        if self.value is None:
            raise ValueError(f"{name}: {self.state.value} coordinate requires a value")
        if not 0.0 <= self.value <= 1.0:
            raise ValueError(f"{name}: value must be in [0, 1]")
        if not self.basis:
            raise ValueError(f"{name}: defined value requires an explicit basis")


@dataclass(frozen=True)
class Diagnostics:
    coherence: Optional[float] = None
    independence: Optional[float] = None
    discrimination: Optional[float] = None

    def validate(self) -> None:
        for name, value in asdict(self).items():
            if value is not None and not 0.0 <= value <= 1.0:
                raise ValueError(f"{name}: diagnostic must be in [0, 1]")


@dataclass(frozen=True)
class TLICAEvent:
    run_id: str
    step_index: int
    world_time_s: float
    brain_time_s: float
    kind: str
    raw: Dict[str, Any]
    sigma: SourceMap
    mu: ProbeSet
    kappa: CoordinateValue = field(
        default_factory=lambda: CoordinateValue(CoordinateState.UNDEFINED)
    )
    phi: CoordinateValue = field(
        default_factory=lambda: CoordinateValue(CoordinateState.UNDEFINED)
    )
    rho: CoordinateValue = field(
        default_factory=lambda: CoordinateValue(CoordinateState.UNDEFINED)
    )
    diagnostics: Diagnostics = field(default_factory=Diagnostics)
    epistemic_status: ClaimStatus = ClaimStatus.OBSERVED
    assumptions: List[str] = field(default_factory=list)
    controls: List[str] = field(default_factory=list)
    upstream: Dict[str, str] = field(default_factory=dict)

    def validate(self) -> None:
        if not self.run_id:
            raise ValueError("run_id is required")
        if self.step_index < 0:
            raise ValueError("step_index must be non-negative")
        if self.world_time_s < 0 or self.brain_time_s < 0:
            raise ValueError("times must be non-negative")
        if not self.kind:
            raise ValueError("kind is required")

        self.kappa.validate("kappa")
        self.phi.validate("phi")
        self.rho.validate("rho")
        self.diagnostics.validate()

    def to_dict(self) -> Dict[str, Any]:
        self.validate()
        out = asdict(self)
        out["kappa"]["state"] = self.kappa.state.value
        out["phi"]["state"] = self.phi.state.value
        out["rho"]["state"] = self.rho.state.value
        out["epistemic_status"] = self.epistemic_status.value
        return out
