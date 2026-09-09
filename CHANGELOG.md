# Changelog

A human-readable history of the TLICA archive. The authoritative record is the
git log; this file groups it into meaningful cycles. Dates are the commit dates.
The **foundation** (Files 0–5) has been frozen at v5.3.3 since initialization;
entries below concern the wiki, the application papers, and repository tooling.

## 2026-09-09 — Actualization / recognition dossier landed on main

*(Merged `--no-ff`: `agent/geometry-of-actualization-2026-09-07`,
`agent/actualization-recognition-2026-09-09`, `agent/idubbbz-hyde-paper-2026-09-09`,
`agent/four-horsemen-postmortem-2026-09-09`, plus an integration commit.)*

### Added
- **Geometry of Actualization dossier** (`research/geometry_of_actualization_2026-09-07/`)
  — the Bataille/Dostoevsky/Wallace paper plus its immersion/correctable-commitment and
  traversability/steerable-commitment continuations. Research-tier, v0.1.0.
- **Depth Without Capture** (`research/actualization_recognition_2026-09-09/`) — recognition
  as faithful bounded reconstruction; personhood not the residual beyond the model.
- **Inside Out and Reflected** (`research/idubbbz_hyde_paper_2026-09-09/`) — iDubbbz/Hyde as
  norm-referenced adjudication vs protocol-disrupting inquiry; authority allocation, not a duality.
- **A Post-Mortem of the Four Horsemen** (`research/four_horsemen_postmortem_2026-09-09/`) —
  warrant substitution across Hitchens/Dennett/Dawkins/Harris; the four diagnoses narrowed by
  evidence.
- All four registered in `research/README.md` under a grouped "Actualization / recognition
  dossier" section. Foundation (v5.3.3) untouched; nothing promoted to `applications/`.

### Changed
- **Self-containment fix** — the Four Horsemen source ledger's five absolute self-repo GitHub
  URLs (CTX-01/02/03) were relativized to in-archive paths so `make validate` stays green.

## 2026-08-10 — Interop publication workspace; authorship-protocol correction

