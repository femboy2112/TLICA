# Research dossier: pre-registration — the opposition-checksum dialogue intervention

**Date:** 2026-08-09
**Status:** Proposed pre-registration for a study **not yet run**. This is a *design*, not a result. Every hypothesis is **UNVERIFIED**; the document exists so that the flagship prediction of the parent paper can be tested in a way that can *lose*.
**Companion note:** [`semantic_interoperability_culture_war_constraint_closed_politics_2026-08-09.md`](semantic_interoperability_culture_war_constraint_closed_politics_2026-08-09.md)
**Target paper:** [`../applications/shared_reality_divergent_maps_v0_2_0.md`](../applications/shared_reality_divergent_maps_v0_2_0.md), §13.4 (the opposition-checksum intervention), operationalized against §13.1 (constructs) and bounded by §12.6 (the validator problem).
**Foundation impact:** None proposed. This is an application-level empirical protocol, not a new TLICA coordinate or a modification of the frozen foundation.

---

## 0. What this pre-registers

The parent paper proposes **constraint-closed compromise** built on an **opposition checksum**: the strongest valid variable a rival tracks that one's own model is tempted to discard, which — once it survives five validity gates — must be permanently incorporated (§8.2). §13.4 sketches a randomized test of the claim that a dialogue protocol enforcing this discipline produces *durable model revision* rather than transient warmth.

This dossier turns that sketch into a runnable, pre-registered randomized controlled experiment: fixed hypotheses, a design that isolates the protocol's active ingredient, an adjudication procedure for "valid" that respects §12.6, a delayed follow-up that separates durable revision from a demand effect, and — the load-bearing part — decision rules written **before** data collection so the result cannot be reverse-fit.

The single most important design commitment: **the study is built to be able to fail in a way that would falsify a load-bearing claim of the paper**, not merely to trim a parameter. §13.7 already names the falsifier — "a checksum protocol that moves warmth but never durable model revision." This protocol is engineered so that outcome is a clean, pre-declared FAIL.

---

## 1. The claim under test

From §13.4, restated as a directional causal claim:

> Relative to an equal-intensity structured dialogue that does **not** enforce the checksum discipline, a dialogue protocol that requires each discussant to (1) name the strongest valid variable their **own** side tracks, (2) name the strongest valid variable the **other** side tracks, (3) state one downstream obligation their **own** principle generates, and (4) state one observation that would narrow their preferred policy, will raise **durable incorporation of the rival's strongest valid variable** and **discovery of third options**, **without** a false-balance cost (participants do not adopt *invalid* variables at equal rates).

Two clauses are separable and both must hold for the paper's claim to survive:

$$
\boxed{
\text{durable rival-variable incorporation}\uparrow
\quad\land\quad
\text{invalid-variable adoption not}\uparrow
}
$$

The second clause is what distinguishes constraint closure from mere agreeableness. A protocol that raised incorporation of *everything* — valid and invalid alike — would be manufacturing false balance, the exact failure §12.1 warns against. The paper only earns its claim if the protocol is **selective for validity**.

---

## 2. Hypotheses

Directional, pre-registered. **H1 is primary and confirmatory**; H2–H6 are secondary.

