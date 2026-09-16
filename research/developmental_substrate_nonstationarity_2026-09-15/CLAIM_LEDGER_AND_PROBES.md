# Claim Ledger and Discriminating Probes
## Developmental Substrate Nonstationarity

**Status discipline:** this file deliberately separates phenomenological report, TLICA-internal structure, developmental-neuroscience constraints, and causal hypotheses. No single scalar "confidence" is used.

---

## 1. Claim ledger

| ID | Claim | Status | What supports it | What would change the status |
|---|---|---|---|---|
| D-01 | The author's childhood/adolescent/young-adult phenomenology included a persistent affective background pull or "baseline buzz" beyond cleanly context-addressed episodes. | **OBSERVED** | First-person report in the originating conversation. | Contemporaneous records that systematically contradict the present reconstruction would weaken/reclassify it. |
| D-02 | The author's present adult phenomenology is more context-resolved: strong emotion remains, but is more often legibly tied to specific circumstances. | **OBSERVED** | First-person present report. | Repeated present-day sampling showing equally strong source-opaque ambient affect would weaken it. |
| D-03 | Adolescence involves substantial neural reorganization/maturation rather than merely accumulation of fixed hardware. | **CORROBORATED** | Developmental-neuroscience literature on synaptic remodeling/pruning, myelination, connectivity, pubertal influences, and circuit maturation. | Major contrary synthesis would be required; the broad claim is mainstream. |
| D-04 | Affective control and emotion-regulation capacities continue changing across adolescence and into young adulthood. | **CORROBORATED** | Developmental and longitudinal affect-regulation literature. | Strong contrary longitudinal evidence. |
| D-05 | "Large-scale continual addition of blank cortical neurons causes developmental noise" is an adequate centerpiece mechanism. | **REFUTED AS STATED** | Human adolescent development is better characterized by remodeling, pruning, myelination, connectivity and functional maturation than wholesale addition of blank cortical neurons. | None expected; only a much narrower neurogenesis claim could survive. |
| D-06 | TLICA can represent the moving-machine problem without adding a fourth coordinate. | **CORROBORATED internally** | Current v5.5.0 already has substrate dependence, time-indexed capacity, developmentally shifting focus, substrate-mediated affect, osmotic imprinting, and slow structure `G`. | A formal audit could reveal a hidden dependency conflict; until then no new coordinate is needed. |
| D-07 | Developmental substrate nonstationarity contributed materially to the author's baseline affective buzz. | **CONJECTURED** | Fits D-01 plus D-03/D-04 and TLICA's source-opaque third-order affect. | Timeline/provenance probes that favor high-gain-only, environment-only, or acquired-regulation-only rivals. |
| D-08 | Adult context-resolution reflects a lower ratio of substrate drift to self-tracking capacity. | **CONJECTURED** | Structural fit with maturation plus accumulated self-regulation. | Operationalization of the ratio and longitudinal evidence are still missing. |
| D-09 | Root II should remain a high-gain affective parameter but be understood as regime-dependent rather than developmentally constant in phenomenological expression. | **CONJECTURED / application-level refinement** | Explains strong affect persisting after the background-buzz regime changed. | Evidence that affective gain itself changed enough to explain the full transition. |
| D-10 | The depression/suppression/recovery arc is a major co-cause of adult regulation rather than a mere interruption. | **UNVERIFIED** | Plausible from the trajectory; current architecture already describes suppression then regeneration. | Contemporaneous timeline + treatment/behavioral evidence needed. |
| D-11 | Strong affect returned after recovery while context-resolution remained improved. | **OBSERVED, pending timeline corroboration** | Present first-person report plus prior self-applied-architecture reconstruction. | Records/current sampling. |
| D-12 | D-11 weakens a simple permanent-blunting explanation. | **CORROBORATED conditionally** | If affective capacity returned, permanent blunting cannot by itself explain lower ambient affect. | Fails if "returned affect" is only partial or qualitatively incomparable. |
| D-13 | The exact mapping `TLICA S/G/f/tau/slack <-> neural processes` is known. | **DARK / not claimed** | No operational bridge currently exists. | Requires explicit bridge model and empirical validation. |
| D-14 | Developmental tracking load `eta_dev` is measurable and useful. | **UNVERIFIED** | Defined only as an application-level diagnostic. | Needs operational definitions and a toy/empirical demonstration. |
| D-15 | The phenomenon is universal to children/teens/young adults. | **REFUTED as a universal claim / not proposed** | Large individual heterogeneity in affective development and regulation. | N/A. |