*(Branch `pub/interop-workspace-setup-2026-08-10`, PR #3.)*

### Added
- **Interop publication workspace** (`publication/semantic-interoperability/`) — the
  controlled workspace for Paper I (Semantic Interoperability), first of the
  Interop → Genie → Cave sequence. Operational scaffolding only: a `README.md` with the
  program state and the single "next physically executable action" (write the native
  one-page thesis); an honest human–AI `provenance.md`; a per-concept
  `canonical_notes.md` template; a `claim_ledger.md` whose candidate claims (seeded from
  the research note) are all marked unowned and manuscript-ineligible pending Leah's
  ownership test; a `formal_ledger.md` seeded with pointers to the *real* schematic
  formulas in the interop note, every one labeled unvalidated; a `reading_ledger.md`
  starting from *Surfaces and Essences* with no fabricated page references; an empty
  `human_outline.md`; a `manuscript.md` marked **Leah-authored submission prose only**
  (zero generated prose); an `ai_use_log.md` that honestly logs this setup session; a
  `venue_matrix.md` porting only verified policies, each marked temporally unstable; and a
  `submission/` folder of templates whose `receipt.md` reads **NOT SUBMITTED**. No
  manuscript prose was written.

### Changed
- **Publication roadmap** (`research/publication_roadmap_interop_genie_cave_2026-08-10.md`)
  — corrected the authorship protocol. The earlier rigid rule ("100% of submission-facing
  prose written from a blank document without consulting AI-assisted prose") is replaced by
  an **epistemic-authorship / prosthesis standard**: Leah is the epistemic and final prose
  author and may consult her own verified notes, formulas, and ledgers, but may not
  outsource the judgment or the writing; the operative test is whether she can explain,
  defend, revise, or abandon every load-bearing claim without outsourcing the judgment. AI
  executive-function / ADHD prosthetic use is recognized explicitly in the §6 taxonomy,
  distinct from A4 generation of submission prose. The stronger requirements are preserved
  (citations personally verified; every load-bearing claim commandable by Leah; AI
  provenance truthful and logged; exact venue policy controls eligibility; submission, not
  acceptance, is the finish line). §5, §5.1, §6, Gate H2, both disclosure templates, the
  roadmap claim ledger, and the §40 workspace step were updated for consistency and to point
  at the new workspace. No foundation or application manuscript was touched.

## 2026-08-10 — Publication roadmap; citation hygiene

### Added
- **Publication roadmap** (`research/publication_roadmap_interop_genie_cave_2026-08-10.md`)
  — a Leah-authored provenance-tier dossier laying out the plan to bring the work to
  publishable form: a three-paper sequence (Semantic Interoperability → Genie/Severed
  Map → Out of the Cave, ordered by decreasing initial architecture-dependence), a
  human-authorship recovery protocol (the existing AI-assisted drafts are treated as
  research scaffolds, not submission manuscripts), an AI-use taxonomy and disclosure
  discipline, a venue/policy matrix, and a work-management scheme. Merged `--no-ff`
  from its agent branch to preserve authorship; the integration commit normalized its
  math delimiters to the archive `$$`/`$` convention, fixed a stale link to the renamed
  Shared Reality file, and escaped a literal `%` inside a math box. Renders 21pp/0
  dropped. Not part of the primary reading path (research tier).

### Fixed
- **Shared Reality, Divergent Maps** (in place, no version bump) — hyperlinked nine
  previously bare references, each verified against a primary source: Swann et al.
  (2012), Graham/Haidt/Nosek (2009), Clark & Wilkes-Gibbs (1986), Soss (1999), and
  Lind & Tyler (1988) to CrossRef-confirmed DOIs; Pew (2021), Cramer (2016), Rawls
  (1993), and Habermas (1996) to their publisher/primary pages. Sourced the §4.1
  Reconstruction sketch to the U.S. House "Black Americans in Congress" essay,
  matching the archival citations already used for the New Deal and civil-rights
  paragraphs. No fabricated identifiers; `make validate` PASS, renders 32pp/0 dropped.

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
- **Shared Reality, Divergent Maps** — added §6, "The civic
  participation–disillusionment trap": the two-equilibria dynamics, the
  failed-acknowledgment → culture-war-migration bridge back to §5.1, and
  conditional civic loyalty as a constraint-closed repair carrying both
  opposition checksums, and its own robustness caveats. Rebuilt §13 into an operationalized empirical program
  (constructs table, per-study pass/fail/ambiguous criteria, the civic-trap
  predictions, and an explicit falsification section). Sections 6–15 renumbered
  by one. Absorbs `research/civic_participation_disillusionment_trap_2026-08-09.md`,
  previously deferred. In place; no version bump; still first-draft UNVERIFIED.
- **This Is Water** — §3.2.1: renamed the inter-mind "transported object" to a
  "concept transferred between minds," reserving *transport* for the paper's
  intra-mind epistemic-to-agential sense (§6), matching the sister paper's
  transport/transfer convention.
- **Shared Reality, Divergent Maps → v0.2.0** — version bump, renamed and
  re-registered across the README, `docs/`, and Makefile. This cycle: the
  *New York Jets* refinement to §6 (withdrawal is heterogeneous — the general
  public exits while a committed core keeps conditional loyalty, wiring the
  metaphor into the §6.4 repair); a new §6-through-§15-consistent **§13.8, "Existing
  evidence and where it cuts,"** folding in a three-lane literature-mining pass that
  grounds the descriptive premises (Soss 1999; Sjöberg/Mellon/Peixoto 2015;
  Johnson/Carlson/Reynolds 2023; Pew 2021; de Bruin et al. 2023) while honestly
  carrying the counter-evidence (the procedural-justice voice effect; the
  preference–behavior sorting gap of Mummolo & Nall 2017; the unfavorable
  affective-polarization base rate of Voelkel et al. 2023); a §12.4 extension
  recasting the voice effect as *emergent, accidental propaganda*; §15
  claim-ledger refinements; and the New Deal citation title corrected against the
  live source. Thirteen references added. Still first-draft UNVERIFIED.
- **`research/opposition_checksum_intervention_preregistration_2026-08-09.md`** —
  a new provenance-tier dossier: a full pre-registration of the flagship §13.4
  opposition-checksum study (three arms, delayed durability follow-up,
  pre-registered validity adjudication and decision rules), turning the sketched
  prediction into a runnable instrument.
- **Archive-wide LaTeX repair** — replaced the GitHub-incompatible `\operatorname`
  macro with `\mathrm` across five files (both application papers, *Out of the
  Cave*, and two research dossiers) so math renders on GitHub as well as in the
  lualatex PDF pipeline; fixed an unescaped-`$` parity break in *Differentiated
  Affect*'s changelog appendix.

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
