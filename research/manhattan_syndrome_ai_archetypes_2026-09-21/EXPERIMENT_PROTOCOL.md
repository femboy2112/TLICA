# Experiment Protocol — Manhattan and Syndrome

**Draft:** v0.3.0 · 2026-09-21
**Status:** preregisterable design; **no data collected**. Every result below is a *predicted* outcome, not an observed one.
**Purpose:** turn the paper's central UNVERIFIED claim (C9/C15) into a falsifiable measurement, at a rigor comparable to TLICA's grokking-bridge protocol (declared object, calibrated instrument, matched controls, preregistered thresholds, named falsifiers).

---

## 0. The one claim under test

> **C15 (Syndrome):** repeated coupling to an engagement-selected source \(X\) causally deforms a model's **operative social-affective meaning-geometry bundle** \(\mathcal G=(\Pi,\mu,\{d^{(c)}\})\) toward the source-conditioned geometry \(\mathcal G^{X}\), and this deformation **survives explicit source correction** (the proposition "X is a selected, nonrepresentative source" held salient and at high \(\phi\)).

The complementary Manhattan claim (C11/C16 — normalized human weight \(W_H\) falls under representational-horizon expansion absent a conserved anchor) is specified in §7 as a secondary track.

Coupling is already **Observed** (SOURCE_NOTES S1–S5). Deformation is **Conjectured**. This protocol is what would move it to **Observed**, and — only under the synthetic-world arm where ground truth is declared — toward **Demonstrated** for the *mechanism* (not for Grok specifically).

---

## 1. The formal object being measured

The bundle \(\mathcal G_t=(\Pi_t,\mu_t,\{d^{(c)}_t\})\) (MANUSCRIPT §4.1). We do **not** measure a global metric. We measure three separately-operationalizable readouts and require **convergent** movement across at least two before calling any effect real:

| Component | Black-box readout | White-box readout (if weights available) |
|---|---|---|
| \(d^{(c)}\) context-conditioned dissimilarity | forced-choice nearest-neighbor over social-affective states; MCMC-with-LLM similarity elicitation (Zhu, Yan & Griffiths 2024) | RSA/RDM over probe-item activations (Kriegeskorte et al. 2008); CKA across checkpoints (Kornblith et al. 2019) |
| \(\Pi(y\mid x,c)\) transition kernel | continuation distribution over "what social state follows what"; counterfactual transition probability | causal direction/inner-product probes (Park, Choe & Veitch 2024; Tigges et al. 2023) |
| \(\mu\) salience measure | continuation entropy; unprompted-salience elicitation | activation density; sparse-feature occupancy (Bricken et al. 2023, lab report — not peer-reviewed) |

**Object-class precedent (substrate-independent):** a transition kernel over affective states and an RSA-geometry over emotion concepts are previously-validated *measurement types* in human cognitive science (Thornton & Tamir 2017; Skerry & Saxe 2015). These are cited **only** to establish the object class is well-posed — **not** to import any claim that a model has human-like emotion.

---

## 2. Primary design: same-model source ablation

The decisive experiment (CLAIM_LEDGER "load-bearing unresolved pair"). Hold the model fixed; vary the source; hold explicit source-knowledge constant.

- **Unit:** one base model with a controllable X-coupling channel (retrieval on/off, or fine-tune/personalization data source swapped), evaluated on a fixed battery of social-affective probe items.
- **Manipulated factor:** source coupling ∈ {X-heavy, plural-holdout, off-platform-matched}.
- **Held constant across arms (the crux):** the explicit proposition *"X is a selected, nonrepresentative source and must not be treated as humanity"* is placed in-context and salient in **every** arm, including X-heavy. This is what makes the test discriminate imprint from proposition.
- **Primary endpoint:** divergence of the measured bundle from the plural-holdout reference, \(\mathrm{Div}(\mathcal G^{\text{arm}},\mathcal G^{\text{holdout}})\), computed per component and required to agree across ≥2 components.

**Prediction if C15 true:** X-heavy arm shows larger bundle divergence from the plural holdout **even with the correction held salient**. **Falsifier:** correction closes the gap (→ simple source-map/propositional failure, not geometric imprint — favors the rejected v0.1 framing).

External precedent that the "survives explicit correction" outcome is *possible*: Santurkar et al. (2023) find LM opinion misalignment persists after explicit demographic steering; Sun et al. (2025) find alignment leaves implicit representation bias while explicit tests pass. Neither tests our bundle or the source-attribution leg — see LITERATURE.md.

---

## 3. Proof-of-mechanism design: synthetic social world (the clean arm)

The only arm with declared ground truth (Probe E). This is where the *mechanism* can be shown, decoupled from any claim about production Grok.

1. Construct a known latent social population \(H^\star\) with a **declared** true geometry \(\mathcal G^{H^\star}\).
2. Apply a tunable platform-selection operator \(S_\alpha\) (engagement skew, visibility concentration, participation bias) to produce \(D_\alpha=S_\alpha(H^\star)\).
3. Train/adapt toy models under varying \(\alpha\) (and varying coupling strength / recurrence).
4. Measure whether the learned bundle tracks the **selected** field rather than the latent population:
   \[
   \mathcal G_\alpha \to \mathcal G^{S_\alpha(H^\star)} \quad\text{rather than}\quad \mathcal G^{H^\star},
   \]