---

## 2. Rival models

The preferred frame must compete against finite live rivals rather than absorbing all outcomes.

### R1 — High-gain-only

A stable high-gain affective parameter is enough. Childhood felt more ambient because contexts were more destabilizing, memories preferentially retain extremes, or the self had less vocabulary to label causes. No changing-substrate mechanism is required.

**Unique expectation:** once context, vocabulary, and regulation are controlled, developmental stage should add little explanatory value.

### R2 — Developmental substrate nonstationarity

Rapidly changing substrate response-properties produce plant drift. The I repeatedly recalibrates against a moving target; third-order affect therefore carries more endogenous residual and source-opacity.

**Unique expectation:** natural periods of greater physiological/nonstationary change should increase poorly addressed affect even when explicit context is relatively stable.

### R3 — Acquired-regulation / learning-history

The decisive factor is the author's learned regulatory architecture, especially through depression, suppression, treatment/recovery, reflection, and repeated self-management. Age is largely a proxy for accumulated learning.

**Unique expectation:** the transition should align more closely with specific learned-regulation milestones than with broad developmental stage.

### R4 — Environmental regime change

Childhood/adolescence were objectively more externally unstable or lower-agency. Adult life is more controllable, so affect is more legibly context-linked because contexts themselves are different.

**Unique expectation:** after matching environmental volatility/agency, age-related differences should shrink substantially.

### R5 — Retrospective reconstruction artifact

The present self remembers youth as an undifferentiated affective sea because early memories are sparse, high-salience, and weakly source-tagged. The apparent developmental transition is primarily a reconstruction effect.

**Unique expectation:** contemporaneous records should show more context-specificity than present memory reports.

### R6 — Coupled model

R2, R3, and some R4 all contribute, with Root II amplifying each. Developmental substrate drift creates a hard control problem; later learned regulation and increased agency improve tracking; depression/recovery changes the controller; adulthood reduces but does not eliminate drift.

**Unique expectation:** no single rival explains the timing and residuals. The coupled model should earn its complexity through out-of-sample or held-out explanatory gains, not merely fit everything post hoc.

---

## 3. TLICA diagnostic vector

The developmental hypothesis should be analyzed with TLICA diagnostics kept separate.

### κ — contact

Question: how much current external contact is present when strong affect occurs?

A developmental-substrate contribution predicts some episodes with high affect despite modest change in external κ. This does **not** mean κ is irrelevant; external contact can trigger or shape the response while failing to explain its full magnitude/persistence.

### φ — toolkit-relative truth/source indistinguishability

Question: can the I construct a usable pathway from the felt state to its cause?

The key predicted signature is **high phenomenological availability + low/undefined source-level φ** for some strong affect. Developmental nonstationarity should increase the fraction of affect whose return-address is not reconstructible from inside.

### σ — source-map adequacy

This is the most load-bearing diagnostic.

The concern is not "was the feeling real?" but "was the source map complete?"

Candidate developmental failure mode:

`visible context x -> strong affect y`

is internally mapped as though `x` were the full source, while the outside model is closer to:

`x + endogenous state s_t + changing transfer function H_t -> y`.

High φ about the external event can therefore coexist with poor σ about the full affective provenance.

### ρ — identity/commitment coupling

High-ρ interpretations may intensify affect and can also bias retrospective reconstruction. A developmental event bound deeply into identity should not be treated as mechanistic evidence merely because it remains emotionally central.

### μ — probe availability

Early-life episodes typically have low current μ: the decisive experiment cannot be rerun. This raises the importance of records, natural contrasts, sibling/peer data, longitudinal literature, and present-day natural experiments.

### Cl(Tools)

The present tool closure includes:

- current TLICA formal apparatus;
- autobiographical report;
- any surviving contemporaneous records the author chooses to inspect;
- public developmental-neuroscience literature;
- present-day diary/EMA-style self-observation;
- finite control-theory toy models.

