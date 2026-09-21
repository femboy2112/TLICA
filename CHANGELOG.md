# Changelog

A human-readable history of the TLICA archive. The authoritative record is the
git log; this file groups it into meaningful cycles. Dates are the commit dates.
The **foundation** (Files 0–5) was frozen at v5.3.3 from initialization through
2026-09-13, when the v5.4.x–v5.5.x line seated a dynamical apparatus (current: **v5.5.0**,
*main-but-experimental*); the settled v5.3.3 foundation is retained read-only at
`foundation/previous_v5.3.3/`. Earlier entries concern the wiki, the application
papers, and repository tooling.

## 2026-09-20 — Moreish v1.0.1: preprint hardening (hedges + closed novelty flanks)

A patch over the frozen v1.0 (tag `moreish-v1.0`), re-frozen as the public preprint and tagged
`moreish-v1.0.1`. Foundation (v5.5.1) untouched; `make validate` PASS; preprint PDF 22 pages, 0
dropped glyphs.

### Changed
- **Three overclaim sentences hedged** in the manuscript master and the canonical paper:
  "removes the ability to override" → "reduces — and under sufficiently severe depletion may remove";
  "stops being a deliberation" → "can cease to require the same deliberative effort";
  "the joke proves that integration occurred" → "the joke marks that integration occurred".
- **Two closest novelty flanks closed** (cite-and-distinguish, Crossref-verified field-by-field):
  Alchourrón, Gärdenfors & Makinson (1985) — AGM belief change is orthogonal normative logic, not the
  owner of the ratchet's psychological threshold asymmetry; Taber & Lodge (2006) — an adjacent,
  population-level instantiation of differential evidential treatment, distinct from Moreish's
  idiographic claim. Reference list renumbered 1→28; Sutton & Barto made a clickable cite; Dostoevsky
  given a Part-level locus (*Notes from Underground*, Part I); the Varela/Shear method reference tightened.
- **Canonical `applications/moreish_ontology_v1_0.md` regenerated to v1.0.1** (same filename; carries
  the hedges and closed flanks). Publication apparatus (branch README, submission checklist, title
  page, source/novelty audit) reconciled to the frozen/merged state.

### Added
- **Tag** `moreish-v1.0.1` marks the frozen preprint commit.

### Note — double-blind cut
- The anonymized journal cut was hardened separately: the branded framework vocabulary (Mode-B
  projection, slack, imprinting, identity-correlation) neutralized alongside the TLICA name, and a
  neutral working title adopted for anonymized review; the blind build's identity guard now fails
  loudly on any fingerprint regression. By author direction this cut is kept as a **local
  journal-submission artifact and is not pushed to the public tree**, so its neutral title stays
  un-searchable. (An earlier blind file remains on `main` from the v1.0 landing, pending an author
  cleanup decision.)

### Unchanged
- **Foundation** v5.5.1 byte-identical. **Canonical v0.2.9 retained.** The §11 TLICA quarantine and
  the AI-provenance floor hold.

## 2026-09-20 — Moreish v1.0: frozen, brought to main, promoted to canonical

Publication-hardened the Moreish paper to **v1.0**, froze it (tag `moreish-v1.0`), brought the
publication workstream to `main`, and promoted v1.0 to the canonical application paper. Foundation
(v5.5.1) untouched.

### Added
- **New canonical application paper** `applications/moreish_ontology_v1_0.md` — the frozen v1.0 body
  with the app-tier front-matter block. Over v0.2.9 it adds a method/claim-boundary section, an
  adjacent-literature / novelty-boundary section (integration graded CONJECTURED), the costume-party
  developmental root (§2.5), the name "TLICA" withheld until §11, an inline Bellman (1957) cite at the
  Greedy Integral, a clickable numbered reference apparatus, and the "really fucking moreish" ending.
  Journal-submission apparatus (title page, ORCID, corresponding-author, Statements and Declarations)
  and the double-blind cut live with the publication master, not in the app-tier paper.
- **Publication workstream on main** `research/moreish_ontology_2026-09-13/publication_v1_0/` — the
  frozen manuscript master, submission checklist, AI provenance/disclosure, source & novelty audit,
  venue/submission notes, title-page scaffold, and a double-blind (anonymized) manuscript cut.
- **Tag** `moreish-v1.0` marks the frozen commit.

### Changed
- **v0.2.9 marked superseded** (retained as immediate predecessor; not deleted).
- **Registration surfaces repointed** to v1.0: `README.md` (narrative + application table),
  `docs/applications.md`, and the research dossier (`research/README.md`).