- **H1 (primary).** At delayed follow-up, participants in the checksum arm show higher **durable incorporation** of the rival's pre-identified strongest valid variable than participants in the active-control arm.
- **H2 (false-balance guard, primary co-condition).** Participants in the checksum arm do **not** adopt pre-identified **invalid** variables (fabricated, dehumanizing, or domination-coded) at a higher rate than the active-control arm. *If H2 fails, H1 alone does not count as support for the paper's claim.*
- **H3.** The checksum arm generates more, and higher-rated, **third options** (policy proposals that address both sides' valid variables) than the active-control arm.
- **H4.** The checksum arm shows higher **opponent-model accuracy** (reconstruction of the rival's strongest reasons, scored against the rival's self-report and the expert panel).
- **H5.** The checksum arm shows equal-or-lower **out-group cost imposition** (a behavioral allocation measure) relative to control, and this is **not** achieved by collapsing the three separated quantities in §5 below.
- **H6 (mechanism).** The effect of arm on durable incorporation (H1) is mediated by opponent-model accuracy (H4), not by change in affect (feeling thermometer) alone.

Explicitly **not** hypothesized: that the protocol increases *agreement* or *policy convergence*. The paper predicts model revision, which may *sharpen* a disagreement (§1, §5.2). Convergence is measured (§5) but a null or divergent result on it is theory-consistent, not a failure.

---

## 3. Design

A three-arm, between-subjects randomized experiment on cross-partisan dyads, with a baseline, an immediate post-test, and a **delayed follow-up at 14–21 days** (the durability window).

| Arm | Condition | Purpose |
|---|---|---|
| **A — Checksum** | Structured cross-partisan dialogue with the four checksum requirements enforced (§1) | The intervention |
| **B — Active control** | Structured cross-partisan dialogue, matched for length, structure, facilitation, and contact, **without** the four requirements (open exchange of views on the same issue) | Isolates the checksum's *specific* ingredient from generic contact/dialogue |
| **C — No-contact baseline** | Complete the same measures at the same intervals, no dialogue | Benchmarks how much of any A-vs-B effect is dialogue-per-se vs. no intervention |

The primary contrast is **A vs B**. B is the demanding comparison: it holds constant everything the intervention shares with ordinary structured dialogue, so a positive A-vs-B result cannot be explained by "they just talked to someone across the aisle." C is included only to calibrate effect sizes and detect a ceiling in B.

Assignment is at the **dyad** level (both members of a dyad receive the same arm), stratified by issue and by the pro/anti composition of the dyad, using a pre-generated randomization sequence held by someone not running sessions.

---

## 4. Participants, sampling, and power

**Population.** Adults in a single national polity, recruited through an online panel with quotas on party, age, education, and region to avoid a convenience-sample monoculture. Pre-screened to hold a non-trivial position on the target issue (excludes the genuinely indifferent, for whom "incorporation" is undefined).

**Issue.** One **primary** contested issue selected for a clear pro/anti structure and moderate (not maximal) affective charge to avoid floor/ceiling effects, plus one **replication** issue run identically. The parent paper's abortion example is deliberately *not* the primary issue — its charge risks ceiling effects on affect and identity — but is a candidate for a high-charge replication.

**Dyads.** Cross-partisan, matched one pro / one anti on the target issue.

**Inclusion/exclusion (pre-registered).** Exclude: attention-check failures (≥2 of 3), non-completion of the dialogue, dropout before the immediate post-test. Follow-up non-completers are retained for immediate-outcome analyses and handled by the attrition plan (§7) for H1.

**Sample size and power.** The primary outcome (H1) is treated as a binary at follow-up: did the participant spontaneously incorporate the rival's strongest valid variable (blind-coded, §5)? Assume a control base rate $p_B = 0.25$ and a target detectable rate $p_A = 0.40$ (a 15-point lift). For a two-proportion test, two-sided $\alpha = 0.05$, power $= 0.80$:

$$
n_{\text{per arm}} \approx
\frac{\bigl(z_{1-\alpha/2}\sqrt{2\bar p(1-\bar p)} + z_{1-\beta}\sqrt{p_A(1-p_A)+p_B(1-p_B)}\bigr)^2}{(p_A-p_B)^2}
\approx 152,
\qquad \bar p = 0.325.
$$

Inflating for dyad-level clustering (design effect for the analyzed contrast) and $\approx 25\%$ follow-up attrition yields a recruitment target of **≈ 230 participants per arm** (≈ 115 dyads/arm), **≈ 690 total** across three arms, per issue. The replication issue doubles recruitment. These numbers are the pre-registered minimum; the confirmatory analysis is powered for H1, and secondary analyses are reported as powered-or-not per outcome.

---

## 5. Measures (operationalized against §13.1)

Three quantities are held **strictly apart** throughout, per §13.1 — collapsing them is the characteristic measurement error this program exists to avoid:

$$
\boxed{
\text{feeling heard}
\;\ne\;
\text{being causally influential}
\;\ne\;
\text{being factually correct}.
}
$$

| Construct (§13.1) | Measure | Timing |
|---|---|---|
| **Durable rival-variable incorporation** (H1) | Blind-coded presence of the rival's pre-identified strongest valid variable in the participant's *own* free-response reasoning about the issue | baseline, immediate, **follow-up** |
| **False-balance guard** (H2) | Blind-coded adoption rate of pre-identified **invalid** variables (planted; see §6) | immediate, follow-up |
| **Third-option discovery** (H3) | Count and expert-rated quality of novel policy proposals addressing both sides' valid variables | immediate |
| **Opponent-model accuracy** (H4) | Reconstruction of the rival's strongest reasons, scored against (a) the rival's own self-report and (b) the expert panel | immediate, follow-up |
| **Affective polarization** | Feeling thermometer + social-distance battery toward the out-party | baseline, immediate, follow-up |
| **Policy position** | Position on the target issue (not hypothesized to converge) | baseline, immediate, follow-up |
| **Factual learning** | Accuracy on a fixed set of issue-relevant factual items | baseline, immediate, follow-up |
| **Out-group cost imposition** (H5) | Incentivized allocation task (real stakes) toward an out-party recipient | immediate |
| **Feeling heard / causal influence / correctness** | Three separately worded self-report items, never summed | immediate, follow-up |

"Durable" is defined by the **follow-up** measurement, not the immediate post-test. An effect present immediately but absent at follow-up is the pre-registered **AMBIGUOUS** outcome (demand effect, not revision).

---

## 6. The validity adjudication (respecting §12.6)

The constructs "strongest **valid** variable" and "**invalid** variable" cannot be read off a neutral vantage the parent paper denies exists (§8; §12.6). They are fixed **in advance**, transparently, and their reliability is itself a reported quantity:

1. **Pre-registered expert panel.** Before data collection, a declared, boundary-relative panel (with its composition and standpoint stated, per §12.6) applies the five gates of §8.2 to a candidate pool of variables for each issue and designates, per side, the **strongest valid variable** (the checksum floor) and a set of **planted invalid variables** — fabricated, dehumanizing, or domination-coded items that fail the gates. The planted-invalid set is what H2 uses to detect false balance.
2. **Inter-coder reliability is reported, not assumed.** Agreement among panelists on $\mathrm{Valid}(x)$ and on the hostile-control gate is computed and published (e.g., Krippendorff's $\alpha$). A checksum or incorporation score is therefore always **relative to a declared panel and its measured agreement** — never a claim to the total view.
3. **Blind response coding.** The free-response outcome coders (for H1, H2, H4) are blind to arm and to hypothesis, code against the fixed panel key, and their reliability is reported separately from the panel's.

This is the concrete instantiation of §12.6's discipline: the study does not claim a neutral referee's seat. It declares its validator, its panel, and its residual disagreements, and makes all three contestable — which is the only honest status the framework permits.

---

## 7. Procedure, timeline, and attrition

1. **Baseline** (day 0): consent, screening, quotas, baseline measures.
2. **Randomization** to arm at the dyad level.
3. **Intervention** (day 0): Arm A runs the four-step checksum protocol with light facilitation and equal time-on-task to Arm B; Arm B runs matched open dialogue; Arm C skips to measures.
4. **Immediate post-test** (day 0).
5. **Delayed follow-up** (days 14–21): re-measure the durable outcomes.

**Attrition plan (pre-registered).** Primary H1 analysis uses follow-up completers; a sensitivity analysis reports (a) intention-to-treat with the conservative assumption that non-completers did *not* incorporate, and (b) inverse-probability weighting on baseline covariates. A divergence between these that changes the H1 verdict is reported as a limitation, not resolved by picking the favorable one.

---

## 8. Analysis plan

- **Primary (H1).** Mixed-effects logistic regression of durable incorporation on arm (A vs B as the pre-registered contrast), with random intercepts for dyad, controlling for baseline position strength, baseline efficacy, and an education/coverage proxy. Effect reported as a risk difference with a 95% interval.
- **H2 (false-balance guard).** The same model on invalid-variable adoption; the pre-registered success condition is a null-or-negative A-vs-B effect (a **non-inferiority-style** test, with the margin declared in advance).
- **H3–H5.** Pre-specified models per outcome; family-wise error across the secondary set controlled (Holm), with the primary/secondary split declared so H1 is not penalized for the secondary family.
- **H6 (mediation).** Pre-registered mediation of arm → durable incorporation through opponent-model accuracy vs. through affect, with bootstrapped indirect effects.
- **Covariates, exclusions, and any transformation are fixed here**; anything decided after seeing outcomes is labeled exploratory in the write-up.

---

## 9. Pre-registered decision rules

Mirrors §13.4's pass/fail/ambiguous, made precise:

- **PASS** — H1 supported (A > B on durable incorporation, interval excluding the null) **and** H2 satisfied (no false-balance cost). The paper's flagship claim survives this test.
- **FAIL** — either (a) no durable A-vs-B difference in incorporation, **or** (b) an incorporation gain accompanied by an equal-or-greater rise in invalid-variable adoption (warmth/agreeableness bought with false balance). Case (b) is the §13.7 falsifier realized: "moves warmth but never durable model revision" — or worse, moves warmth by degrading validity.
- **AMBIGUOUS** — an immediate A-vs-B effect that decays to baseline by follow-up (demand effect), or an effect confined to within-group reconstruction (§13.2's ambiguous case: shared identity, not shared concepts, doing the work).

The verdict is read off these rules mechanically. No outcome is re-narrated into a success.

---

## 10. Threats to validity

- **Demand effects.** The delayed follow-up and the blind coding are the primary defenses; the AMBIGUOUS rule exists precisely to catch what survives them only briefly.
- **The validator problem (§12.6).** The panel has a standpoint. The study does not pretend otherwise; it reports the panel's composition and reliability and treats every score as panel-relative. A different panel is a different (declarable) study, not a refutation.
- **Facilitation confound.** Arm A's structure could work through facilitator attention rather than the checksum. Matched facilitation and time-on-task in Arm B is the control; a manipulation check confirms A participants actually produced the four elements.
- **Generalizability.** One polity, an online panel, two issues. The replication issue tests topic-generality; cross-polity generality is explicitly out of scope and flagged as such.
- **Ceiling/floor.** Issue selection targets moderate charge; the high-charge replication (e.g., abortion) is where a ceiling on affect is most likely and is interpreted accordingly.

---

## 11. What a null (FAIL) result would mean

A clean FAIL does not merely trim the model. Per §13.7 it sinks a load-bearing claim: that constraint-closed dialogue produces durable, validity-selective model revision rather than transient warmth. The honest consequence would be to **downgrade** the §15 ledger rows "Opposition checksums improve compromise quality" and "Constraint closure improves viewpoint coherence" from UNVERIFIED-prediction to **contradicted-under-test**, and to say so in the paper. The framework would retain its *diagnostic* value (making omissions visible and auditable, §12.6) while losing its *interventional* claim. That asymmetry — a method that clarifies even if it does not persuade — is worth stating in advance so a null is informative rather than embarrassing.

---

## 12. Provenance

This protocol operationalizes §13.4 of the target paper and is bounded by its §12.6. It is registered here in the provenance tier because it is a *design*, not a finding: nothing in this dossier is evidence for the parent paper's predictions. It becomes evidence only when the study is run, its pre-registered rules are applied, and the result — pass, fail, or ambiguous — is reported without revision.
