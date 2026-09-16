#!/usr/bin/env python3
"""Verify the recovered source archive; standard library only, no network.

Checks source bytes, historical hash bindings, source coverage, ZIP extraction
identity, prompt-string integrity, and negative controls. This does not verify
external claims, author clearance, PDF layout, or completeness of chat history.
"""
from __future__ import annotations
import hashlib
import json
import re
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HISTORICAL_BINDINGS = {
    'history/source_prompts/editorial_publication_handoff_2026-08-16.md':
        '70c05b09abc949dee0ab995c2d3e977f89c8875559af72c0be1fb03634b90be3',
    'originals/ethical_quiet_quitting_manifesto_v1_4.md':
        '44c7f40893b45d9682a7979892dbaccedd2ab846afbb282af11972b132614b66',
    'originals/ethical_quiet_quitting_manifesto_v1_5.md':
        'ef4babaa0b90a1f8af29e22ff03efb0a973db578d19a53e24a1a41bf1d613dea',
    'originals/ethical_quiet_quitting_manifesto_v1_5_3.md':
        '63f0d0da904ea6e2d26842c6ba7e9f96f2d7a78eba90fe01d1f6b64d58d274c9',
}

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def payload_errors(path: Path, size: int, expected: str) -> list[str]:
    if not path.is_file():
        return ['missing file']
    data = path.read_bytes()
    errors = []
    if len(data) != size:
        errors.append('size mismatch')
    if sha(data) != expected:
        errors.append('SHA-256 mismatch')
    return errors

def main() -> int:
    manifest = json.loads((ROOT/'provenance/ARTIFACTS.json').read_text())
    records = manifest['records']
    errors = []
    paths = [r['path'] for r in records]
    if len(paths) != len(set(paths)):
        errors.append('duplicate manifest path')
    if len(records) != 86:
        errors.append('source coverage differs from the documented 86-file recovery')
    for record in records:
        relative = Path(record['path'])
        path = ROOT/relative
        if relative.is_absolute() or '..' in relative.parts or path.is_symlink():
            errors.append(f'unsafe source path: {relative}')
            continue
        for error in payload_errors(path, record['bytes'], record['sha256']):
            errors.append(f'{relative}: {error}')

    actual = {str(p.relative_to(ROOT)) for directory in ['originals','working','history/source_prompts']
              for p in (ROOT/directory).rglob('*') if p.is_file()}
    if actual != set(paths):
        errors.append(f'source coverage mismatch: absent={sorted(set(paths)-actual)}, unlisted={sorted(actual-set(paths))}')
    expected_sums = ''.join(r['sha256']+'  '+r['path']+'\n' for r in records)
    if (ROOT/'provenance/SHA256SUMS').read_text() != expected_sums:
        errors.append('SHA256SUMS differs from the manifest')
    for rel, expected in HISTORICAL_BINDINGS.items():
        if sha((ROOT/rel).read_bytes()) != expected:
            errors.append(f'{rel}: historical hash binding failed')

    versions = {r['declared_version'] for r in records
                if re.fullmatch(r'originals/ethical_quiet_quitting_manifesto(?:_v[0-9_]+)?\.md', r['path'])}
    expected_versions = {'1.0','1.1','1.2','1.3','1.4','2.0','1.5','1.5.1','1.5.2','1.5.3','1.5.4'}
    if versions != expected_versions:
        errors.append('numbered manuscript coverage differs from the documented eleven versions')

    expected_members = {(m['zip'],m['member']): m for m in manifest['zip_members']}
    checked_members = set()
    zips = sorted((ROOT/'originals').glob('*.zip'))
    for path in zips:
        relative = str(path.relative_to(ROOT))
        with zipfile.ZipFile(path) as archive:
            if archive.testzip() is not None:
                errors.append(f'{relative}: CRC failure')
            for info in archive.infolist():
                if info.is_dir():
                    continue
                key = (relative, info.filename)
                checked_members.add(key)
                if key not in expected_members:
                    errors.append(f'{key}: unlisted ZIP member')
                    continue
                entry = expected_members[key]
                data = archive.read(info)
                if sha(data) != entry['sha256'] or len(data) != entry['bytes']:
                    errors.append(f'{key}: ZIP-member manifest mismatch')
                if data != (ROOT/entry['extracted_path']).read_bytes():
                    errors.append(f'{key}: extracted source differs from ZIP member')
    if checked_members != set(expected_members):
        errors.append('ZIP membership coverage mismatch')
    if len(zips) != 6 or len(checked_members) != 43:
        errors.append('package coverage differs from the documented six ZIPs / 43 members')

    evidence = json.loads((ROOT/'history/retrieved_evidence.json').read_text())
    for item in evidence['messages']+evidence['reported_quotations']:
        if sha(item['text'].encode()) != item['text_sha256']:
            errors.append(f"{item['id']}: retrieved-text hash mismatch")
        target = 'USER_PROMPTS_VERBATIM.md' if 'role' in item else 'RETRIEVED_QUOTATIONS.md'
        if item['text'] not in (ROOT/'history'/target).read_text():
            errors.append(f"{item['id']}: human-readable appendix does not preserve payload")

    # Exercise the actual file-check path on an unchanged copy, a same-length
    # one-byte mutation, and a missing source. Source artifacts are never edited.
    sample = (ROOT/'history/source_prompts/editorial_publication_handoff_2026-08-16.md').read_bytes()
    controls = {}
    with tempfile.TemporaryDirectory(prefix='qq-archive-control-') as tmp:
        path = Path(tmp)/'source.bin'
        path.write_bytes(sample)
        controls['unchanged_copy_accepted'] = not payload_errors(path,len(sample),sha(sample))
        path.write_bytes(bytes([sample[0]^1])+sample[1:])
        controls['same_length_mutation_rejected'] = 'SHA-256 mismatch' in payload_errors(path,len(sample),sha(sample))
        path.unlink()
        controls['missing_file_rejected'] = payload_errors(path,len(sample),sha(sample)) == ['missing file']
    if not all(controls.values()):
        errors.append('integrity control failed')

    report = {'status':'PASS' if not errors else 'FAIL','source_files':len(records),
        'source_bytes':sum(r['bytes'] for r in records),'distinct_source_hashes':len({r['sha256'] for r in records}),
        'historical_hash_bindings':len(HISTORICAL_BINDINGS),'numbered_manuscript_versions':sorted(versions),
        'zip_archives':len(zips),'zip_members':len(checked_members),'role_labeled_messages':len(evidence['messages']),
        'qualified_quotations':len(evidence['reported_quotations']),'controls':controls,'errors':errors,
        'boundary':'Artifact integrity and documented coverage only; no empirical validation, external source audit or complete transcript certification.'}
    print(json.dumps(report,indent=2))
    return 0 if not errors else 1

if __name__ == '__main__':
    sys.exit(main())
