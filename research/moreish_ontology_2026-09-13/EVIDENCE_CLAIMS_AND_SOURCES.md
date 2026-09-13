# Evidence, claim ledger, and sources

**Dossier:** [This Ontology Is Really Moreish](MANUSCRIPT.md). **Date:** 2026-09-13.
**Status:** research-tier; author review pending. **Foundation untouched.**

This ledger distinguishes the essay's standard mathematics, its author-originating
phenomenological claims, its borrowed cultural figures, and its cross-references into the
TLICA corpus. It is honest about what was checked against the bytes and what is asserted
from general knowledge. The manuscript is author-derived and, as a whole, **UNVERIFIED**
as an empirical account of any person; nothing here promotes it.

## 1. TLICA cross-reference verification

The manuscript borrows four TLICA constructs by name. Each was checked against the frozen
foundation and the landed research corpus on `main` at base `cd71c9f`. Verdicts:

| Anchor (§) | Essay's use | Where it actually lives | Verdict |
|---|---|---|---|
| **Mode-B projection** (§5) | Future-Me is available "through Mode-B projection: simulations of possible imprinting rather than already-imprinted actuality." | [foundation/4](../../foundation/4_derived_concepts_and_predictions.md): "Mode B operates on projected post-action profiles; the modeling I imagines the lived-I in each represented future-state" (§10.6); "Future-state projection across the lived-I (Mode B operating on represented post-action profiles)." Glossary pins *Mode B — reflexive meta-reasoning*. | **Faithful to frozen foundation.** The essay's use matches the pinned sense. |
| **Steerable / correctable commitment; "an endorsed destination is not itself an actuator"** (§8) | The recognized destination is not an intervention; "better forecast ≠ better controller." | [research/geometry_of_actualization](../geometry_of_actualization_2026-09-07/AGENCY_AND_STEERABLE_COMMITMENT.md) ("observer versus actuator", commitment–tactic separation) and [IMMERSION_AND_REORIENTATION §13](../geometry_of_actualization_2026-09-07/IMMERSION_AND_REORIENTATION.md) ("correctable commitment, not permanent self-surveillance"). **Absent from foundation and applications.** | **Faithful, but to a research-tier SIBLING, not the foundation.** Label accordingly. |
| **Plural inhabited life with low-cost reflective transitions** (§10) | The goal is "plural inhabited life with low-cost reflective transitions," not zero reflection. | [research/geometry_of_actualization/SLACK_RESONANCE_AND_PLURAL_LIFE.md §8](../geometry_of_actualization_2026-09-07/SLACK_RESONANCE_AND_PLURAL_LIFE.md): "A plural life asks for depth without monopoly and reconsideration without permanent suspension… The Underground can become one passage through such a life." (Same Dostoevsky lineage.) **Absent from foundation.** | **Faithful, research-tier sibling.** |
| **Slack** (§5) | "This is particularly important under low slack" — expensive model-predictive control is unaffordable when slack is low. | A **developed theory construct**: pinned in the glossary and load-bearing across [cold_frame](../../applications/cold_frame_v0_4_3.md), referent_routing, and the geometry dossier. **Absent from the frozen v5.3.3 files only because those are a first iteration** — its frozen-file seat is pending the foundation upgrade. The glossary's primary pin is the *will-room* sense (residual latitude the unchosen parameters leave for willing); §5 uses a *load / planning-budget* sense (cf. cold_frame's load-driven thinning). | **Faithful use of a developed construct.** Absence from the freeze is **provenance, not an epistemic demerit** (the papers are the growing edge the foundation upgrade will seat). Two live items, neither a strike against §5: (i) **scope** — tag which sense of slack is meant, per the archive's term-discipline; (ii) **operationalization** — making slack *bite* in a *dynamical* model is an open research thread (the differential-field attempt returned S=0), a question about that model, not about slack's standing. |

**Net:** all four anchors are sound. Mode-B traces to the frozen foundation; steerable
commitment and plural life to research-tier siblings; slack to the theory's developed
research/application tier. **Absence from the frozen v5.3.3 files is a provenance fact, not
an epistemic demerit** — those files are an explicitly incomplete first iteration, and the
papers (this one included) are the growing edge the foundation upgrade will eventually seat;
a construct's grade rests on its own derivations and role, never on whether it has been
written into the freeze yet. No anchor is fabricated or misattributed. The §5 argument
stands on both the Mode-B asymmetry and a faithful use of slack; the only open items are
slack's scope-tag and its operationalization in a dynamical model — neither a weakness in
the essay.

