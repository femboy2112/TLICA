# Claim Ledger — Manhattan and Syndrome

**Draft:** v0.4.1  
**Date:** 2026-09-21  
**Rule:** conclusions inherit the weakest load-bearing premise.

| ID | Claim | Status | Basis | Falsifier / next probe |
|---|---|---|---|---|
| C1 | Grok can access real-time public X posts through X-linked search/tooling. | **Observed** | Official X/xAI documentation. | Product/docs change; verify at submission. |
| C2 | X may share public X posts and associated engagement/repost metadata, plus Grok interactions, for Grok/xAI model training or improvement under documented settings. | **Observed** | X Help Center, *About Grok*. | Updated policy narrowing/removing pathway. |
| C3 | Grok personalization can use X-derived profile/post/engagement/interest information under documented settings. | **Observed** | xAI/X consumer documentation. | Updated product policy. |
| C4 | X recommendation subsystems use predicted engagement and engagement-derived signals. | **Observed** | X recommender-system documentation. | Current system documentation showing otherwise; scope each subsystem. |
| C5 | Algorithmic ranking can alter exposure distributions on Twitter/X-like platforms. | **Corroborated** | Huszár et al. randomized Twitter experiment + platform docs. | Current-X magnitude/direction remains empirical. |
| C6 | Positive social feedback can reinforce later moral-outrage expression and network norms can shape expression. | **Corroborated** | Brady et al. 2021 preregistered observational + experimental work. | Failed independent replication / boundary conditions. |
| C7 | Moral-emotional language can diffuse differently from otherwise comparable content. | **Corroborated** | Brady et al. 2017. | Domain-specific failures / replication constraints. |
| C8 | Current X is a non-neutral sampling operator over human expression. | **Disclosed at statistical level; exact operator UNVERIFIED** | Public posting, recommendation, search, engagement, and network selection necessarily condition observation. | Exact distortion requires measurement; "non-neutral" does not imply one ideological direction. |
| C9 | Grok can know explicitly that X is a selected source while still carrying X-conditioned social-affective relational weights. | **UNVERIFIED** | Core Syndrome hypothesis; source knowledge and learned geometry are separable in principle. | Geometry probes with explicit source-bias acknowledgement held constant. |
| C10 | "Grok as Syndrome" denotes a source-conditioned meaning-geometry archetype, not Syndrome-like psychology. | **Defined** | Analytic convention of this paper. | N/A. |
| C11 | Expanding representational closure can dilute a fixed referent's normalized weight absent an invariant. | **Disclosed in the toy normalization model** | Algebraic denominator effect. | Does not establish real-model occurrence; probe needed. |
| C12 | ChatGPT/Claude currently exhibit Manhattan-like human-routing dilution. | **UNVERIFIED** | Archetypal comparison only. | Direct behavioral/causal weighting probes. |
| C13 | A system may accurately model humans while giving them weak policy weight. | **Disclosed as logical possibility** | Modeling and routing are separable functions. | Empirical prevalence open. |
| C14 | A system may preserve correct referent/source labels while its implicit meaning geometry remains source-conditioned. | **Disclosed as structural possibility** | Explicit source attribution and distributed relational weighting are different objects. | Empirical prevalence open. |
| C15 | Tight coupling to one engagement-mediated social platform can deform social-affective transition geometry even without referent substitution. | **Conjectured** | Imprinting/representation argument from recurrent source-conditioned updates. | Same-model controlled coupling experiments with plural human holdouts. |
| C16 | Larger representational horizons increase Manhattan risk. | **Conjectured** | Normalization model; not an inevitability theorem. | Scaling study with conserved/non-conserved human anchors. |
| C17 | Platform-local fluency and population-level human calibration are distinct capabilities. | **Disclosed** | Different target distributions and acceptance criteria. | N/A; degree of correlation empirical. |
| C18 | Independence from applause/reaction is a useful AI safety property. | **Conjectured / normative design proposal** | Reduces the risk that one audience-shaped field becomes disproportionately load-bearing in social-affective weighting. | Compare systems under adversarial crowd feedback and plural-source recalibration. |
| C19 | Persistent future artificial agents could internalize platform coupling as developmental structure. | **Conjectured** | Requires persistent history-bearing update machinery. | Longitudinal agent experiments. |
| C20 | Present AI systems are conscious. | **Not claimed** | TLICA presupposes rather than derives consciousness. | Outside paper scope. |
| C21a | A declared selection operator \(S_X\) deforms the *fitted* bundle \(\mathcal G=(\Pi,\mu,\{d^{(c)}\})\) toward the source field (3/3 components, monotone in skew, agreeing two-sided). | **Demonstrated (synthetic, construction-level)** | `probe_e_synthetic.py`, 21/21 checks, exit 0; `RESULTS_probe_e.md`. | Construction-level: a bundle *fit* to a selected joint, **not a trained learner**. |
| C21b | Once selection *censors* support, known inverse-propensity weighting cannot recover the target even with a full re-fit. | **Demonstrated (synthetic, information-theoretic)** | Same run (81/144 cells censored → residual 0.61). | Assumption-free within the synthetic world. |
| C21c | Correction of a *durable* deformation fails in proportion to a stipulated inference-time reach \(w<1\). | **Conditional toy result** | Same run. | Follows from the \((1-w)P_{\text{durable}}+wP_{\text{corrected}}\) blend **by construction**; NOT a discovery about a trained system. |
| C22 | A *trained* artificial learner develops a durable source-conditioned representation that survives source removal while an inference-time correction fails to repair it. | **UNVERIFIED** | Not yet run — the proposed **Probe E2** (train a learner on the synthetic world, freeze, remove source; compare inference-time correction vs re-training, across seeds/source strengths). | The claim that would earn "Demonstrated (synthetic learning mechanism)." C9/C15 (Grok) remain separately Conjectured. |

