# TLICA Research Frontier — Status Dashboard

**Purpose.** A living orientation map for returning to any TLICA research program after
weeks away and immediately recovering: *what question is open, what is actually
established, what failed, which rivals are live, the strongest current result, and the
next probe that could move the verdict.* It groups fronts by **conceptual program and
dependency**, not by date. For the dense detail behind each line, open that dossier's own
`CLAIM_LEDGER.md` / `README.md` and the per-front handoffs — this page is the navigator,
not a replacement for them.

**As of** 2026-10-23. **Foundation:** frozen at **v5.5.2** (`foundation/0..5_*.md`). All
fronts below are **research-tier** and change nothing in the foundation unless a gated
amendment is explicitly adopted. Status words follow the archive's ledger grammar:
**Derived** (proved from stated axioms), **Observed** (one clean run / witness), **Conjectured**
(honest guess, unproven), **Refuted** (a strong version was checked and failed), **UNVERIFIED**
(no outside test run). Current-state legend: 🟢 landed on main · 🟡 staged/verified, land pending ·
⏸ held (author/sensitivity gate) · 🔬 active edge.

---

## Program 0 — The dynamical substrate (the load-bearing core)

**Question.** Can TLICA's lived self-dynamics be written as an earned mathematical system —
felt salience, a driven baseline that chases a moving target, a slack gate, and a reflexive
actuator — rather than borrowed vocabulary?

**State.** This is the one program that has reached the **frozen foundation**: the dynamical
apparatus is seated as §8.9–8.11 (File 3) + §2.10 (File 1), v5.4.0→v5.5.2. **Strongest result
(Derived):** the driven allostatic orbit is bounded — `$\limsup V \le \tau L/\gamma$` — refuting
the earlier "felt salience never settles" overclaim; the Mode-B actuator moves the *target* by
rewriting the slow structure `$G$` (with `$\rho=R(G)$`, `$f=F(G,\cdot)$`), and `$\rho$` cancels
from the baseline law `$\dot b=\gamma(f-b)$`, so there is no anti-gradient force. **Biggest
obstruction / next probe:** Round 3 — basin/attractor structure and whether multi-well
set-points live in `$G$` (currently a labelled *open direction*, not asserted).

| Front | State | Strongest result | Path |
|---|---|---|---|
| Math-justification / dynamical substrate | 🟢 in foundation | bounded driven regime (Derived); Mode-B G-actuator | `foundation/5_*` §13.4, research math-justification notes |
| Differential field model | ⏸ held | full differential reformulation (REDESCRIPTION + 2 edges) | `research/differential_field_model_2026-09-12/WORKING_MODEL.md` |
| Stickman affective dynamics | 🟢 landed | substrate response *before* Mode B; overdamped-null vs 2nd-order Lagrangian (neither privileged) | `research/stickman_affective_dynamics_2026-09-26/` |

---

## Program 1 — Representation, transport, and provenance (what the coordinates are, and how they move)

**Question.** When meaning is carried across frames, contexts, and observers, what is
preserved, what is lost, and what is a provenance artifact rather than a fact?

**State.** The archive's most mathematically developed cluster. **Semantic Optics** carries
the heaviest formalism (categorical cybernetics; the Yoneda "moonshot"). **TLICA–EPIC** gives a
typed inferential-path-geometry diagram standard. Strongest results are **finite/conditional**,
not empirical; the recurring rival is "this is a re-description, not a mechanism."

| Front | State | Strongest result | Next probe | Path |
|---|---|---|---|---|
| Semantic Optics / Yoneda | 🟢 landed | categorical optics bridge; finite reparametrisation (conditional) | close the Yoneda-moonshot proof obligations in `THEOREM_STATUS.md` | `research/semantic_optics_2026-10-01/` |
| TLICA–EPIC path geometry | 🟢 landed | typed path algebra + dual-pass diagram standard | independent coder reproduces the diagram typing | `research/tlica_epic_path_geometry_2026-10-03/` |
| Salience / frame transport / lossy provenance | 🟢 landed | Stage-B coding/bridge rules (spec, frozen) | executable `records.py` validator + independent-coder pilot (owed) | `research/salience_frame_provenance_2026-10-14/` |
| Recursive epistemic ratchet | 🟢 landed | world-state updating vs compiled truth distinction | — | `research/recursive_epistemic_ratchet_2026-10-02/` |
| Semantic wake drag | 🟢 landed | τ_A/τ_C/τ_O, χ diagnostic (composed, no new primitive) | test the UNVERIFIED semantic-header `H=(G,I,R,Δ,B)` | `research/semantic_wake_drag_2026-09-26/` |
| Vernacular dynamics | 🟢 landed | lexicon formalism (research) | — | `research/vernacular_dynamics_2026-10-12/FORMALISM.md` |

