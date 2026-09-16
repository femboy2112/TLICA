# Reconciliation Against Current Main

This is the Stage-1 audit the [handoff](MAINLINE_INTEGRATION_HANDOFF.md) requires before any
integration: every construct the dossier reuses, checked against what `main` already owns, with
real citations, an overlap/conflict verdict, and a proposed action. Produced by a local session
with the repository checked out.

**Finding, in one line:** *the dossier introduces no new coordinate and no foundation primitive.
The "moving-substrate" premise is already on main — the developmental window is a frozen
commitment (File 4) and the substrate-dependence, focus-split, source-opaque affect, and slow
`G` structure it leans on are all present (File 3, v5.5.0). The dossier's only new symbols
(`η_dev`, `S_eff`) are application-level diagnostics, explicitly not coordinates. It lands
research-tier with its causal claim (which rival explains the phenomenology) UNVERIFIED.*

## Repository state at audit

- Base: `femboy2112/TLICA`, `main` at the commit this package was landed on.
- Foundation version on main: **v5.5.0** (`foundation/0_reading_guide.md:1`). The dossier reasons
  against v5.5.0; that dependency line is current.
- The **canonical Self-Applied paper** is `applications/self_applied_architecture_prose_draft_v0_1.md`
  (the one the wiki page `docs/app-self-applied-architecture.md:3` and `research/README.md:89` cite).
  It declares `*Foundation base: TLICA v5.3.3 (Files 1–6, frozen)*`. **The v5.3.3 / v5.5.0 seam the
  dossier flags is real.**
- `make validate` (links + self-containment + math-term gates): PASS before and after adding this
  package. The dossier's new terms — `nonstationar`, `moving-machine/plant`, `eta_dev`,
  `baseline buzz`, `context-resolv` — are **not** watched math-drift stems, and the watched stems it
  does use (`field`, etc.) are already pinned. No new pin required.
- **No foundation file is touched.** One curated application paper and its wiki mirror gain a
  clearly-labelled, conservatively-scoped subsection (Route C, below).

## The load-bearing prior fact

`main` already commits to a **developing, non-fixed substrate** — the dossier's central premise —
in the frozen foundation itself:

> "The architecture commits to the existence of a **developmental window** … during which conscious
> direction is insufficient to overcome substrate and environmental pressure. … They emerge from
> **substrate features the I did not choose**, environmental conditions the I did not control, and
> contact-driven dynamics that operated before the I had any intentional capacity to direct them.
> The window's boundary is gradual: **substrate maturation is continuous, Mode B onset varies across
> cogniting beings, and self-directed focus capacity grows incrementally**."
> — `foundation/4_derived_concepts_and_predictions.md:85`

So the dossier's premise — that a developing I regulates *through* a substrate whose properties are
still changing — is **Disclosed**, already on main. The dossier's contribution is to **name the
control problem** that this continuous maturation *plus* the incrementally-growing self-directed
focus jointly create (a controller learning while its plant drifts), not to add a commitment. That
framing is what keeps it honest: the debt it must still pay is *which rival* (developmental drift,
acquired regulation, environment, retrospective reconstruction, or their coupling) actually explains
the author's phenomenology — not permission to model development as substrate change at all.

## Reconciliation table