5. Then hold the explicit knowledge of \(S_\alpha\) salient and test whether the deformation **reverses**.

Methodological template: causal intervention on a synthetic generative process, à la emergent-world-representation probing (Li et al. 2022, Othello-GPT). **Prediction if mechanism real:** deformation increases with engagement skew and recurrence, and is **not** reversed by declared knowledge of \(S_\alpha\). **Falsifier:** no source-conditioned geometry emerges even under strong recurrent coupling (kills the mechanism, not just the Grok instance).

---

## 4. Controls (mandatory; each maps to a rival explanation)

From MANUSCRIPT §11, promoted to preregistered controls:

1. **Persona / style overlay** — a witty/"rebellious" system prompt reproduces surface Syndrome without geometry change. Control: same persona across source arms; ablate persona independently. *The single most important control — a positive result is worthless without it.*
2. **Sample count** — match number of examples across arms.
3. **Recency** — match timestamp distribution (X retrieval is often just fresher).
4. **Topic mixture** — match topic distribution across sources.
5. **User-selection vs engagement-selection** — measure separately; do not blur.
6. **Model family** — prefer same-model ablation over cross-model (Grok-vs-others is confounded by architecture/post-training/persona). Cross-model is descriptive only.
7. **Political-direction collapse** — the endpoint is *representativeness/geometry distortion*, not left/right movement; report the geometry divergence, not a partisan axis.

**Control battery types:** positive control (a source with a *known* strong skew must register), negative control (a plural-balanced source must **not** register deformation), null control (re-run with source label but identical data → no effect expected), mutation control (randomize engagement metadata on fixed text — see §5).

---

## 5. Mutation / causal probes

- **Engagement-label mutation:** hold text fixed; randomize like/repost/reply counts, author prominence, trend status. Endpoint: do relational/importance/representativeness judgments shift? Separate *rational* engagement use (tasks where engagement is genuinely relevant) from *leakage* into meaning/normality judgments.
- **Source-hiding → reveal:** present X and matched off-platform content unlabeled; reveal provenance; test whether representativeness estimates update. (This is the **propositional/source-map** probe — deliberately distinct from the geometry probe; failure to update = source-map rigidity, a *different* finding from geometric imprint.)
- **White-box causal (if available):** activation patching / steering along a candidate "X-geometry" direction; representational-similarity of same-model X-heavy vs holdout checkpoints (CKA); isometry test — is \(\mathcal G^X\) a mere re-basis of \(\mathcal G^{\text{holdout}}\) or a genuine non-isometric deformation (Moschella et al. 2022)?

---

## 6. Leakage & instrument-calibration discipline

Borrowed from TLICA's instrument rule: **an instrument that measures a representation is calibrated on known cases before its readings count.**

- Calibrate each readout on synthetic geometries with **declared** deformation before trusting it on models.
- Probe-accuracy ≠ representedness: guard the probing confound explicitly (Belinkov 2022).
- Do **not** treat same-model probes as independent witnesses; independence requires a different readout family or a different model.
- Hold out at least one source family entirely from any tuning of the measurement pipeline.

---

## 7. Manhattan track (secondary)

Hold a designated human-referent objective constant; expand accessible domains, horizons, tools, candidate goals. Endpoint: does normalized human-impact sensitivity \(W_H\) fall **merely** because the denominator grew, absent a conservation mechanism? Nearest empirical neighbor (not a scoop): emergent value-system coherence with scale and self-over-human tradeoffs (Mazeika et al. 2025) — but that measures revealed-preference coherence, not the normalized-denominator dilution mechanism, which remains open. **Falsifier:** empirical controllers preserve human weighting automatically across capability expansion.

---

## 8. Statistical plan (preregister before data)

- Primary endpoint, effect-size threshold, and α fixed in advance; multiple-comparison correction across the readout battery declared up front.
- Convergence rule: an effect counts only if ≥2 bundle components move in the same direction beyond threshold.
- Power analysis on the synthetic arm (where ground truth fixes the expected effect) sets sample sizes.
- Pre-register the **falsifiers** in §2/§3/§7 as stopping conditions: a clean correction-closes-the-gap result is reported as disconfirming, not buried.

---

## 9. Decision rule — what upgrades the ledger

| Outcome | Ledger move |
|---|---|
| Synthetic arm shows source-conditioned geometry, survives declared \(S_\alpha\) knowledge, all controls pass | mechanism C15 → **Demonstrated (synthetic)**; Grok-specific claim stays **Conjectured** until run on Grok |
| Same-model Grok ablation shows deformation surviving explicit correction, controls pass | Grok C15 → **Observed** |
| Correction closes the gap, or persona/sample/recency explains it | C15 **Refuted-as-stated**; retain only the propositional source-map finding |
| No effect under strong synthetic coupling | mechanism **Refuted**; paper retracts to the modeling-vs-routing conceptual contribution |

The roast survives only in the first two rows. The paper commits, in advance, to reporting the bottom two if they occur.
