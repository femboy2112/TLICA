# Formalism, math-repair handoff, and probes

**Dossier:** [This Ontology Is Really Moreish](../../applications/moreish_ontology_v0_1_0.md). **Date:** 2026-09-13.
**Status:** research-tier working note; author review pending. **Foundation untouched.**

This companion does three jobs: (1) it records the display-math repairs the paste
needs, **as a handoff for the author to apply** — the manuscript is captured verbatim
and nothing here has been written into it; (2) it states the control-theory skeleton
the essay uses, separating the standard results from the author's phenomenological
overlay; and (3) it specifies the finite-model demonstration and the falsification
probes. The governing convention is the archive's: **a borrowed mathematical shape is
dimensional analysis, not an equality** — the phenomenon shares the term's *shape*; the
literal law is a separate, earned claim.

## 1. Display-math repair handoff (author to apply — manuscript is verbatim)

The manuscript's display blocks were pasted with LaTeX relations/spacing stripped and
`[ … ]` used as display delimiters. Most blocks are well-formed once the delimiters are
normalized (`[ … ]` → `\[ … \]` or `$$ … $$`) and `,dt` → `\,dt`. **Two blocks are
missing a symbol and are ambiguous as written.** Neither is repaired in the manuscript;
each is recorded here with a candidate and a confidence, for the author's decision.

| Block | As pasted | Candidate repair | Confidence | Note |
|---|---|---|---|---|
| **§4 greedy policy** | `a_t^{G}  \arg\max_a u(x_t,a)` | `a_t^{G} := \arg\max_a u(x_t,a)` | **High** | The line *introduces* the greedy action; only a definitional relation (`:=`, or `=`) fits. No semantic ambiguity — just pick the definitional symbol. |
| **§9 objective, `I` term** | `… + \lambda O(F(x,a))  \mu I(x,a)` | `… + \lambda O(F(x,a)) - \mu I(x,a)` | **High on semantics, confirm before typesetting** | §9 names `I` "irreversible downside" and lists it as a cost, so the missing operator reads as a subtraction (`-\mu I`), with `\lambda, \mu \ge 0`. The manuscript does **not** print the sign; do not insert it silently. |

Cosmetic (no ambiguity, apply in a pass): `J=\int_0^T u(t),dt` → `\,dt` (§4, twice);
normalize all `[ … ]` display delimiters; the `\boxed{ … }` blocks are already well-formed.

## 2. The control-theory skeleton (standard results, stated cleanly)

The essay's spine is a textbook fact dressed in two comic figures. Stated plainly:

- **Objective.** A life's value is schematized as an integral of a per-moment integrand,
  `J = ∫₀ᵀ u(x_t, a_t) dt` (discrete analogue `J = Σ_t u(x_t, a_t)`).
- **Coupling.** The state evolves under the agent's own actions, `x_{t+1} = F(x_t, a_t, η_t)`,
  where `η_t` is what the agent does not control. This is the load-bearing premise: the
  moments are **not independent**.
- **Greedy policy.** `a_t^G := argmax_a u(x_t, a)` — maximize the current integrand, ignore
  the coupling.
- **The standard result (DERIVED, textbook).** Under state coupling the greedy policy is
  generally **not** optimal for `J`: `argmax` of the integrand ≠ `argmax` of the integral.
  This is Bellman's principle of optimality read in the contrapositive — an optimal policy
  must account for the value of the successor state `V(F(x, a))`, which the greedy policy
  discards. The manuscript's boxed §4 claim ("maximizing the integrand locally does not
  maximize the integral when the integrand is dynamically coupled through state") is exactly
  this, and it is **not** in question; what is author-supplied is the *identification* of
  this failure with a lived worldview.
- **Open-loop vs. feedback (§8).** An open-loop plan fixes a sequence `(a_0, …, a_T)` in
  advance; a **feedback policy** sets `a_t = π(x_t)`, responding to whichever state actually
  arrives. The essay's key move — "better forecast ≠ better controller" — is the standard
  observation that feedback control does not require an accurate forward model, only an
  adequate response map. This is why "just plan more" (§8) misdiagnoses the problem.
- **The invariant-preserving objective (§9).** `π*(x) = argmax_a [ R_present(x, a)
  + λ·O(F(x, a)) − μ·I(x, a) ]` (sign per §1 above), with `R_present` the self-congruent
  present value, `O` future **option value**, `I` irreversible downside, `λ, μ ≥ 0`.
- **Option value ↔ reachability.** The manuscript's boxed §9 constraint — *avoid gratuitous
  actions for which `|A(x_{t+1})| ≪ |A(x_t)|`*, where `A(x)` is the action set reachable
  from `x` — is a **reachability** statement in the archive's pinned sense (attainability
  under the system's own dynamics; see [glossary: Reachability / κ-reachability](../../docs/glossary.md)).
  Option preservation is: keep `|A(x_t)|` large so Future-Me retains moves, without
  committing to any one predicted future. This is one bridge from the essay to the apparatus
  (reachability, seated in the frozen foundation); §5's use of **slack** is a second,
  equally legitimate route through a developed theory construct whose frozen-file seat is
  now **seated in the foundation** (v5.4.0, §8.11, File 3; scoping refined in v5.4.1 — slack is one margin of a family, the `S = 0` gate posited); its earlier "frozen-file seat pending" status is resolved — a matter of provenance throughout, not merit (see the
  [evidence ledger](EVIDENCE_CLAIMS_AND_SOURCES.md) §1).