## 2. Sources (cited from general knowledge; not re-verified against primary text this session)

Following the archive convention of stating access honestly. These are canonical objects;
the citations are at author/title/year confidence. **Confirm exact loci on finish.**

- **S1 — Underground Man.** Fyodor Dostoevsky, *Notes from Underground* (1864). Used for:
  reflection-as-habitat, consciousness reopening every closure (§2, §10). *Not* used for a
  scholarly reading of the text.
- **S2 — Super Hans.** *Peep Show* (Channel 4, 2003–2015), the character Super Hans. Used
  for: the comic register of "the game itself is absurd, so I refuse its categories'
  jurisdiction" (§2). A comic amplifier, not a psychological characterization.
- **S3 — Veruca Salt.** Roald Dahl, *Charlie and the Chocolate Factory* (1964); film
  adaptations 1971 and 2005. Used for: an exaggerated *reward function* ("she wants it
  now"), explicitly "not a literal psychological characterization" (§3, author's own words).
- **S4 — Pavlovian conditioning.** Ivan Pavlov, classical conditioning. Used for: the
  "immediate resonance → repeat the action" reinforcement shape (§3). Shape-borrow, not a
  neuroscientific claim.
- **S5 — Control-theory frame.** The greedy-vs-optimal distinction and the principle of
  optimality (Bellman, *Dynamic Programming*, 1957); open-loop vs. closed-loop/feedback
  control (standard control theory); option value / real options (canonical text: Dixit &
  Pindyck, *Investment Under Uncertainty*, 1994). Used for: the whole §4/§8/§9 skeleton.
  These are standard results; see the [formalism note](FORMALISM_AND_PROBES.md).

## 3. Claim ledger

Grades: **DERIVED** (follows from stated premises / a standard theorem), **OBSERVED**
(seen in an executed run), **CONJECTURED** (author's honest hypothesis), **UNVERIFIED**
(no test run), **REFUTED**. "Faithful cross-reference" is a §1 verdict, not a grade.

| ID | Claim | Grade & boundary | What changes the verdict |
|---|---|---|---|
| M1 | Maximizing the integrand `u(x,a)` locally *need not* maximize the integral `J` when the state is coupled (`x_{t+1}=F(x_t,a_t)`) — coupling is **necessary, not sufficient**, for a greedy–optimal gap. (§4 boxed) | **DERIVED** — the existential form is a standard consequence of Bellman's principle (the optimal action weighs the successor's continuation value `V(F(x,a))`, which greedy discards; sometimes the same action maximizes both, sometimes not); **OBSERVED** in the toy (a coupled instance: greedy J=12 < optimal 30). | A coding error in the demo (cross-checked by brute force). **Not** changed by a coupled instance where greedy *equals* optimal — those exist (many coupled parameter cells tie: e.g. the D0=5 variant, greedy=optimal=40) and are *consistent* with the claim, precisely because coupling is necessary-not-sufficient. The over-strong universal reading ("greedy fails in *every* coupled system") is neither what Bellman establishes nor what this row asserts, and would itself be refuted by any such tie. |
| M2 | A feedback policy `π(x)` valuing option value beats greedy on `J`, by refusing gratuitous `|A(x_{t+1})| ≪ |A(x_t)|` moves. (§9 boxed) | **OBSERVED in one toy** (feedback J=30, terminal `\|A\|`=5 vs greedy 12, 0); **CONJECTURED as life-guidance**. | A coupled family where `π*` fails to beat greedy or to preserve `\|A\|` weakens it; the demo is one instance, not a proof for all `F`. |
| M3 | Greedy is optimal when moments are independent. | **DERIVED / OBSERVED** — calibration variant (decoupled greedy J=32 = optimal 32). | — (instrument-rule check; passing it is a precondition, not the finding). |
| P1 | The "moreish" worldview is a self-reinforcing loop: constraint → Hans frame → felt liberation → reduced correction → more constraint → stronger evidence for Hans. (§6) | **CONJECTURED** — author phenomenological mechanism. | Process-sensitive measures distinguishing the loop from ordinary coping; a rival that explains the same reports. |
| P2 | The category mistake is treating model *uncertainty* as if it weakened the *causal* coupling ("the future is epistemically weak and causally real; that distinction is the hinge"). (§5, §12) | **CONJECTURED** as diagnosis; the uncertainty≠irrelevance distinction itself is **DERIVED/definitional**. | Author revision; a case where the diagnosis misfits the phenomenology. |
| P3 | Providential and self-authorship narratives share the comedy structure (opaque suffering → expanded horizon → retrospective integration → laughter). (§7) | **CONJECTURED**; also a **known over-coherence hazard** — see cross-reference to [self_applied_architecture](../../applications/self_applied_architecture_prose_draft_v0_1.md) O1 (redemptive over-coherence) in the [handoff](AUTHOR_INTENT_AND_HANDOFF.md). | The firewall from the Self-Applied paper: is the integration faithful or self-serving? |
| X1 | Mode-B projection is the phenomenological status of Future-Me. (§5) | **Faithful cross-reference to frozen foundation** (§1). | Foundation edit (frozen) — not expected. |
| X2 | The §5 low-slack argument. | **Faithful use of a developed theory construct** (§1) — slack's correctness rests on its own derivations across the corpus, not on presence in the frozen v5.3.3 files; its frozen-file seat is pending the foundation upgrade. | Its grade would change on the merits of the construct, not on freeze-location. Open items: tag which sense of slack §5 means; operationalize slack in a dynamical model (differential-field attempt returned S=0). |
| A1 | This essay is a good *light / accessible intro to TLICA*. | **AUTHOR-DECLARED / UNVERIFIED** — a pedagogical claim, untested. | A reader trial; or the judgment that it presumes too much apparatus to stand alone. |

## 4. Diagnostic and provenance discipline

- Keep the separations: **κ/contact**, **φ/toolkit-relative indistinguishability**,
  **σ/source-map adequacy**, **ρ/identity coupling**. The essay is a φ-level structural
  account; it is not a σ-resolved causal history of a person, and its comic charge
  (a ρ-level pull) is not evidence for its φ-level claims.
- The finite-model demo is an **illustration, not corroboration**. It shows a standard
  control-theory identity; it says nothing about whether the phenomenological reading is
  correct. It is a single toy, not a family, and not independent of the mathematics it
  illustrates.
- The cultural figures (S1–S4) are **comic amplifiers**, per the author's own framing —
  not psychological characterizations of the referents and not clinical claims.

## 5. Work actually performed

- On `main` at base `cd71c9f`, the four anchors of §1 were checked against the bytes:
  `Mode-B` grep in `foundation/` (present, at 4:178/197); `slack` grep in `foundation/`
  (**zero** hits) and in `research/`/`applications/` (present, research/app-tier);
  `steerable`/`correctable commitment`/`actuator` and `plural inhabited life` located in
  the geometry-of-actualization sibling dossier.
- [`greedy_vs_option_demo.py`](greedy_vs_option_demo.py) was written, `py_compile`'d, and
  run under **Python 3.12.3** (pure standard library): **6/6 checks passed, exit 0**. Raw
  output in [`greedy_vs_option_demo_results.json`](greedy_vs_option_demo_results.json);
  summary in [`greedy_vs_option_demo_tests.txt`](greedy_vs_option_demo_tests.txt). Script
  SHA-256: `10f0b523c156e4e2b5ea03811713647d22b3f77caf4200b4763282b9d2572fcf`. The optimum
  was computed two independent ways (backward-induction DP and exhaustive search) and they
  agree; the decoupled calibration check passed (greedy = optimal).
- `make validate` was run for the whole archive after these files were added; result is
  recorded in the [README](README.md) and the [handoff](AUTHOR_INTENT_AND_HANDOFF.md).
- The manuscript was **not edited**; the two display-math repairs are recorded in the
  [formalism note](FORMALISM_AND_PROBES.md) as a handoff, not applied. No frozen foundation
  file was touched. No external sources were fetched this session; S1–S5 are cited from
  general knowledge and flagged for locus confirmation on finish.