---

## Program 2 — Identity, agency, and coupling (ρ, φ, and the specific self)

**Question.** How does identity-correlation ρ couple to reality-reading, and what is a
coherent, correctable, specific agency — distinct from ρ itself?

**State.** **Specific Coherent Agency (SCA)** is the precursor: agency normalized by an
operational effective self-dimension `$d_{self}$` — explicitly **not** ρ (that would be
ill-typed). Scalar η remains **UNVERIFIED**. Coupling direction (φ couples ρ→reality forward;
ρ couples φ backward/capture) is the live model.

| Front | State | Strongest result | Path |
|---|---|---|---|
| Specific coherent agency | 🟢 landed (local) | SCA = reality-coupled/self-resonant/correctable agency ÷ `$d_{self}$`; capability vector (E,M,D,R,X,C,S,O) | `research/specific_coherent_agency_2026-09-18/` |
| Authority-compatible frame dynamics | 🟢 landed | constraint reification + positive self-resonance | `research/` (authority-compatible dossier) |
| Affective epistemic compression | 🟢 landed | felt resolution ≠ epistemic resolution; competence/anger/probe-suppression | `research/affective_epistemic_compression_2026-10-03/` |
| Facts / feelings dissonance filter | ⏸ candidate | v0.1 evidence-filter paper (3 files, unmerged) | sensitivity/source pass → land research-tier | `research/facts_feelings_dissonance_2026-09-28/` (branch) |

---

## Program 3 — Social, institutional, and moral realization

**Question.** How do selves compose into institutions and moral situations without positing a
group mind, and how is an ethical invariant *transported* through hostile couplings without
being redefined away?

**State.** **Distributed institutional realization** gives the formal spine: an institution as a
**quotient macrostate** `$I_t^T=[X_t]_{\sim_T}$` — causally real via indexed people + typed
relations + artifacts, no group mind; demos executed (badge-door 14 checks + quotient 12 checks).
**One Ring / Thousand Dominoes** (staged this round) is the moral-agency front: ethical invariants
vs hostile social dynamics, first-domino causal accountability, referent routing vs moral
disengagement.

| Front | State | Strongest result | Next probe | Path |
|---|---|---|---|---|
| Distributed institutional realization | 🟢 landed (v0.2) | institution = response-signature quotient macrostate; factorization exact on 36 cells | C-006-empirical / C-025 (UNVERIFIED) | `research/distributed_institutional_realization_2026-09-15/` |
| One Ring / Thousand Dominoes | 🟡 staged | invariant-transport framing; narrative-causal coupling (10-test witness) | land; then outside-σ vs narrated-attribution probes | `research/one_ring_thousand_dominoes_2026-10-21/` |
| Cultural interoperability + realness probe | 🟢 landed | reality-grounded coexistence umbrella; music/realness probe | Stage-B `records.py` + independent-coder pilot (owed) | `research/cultural_interoperability_2026-09-22/` |
| Intergenerational conflict | 🟢 landed | dossier (research) | — | `research/children_of_our_enemies_2026-09-10/` |

---

## Program 4 — AI self-application and relational-failure archetypes

**Question.** What goes wrong when a TLICA-like system maps or weights reality badly — and can
the failure be stated as a falsifiable variable rather than a motive attribution?

**State.** **Manhattan vs Syndrome**: two opposite archetypes — Manhattan = good map, diluted
human weighting; Syndrome = correct referent, source-deformed meaning geometry. **Red line held:**
no consciousness/motive attribution; the core Syndrome deformation claim is **Conjectured**
(coupling Observed, deformation not). Freeze-prep landed; v1.0 tag + Zenodo DOI author-gated.

| Front | State | Strongest result | Next probe | Path |
|---|---|---|---|---|
| Manhattan / Syndrome archetypes | 🟢 landed (v0.4.1) | two typed archetypes; Probe E 21/21 synthetic | Probe E2 (real learner → C22); submission-day source re-verify | `research/manhattan_syndrome_ai_archetypes_2026-09-21/` |
| Grokking / toolkit-closure | 🟢 landed | Cl(Tools) closure dossier | — | `research/` (grokking dossier) |

---

## Program 5 — Developmental and phenomenological roots

**Question.** How does the regulating self form and change through a substrate that is itself
still changing, and what are the honest limits of first-person source material?

