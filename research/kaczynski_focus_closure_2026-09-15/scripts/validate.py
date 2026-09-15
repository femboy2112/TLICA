#!/usr/bin/env python3
"""Offline package integrity only; not historical or psychological validation."""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PIN = 'e925fec1897488038e9efc20769b9bce403fd6ea'
FORBIDDEN = re.compile(r'https?://github\.com/[^/\s)]+/TLICA/(?:blob|tree|raw)/[^)\s]+')
# Verified as paths in the pinned remote tree. This is NOT a full checkout check.
UPSTREAM = {
    '../../CITATION.md', '../../foundation/0_reading_guide.md',
    '../../foundation/3_formal_apparatus.md', '../../foundation/previous_v5.3.3/',
    '../../docs/three-coordinates.md', '../../docs/app-choice-as-filter.md',
    '../../docs/app-free-will.md', '../../applications/choice_as_filter_v0_1_0.md',
    '../../applications/free_will_v0_3_0.md',
}


def parse_date(value: Any) -> dt.date | None:
    """Return the lower bound of an ISO date/year/month; preserve null as unknown."""
    if value is None:
        return None
    if not isinstance(value, str) or not re.fullmatch(r'\d{4}(?:-\d{2}){0,2}', value):
        raise ValueError('date must be null or YYYY[-MM[-DD]]')
    bits = [int(x) for x in value.split('-')]
    return dt.date(*(bits + [1] * (3 - len(bits))))


def chronology_relation(candidate: Any, onset: Any) -> str:
    """Only separate nonoverlapping years here; same-year ordering is unresolved."""
    a, b = parse_date(candidate), parse_date(onset)
    if a is None or b is None or a.year == b.year:
        return 'ambiguous'
    return 'later' if a.year > b.year else 'earlier'


def validate_data(data: Any, sources: set[str], claims: set[str]) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ['root must be an object']
    if data.get('schema_version') != '0.1.0' or data.get('theory_base_commit') != PIN:
        errors.append('schema or theory pin changed without migration')
    if data.get('corpus_role') != 'development_only':
        errors.append('pilot must remain development_only')
    rows = data.get('records')
    if not isinstance(rows, list) or not rows:
        return errors + ['records must be a nonempty list']
    ids: set[str] = set()
    by_id: dict[str, dict[str, Any]] = {}
    required = {'id', 'source', 'family', 'actor_provenance', 'event_date',
                'report_date', 'locator', 'claim', 'observation', 'kind',
                'status', 'coordinates', 'analyst_pathway_state', 'development_set', 'date_note'}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            errors.append(f'row {index}: not an object')
            continue
        label = str(row.get('id', index))
        if required - row.keys():
            errors.append(f'{label}: missing fields {sorted(required - row.keys())}')
        ident = row.get('id')
        if not isinstance(ident, str) or not re.fullmatch(r'E\d{2}', ident) or ident in ids:
            errors.append(f'{label}: invalid or duplicate id')
        else:
            ids.add(ident)
            by_id[ident] = row
        if not isinstance(row.get('source'), str) or row.get('source') not in sources:
            errors.append(f'{label}: unknown source')
        if not isinstance(row.get('claim'), str) or row.get('claim') not in claims:
            errors.append(f'{label}: unknown claim')
        for key in ('family', 'actor_provenance', 'locator', 'observation', 'kind', 'date_note'):
            if not isinstance(row.get(key), str) or not row[key].strip():
                errors.append(f'{label}: missing text for {key}')
        if row.get('coordinates') != 'not_estimated':
            errors.append(f'{label}: numerical coordinates are not supported')
        if row.get('analyst_pathway_state') != 'unknown':
            errors.append(f'{label}: archival unknown must not become actor undefined-phi')
        if row.get('development_set') is not True:
            errors.append(f'{label}: pilot item cannot become a holdout')
        if row.get('status') != 'OBSERVED_RECORD_NOT_CAUSAL_FINDING':
            errors.append(f'{label}: pilot observation promoted beyond scope')
        try:
            event, report = parse_date(row.get('event_date')), parse_date(row.get('report_date'))
            # A later year is decisive; coarse within-year ordering is deliberately not inferred.
            if event and report and event.year > report.year:
                errors.append(f'{label}: historical report precedes represented event year')
        except ValueError as exc:
            errors.append(f'{label}: {exc}')
    if 'E01' not in by_id or 'E04' not in by_id:
        errors.append('chronology anchors E01 and E04 are required')
    else:
        try:
            relation = chronology_relation(by_id['E04'].get('event_date'), by_id['E01'].get('event_date'))
            if relation != 'later':
                errors.append('C03 requires a later E04; manuscript chronology must be revisited')
        except ValueError:
            pass  # The malformed date is already reported above.
    return errors


def main() -> int:
    try:
        source_text = (ROOT / 'SOURCES.md').read_text(encoding='utf-8')
        claim_text = (ROOT / 'CLAIM_LEDGER.md').read_text(encoding='utf-8')
        sources = set(re.findall(r'^## ([STL]\d{2})\b', source_text, re.M))
        claims = set(re.findall(r'^## (C\d{2})\b', claim_text, re.M))
        data = json.loads((ROOT / 'data/evidence.json').read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        return 1
    errors = validate_data(data, sources, claims)
    upstream_references: set[str] = set()
    files = sorted(ROOT.rglob('*.md'))
    for path in files:
        text = path.read_text(encoding='utf-8')
        if FORBIDDEN.search(text):
            errors.append(f'{path.name}: absolute self-repository link')
        for block in re.findall(r'\[([^\]\n]+)\]', text):
            for token in re.findall(r'\b[STLC]\d{2}\b', block):
                if token not in sources | claims:
                    errors.append(f'{path.name}: unresolved identifier {token}')
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if target.startswith(('https://', 'http://', '#', 'mailto:')):
                continue
            target = target.split('#', 1)[0]
            if target in UPSTREAM:
                upstream_references.add(target)
                continue
            if not (path.parent / target).exists():
                errors.append(f'{path.name}: missing local target {target}')
    if errors:
        for error in errors:
            print(f'FAIL: {error}', file=sys.stderr)
        return 1
    print(f'PASS: {len(data["records"])} development records; {len(sources)} sources/leads; {len(claims)} claims')
    print(f'PASS: dates, provenance fields, identifiers, scope guards, and {len(files)} Markdown files')
    print(f'PASS: local package links; {len(upstream_references)} upstream targets checked against pinned path inventory only')
    print('NOT RUN: whole-repository make validate (complete checkout unavailable)')
    print('NOT TESTED: historical causal hypotheses, clinical claims, and TLICA validity')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