### Unchanged
- **Foundation** v5.5.1 byte-identical. **Canonical v0.2.9 retained.** The AI-provenance floor and
  the §11 TLICA quarantine hold.

## 2026-09-17 — Moreish promoted to its final draft (v0.1.0 → v0.2.9)

Promoted the author's finished Moreish draft to the canonical application paper. The final-draft
lineage `v0.2.8 → v0.2.9` had been merged research-tier (`722639b`/`92fbaea`) and surfaced on the
wiki (`779155f`); on author direction, **v0.2.9 replaces v0.1.0 as the application paper**.

### Changed
- **New application paper** `applications/moreish_ontology_v0_2_9.md` — the v0.2.9 body verbatim
  (three sensors: Underground Super Hans, Pavlov's Veruca, Jesus-without-root-access; the Greedy
  Integral Problem, the epistemic ratchet, the council meeting; TLICA bridge quarantined to §11),
  with the application-paper front-matter block re-attached (status / foundation-impact: none /
  epistemic-status / authorship).
- **Retired** `applications/moreish_ontology_v0_1_0.md` (the 2026-09-14 first draft; superseded, git
  history retained).
- **Registration surfaces repointed** to v0.2.9: `README.md` (narrative + application table),
  `docs/applications.md`, `docs/README.md`, the wiki page `docs/app-moreish-ontology.md`, and the
  research dossier (`research/README.md`, its dir README, and the four apparatus files).

### Unchanged
- **Foundation** v5.5.1 byte-identical — no new primitive, coordinate, mode, or law. The paper
  *applies* existing machinery (Mode-B projection §8.9, slack §8.11).
- **Raw Providence provenance** stays research-tier on branch `moreish-wwjd-moral-actuator-2026-09-14`,
  off `main`.
- `make validate`: OK (links + self-containment + term pins).

## 2026-09-16 — Quiet Quitting Manifesto archive internalized (research-tier + public page)

Integrated the recovered *Ethical Quiet Quitting Manifesto* history from branch
`research/quiet-quitting-manifesto-history-2026-09-16` (based on `34768a4`, foundation v5.5.0).
The manifesto is Leah's own work (disclosed AI assistance); it is preserved as an independently
readable historical archive, **not** rewritten into TLICA terms.

### Moved onto canonical surfaces
- **Research dossier** `research/quiet_quitting_manifesto_2026-09-16/` (106 files) — the self-contained
  archive: eleven numbered manuscripts (`.md`/`.tex`/`.pdf`), the rejected v2.0 and preliminary-v1.5
  directions, working drafts, editorial audits, source ledgers, six release ZIPs (43 members), a
  public-companion draft, the complete uploaded nineteen-section editorial handoff, provenance JSON,
  and a repeatable byte-integrity checker. All historical source bytes preserved unchanged.
- **Research index** `research/README.md` — new dossier section (carried from the branch; its base was
  current `main`, so it applied without conflict).
- **New public wiki page** `docs/quiet-quitting-manifesto.md` — a plain-language page that presents the
  argument on its own terms, records the branching editorial history, and quarantines the TLICA bridge
  as *a translation, not a validation*.
- **Registration** — a Part-3 bullet in `docs/README.md` and a §9 research-notes block in `README.md`,
  both in the research-tier (not application-paper) style.

### Deliberately kept historical / NOT promoted
- **No application paper.** Not added to `Makefile` `PAPERS`, `docs/applications.md`, the `README.md`
  application tables, or `CITATION.md`. This is a historical archive, not a registered current paper.
- **No foundation change.** Foundation v5.5.0 byte-identical; no new coordinate, mode, or law.
- **No canonization by version number.** v1.4 stays the voice parent; v2.0 stays a *rejected* direction;
  the preliminary false-symmetry v1.5 stays a rejected draft; v1.5.4 is the latest *recovered* revision,
  **not** a newly approved release, and does not retroactively certify earlier conduct.
- **No executed outreach / publication.** The historical publication handoffs, draft companion, and
  proposed first-person messages remain *proposed copy and evidence*, not sent or published. Old
  author-clearance and venue gates are neither used to block the archive nor silently marked passed.
- **No fabricated recovery.** Partial conversation recovery is preserved with its fidelity classes; the
  missing August 27 quantitative companion is left missing, not reconstructed.

