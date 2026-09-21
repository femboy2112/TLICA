# Manhattan and Syndrome — AI Archetypes Research Dossier

**Status:** research-tier application dossier · v0.4.0 · 2026-09-21  
**Branch:** landed on `main` (development branch `research/manhattan-syndrome-ai-archetypes-2026-09-21`)  
**Foundation dependency:** TLICA v5.5.1 (unchanged)  
**Publication posture:** **non-anonymous, DOI-first** — a public Zenodo preprint whose DOI is circulated directly to specific researchers (see `PUBLICATION_NOTES.md` and the redacted `EXPERT_OUTREACH_PLAN.md`). The earlier anonymous/blinded plan is dropped.

## Core question

As artificial systems become more capable, more persistent, and more deeply coupled to human environments, what distinct developmental failures can arise even without an explicit objective to harm humans?

This dossier develops two fictional archetypes as compact analytic instruments:

- **Manhattan failure** — the human referent remains legible, but its routing weight dilutes as the system's reachable representational horizon expands. The danger is not hatred but distance.
- **Syndrome failure** — the human referent can remain explicit and correctly sourced while repeated coupling to a selected social field deforms the relational geometry through which human social/emotional meaning is organized. The danger is not 'X = humanity' confusion but source-conditioned reweighting of meaning-space.

The motivating contemporary contrast is deliberately provocative: **Claude/ChatGPT as Manhattan-like risk archetypes; Grok as a Syndrome-like risk archetype because of its unusually tight product/data/retrieval coupling to X.** This is an analogy and research hypothesis, not a diagnosis of current systems, an attribution of motives, or a claim that any present model is conscious.

## Cold-start entry point

If you have no prior conversation context, read [ZERO_CONTEXT_HANDOFF.md](ZERO_CONTEXT_HANDOFF.md) first. If you are handing the branch to another coding/research session, use [LOCAL_SESSION_PROMPT.md](LOCAL_SESSION_PROMPT.md).

## Files

- [ZERO_CONTEXT_HANDOFF.md](ZERO_CONTEXT_HANDOFF.md) — complete genesis, corrected thesis, TLICA dependency map, equations, epistemic boundaries, probes, falsifiers, manuscript debt, and next-work queue.
- [LOCAL_SESSION_PROMPT.md](LOCAL_SESSION_PROMPT.md) — copy-paste bootstrap prompt for a zero-context local session.
- [MANUSCRIPT.md](MANUSCRIPT.md) — full paper draft (v0.4.0; 16 sections incl. related-work).
- [EXPERIMENT_PROTOCOL.md](EXPERIMENT_PROTOCOL.md) — preregisterable discriminating-experiment protocol (formal object, same-model ablation, synthetic-world proof-of-mechanism, controls, statistical plan, decision rule).
- [RESULTS_probe_e.md](RESULTS_probe_e.md) — executed synthetic proof-of-mechanism (Probe E): numbers, self-checks, and the honest ledger move (mechanism-level, not Grok).
- [probe_e_synthetic.py](probe_e_synthetic.py) — the runnable, self-checking Probe E instrument (numpy-only; declared ground truth).
- [LITERATURE.md](LITERATURE.md) — triangulated related-work map with per-reference status labels and the no-scoop novelty verdict.
- [CLAIM_LEDGER.md](CLAIM_LEDGER.md) — claim status, evidence, falsifiers, and truth debt.
- [SOURCE_NOTES.md](SOURCE_NOTES.md) — source/provenance notes for the empirical X/Grok and social-feedback claims.
- [PUBLICATION_NOTES.md](PUBLICATION_NOTES.md) — release posture (non-anonymous, DOI-first), framing, the DOI release gate, and venue notes.
- [PAPER_AUDIT_2026-09-21.md](PAPER_AUDIT_2026-09-21.md) — the 2026-09-21 second audit (run against v0.3.0; a status banner records that B1–B6/C1–C5 are resolved in v0.3.1/v0.4.0). Retained as the audit record.
- [EXPERT_OUTREACH_PLAN.md](EXPERT_OUTREACH_PLAN.md) — public, **redacted** reviewer-mapping (who owns which edge of the claim); operational details kept in a private local copy.