**State.** **Developmental substrate nonstationarity** reframes "new neurons = noise" (Refuted
as stated) into the moving-machine problem; adds no coordinate (`η_dev` is an app-level
UNVERIFIED diagnostic). **Costume party / chosen sincerity** is the Moreish developmental
precursor (shame-vs-disagreement AUTHOR-AFFIRMED; causal account CONJECTURED). The
**phenomenological-integration** material is **sensitive first-person dialogue** — held off
public main.

| Front | State | Strongest result | Path |
|---|---|---|---|
| Developmental substrate nonstationarity | 🟢 landed | moving-substrate premise already frozen; regime-qualified Root II | `research/developmental_substrate_nonstationarity_2026-09-15/` |
| Costume party / chosen sincerity | 🟢 landed | shame≠disagreement (author-affirmed); chosen sincerity = commitment≠submission | `research/costume_party_chosen_sincerity_2026-09-20/` |
| Phenomenology→analogy→model→probe method | 🟢 landed | reconstruction of the research loop (workflow object, no primitive) | `research/phenomenology_analogy_model_probe_loop_2026-09-15/` |
| Phenomenological integration | ⏸ held (SENSITIVE) | 6-file dossier incl. verbatim prompts | `research/phenomenological_integration_2026-09-12/` (branch) |

---

## Program 6 — Physics-analogy explorations (exploratory, newest)

**Question.** Can Higgs-mechanism *structure* (effective response-gap from coupling to a slow
background) be borrowed as a phenomenological analogy — explicitly without claiming physics?

**State.** **TLICA–HIGGS** (staged this round). **Strongest result (Observed/finite):** a
rank-one cross-context signature for a fixed-coupling single-field hypothesis, with a refutation
test, a dissipation identity, and a hostile counterexample to "heavier always means slower";
14/14 finite witness + 16-control causal-diagram witness. **Hard boundary:** the toy is a
mathematical analogy; **no physical Higgs mechanism is established** (empirical mechanism
CONJECTURED/UNVERIFIED). Distinguishes spectral mass/stiffness, friction/damping, and response
inertia — and does **not** confuse these with ρ, λ, φ, or phenomenal worth.

| Front | State | Strongest result | Next probe | Path |
|---|---|---|---|---|
| TLICA–HIGGS phenomenological mass | 🟡 staged | rank-one cross-context theorem (finite); 14/14 + 16-control witnesses | real cross-context dataset vs the rank-one prediction | `research/tlica_higgs_phenomenological_mass_2026-10-21/` |

---

## Held, gated, and sensitive (dormant states, made explicit)

| Item | Why held | Gate to move it |
|---|---|---|
| KIN-1-11 (PR #13) | normative doctrine, draft v0.1/v0.2 | **author review** + nonviolence/non-domination affirmation |
| Phenomenological integration | sensitive first-person transcript | explicit privacy/scope review before any public exposure |
| Moreish controller/mindfulness bridge | edits the **DOI-frozen** `applications/moreish_ontology_v1_0.md` | a v1.0.3 decision (Moreish is author-paused) |
| Moreish WWJD actuator | Moreish paused; providence conversation records | provenance + sensitivity pass |
| Drosophila bootstrap | standalone embodied test-bed | Phase-II hardware decision (separate project) |
| Differential field model | prior author-held | author's call to land the full reformulation |

## Strongest current mathematical results (one glance)

- **Bounded driven regime** `$\limsup V \le \tau L/\gamma$` — *Derived*, in frozen foundation (§8.10).
- **Institution as response-signature quotient** with exact factorization on a 36-cell demo — *Observed*.
- **Rank-one cross-context signature** (TLICA–HIGGS single-field) — *Derived (finite toy)*, empirical status UNVERIFIED.
- **Semantic-optics categorical bridge / finite reparametrisation** — *conditional*, proof obligations open in `THEOREM_STATUS.md`.

## Reproduce the live witnesses

```
# One-Ring / TLICA-HIGGS (staged branch): 61/61
python3 -I research/one_ring_thousand_dominoes_2026-10-21/narrative_causal_witness.py
python3 -I research/tlica_higgs_phenomenological_mass_2026-10-21/finite_higgs_witness.py
python3 -I research/tlica_higgs_phenomenological_mass_2026-10-21/causal_diagram_witness.py
python3 -I research/tlica_higgs_phenomenological_mass_2026-10-21/frame_scattering_imprinting_witness.py
# archive invariants + GitHub-math survey
make validate
make check-github-math
```

*This dashboard is a snapshot. Dossier `CLAIM_LEDGER.md` files are the authority for any
individual claim's status; where this page and a dossier disagree, the dossier wins and this
page is stale.*
