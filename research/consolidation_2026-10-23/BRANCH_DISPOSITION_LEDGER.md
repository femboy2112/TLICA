# Branch Disposition Ledger — Consolidation Round 2026-10-23

**Status:** Operational audit artifact for the 2026-10-23 consolidation round. Not a theory
document; adds no foundation commitment. Produced by direct inspection of Git state, not from
any prior session's audit.

**Inspected main:** `4dbd0e5` (`docs(wiki): fill out the front door …`).
**Baseline `make validate`:** PASS (exit 0) — 2098 links resolve across 430 files; self-containment
clean; 26 watched terms pinned.

## Method and a caught error

For each branch the **effective content integration** was computed from blob identity, not from
commit ancestry — divergent history is not the same as missing content. Each file changed versus
the branch's merge-base with `main` was classified:

- `SAME` — blob byte-identical to the file on `main` (already integrated);
- `DIFF` — file exists on `main` with a different blob (a real modification);
- `NEW` — path absent on `main` (genuinely new content).

**Correction recorded (anti-laundering):** the first classifier used `git rev-parse main:<path>`
*without* `--verify`, which echoes its argument for an absent path instead of returning empty, so
genuinely-`NEW` files were mislabeled `DIFF`. Caught because the classifier's "already on main"
verdict for the One-Ring dossier contradicted `git ls-tree -r main` ("none on main"). The device
was fixed to test existence with `git cat-file -e`; every count below is from the corrected run.
`SAME` counts were trustworthy throughout (both sides must hash to a real blob).

## Summary table

Ahead/behind are relative to `main` at `4dbd0e5`. "Integration" is the corrected per-file
classification. "Gate" marks what blocks a disposition.