## v0.3.0 hardening pass (2026-09-21)

P1 coherence audit (stale v0.1 proxy tokens swept; 5 fused-heading artifacts removed), P2 formalization (loose single-metric replaced by the weakest-object bundle \(\mathcal G=(\Pi,\mu,\{d^{(c)}\})\), anchored to frozen-foundation osmotic imprinting §8.7 and the "low φ protects high-ρ from correction" dissociation), P3 experiment protocol added, P4 literature triangulated (performative prediction earned as the formal skeleton; *Aligned but Blind* named as the nearest flank; no directly matching prior result located in the scoped pass), P5 related-work section + references integrated. Foundation v5.5.1 unchanged.

## v0.3.1 correction pass (2026-09-21)

A second-review pass fixing category errors flagged after v0.3.0: the notation regression swept (single-metric \(g\) → bundle \(\mathcal G\) everywhere), the surviving proxy-substitution sentence in §14 corrected (referent stays intact; geometry is audience-conditioned), the AI/TLICA boundary demoted from mechanism-identity to **structural analogue** in §6–7 (no consciousness inference — κ/ρ/φ literal for the human case, operational counterparts for the machine), performative prediction separated from selection bias (§6 — only the closed loop earns "performative"), the primary experiment split into **acute vs durable** arms with a **graded correction ladder** L0–L4 (§2), continuation entropy dropped as a salience readout, and the Skalse and "no scoop" wording tightened. The synthetic proof-of-mechanism (Probe E) was **executed** in a first minimal form — see `RESULTS_probe_e.md` and `probe_e_synthetic.py`. Foundation v5.5.1 unchanged.

## v0.4.0 DOI-hardening + audit reconciliation (2026-09-21)

Folds in the 2026-09-21 second audit (`PAPER_AUDIT_2026-09-21.md`) — whose six headline blockers were already resolved in v0.3.1 — by clearing its **residuals**: the prose "metric" language swept to "geometry/relational bundle" throughout the manuscript (the equations were already bundle-form); the primary experiment's durable arm refined into **persistent-nonparametric (B)** vs **parametric (C)** with a "source removed at evaluation" imprint criterion (plus acute **A** and plural-control **D**); a **positive control** added to the correction ladder; **two-sided signed contrasts** (toward source *and* away from target) for the convergence rule; **sycophancy/RLHF demoted from shared-mechanism to output-level analogue** (§15); and a new X **feedback-loop** fact recorded in `SOURCE_NOTES.md` S10 (UNVERIFIED this session — release-day re-verify gate). Publication posture switched to **non-anonymous, DOI-first**; a DOI release gate added to `PUBLICATION_NOTES.md`. Redacted `EXPERT_OUTREACH_PLAN.md` added. Foundation v5.5.1 unchanged; `make validate` OK.

## Load-bearing discipline

1. **No consciousness inference.** TLICA presupposes consciousness; the paper does not use TLICA-like dynamics to prove present AI consciousness.
2. **No motive attribution.** "Syndrome" names a coupling topology, not vanity, resentment, or a psychological diagnosis in Grok.
3. **No 'X = humanity' strawman.** The strong claim explicitly allows Grok to know that X is only X. The question is whether X-heavy coupling still reshapes implicit distances, saliences, transition priors, and social-affective neighborhoods.
4. **No 'engagement necessarily corrupts' theorem.** Engagement selection can be useful; the paper asks when coupling to engagement-selected data creates systematic source-map error.
5. **No 'more intelligence necessarily means less care.'** Manhattan is a possible normalization/dilution failure unless human-referent weighting is actively preserved.
6. **The roast must cash out mathematically.** Every memorable metaphor must map to a declared structural variable, pathway, or falsifiable prediction.

## One-sentence thesis

> Two advanced artificial systems can fail in opposite ways: one may model humanity accurately while routing it too weakly to matter, while another may retain the correct human referent yet encounter it through a social-affective geometry disproportionately shaped by one contaminated source.

No foundation files are modified by this branch.