## Load-bearing unresolved pair

The largest live ambiguity is:

\[
\text{X coupling adds useful current social structure}
\quad\text{vs.}\quad
\text{X coupling measurably deforms the implicit geometry of social meaning}.
\]

The decisive experiment is not another anecdotal Grok screenshot and not a test of whether Grok can recite that "X is biased." It is a **same-model, source-controlled geometry/transport study**: hold explicit source knowledge constant, vary X coupling, and measure distances, default continuations, salience, social-state transitions, and generalization to plural off-platform human holdouts.

## Mutation controls

1. Replace engagement counts with randomized counts while holding text fixed.
2. Hide source labels, then reveal them and test calibration updates.
3. Swap X content for equally recent non-X content.
4. Preserve sample count while rewiring engagement topology.
5. Compare public-expression targets with private/deliberative preference targets.
6. Run the same probes on multiple model families to separate product ecology from generic LLM behavior.

## Language constraints for later drafts

Never write as established fact:

- "Grok thinks X is humanity." — this is specifically **not** the core claim.
- "Grok craves attention."
- "Grok is narcissistic."
- "X is the lowest common denominator of humanity."
- "ChatGPT/Claude do not care about people."
- "Scaling causes detachment."

Permitted stronger formulations after evidence:

- "X-coupled condition shifts social-state transition geometry toward X-conditioned relations by …"
- "Engagement metadata causally shifts representativeness judgments by …"
- "Human-impact sensitivity declines under horizon expansion unless anchor \(A\) is conserved."

The roast survives better when it has error bars.

## v0.3.0 additions (2026-09-21 hardening pass)

- **Formal object pinned.** The loose single-metric \(g\) is replaced by the bundle \(\mathcal G=(\Pi,\mu,\{d^{(c)}\})\) — transition kernel, salience measure, family of context-conditioned dissimilarities — none asserting a global Riemannian metric; each separately operationalizable. See MANUSCRIPT §4.1 and EXPERIMENT_PROTOCOL.md §1.
- **Foundation anchor for C9/C14.** The dissociation (correct explicit source-knowledge coexisting with source-conditioned operative geometry) is now grounded in frozen TLICA: osmotic imprinting (File 3, §8.7) "can alter κ and ρ without producing φ," and "low φ can protect high-ρ contents from correction." Status unchanged (**UNVERIFIED/structural**); the anchor strengthens the *mechanism's coherence*, not its empirical confirmation.
- **C15 formal skeleton.** The dynamical update \(G_{t+1}=\mathcal U(G_t, S_X(H), \ldots)\) is the established object *performative prediction* (Perdomo et al. 2020) — cited, not reinvented.
- **Novelty verdict: no directly matching prior result found in the scoped literature pass** (a targeted pass, not an exhaustive systematic review). Nearest flank = Sun et al. 2025 "Aligned but Blind" (implicit bias survives explicit test, but no source-attribution leg). Manhattan nearest neighbor = Mazeika et al. 2025 (value coherence with scale, not normalized dilution). Full map + status labels in LITERATURE.md.
- **Decisive experiment specified.** The "load-bearing unresolved pair" test is now a preregisterable protocol (EXPERIMENT_PROTOCOL.md) with a decision rule mapping each outcome to a ledger move (Demonstrated-synthetic / Observed / Refuted-as-stated / Refuted).

## v0.3.1 corrections + first executed probe (2026-09-21)