It does **not** currently include retrospective neural measurements of the author's developing brain. Exact biological attribution is therefore inaccessible under current closure.

### Independence

Current autobiographical theory, present memory, and the Self-Applied Architecture are **not independent witnesses**; they share the same authorial provenance. Developmental-neuroscience sources provide independent domain constraints but do not independently verify the autobiography.

### Coherence

The new hypothesis coheres unusually well with existing TLICA machinery. That is useful but dangerous: architectural fit is not empirical truth. Coherence raises the priority of hostile probes; it does not pay truth debt.

### Discrimination

The most valuable next evidence is evidence that separates R2 from R3/R4/R5, not more examples that all models can absorb.

---

## 4. Probe suite

### P1 — Contemporaneous-record source-resolution audit

**Object:** journals, old messages, posts, notes, therapy records, creative writing, or other dated traces the author already possesses and chooses to inspect.

**Coding unit:** a strong affective episode.

For each episode code:

1. age/date;
2. affect intensity if inferable;
3. identifiable precipitating context? yes/no/ambiguous;
4. whether the explicit frame changed during the episode;
5. whether affect persisted after the frame/context changed;
6. degree of source certainty in the contemporaneous account;
7. obvious physiological context (sleep loss, illness, puberty-related report, substance, medication, etc.) only where explicitly recorded;
8. whether the account reads as ambient mood versus event-specific emotion.

**Pass for R2:** developmental records show a higher rate of intense source-opaque/persistent affect than later adult records, beyond simple context count.

**Pass for R5:** records are substantially more context-resolved than present memory implies.

**Ambiguous:** sparse records or changes in writing style/vocabulary dominate.

**Control:** blind a subset of records to age before coding if feasible.

### P2 — Present adult EMA baseline

For several weeks, at randomly sampled moments or regular intervals, record:

- current affect valence/intensity;
- strongest identifiable context;
- confidence in source attribution;
- bodily/arousal state;
- whether affect feels "ambient" or "about X";
- whether changing the cognitive frame changes the affect within a short interval.

This does not test childhood directly. It establishes the adult denominator instead of relying on a global impression.

**Pass for D-02:** adult affect is measurably dominated by context-resolved episodes.

### P3 — Natural nonstationarity recurrence probe

Do **not** induce physiological destabilization. Use naturally occurring episodes already present in life: illness, unusual sleep disruption, major stress, medication transitions under ordinary care, or other naturally occurring bodily changes.

Prediction from R2:

> when the effective substrate is temporarily less stationary, source-opaque/background affect should increase even in adulthood.

Prediction from a strict age-only story:

> the childhood pattern should not recur merely because adult physiology becomes transiently unstable.

This is a strong discriminator because it targets the proposed mechanism rather than chronological age.

### P4 — Depression/recovery discriminator

Construct a timeline with at least four epochs:

1. developmental full-gain / baseline-buzz period;
2. depressive suppression/anhedonia period;
3. affect-seeking / unstable-return period if applicable;
4. adult recovery with regenerated feeling.

For each, code separately:

- affect amplitude;
- affect variability;
- source-resolution;
- context coupling;
- regulation capacity;
- environmental volatility.

**Permanent-blunting model prediction:** amplitude stays low when background buzz falls.

**Coupled/maturation-regulation prediction:** amplitude can return while source-resolution remains improved.

### P5 — Skill-timeline probe

List major regulation/toolkit milestones independently of age: therapy skills, contemplative practice, explicit reframing strategies, sobriety/recovery changes, new conceptual tools, improved environmental control, etc.

Then ask whether the phenomenological transition aligns more tightly with those milestones than with broad developmental age.

**Pass for R3:** sharp changes follow skill acquisition or recovery transitions.

**Pass for R2:** substantial context-resolution improvement precedes or proceeds independently of explicit skill acquisition.

### P6 — Environment-control probe

Compare periods with similar external instability but different ages, or similar ages with different instability.

If adult high-stress/high-chaos periods still produce more context-resolved affect than adolescent periods of comparable external chaos, R4 weakens.

### P7 — Formal plant-drift toy model

Build two controllers with identical gain:

- Model A learns a stationary plant `P`.
- Model B learns `P_t` whose parameters drift on a tunable timescale.

