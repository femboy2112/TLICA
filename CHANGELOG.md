# Changelog

A human-readable history of the TLICA archive. The authoritative record is the
git log; this file groups it into meaningful cycles. Dates are the commit dates.
The **foundation** (Files 0–5) has been frozen at v5.3.3 since initialization;
entries below concern the wiki, the application papers, and repository tooling.

## 2026-08-09 — Shared Reality, Divergent Maps; research provenance tier

### Added
- **Shared Reality, Divergent Maps** (v0.1.0) — "Semantic Interoperability,
  Culture War, and Constraint-Closed Compromise." Models democratic politics as
  a contest among socially-learned representations: candidate "vibe" as a
  compressed, affectively weighted world-model, culture war as falling
  cross-group semantic interoperability, and repair as constraint-closed
  compromise built on an opposition checksum. Worked abortion and Goldwater-1981
  examples. First draft; the formal model and predictions are UNVERIFIED. Merged
  from its draft branch and registered across the README, `docs/applications.md`,
  `docs/README.md`, and a new wiki page
  `docs/app-shared-reality-divergent-maps.md` (kept neutral, with the author's
  stance attributed and the archive taking no position).
- **`research/`** — an un-indexed provenance tier for working notes and dossiers
  that feed the application papers. Not part of the primary reading path; carries
  its own `research/README.md`.

### Changed
- **This Is Water** — added §3.2.1, a fourth (interpersonal) function of liberal
  education, "education as semantic infrastructure," sourced from the research
  note and marked UNVERIFIED. Edited in place; no version bump; the frozen
  foundation is unchanged.
- **Shared Reality, Divergent Maps** — first-draft revision pass (in place):
  defined the hostile-control validation gate; reconciled the opposition checksum
  as a set with the strongest variable as its floor; renamed inter-mind
  *transport* to *transfer* to avoid collision with This Is Water's intra-mind
  transport; pinned "vibe" to the representation as distinct from resonance; and
  added §2.3 stating the paper's TLICA-adjacent (not TLICA-derived) coupling to
  the κ/φ/ρ coordinates, with source-map located against the archive's existing
  source-error discipline rather than a foundation coordinate.
- Converted the three `research/` dossiers' math delimiters from LaTeX
  `\[ \]` / `\( \)` to the archive's `$$` / `$` convention for GitHub rendering.

## 2026-08-06 — Tooling and two new papers

### Added
- **Validation harness** (`make validate`): `scripts/check_links.py` verifies
  every internal Markdown link resolves; `scripts/check_self_contained.py`
  enforces the self-containment invariant (no absolute self-repo GitHub URLs).
  Pure standard library — needs only `python3`.
- **PDF pipeline** (`make pdfs`): renders the current application papers to
  reading-copy PDFs via pandoc + lualatex (DejaVu Serif + DejaVu Sans Mono, for
  full Greek/subscript/symbol coverage). Markdown stays authoritative; PDFs are
  on-demand artifacts
  under `output/` and are not tracked. The build surfaces any dropped glyph so a
  missing symbol can never hide behind a clean exit code.
- **Repository hygiene**: `.editorconfig`, `.gitignore`, `CITATION.md`,
  and this `CHANGELOG.md`.
- **The Cave's Lagrange Points** (v0.1.0) — constriction and dual-fidelity
  integration, a companion to *Out of the Cave*; merged from its draft branch.
- **This Is Water: Truth-Respecting Choice** (v0.1.0) — a David Foster Wallace
  bridge, epistemic-to-agential "micro-periagoge"; merged from its draft branch.

### Changed
- Registered both new papers across the README, `docs/applications.md`,
  `docs/README.md`, and new wiki pages `docs/app-caves-lagrange-points.md` and
  `docs/app-this-is-water.md`.
- Removed an uncommitted external-dependency edit from the foundation, keeping it
  self-contained and frozen at v5.3.3.

## 2026-06-16 — The Self-Applied Architecture

### Added
- **The Self-Applied Architecture** — the autobiographical worked
  self-application, brought to a complete first draft (v0.1), with wiki page.

## 2026-06-15 — The Cold Frame reaches closed prose

### Added
- **The Cold Frame and Its Sources** v0.3.0, then v0.4.3 (fully closed prose;
  signed author's note on moral stance), with the wiki page rewritten to match.

## 2026-06-13 — Wiki, README, and the Cold Frame's first prose

### Added
- The `docs/` wiki: cross-linked concept pages, application-paper pages, and a
  glossary, then deepened with technical→colloquial translations throughout.
- **The Cold Frame** v0.2.0 — prose successor to the referent-routing skeleton.

### Changed
- Rewrote the README as a human-readable guide to the theory; reframed the
  READMEs and added the author's note.

### Fixed
- Broken and inconsistent notation formatting across the wiki.

## Initialization

### Added
- The TLICA archive: foundation v5.3.3 (Files 0–5) and the first six
  application papers.
