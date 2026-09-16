# Archive validation

The baseline repository at `34768a437eda09f076018f0042818dcf3098a41d` passed `make validate`: 1,205 local Markdown links across 189 files, self-containment, and terminology pins. This was checked before adding the archive.

The preservation checker runs from the repository root:

```bash
python3 research/quiet_quitting_manifesto_2026-09-16/checks/verify_archive.py
make validate
```

The [machine-readable preservation result](preservation-result.json) records the final source-integrity run. The checker verifies every manifest-listed source path, byte count and SHA-256; the documented eleven manuscript versions; four hash bindings taken from historical audits; all six ZIPs and all 43 member representations; and the exact strings in both prompt appendices. Its controls accept an unchanged temporary copy, reject a same-length single-byte mutation, and reject a missing file. No preserved source is edited by those controls.

The [PDF inventory](pdf-inventory.json) records read-only parsing of the thirteen archived PDF paths. Selected visual inspections of v1.4, v1.5.3 and v1.5.4 are documented below; this is not a fresh rendering certification of every historical page. The original PDFs, TeX and Markdown remain unchanged, including any old layout defects.

The final [repository-validation output](repository-validation.txt) records the link, self-containment and term-pin checks after the additions. These repository checks resolve local files but do not verify heading anchors, external source truth, historical release clearance, PDF accessibility, or completeness of missing conversations.

## Scope

This is an archive, so the validation goal is faithful preservation, navigability and explicit evidence boundaries. Historical “PASS” statements inside old audits describe their original runs; they are not presented as new runs. No workplace experiment, statistical model validation, source re-audit, main-branch merge or external publication was performed by this checker.

## Selected visual inspection, 2026-09-16

Rendered and inspected physical page 1 of v1.4 and v1.5.3, and physical pages 3, 27 and 28 of v1.5.4. These cover the two title treatments, the latest preamble, provenance/AI disclosure and final notes. Text was legible and no clipping or overlap was observed on those five pages. The thirteen PDF paths parse successfully; the latest v1.5.4 is 28 physical pages, while v1.5.3 is 27. Uninspected pages retain their historical status.

## Editorial and prompt review

A separate source-comparison pass found no fabricated quotation among the ten M/Q payloads and verified the uploaded handoff bytes. Review corrections clarified that the early threshold recurrence already included recovery, supplied Q01's separate timestamp provenance, preserved the identity-wages attribution, and marked superseded v2.0 parking-lot choices. These checks use overlapping source provenance and do not amount to independent empirical corroboration.