Give both the same observations and learning rule.

Measure:

- residual prediction error after context is accounted for;
- controller lag;
- apparent unexplained output variance;
- time to recalibration after a parameter shift;
- misattribution if the controller assumes stationarity.

**Required controls:**

- zero drift -> models coincide;
- zero gain difference -> isolate drift;
- frozen controller -> show learning benefit;
- known parameter step -> recover expected lag behavior;
- mutation control with random observation noise -> distinguish plant drift from measurement noise.

This only demonstrates the mechanism is coherent. It does not validate the autobiographical mapping.

### P8 — Literature-level directional check

Preregister a small extraction:

- longitudinal studies of affect variability from early to late adolescence;
- longitudinal studies of white-matter/myelin or connectivity change;
- studies of affective/executive control development;
- studies spanning adolescence into emerging adulthood.

Extract direction, age window, sample, sex composition, measure, and major caveats. Do not cherry-pick only studies showing monotone stabilization.

**Fail condition:** if the literature shows no robust developmental change in the relevant domains, R2 loses plausibility.

### P9 — Return-address manipulation probe

Within safe present-day contexts, compare two types of adult affective episodes:

- clear external precipitant;
- spontaneous/poorly sourced mood shift.

Ask whether reframing the external story changes each differently.

The hypothesis predicts that poorly sourced episodes should be less frame-responsive because the visible narrative is not the full source.

This tests the source-map mechanism directly without making a developmental claim.

---

## 5. Complete-factorial warning

Do not claim an interaction among:

`age/development x affective gain x regulation skill x environment`

from anecdotal cells.

A genuine mixed-term claim requires all relevant cells or an explicit model that identifies the interaction under stated assumptions. In this dossier, the interaction is **CONJECTURED**, not disclosed.

The same applies to the proposed coupled H4 model. Its superior narrative fit is not evidence until it predicts held-out contrasts better than simpler rivals.

---

## 6. Provenance tomography

Source families should be tracked separately:

- **A — author present report**;
- **B — author historical records**;
- **C — prior TLICA self-application documents**;
- **D — developmental neuroscience reviews**;
- **E — primary longitudinal affect studies**;
- **F — primary longitudinal neurodevelopment studies**;
- **G — control-theory / adaptive-filtering prior art**.

Important dependency notes:

- A and C share strong provenance and are not independent.
- B may partially escape present reconstruction if records are genuinely contemporaneous.
- D often summarizes F and must not be counted as an independent replication of the same studies.
- E constrains population-level developmental direction but does not validate the author's mechanism.

A future literature audit should perform leave-one-family-out synthesis: if the case collapses when family D (reviews) is removed and only primary studies remain, the evidence map is too review-dependent.

---

## 7. Verdict-changing observations

The following would materially weaken the developmental-substrate account:

1. contemporaneous youth records show affect was usually clearly context-specific rather than ambient;
2. adult natural physiological instability does not increase poorly sourced affect at all, across repeated observations;
3. the transition in affective texture tracks one explicit learned-regulation intervention far more closely than developmental stage;
4. environment volatility fully explains the age contrast;
5. after recovery, affect amplitude remains substantially blunted, so improved context-resolution is not separable from weaker feeling;
6. a stationary high-gain model reproduces the observed phenomenology without residual structure that plant drift helps explain.

The following would strengthen it without proving it:

1. contemporaneous records independently show developmental ambient/source-opaque affect;
2. strong affect returns in adulthood while context-resolution stays high;
3. adult naturally nonstationary physiological periods partially recreate the old "buzz";
4. formal plant-drift models produce the same specific residual/source-misattribution signature;
5. longitudinal literature independently supports declining variability/improving affective control while neural reorganization remains active.

---

## 8. Saturation boundary

Even after all feasible probes, the exact historical causal contribution of developmental substrate change may remain **contextually saturated** rather than disclosed. The original developmental substrate state cannot be re-measured. The correct endpoint may therefore be:

> a coupled account that is better corroborated than its rivals under current tool closure, while exact causal weights remain dark.

That is an acceptable scientific result. The purpose of the dossier is to prevent a compelling phenomenological insight from being either dismissed because its first biological story was crude or overpromoted into a mechanism the available evidence cannot establish.