| Branch | Head | Ahead/Behind | Integration | Disposition | Gate |
|---|---|---|---|---|---|
| `research/one-ring-thousand-dominoes-session-2026-10-21` | `f317b43` | 37 / 0 | 24 NEW + 1 index DIFF | **LAND (research-tier)** | run witnesses; privacy re-check |
| `research/kin-1-11-egalitarian-spiritual-field-manual-2026-10-22` (PR #13) | `ba27d2d` | 10 / 0 | 4 NEW + 2 nav DIFF | **HOLD** | author review — normative doctrine |
| `research/phenomenological-integration-2026-09-12` | `200e83a` | 1 / 351 | 6 NEW | **HOLD** | **sensitive first-person transcript** |
| `moreish-wwjd-moral-actuator-2026-09-14` | `085e6fc` | 6 / 336 | 5 NEW + 1 DIFF | **HOLD** | Moreish paused; provenance/sensitivity |
| `research/moreish-controller-mindfulness-bridge-2026-09-29` | `797f804` | 7 / 208 | 1 NEW + 4 DIFF | **HOLD** | edits DOI-frozen `moreish_ontology_v1_0.md` |
| `research/differential-field-model-2026-09-12` | `747cf1b` | 5 / 351 | 1 NEW | **HOLD** | prior author-held |
| `research/drosophila-tlica-bootstrap-2026-09-13` | `fef7ac2` | 10 / 350 | 10 NEW | **HOLD** | separate test-bed / Phase-II hardware |
| `paper/facts-feelings-dissonance-filter` | `b425b88` | 5 / 208 | 3 NEW + 1 DIFF | **CANDIDATE (later wave)** | sensitivity/source check |
| `research/tlica-epic-path-geometry-2026-10-03` (PR #10) | `81b9408` | 23 / 53 | 17 SAME, 1 stale DIFF | **CLOSE PR, prune** | — |
| `research/vernacular-dynamics-2026-10-12` (PR #11) | `30f2d04` | 1 / 53 | 10 SAME, index DIFF | **CLOSE PR, prune** | — |
| `research/salience-frame-provenance-2026-10-14` (PR #12) | `cce9aef` | 8 / 53 | 7 SAME, index DIFF | **CLOSE PR, prune** | — |
| `research/adultclub-ontological-boundary-2026-10-11` | `cfbb211` | 6 / 53 | 14 SAME, index DIFF | **prune** | — |
| `research/affective-epistemic-compression-2026-10-03` | `cb4060d` | 2 / 53 | 3 SAME, 2 stale DIFF | **prune** | — |
| `research/recursive-epistemic-ratchet-2026-10-02` | `85886f2` | 2 / 53 | 1 SAME, index DIFF | **prune** | — |
| `research/quiet-quitting-manifesto-history-2026-09-16` | `99f658d` | 1 / 320 | 106 SAME, index DIFF | **prune** | — |
| `aletheia/cultural-interoperability-2026-09-22` | `e9e95cb` | 0 / 231 | fully in main | **prune** | — |
| `aletheia/semantic-wake-drag-2026-09-26` | `bb157c4` | 0 / 219 | fully in main | **prune** | — |
| `chosen-sincerity-costume-party-2026-09-20` | `4e85c13` | 0 / 291 | fully in main | **prune** | — |
| `moreish-final-draft-v0.2.8-2026-09-16` | `27514cb` | 0 / 316 | fully in main | **prune** | — |
| `moreish-publication-v1.0-2026-09` | `ff792e8` | 0 / 265 | fully in main | **prune** | — |
| `research/authority-compatible-frame-dynamics-2026-09-28` | `3aad16c` | 0 / 207 | fully in main | **prune** | — |
| `research/cinema-self-coupled-meaning-space-2026-10-01` | `0730250` | 0 / 200 | fully in main | **prune** | — |
| `research/cultural-realness-atlas-2026-09-22` | `be686ce` | 0 / 231 | fully in main | **prune** | — |
| `research/semantic-optics-yoneda-2026-10-01` | `35bd0fe` | 0 / 58 | fully in main | **prune** | — |
| `research/stickman-affective-dynamics-2026-09-26` | `9120fd9` | 0 / 217 | fully in main | **prune** | — |
| `specific-coherent-agency-2026-09-18` | `be38198` | 0 / 296 | fully in main | **prune** | — |
| `plan/tlica-consolidation-math-rendering-2026-10-23` (PR #14) | `dae27ce` | 4 / 0 | 4 NEW (`handoffs/`) | **keep until round done** | plan-only |

**Local-only branches** (not on `origin`): `research/foundation-errata-2026-09-12` (local scratch);
`research/manhattan-syndrome-ai-archetypes-2026-09-21` (content already on `main` per `dfb9242`, local
prune candidate); `consolidation/wave0-ledger-and-drift` (this round's working branch).

## Why the "open" PRs #10 / #11 / #12 are close-not-merge

The draft PRs read "open," but their dossier files are byte-identical on `main` (`SAME`). The only
deltas are `research/README.md` (the index, which `main` moved past as later dossiers landed) and, on
#10 and on affective-compression, one dossier file whose **newer** version is on `main`:
`4b9b4c3 fix(research): intake corrections for the 2026-10 dossier landings` is the last commit to
touch both `DUAL_PASS_STRUCTURED_POINTS.md` and the affective `README.md`. Merging these stale heads
would **revert `main`'s intake corrections.** Verdict: record that main integration superseded them,
close the PRs administratively, prune the branches. Do **not** merge.

## Next actions (sequenced, per disposition)

1. **Land** One-Ring + TLICA-HIGGS (research-tier) after running its witnesses and re-checking the
   dossier's own privacy-abstraction claim. Its `research/README.md` edit is a clean superset of
   main's index (branch is `0 behind`).
2. **Close** PR #10/#11/#12 with a recorded supersession note; **prune** the fully-integrated and
   index-only-drift branches above — *author's call* (branch deletion on a public remote).
3. **Hold** KIN-1-11, phenomenological-integration (sensitive), the Moreish-touching branches, the
   differential-field and drosophila branches — each behind its named gate.
4. **Triage** facts-feelings in a later wave (candidate research-tier land pending a sensitivity/source
   pass).

*Branch heads and PR states must be re-checked immediately before any merge, close, or prune — this
ledger is a snapshot of `4dbd0e5`.*