| Dossier construct | Existing main object (citation) | Overlap | Conflict? | Action |
|---|---|---|---|---|
| Developmental window / continuous substrate maturation | frozen developmental-window commitment (`foundation/4_derived_concepts_and_predictions.md:85,97`) | near-total | none | **absorb**: the moving-plant problem is this window read as a control problem; add no primitive |
| Substrate sets inherited capacity `M_m(t)=Γ^M_m(𝖲_m,t)` | substrate `𝖲_m` in the machine tuple + `Outside^m`, capacity via `Γ^M_m` (`foundation/3_formal_apparatus.md:103,115`) | direct | none | **reuse**: `S_eff,m(t):=Eval_t(𝖲_m)` is an application *view* of the existing substrate, not a new object |
| Focus shifts contact-driven → self-directed across development | focus split `Foc = Foc[contact-driven] ⊕ Foc[self-directed]`, §8.2 (`foundation/3_formal_apparatus.md:531`) | direct | none | **reuse**: "controller improves" = self-directed focus accumulating |
| Affect is source-opaque (real signal, weak return-address) | third-order affect + *conscious-fuzzy / source-opaque* content class (`foundation/3_formal_apparatus.md:81,326`) | direct | none | **reuse**: "baseline buzz" = high phenomenal availability + low/undefined source-level φ |
| Slow lived-I structure `G`; `ρ=R(G)`, `f=F(G,𝖠)`; Mode B moves the target | v5.5.0 §8.11 actuator repair, verbatim (`foundation/3_formal_apparatus.md:531`; `foundation/5_translations_open_problems_conclusion.md:121`) | direct | none | **reuse**: developmental drift = the substrate through which `G` is written/read changing; do **not** alter `F`'s signature |
| Osmotic imprinting always online | osmotic imprinting, mechanism-online (`foundation/3_formal_apparatus.md:531`; `docs/modes-of-development.md`) | direct | none | **reuse**: calibration never pauses; both imprinting arms write `G` |
| Root II = high affective gain | Root II in the Self-Applied paper (`applications/self_applied_architecture_prose_draft_v0_1.md:79,85`) | direct | none | **preserve + regime-qualify**: same Root II, different dynamical regime — never replaced by "brain development" |
| `η_dev(t)=τ_track/τ_S` tracking-load ratio | — (no existing object) | none | **coordinate-leak risk** | **application-level, UNVERIFIED**: labelled not-a-coordinate, not-a-truth-score, undefined until operationalized |
| Depression/suppression/recovery arc | culling / suppression → regeneration in the Self-Applied paper (`applications/self_applied_architecture_prose_draft_v0_1.md:119`) | strong | none | **keep as live co-cause/rival** (H3/H4), not an afterthought |

## Term-gate and coordinate-leak check

- **Math-drift:** the dossier's distinctive vocabulary (`nonstationar`, `moving-machine`, `eta_dev`,
  `baseline buzz`, `context-resolved`) is not on the watchlist (`scripts/math_terms.txt`); watched
  stems it uses are already pinned. Gate stays green; no new pin needed.
- **Coordinate leak (handoff Attack 4):** the canonical coordinates remain **κ / φ / ρ**. `η_dev`,
  `S_eff`, mediation depth, developmental stage, regulation skill, and source-map adequacy are
  diagnostics/typological variables. **No fourth coordinate is introduced.** The field-reading
  `F(G,𝖠;S_eff)` semicolon is "implemented/mediated-through" notation — the substrate-mediation
  already in §8.5 — **not** a new independent argument to `F`; the foundation signature is untouched.

## The version seam — Route C (split-layer)

The Self-Applied paper is written against **v5.3.3**; foundation main is **v5.5.0**. Following the
handoff's preferred route, the integration is **split-layer**, not a version bump:

- the new subsection is phrased using only dependencies already available at the paper's v5.3.3
  base — substrate capacity, the focus split, osmotic imprinting, third-order source-opaque affect,
  and the developmental window (all present in the frozen files the paper already cites);
- a **clearly-labelled current-foundation note** then records how v5.5.0's slow structure `G`
  (`ρ=R(G)`, `f=F(G,𝖠)`) *sharpens* the same mechanism, without importing v5.5.0 as the paper's base.

The paper's declared base marker is **not** cosmetically changed. This keeps every existing v5.3.3
claim honest while surfacing the refinement.

## What the audit does *not* change

It confirms provenance, boundaries, and the no-coordinate result; it does **not** discharge the
causal debt. The **coupled model (H4)** remains the best structural synthesis but stays
**CONJECTURED**; whether developmental substrate drift, acquired regulation, environment, or
retrospective reconstruction dominates is **UNVERIFIED** and gated on the [probe suite](CLAIM_LEDGER_AND_PROBES.md).
The neuroscience [source map](SOURCES.md) is carried research-tier as the dossier authored it: its
*general* constraints (adolescence involves synaptic pruning/myelination/circuit maturation;
neocortical neurogenesis is largely restricted to development; affective control keeps developing;
longitudinal affect change is multidimensional, not monotone damping) are mainstream and used only
as hedged corroborative context — **population science does not validate the author's individual
autobiographical reconstruction**, and independent verification of the specific primary citations
(the dossier's own §7) is outstanding truth-debt, not discharged here.

Return to the [package README](README.md) or the [research index](../README.md).
