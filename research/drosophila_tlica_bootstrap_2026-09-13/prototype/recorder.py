"""Append-only JSONL recorder for TLICA fly events."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Iterable

from events import TLICAEvent


class EventRecorder:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, event: TLICAEvent) -> None:
        payload = event.to_dict()
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(payload, sort_keys=True, separators=(",", ":")))
            fh.write("\n")

    def append_many(self, events: Iterable[TLICAEvent]) -> None:
        for event in events:
            self.append(event)

    def sha256(self) -> str:
        digest = hashlib.sha256()
        with self.path.open("rb") as fh:
            for chunk in iter(lambda: fh.read(1024 * 1024), b""):
                digest.update(chunk)
        return digest.hexdigest()