### Validation
- `python3 research/quiet_quitting_manifesto_2026-09-16/checks/verify_archive.py`: **PASS** — 86 source
  files (85 distinct hashes), 4 historical hash-bindings, eleven-version coverage, 6 ZIPs / 43 members,
  prompt-string integrity, and all three negative controls.
- Whole-repository `make validate`: **PASS** (local links, self-containment, term pins).
- Wiki mirror rebuilt (`make wiki-dry`) and the new page inspected: **no** display-math clipping
  regression (it carries no `$…$` or `$$…$$` at all); boundary links resolve to absolute GitHub URLs.

## 2026-09-16 — "When the Map Becomes a Mandate" internalized (draft application + Phase 1 provenance)

### Added
- **Application paper** `applications/when_the_map_becomes_a_mandate_v0_1_0.md` (v0.1.0, AI-assisted,
  author review pending) — a **documentary/case** application of TLICA to attention, institutional
  abstraction, and moral authorization in the writings of Ted Kaczynski. Not a phenomenon derived
  from the apparatus but a source-critical study, and pointedly **not a diagnosis, an endorsement, a
  clinical assessment, or a validated causal biography**. Central discipline: *explanation*,
  *practical evaluation*, and *moral authorization* held distinct even as they interact. Carries four
  conditional formal results (ρ not a force on the baseline law; negative evaluation ≠ representational
  absence; task-preserving institutional quotient can drop ethically load-bearing facts; descriptive
  premises do not entail a permission without a normative bridge), six scoped documentary conclusions,
  and keeps **six rival explanations live**; every causal claim CONJECTURED / UNVERIFIED.
- **Wiki page** `docs/app-map-becomes-mandate.md` — plain-language mirror, hedged at least as hard as
  the paper (no diagnosis, no endorsement, no foundation commitment).
- **Research provenance** (retained, byte-for-byte where historical):
  `research/kaczynski_focus_closure_2026-09-15/` (Phase 1 dossier — manuscript, 19-claim ledger,
  18-source register, prospective protocol, 10 development observations, offline validator + 14 tests)
  and `research/kaczynski_application_2026-09-15/` (application supplement — theory/source audit,
  claims/probes ledger, a 16-check executable with raw results). Registered in `research/README.md`.

### Changed
- **Registration surfaces** updated coherently: root `README.md` (§6 reach list + §9 application
  table), `docs/applications.md` (maturity block + reading-order item 12), `docs/README.md` (Part 2),
  `Makefile` (`PAPERS`), `CITATION.md` (application list). The paper's newer-theory cross-references
  (Self-Applied §3.4, Distributed Institutional Realization v0.2) resolve against current main.

### Validation
- New application executable: **16/16** tests pass; regenerated JSON reproduces the committed
  `RAW_RESULTS.json` (deterministic, substantive fields identical). Phase 1 validator: PASS; Phase 1
  unit tests: **14/14** pass. Whole-repository `make validate`: **PASS** (the drafting environment
  could not run this gate; it was run here). The paper's own honest disclosures that its *drafting*
  environment could not run the gate are preserved unchanged.

### Notes
- **Foundation v5.5.0 untouched; no new coordinate, mode, prerogative, or law.** No clinical,
  risk-profiling, or operational/tactical content is imported; the four propositions are conditional
  formal/logical results (the quotient criterion is a standard factorization fact), not psychological
  validation; the sixteen tests, 32 tracking pairs, eight-state quotient, and dependency removals are
  construction/integrity checks, not a blinded historical reanalysis. The TLICA author's own
  developmental history is not transported onto the subject.

## 2026-09-16 — Phenomenology–analogy–model–probe research method internalized (research-tier + public page)

### Added
- **Research dossier** `research/phenomenology_analogy_model_probe_loop_2026-09-15/` (5 files) — a
  written reconstruction of the author's recurring method for turning a felt pattern into a
  falsifiable model. One six-line author self-report (*Observed*) is unfolded into an auditable
  loop: *phenomenon → analogy → bridge contract → candidate structure → formal model → out-of-fit
  drive → risky prediction → discriminating probe → residual localization → revision*, under the
  firewall **analogy proposes candidate structure, mathematics propagates consequences, reality
  supplies warrant**. Load-bearing pieces preserved: the **bridge contract** `B=(b_O,b_R,b_I,b_D,b_neg)`
  with explicit non-transports (no declared bridge, no transported claim); the **fit-vs-holdout**
  provenance rule (`D_fit` cannot validate the construction it shaped); the **out-of-fit drive**
  (`u*` outside the motivating cases) as the generative hinge; predeclared pass/fail/ambiguous
  probes with controls and rivals; and residual **failure localization**. **Refuted** is an allowed
  terminal outcome; the loop is required never to be self-sealing. Carries a 25-claim ledger
  (C-001…C-025), the exact `AUTHOR_SEED.md`, and a `RECONCILIATION.md` audit against `main`.