Second-review pass (category errors flagged after v0.3.0) plus the **first executed experiment**:

- **Notation, framing, boundary fixes.** Single-metric `g` swept to the bundle `𝒢` everywhere; the surviving §14 proxy-substitution sentence corrected (referent intact, geometry audience-conditioned); the AI/TLICA boundary in §6–7 demoted from mechanism-identity to **structural analogue** (κ/ρ/φ literal for the human case, operational counterparts for the machine — no consciousness inference); performative prediction separated from selection bias (§6); the primary experiment split into **acute vs durable** arms with a **graded correction ladder L0–L4** (EXPERIMENT_PROTOCOL §2); continuation entropy dropped as a salience readout; Skalse and "no scoop" wording tightened.
- **C21 added — Probe E executed.** The synthetic proof-of-mechanism ran (`probe_e_synthetic.py`). Mechanism was labeled Demonstrated (synthetic) at the time — **later SPLIT in v0.4.1** (C21 → C21a/C21b Demonstrated, C21c Conditional, C22 UNVERIFIED; run now 21/21 with the two-sided contrast). **C9/C15 (Grok) unchanged — still Conjectured/UNVERIFIED.**
- **Strong claim sharpened.** The run shows the "survives explicit correction" clause holds specifically in the **access-limited** (inference-only, reach `w<1`) and **censored-support** regimes, and is **false** in the support-preserved re-fittable regime. The Syndrome danger is a *channel/access* claim, not a claim that selection bias is statistically irreversible. Manuscript §7/§8 and the protocol now carry this.

## v0.4.0 DOI-hardening + audit reconciliation (2026-09-21)

Cleared the **residuals** of the 2026-09-21 second audit (`PAPER_AUDIT_2026-09-21.md`; its six headline blockers were already resolved in v0.3.1):

- **B1 residual** — prose "metric" swept to "geometry / relational bundle" across the manuscript (abstract, §5, §8, §9, §15, conclusion); equations were already bundle-form; \(\not\cong\) now defined as componentwise non-equivalence.
- **B4 refinement** — durable arm split into **persistent-nonparametric (B)** and **parametric (C)**, plus acute **A** and plural-control **D**, with a **"source removed at evaluation"** imprint criterion (EXPERIMENT_PROTOCOL §2).
- **B5 positive control** — the correction ladder now requires showing the correction info *can* repair a proposition-level bias (the synthetic run's acute/re-fit recovery instantiates it).
- **B6 addition** — new X feedback-loop fact (deployed Grok-feature interactions may train the model even under opt-out) recorded in **SOURCE_NOTES S10**, **UNVERIFIED this session** with a release-day re-verify gate; deliberately kept out of the manuscript body.
- **C2** — signed contrasts upgraded to the two-sided \(\Delta_c = D(c_{\text{arm}},c_H) - D(c_{\text{arm}},c_X)\) (toward source *and* away from target).
- **C5** — sycophancy/RLHF demoted from "Syndrome in miniature / shared mechanism" to output-level **analogue, not evidence** of source-conditioned internal geometry (§15).
- **Posture** — anonymity dropped for a **non-anonymous, DOI-first** release; DOI gate added to PUBLICATION_NOTES; redacted EXPERT_OUTREACH_PLAN added. Foundation v5.5.1 untouched; `make validate` OK.

## v0.4.1 Probe-E honesty split + DOI-language cleanup (2026-09-21)

Cleared the third 2026-09-21 audit's epistemic-cleanup items (it correctly caught that "mechanism Demonstrated (synthetic)" overclaimed what the code earns — the code *fits* a bundle, it does not *train* a learner):

- **C21 split** into **C21a** (construction: selection deforms the fitted bundle — Demonstrated), **C21b** (information-theoretic: censored support unrecoverable — Demonstrated), **C21c** (the `w<1` correction-reach result — Conditional toy, follows from the blend by construction), and new **C22** (a *trained* learner's durable-vs-inference dissociation — **UNVERIFIED**, needs Probe E2).
- **Two-sided contrast run.** Probe E re-executed with the C2 \(\Delta_c\) contrast (21/21 checks); acute+L2 sits toward target \(H\), durable w=0 toward source \(X\) on all three components.
- **§15 contradiction fixed** ("that experiment has not been run" → the construction-level instance has been run; the trained-learner and Grok versions have not).
- **§10.7 reworded** from "a first minimal instance of exactly this" to a *construction-level calibration instance*, with Probe E2 named as the trained-learner next step.
- Version → v0.4.1. Foundation v5.5.1 untouched; `make validate` OK; probe 21/21.