- **Two interpretation caveats on the toy (v5.4.1 audit).** (a) The counter `d` is an
  *option-richness / reachability-under-the-operative-policy* proxy, **not** the literal
  count of legal actions `|A(x)|`: in the demo `|A(x)| = 2` at both `d=0` and `d=5` (the
  environment is never absorbing — `OPEN` takes `d=0 → 1`), so the toy exhibits *option value
  collapsing under a myopic controller* — "the route exists but the operative controller does
  not select it" — not literal irreversible deletion of every move. Genuine irreversibility
  would be a separate build. (b) Both policies compared are **feedback** policies (each sets
  `a_t = π(x_t)`); what distinguishes them is *horizon* — myopic (one-step) vs full-horizon
  lookahead — not feedback-vs-open-loop. The open-loop/feedback axis above (the "better
  forecast ≠ better controller" point) is a *different* contrast, which the demo does not
  itself test.

## 3. Finite-model demonstration

[`greedy_vs_option_demo.py`](greedy_vs_option_demo.py) (SHA-256
`10f0b523c156e4e2b5ea03811713647d22b3f77caf4200b4763282b9d2572fcf`, Python 3.12.3, pure
standard library) makes the §4/§9 claims concrete on a deterministic toy state machine.
It is an **illustration**, not evidence about any person and not corroboration of the
phenomenological reading. Raw output: [`greedy_vs_option_demo_results.json`](greedy_vs_option_demo_results.json);
human summary: [`greedy_vs_option_demo_tests.txt`](greedy_vs_option_demo_tests.txt).

**Model.** State `x = (d, t)`; `d` = open "doors" in `{0..5}` (the concrete `|A(x)|` proxy),
start `d0 = 3`, horizon `T = 8`. Actions: `INDULGE` (reward 4, `d → d−1`, the resonant
present that closes a door), `MAINTAIN` (reward `d`, `d → d`, a sustainable present that
scales with open doors), `OPEN` (reward 0, `d → min(d+1, 5)`, buys nothing now, widens
tomorrow). `GREEDY` is the myopic argmax of immediate reward; `FEEDBACK` is the
full-lookahead optimal `π(x) = argmax_a[u + V(F(x,a))]` with `V` by backward induction.

**Instrument rule (calibration first).** On the *decoupled* variant (`F(x,a)=x` on `d`),
greedy `J = 32` equals the optimum `J = 32` (and the brute-force max `32`) — where the
moments are independent, greedy **is** optimal, so the instrument recovers the known
answer before any coupled reading is trusted. The optimum is also computed two independent
ways — backward-induction DP and exhaustive search over all action sequences — and they
agree (`30` coupled, `32` decoupled).

**Results (coupled), all 6 checks pass, exit 0:**

- Greedy: `INDULGE×3` (d: 3→2→1→0), then stuck at `MAINTAIN` (u=0) — `J = 12`, terminal
  `d = 0`, **3** option-deleting moves. It eats every door for u=4, then the present it
  fought to keep pays nothing.
- Feedback: `OPEN×2` (u=0, d: 3→4→5), then `MAINTAIN×6` at `d=5` (u=5) — `J = 30`, terminal
  `d = 5`, **0** option-deleting moves. Two "boring" moves buy a sustained *richer* present
  and leave Future-Me's action space wide open.
- So `J_greedy (12) < J_optimal (30)`, and greedy's terminal `|A(x)|` (0) collapses while the
  feedback policy's stays maximal (5) — the §4 and §9 claims, side by side.

## 4. Probes and falsification hooks

The manuscript's §10 "cheaper computations" become testable checks:

- **Repeat-thirty-times probe.** Simulate the candidate policy autonomously for `N` steps
  under the coupled dynamics; report the trajectory of `|A(x_t)|`. A policy whose reachable
  set trends monotonically down is a greedy-integral failure regardless of its early reward.
- **Reversibility check.** Label each action reversible/irreversible; a policy is
  option-preserving only if its irreversible-commitment rate is bounded and each such
  commitment clears a stated `O`-vs-`R_present` threshold, not merely a present-reward one.
- **Relief-by-obligation check.** Flag actions whose `R_present` gain is financed by future
  `I` (buying present relief by manufacturing downstream obligation) — the §6 "self-seasoning"
  loop in operational form.
- **Falsifier for the corrective.** If, on a family of coupled toys, the option-value policy
  `π*` does **not** beat greedy on `J` (or does not preserve `|A|`), the §9 corrective is
  weaker than claimed. The demo is one instance where it holds; it is not a proof for all
  `F`, and the ledger records this boundary.