- **`docs/research-method.md`** — public plain-language page *"From Felt Structure to Falsifiable
  Model"*: the loop, the bridge contract, the four warrant boundaries, the failure-localization
  table, and an explicit **common-provenance warning** (internal specimens are not independent
  corroboration). Linked from `docs/README.md` (Part 3) and registered in `research/README.md`.

### Changed
- **`README.md`** — a compact research-method pointer added to the research-notes section (front
  page kept un-bloated).

### Notes
- **Foundation v5.5.0 untouched; no new coordinate, mode, prerogative, or law.** Per the dossier's
  own reconciliation, this is a *research-methodology* object, not a selfhood primitive — promoting
  it into the foundation would be a category error. Epistemic statuses held exactly as authored:
  the decomposition is **Disclosed**; that the loop captures a substantial part of the author's real
  workflow is **Conjectured**; that using it explicitly improves research generally is **UNVERIFIED**
  (needs a prospective comparative study); the deeper cognitive reason analogy search is productive
  for this author is **Dark**. Existing repository artifacts that instantiate pieces of the loop
  (*Cave's Lagrange Points*, the motion-word audit, the institutional and developmental revisions)
  are labelled **specimens, not independent corroboration** — common project provenance.

## 2026-09-15 — Developmental substrate nonstationarity internalized (research-tier + Self-Applied refinement)

### Added
- **Research dossier** `research/developmental_substrate_nonstationarity_2026-09-15/` (6 files +
  a new `RECONCILIATION.md`) — the *moving-machine problem*: a developing I regulates through a
  substrate whose response-properties are themselves changing, so self-regulation is a moving-plant
  problem, not parameter estimation on a fixed machine. Registered in `research/README.md`.
- **`RECONCILIATION.md`** — Stage-1 audit: the moving-substrate premise is already a frozen
  commitment (the developmental window, `foundation/4_derived_concepts_and_predictions.md:85`), the
  machinery it leans on is all present (substrate capacity, focus split, source-opaque third-order
  affect, osmotic imprinting, v5.5.0 `G`), and **no coordinate** is added; the v5.3.3/v5.5.0 seam is
  resolved by split-layer integration.

### Changed
- **`applications/self_applied_architecture_prose_draft_v0_1.md`** — new subsection §3.4
  *"Developmental substrate nonstationarity: the moving-machine problem"* near Root II. **Route C
  (split-layer):** phrased against the paper's frozen v5.3.3 base, with a clearly-labelled
  current-foundation (v5.5.0 `G`) note. Root II is **preserved and regime-qualified** ("same Root II,
  different regime"), the crude "new blank neurons = noise" mechanism is **replaced** (Refuted as
  stated), source-map adequacy is kept separate from affective reality, adulthood is relative not an
  endpoint, and depression/recovery is kept a live co-cause. Carries an explicit
  OBSERVED/CORROBORATED/REFUTED/CONJECTURED/UNVERIFIED/DARK status block.
- **`docs/app-self-applied-architecture.md`** — plain-language mirror ("The moving machine"), hedged
  at least as hard as the paper.
- **`docs/substrate-focus-and-imprinting.md`** — a short, labelled developmental note (application-level,
  no coordinate, adulthood not static).

### Notes
- **Foundation v5.5.0 untouched; no new coordinate or primitive.** The tracking-load ratio
  `η_dev=τ_track/τ_S` is an application-level, UNVERIFIED, not-a-truth-score diagnostic. Population
  developmental neuroscience does not validate the individual autobiography; the coupled model stays
  CONJECTURED against five rivals; the dossier's specific primary citations await an independent
  verification pass (its own §7).

## 2026-09-15 — Distributed Institutional Realization internalized at v0.2 (quotient macrostate)

### Added
- **Canonical v0.2 manuscript** `research/distributed_institutional_realization_2026-09-15/MANUSCRIPT_DRAFT_V0_2_0.md`
  — replaces the institution *map* `𝕽_t(P,R,D,S)=I_t` with the **quotient macrostate**
  `I_t^T=[X_t]_{~_T}` of the micro-realization `X_t=(P_t,R_t,D_t)` under task-relative
  response-signature equivalence, with the situational field `S_t` external (entering only at
  activation). The v0.1 seed is retained as provenance.
- **Executed quotient demo** `quotient_demo.py` (+ results/tests) — Probe A of the v0.2 program,
  standard-library, deterministic, **12/12 self-checks**: six distinct micro-realizations collapse
  to three macrostates; the induced response map is single-valued and reproduces `Resp_T` on all
  36 `(X,s,u)` cells with zero mismatches (Proposition 1, executed); the quotient is strictly
  coarser than identity; approximate equivalence exhibited as non-transitive.

### Changed
- **Claim ledger** gains a v0.2 status block; **reconciliation** gains a v0.2 addendum. C-006 is
  split into a **Disclosed-and-executed** formal half (quotient ≠ tuple, exact factorization) and an
  **UNVERIFIED** empirical half (usefulness in real domains). The badge-door demo's role-substitution
  and ρ-inertness results are relabeled **construction-level** (not empirical), and the "2×2×2×2 grid"
  is relabeled a **serial-gate pipeline trace** (not orthogonal interaction evidence). C-008 stays
  Conjectured; C-025 stays UNVERIFIED; sheaf language stays gated.
- Surfaced across the plain-language wiki page (`docs/distributed-institutional-realization.md`),
  README §9, `docs/README.md` Part 3, and `research/README.md` — all corrected to the v0.2 framing.

### Notes
- **Foundation v5.5.0 untouched.** No application paper registered; the dossier remains research-tier.
  The disclosure is a formal-model result, **not** empirical corroboration.

## 2026-09-14 — *This Ontology Is Really Moreish* promoted to a mainline application paper

### Added
- **Application paper `applications/moreish_ontology_v0_1_0.md`** (first draft) — the Moreish
  self-application, promoted from the research-tier dossier to `applications/`. A "moreish"
  failure mode read as a control architecture: three sensors (adversarial skepticism,
  present-reward, sacrificial morality) that break when promoted from *sensor* to global
  *governor*; the Greedy Integral Problem and the epistemic ratchet. Carries the third
  (Jesus/WWJD) sensor and the epistemic-ratchet mechanism from the 2026-09-14 continuation.
  **Foundation untouched** (applies Mode-B projection, slack, steerable commitment; adds no primitive).
- Wiki page **`docs/app-moreish-ontology.md`** — plain-language walkthrough.
- Registered across README §6/§9, `docs/applications.md`, `docs/README.md` Part 2, and the
  Makefile `PAPERS` list.

### Changed
- Applied the two author-confirmed display-math repairs to the promoted paper (§4 greedy policy
  `:=`; §9 objective `− μI`), converted the manuscript's display math to `$$` delimiters for
  GitHub/PDF rendering (renders clean: 15 pp, 0 dropped glyphs), and added an application-paper
  status header. Prose otherwise byte-faithful to the author's text.
- The research dossier `research/moreish_ontology_2026-09-13/` is now the paper's **provenance
  and apparatus** (ledgers, formalism, worksheet, demo); its duplicate `MANUSCRIPT.md` was retired
  and its apparatus links redirected to the promoted paper.

### Notes
- The **raw Providence continuation** (source transcripts + clinical/biographical detail) is kept
  research-tier on branch `moreish-wwjd-moral-actuator-2026-09-14`, deliberately **off `main`**. The
  promoted paper carries the refined argument — substrate facts included — at the author's explicit
  direction.

## 2026-09-13 — Dynamical apparatus seated; foundation v5.3.3 → v5.5.0

*(Foundation edits under an ongoing external mathematical audit. The frozen v5.3.3
files are unchanged and now retained in-tree.)*

### Added
- **Dynamical apparatus** in the frozen core (**v5.4.0**): a reading of the architecture
  in motion — the reflexive-differential reading, the driven allostatic (never-settling)
  orbit, and slack — as Sections 8.9–8.11 (File 3), with the dynamical commitment in
  Section 2.10 (File 1). Additive; no prior commitment, coordinate independence, or
  exclusion altered.
- **Retained previous foundation** (`foundation/previous_v5.3.3/`) — the six v5.3.3 files,
  read-only, as a stable pre-dynamical fallback, with a landing note; linked from the README
  as the settled predecessor of the *main-but-experimental* v5.4.x–v5.5.x line.
- Wiki page **`docs/the-self-in-motion.md`** — plain-language walkthrough of the dynamical
  apparatus.

### Changed
- **Foundation v5.4.0 → v5.4.1** — corrective patch following the external audit:
  profile-space typing, the ρ-metric gradient convention, the substrate-death /
  non-equilibrium-steady-state distinction, Mode B read as self-sourced imprinting, and
  slack scoped as one margin of a family.
- **Foundation v5.4.1 → v5.4.2** — errata: the identity-correlation profile's codomain at
  Section 7.6 corrected from $[0,1)$ to $[0,1]$ (admitting the cogito's $\rho = 1$).
- **Foundation v5.4.2 → v5.4.3** — second corrective: Section 8.11's two senses of *Mode B*
  separated (the always-on *mechanism* vs. the *effective, recognizable firing* it produces),
  reconciling with the frozen Sections 4.6/4.7; "ability nonzero for any $t>0$" demoted from
  an entailment to a labeled modeling posit. Frozen File 2 text unchanged.
- **Foundation v5.4.3 → v5.4.4** — third corrective on the driven-orbit apparatus (Section 8.10):
  the over-strong "felt salience never settles" claim corrected to a bounded-driven-regime result
  — the state never comes to *rest at a fixed point* (derived), while the *felt magnitude* settles
  into a bounded orbit ($\limsup V \le \tau L/\gamma$; derived given the relaxation law), and
  "perpetually unsettled" is dropped as underived. Section 2.10 (File 1) matched, the wiki page
  updated, and the reading-guide Supersedes list disambiguated (it had read as crediting v5.3.3
  with the dynamical apparatus that v5.4.0 seated).
- **Foundation v5.4.4 → v5.5.0** — additive refinement of the Mode-B mechanism (Section 8.11): names
  the slow lived-I structure $G$ the reflexive operator rewrites (the metric $\rho = R(G)$ and the
  field-reading $f = F(G,\cdot)$ are two readings of it), and corrects the actuator account — Mode B
  moves the baseline by shifting the target $f$, not by a force on $\rho$ (which cancels from
  $\dot b = \gamma(f-b)$). Multi-stability located in $G$, not the scalar $V$; the cogito-anchor is
  preserved. No prior commitment, coordinate independence, or exclusion altered.
- **Version tags** — the foundation versions are now tagged and cited from `CITATION.md`:
  `v5.3.3` (settled pre-dynamical) and the current line (`v5.5.0`).
- README, `CITATION.md`, `Makefile`, and the wiki version markers moved to v5.5.0; the README
  and `CITATION.md` state the settled-vs-experimental split.

## 2026-09-13 — "This Ontology Is Really Moreish" research dossier

### Added
- **This Ontology Is Really Moreish** (`research/moreish_ontology_2026-09-13/`) — a light,
  self-deprecating on-ramp to TLICA (Underground Super Hans / Pavlov's Veruca / the Greedy
  Integral). Draft manuscript plus a fleshed dossier apparatus (`AUTHOR_INTENT_AND_HANDOFF.md`,
  `EVIDENCE_CLAIMS_AND_SOURCES.md`, `FORMALISM_AND_PROBES.md`) and a standard-library demo
  (`greedy_vs_option_demo.py` + results + tests). Research-tier, foundation untouched, author
  review pending; registered in `research/README.md`.

### Changed
- **Slack framing corrected** in the dossier (`c1aad40`) — the §5 low-slack argument re-grounded
  against the archive's developed *slack* construct.

## 2026-09-12 — Filter glossary headword

### Added
- A standalone **Filter** headword in `docs/glossary.md`, pinning the term as its own entry.

## 2026-09-10 — The Children of Our Enemies; wiki clarity pass

### Added
- **The Children of Our Enemies** (`research/children_of_our_enemies_2026-09-10/`) — a standalone
  research draft (author = Leah) on inherited conflict, goal-relative slack, and the conditions of
  durable victory, with a machine-checked §9 switched-system counterexample (`toy_models.py` +
  `validation.json`; largest eigenvalue of the alternation ≈ 1.26 > 1). Research-tier, v0.1.0,
  foundation untouched; surfaced in the README §9 and a wiki page.

### Changed
- **Wiki clarity pass** — added phenomenological on-ramps to the README + three application pages;
  a Tier-3 gloss-debt pass across the wiki, README, and research index; per-page "reads best
  after" prerequisite banners on the application pages; and fixed four terminology/notation bugs
  on the two profile pages.

## 2026-09-09 — Repository made public; work-in-progress notices

### Changed
- Repository made **public**. Added a **⚠ Work in progress** notice and a first-person **"Why this
  repository is public"** author-note to the README, and surfaced the research-tier dossiers into
  the front-door docs.

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
