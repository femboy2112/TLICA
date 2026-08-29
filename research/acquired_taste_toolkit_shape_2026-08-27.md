# Acquired Taste as Toolkit-Shape Acquisition

**Status:** Research note / candidate application, v0.1  
**Branch:** `research/acquired-taste-toolkit-shape-2026-08-27`  
**Foundation impact:** none. This note proposes an application-level extension and test program; it does **not** modify the frozen TLICA foundation.  
**Epistemic status:** mixed. Several component phenomena are empirically supported; the specific TLICA interpretation as representational-basis growth is **CONJECTURED** and requires discriminating experiments.

---

## 0. Executive claim

The phenomenon of **acquired taste** may be a particularly clean, observable example of a toolkit changing shape while acquisition is still happening.

The key proposal is stronger than "a person learns to like something they used to dislike." It is:

> Repeated encounter can change the representational space in which a stimulus is perceived, so that a feature that originally dominated the entire experienced object becomes one coordinate inside a richer, more factorable object.

In short:

$$
\boxed{\text{acquired taste} \neq \text{only changing a rating}}
$$

and may sometimes instead involve

$$
\boxed{\text{acquired taste} = \text{changing the basis in which the object is represented and rated}.}
$$

This is not claimed to be the only mechanism of acquired taste. Hedonic reweighting, mere exposure, habituation, associative learning, post-ingestive reinforcement, context conditioning, and social learning are live rivals and may coexist. The research target is to determine whether **basis enrichment / discriminative-operator acquisition** contributes independently.

---

## 1. Where this already touches TLICA

The frozen architecture already contains much of the required machinery.

### 1.1 Osmotic imprinting

TLICA treats repeated ambient co-occurrence as capable of changing substrate-level patterning without deliberate reasoning. Osmotic imprinting retunes salience gates and somatic-affective associations and can seed proto-patterns that later become explicitly usable.

The foundation already places **aesthetic dispositions** among patterns that can be strongly osmotic. That makes taste, music, visual style, and other trained preferences natural application domains.

### 1.2 Proto-pattern -> explicit accessibility -> deployable tool

For verification tools, TLICA already specifies a gradual developmental arc:

$$
\text{ambient / repeated encounter}
\to
\text{substrate proto-pattern}
\to
\text{explicit accessibility}
\to
\text{deployable tool}.
$$

The present note asks whether an analogous arc occurs below propositional reasoning:

$$
\text{ambient sensory encounter}
\to
\text{proto-discrimination}
\to
\text{stable perceptual factorization}
\to
\text{deployable discriminative operator}.
$$

If so, verification tools would be one specialized member of a broader family of **acquired discriminative operators**.

### 1.3 The proposed broader toolkit

Let the time-indexed toolkit of an I be decomposed schematically as

$$
\mathcal T_m(t)
=
\mathcal T_m^{\rm perceptual}(t)
\cup
\mathcal T_m^{\rm affective}(t)
\cup
\mathcal T_m^{\rm conceptual}(t)
\cup
\mathcal T_m^{\rm verificational}(t).
$$

Only the last class is currently formalized as a verification toolkit in the foundation. This note does **not** assert that the foundation should immediately be widened. It identifies acquired taste as a candidate application that can determine whether the broader superclass is actually needed.

---

## 2. The motivating case: alcohol

Alcohol is useful because the same family of chemical stimuli can be strongly aversive to an inexperienced person and later become richly differentiated and positively valenced.

Ethanol-containing beverages are not sensory-simple. Human alcohol perception includes combinations of sweet and bitter taste, olfaction, and oral chemesthetic irritation/burning. The beginner may nevertheless experience only a low-dimensional summary such as:

$$
\boxed{\text{BITTER} + \text{BURN} + \text{BAD}.}
$$

The mature drinker may instead report a much more structured object:

$$
\begin{aligned}
\text{beverage} ={}&
\text{ethanol burn}
+\text{bitterness}
+\text{sweetness}
+\text{aroma}\\
&+\text{oak / malt / hop / ester / smoke structure}
+\text{texture}
+\text{finish}\\
&+\text{context}
+\text{ritual}
+\text{memory}
+\text{anticipated post-ingestive effect}.
\end{aligned}
$$

The crucial possibility is that the burn and bitterness did **not** disappear. Rather, they ceased to exhaust the representation.

> The once-dominant aversive feature becomes a coordinate of the object instead of approximately being the whole object.

This is the durable form of the intuition that the first taste is a "spiky graph" and the acquired taste is a complicated object that contains, but contextualizes, the spike.

---

## 3. Formalizing the "spiky graph"

Calling the initial experience literally discontinuous is probably too strong. A better mathematical formulation is **high local gain / metric distortion / high curvature** in the experienced representation.

Let

$$
x\in X
$$

be a physical stimulus represented in some external feature space $X$, and let

$$
R_t:X\times C\to Y_t
$$

be the time-dependent substrate/toolkit representation map, with context $C$.

The local amplification of a small physical perturbation $v$ can be written

$$
G_t(x;v)
=
\frac{\|D R_t(x)v\|}{\|v\|}.
$$

If an aversive direction $v_a$ has

$$
G_t(x;v_a)\gg G_t(x;v_j)
\qquad\text{for most other directions }v_j,
$$

then the representation is **salience-dominated** along that dimension.

Equivalently, for a world-space metric $d_X$ and experienced metric $d_t$, nearby physical stimuli can become phenomenologically far apart:

$$
d_X(x,y)\ll 1
\qquad\text{while}\qquad
 d_t(R_t(x),R_t(y))\gg 1.
$$

This is the precise version of "discontinuous information" intended here: not a claim of mathematical discontinuity, but a claim that the perceptual map can contain steep local gradients or large metric expansion along particular sensory axes.

---

## 4. A minimal acquired-taste model

Suppose the input contains latent sensory features

$$
x=(b,s,e,a,o,\tau,\ldots)
$$

for bitterness, sweetness, ethanol irritation, aroma, odor families, texture, and so on.

An inexperienced representation may be effectively compressed:

$$
R_0(x)\approx(-12b,-9e,+2s)+\epsilon.
$$

The experienced value is then dominated by bitterness and burn.

After repeated exposure, discrimination and association, the representation may expand:

$$
R_t(x)=
(f_1(x),f_2(x),\ldots,f_{k_t}(x)),
\qquad k_t>k_0.
$$

A useful operational definition is therefore:

> **Representational unfolding:** an increase in the number, stability, or separability of stimulus features that the subject can reliably discriminate or use in prediction, categorization, or description.

Valuation can then act on the richer representation:

$$
V_t(x,c)
=
\sum_i w_i(t)f_i(x)
+
\sum_{i<j}J_{ij}(t)f_i(x)f_j(x)
+
C_t(c).
$$

This matters because the interaction terms allow a formerly aversive feature to become relationally meaningful.

Bitterness alone may be negative:

$$
-b.
$$

But bitterness in relation to sweetness, aroma, roast, fermentation, or expected finish may contribute positively to the whole:

$$
-b+s+a+J_{b,a}\,ba+J_{b,s}\,bs.
$$

The phenomenological statement becomes:

> "I still taste the bitterness; I now taste what it is doing."

That is categorically different from simple desensitization.

---

## 5. Toolkit closure formulation

Let $\mathcal T_t$ be the set of currently deployable discriminative operators and $\mathrm{Cl}(\mathcal T_t)$ the structures constructible from them under permitted composition.

At an early stage:

$$
\mathrm{Cl}(\mathcal T_0)
$$

may distinguish only coarse classes such as

$$
\{\text{sweet},\text{bitter},\text{burning},\text{safe},\text{aversive}\}.
$$

Exposure can seed a candidate operator $\tau_{new}$. If it stabilizes, then

$$
\mathcal T_{t+1}=\mathcal T_t\cup\{\tau_{new}\},
$$

which changes the closure:

$$
\mathrm{Cl}(\mathcal T_t)
\subsetneq
\mathrm{Cl}(\mathcal T_{t+1}).
$$

This gives acquired taste unusually high theoretical value: unlike childhood acquisition of object permanence or implication, the observer can often report and measure **both sides of the transition**.

The same physical class of objects is encountered before, during, and after toolkit growth.

---

## 6. Important distinction: resolution is not truth

This proposal must not collapse TLICA's diagnostics.

A richer perceptual toolkit does **not** imply higher $\phi$ in the truth-indistinguishability sense unless the new operator participates in a constructible verification pathway.

Someone can acquire exquisite wine discrimination while being no better at establishing the truth of propositions about wine provenance. Conversely, a chemist can possess strong verificational tools while having mediocre perceptual discrimination.

Therefore track separately:

- **perceptual discrimination / representational resolution** — proposed application-level quantity;
- **$\kappa$** — live contact;
- **$\phi$** — toolkit-relative truth-indistinguishability / verification-pathway state;
- **$\rho$** — identity integration;
- **$\sigma$** — source-map adequacy;
- **$\mu$** — probe availability.

The acquired-taste proposal should not smuggle perceptual expertise into $\phi$.

---

## 7. Alcohol: associative and post-ingestive dimensions

The alcohol example has an additional complication: the stimulus is pharmacologically active.

A person may first drink because of peer pressure, ceremony, curiosity, or cultural participation. The later intoxication, social bonding, ritual, relief, celebration, or other consequences can add learned value to the sensory object.

Schematically:

$$
\text{flavor}
\to
\text{social / ritual context}
\to
\text{post-ingestive state}
\to
\text{updated valuation and expectation}.
$$

This gives at least three separable learning processes:

1. **sensory adaptation / habituation** — the aversive magnitude may decrease;
2. **hedonic or associative reweighting** — the same percept may receive a different value;
3. **representational unfolding** — the percept itself becomes more differentiated.

The present hypothesis concerns (3). Alcohol is a vivid example, but a poor clean-room experiment because all three can occur simultaneously. Coffee, unsweetened cocoa, bitter vegetables, fermented foods, hot peppers, complex cheeses, and non-food domains such as music may permit cleaner tests.

---

## 8. Autism and food selectivity: the candidate metric-distortion hypothesis

### 8.1 What is actually supported

At the group level, autistic children show elevated food selectivity relative to typically developing peers in the reviewed literature. Sensory processing differences — particularly texture, taste, smell, temperature, and related oral/tactile features — are repeatedly associated with food refusal and restricted repertoires.

This must be stated heterogeneously. Autism includes both hyper-responsive and hypo-responsive sensory profiles, and food selectivity is multifactorial. Rigidity/predictability, gastrointestinal symptoms, anxiety, prior aversive learning, motor/oral factors, family context, and other variables are live contributors.

### 8.2 The proposed TLICA mechanism

For a sensory-hyperresponsive individual, suppose one feature has unusually high experienced gain:

$$
g_a\gg g_j\qquad(j\neq a).
$$

Then

$$
R_t(x)
\approx
 g_a f_a(x)
+
\sum_{j\neq a}g_j f_j(x)
$$

is dominated by the aversive coordinate.

For example, two bites that differ only slightly in texture in physical stimulus space may be experienced as very far apart:

$$
d_X(x,y)\ll1,
\qquad
 d_t(x,y)\gg1.
$$

This predicts the subjective form:

> "Everyone else is treating these as nearly the same food, but they are not nearly the same event to me."

### 8.3 Why repeated exposure may sometimes fail

A common story says that repeated exposure should permit acquired taste. But if one aversive coordinate saturates the representation on each exposure,

$$
g_a f_a(x)
\gg
\sum_{j\ne a} g_j f_j(x),
$$

then each exposure can collapse toward the same coarse code:

$$
x\mapsto\boxed{\text{AWFUL}}.
$$

The residual structure may not become accessible enough to seed finer discriminations.

This yields a concrete hypothesis:

$$
\boxed{\text{Toolkit growth requires accessible residual variation beneath the current salience ceiling.}}
$$

If a dominant channel repeatedly saturates the available perceptual/focus bandwidth, basis enrichment may be slowed or blocked.

This is **CONJECTURED**, not established autism mechanism.

### 8.4 Why this matters clinically and conceptually

If the hypothesis is true, "just keep trying it" can fail for a principled reason. The person may not be refusing to learn a preference; the exposure may be failing to expose the lower-amplitude structure needed for learning.

A better acquisition procedure would reduce the dominant spike while preserving enough neighboring structure to permit discrimination. In principle:

$$
\text{attenuate dominant feature}
\to
\text{expose residual structure}
\to
\text{learn discriminations}
\to
\text{gradually reintroduce feature}.
$$

This is a research prediction, **not** treatment advice. Any feeding intervention — especially where nutrition, ARFID, medical conditions, or significant distress are involved — belongs with qualified clinicians and must respect consent and sensory safety.

---

## 9. Rival explanations that must remain live

The preferred frame only earns value if it predicts something beyond existing explanations.

### R1 — Pure hedonic reweighting

The representation does not become richer. The same perceptual object simply receives a less negative or more positive value.

Prediction: liking changes, but discrimination, identification, and generalization structure do not materially improve.

### R2 — Habituation / adaptation

The aversive feature decreases in perceived intensity with repeated exposure.

Prediction: the spike flattens, but no new stable feature dimensions appear.

### R3 — Associative / post-ingestive reinforcement

The sensory object acquires value by association with consequences such as caloric reward, pharmacological effect, social bonding, ritual, or relief.

Prediction: preference can change even without improved sensory decomposition.

### R4 — Semantic relabeling only

The person learns a vocabulary and constructs richer verbal reports without corresponding perceptual change.

Prediction: verbal descriptions become more elaborate, but nonverbal discrimination does not improve.

### R5 — Representational unfolding

New discriminative operators become stable enough that the stimulus occupies a richer accessible space.

Prediction: nonverbal discrimination, transfer, mixture decomposition, oddball detection, and/or prediction improve even when vocabulary and immediate hedonic judgment are controlled.

The experimentally serious version of this project is therefore **R1-R5 discrimination**, not merely collecting anecdotes of acquired taste.

---

## 10. Discriminating probes

### Probe A — Same liking, different resolution

Train two groups on the same stimulus family. Manipulate one condition to encourage sensory discrimination and another to encourage only evaluative exposure.

Pre-register outcomes:

- **R5 support:** discrimination improves in the sensory-learning condition even after matching for liking.
- **R1/R2 support:** liking/intensity changes without independent discrimination gain.
- **Ambiguous:** both move and cannot be causally separated.

### Probe B — Nonverbal oddball detection

Use pairs or triplets of closely related stimuli that differ along latent feature dimensions. Require only same/different or oddball choice.

This avoids confusing vocabulary acquisition with perceptual basis acquisition.

### Probe C — Mixture decomposition

Before and after exposure, ask whether a subject can recognize component A inside A+B mixtures, or predict how changing component A will alter the whole.

Representational unfolding predicts improved compositional access.

### Probe D — Transfer to novel exemplars

Train on one stimulus family and test novel members sharing the same latent feature.

A true acquired operator should generalize better than rote item familiarity.

### Probe E — Attenuate the spike

For participants with a strong aversive feature, construct graded stimuli in which that feature is reduced while secondary structure is preserved.

Compare:

$$
\text{full-spike repeated exposure}
\quad\text{vs}\quad
\text{attenuated-spike discrimination training}.
$$

The metric-distortion hypothesis predicts that attenuating the dominant feature can reveal residual variance and accelerate acquisition of discriminative structure.

### Probe F — Autism-specific falsifier

Within autistic participants, measure sensory responsivity independently rather than treating diagnosis as the mechanism.

The hypothesis predicts that the relevant variable is feature-specific gain / over-responsivity, not "autism" simpliciter.

If food selectivity is better predicted entirely by rigidity, GI variables, anxiety, or learned avoidance after sensory gain is controlled, the proposed metric-distortion mechanism loses explanatory weight.

---

## 11. Measurement sketch

For stimulus set $S=\{x_1,\dots,x_n\}$, collect at multiple times $t$:

1. pairwise perceptual distances $\hat d_t(x_i,x_j)$;
2. nonverbal discrimination accuracy;
3. response time;
4. intensity ratings for candidate dominant features;
5. hedonic ratings;
6. free description / vocabulary;
7. context and expectation measures.

Construct an empirical representational geometry from $\hat d_t$.

Candidate signatures of unfolding:

- increased rank or effective dimensionality of the representational matrix;
- new stable clusters aligned with latent stimulus features;
- improved out-of-sample decoding of stimulus parameters from perceptual judgments;
- improved discrimination without corresponding reduction in dominant-feature intensity;
- preserved detection of the formerly aversive component alongside richer decomposition of the whole.

That last signature is especially important. It distinguishes

$$
\text{"I no longer taste the bitterness"}
$$

from

$$
\text{"I still taste it; it is no longer the whole object."}
$$

---

## 12. TLICA-level consequence if supported

If R5 survives the probes, TLICA gains a useful general distinction:

$$
\boxed{\text{world complexity} \neq \text{accessible complexity}.}
$$

Let the world present structure $X$, while the subject's current toolkit induces

$$
R_{\mathcal T_t}:X\to Y_t.
$$

Learning can leave $X$ approximately fixed while changing the map:

$$
R_{\mathcal T_0}
\longrightarrow
R_{\mathcal T_1}
\longrightarrow
R_{\mathcal T_2}
\longrightarrow\cdots.
$$

A stimulus initially compressed to

$$
R_{\mathcal T_0}(X)=\{\text{gross}\}
$$

can later unfold into

$$
R_{\mathcal T_n}(X)
=
\{\text{bitter},\text{smoky},\text{floral},\text{oaky},\text{dry},\text{warm},\ldots\}.
$$

The substrate need not receive radically more physical information. More of the information already entering through contact becomes **factorable** by the acquired toolkit.

A deliberately strong but testable formulation is:

$$
\boxed{\text{Some acquired tastes are experienced dimensionality increasing.}}
$$

"Dimensionality" here means operationally recoverable discriminative structure, not a metaphysical claim about qualia and not necessarily an increase in receptor count or raw sensory-channel capacity.

---

## 13. Broader application domain

If the mechanism is real, food is only the easiest case to see.

Potential homologues:

- **music:** noise / unpleasant complexity -> separable rhythm, timbre, harmonic tension, form;
- **visual art:** "random marks" -> compositional, historical, material, and stylistic dimensions;
- **mathematics:** undifferentiated symbol mass -> reusable operators, invariants, proof shapes;
- **literature:** opaque prose -> syntax, voice, allusion, narrative architecture;
- **emotion:** "I feel bad" -> separable somatic, situational, affective, and appraisal components;
- **social perception:** coarse like/dislike -> increasingly differentiated cues and relational structure.

These should not be assumed identical. The useful conjecture is that they may share the operator:

$$
\text{coarse compression}
\to
\text{repeated structured encounter}
\to
\text{new discriminators}
\to
\text{richer accessible geometry}.
$$

---

## 14. Claim ledger

| Claim | Status | Notes |
|---|---|---|
| TLICA already contains osmotic imprinting, proto-patterns, and gradual verification-tool acquisition | **Disclosed within TLICA** | Existing foundation commitment; not new here. |
| Repeated exposure can change liking for at least some initially bitter/novel beverages | **Corroborated, bounded** | Supported by experimental literature; not universal across all tastes or contexts. |
| Alcohol flavor perception contains taste, olfactory, and irritation components | **Corroborated** | Established chemosensory literature. |
| Autistic populations show elevated food selectivity, with sensory features including texture/taste/smell often implicated | **Corroborated, population-level** | Heterogeneous; not every autistic person and not a complete causal explanation. |
| Acquired taste sometimes increases the operational dimensionality of accessible sensory representation | **Conjectured** | Central hypothesis; requires nonverbal discrimination and transfer probes. |
| High sensory gain can occlude lower-amplitude residual structure and thereby slow toolkit acquisition | **Conjectured** | Candidate mechanism. |
| The autism-food-selectivity association is substantially explained by this metric-distortion / occlusion mechanism | **UNVERIFIED** | Must be distinguished from rigidity, GI factors, anxiety, motor/oral factors, learned avoidance, etc. |
| Verification tools should be generalized in the foundation to all discriminative operators | **UNVERIFIED / architectural decision** | Do not change foundation until application-level evidence requires it. |

---

## 15. External evidence anchors

These are evidence anchors for later literature work, not a claim that the present note has completed a systematic review.

1. **Stein LJ, Nagai H, Nakagawa M, Beauchamp GK (2003).** *Effects of repeated exposure and health-related information on hedonic evaluation and acceptance of a bitter beverage.* Appetite 40(2):119-129. PMID **12781161**. DOI **10.1016/S0195-6663(02)00173-3**. Repeated daily exposure increased hedonic ratings for the tested bittersweet beverage; context and post-ingestive association were discussed.

2. **Ballard IC, Hennigan K, McClure SM (2017).** *Mere Exposure: Preference Change for Novel Drinks Reflected in Human Ventral Tegmental Area.* Journal of Cognitive Neuroscience 29(5):793-804. PMID **28129051**. DOI **10.1162/jocn_a_01098**. Repeated novel-drink exposure produced preference changes associated with valuation-network changes.

3. **Mattes RD (1994).** *Influences on acceptance of bitter foods and beverages.* Physiology & Behavior 56(6):1229-1236. PMID **7878095**. DOI **10.1016/0031-9384(94)90370-0**. Useful counterweight: repeated exposure did not uniformly increase pleasantness for all bitter/sour foods in the tested design; individual differences matter.

4. **Mennella JA et al. (symposium overview, 2003).** *Chemosensory Factors Influencing Alcohol Perception, Preferences, and Consumption.* Alcohol-related chemosensory review material, PMC **PMC1940064**. Alcohol flavor involves taste, olfaction, and oral irritation, and varies with concentration and individual factors.

5. **Food selectivity and autism: a systematic review (2025).** PMID **40881072**, PMC **PMC12304907**. Review of literature through 2024; reports greater food selectivity in autistic children and identifies texture, taste, smell and other sensory factors as important contributors.

6. **Feeding and eating problems in children and adolescents with autism: a scoping review (2021).** PMC **PMC8323334**. Reviews evidence linking selective eating with sensory sensitivities, with texture repeatedly prominent while also noting heterogeneity and some null findings.

7. **Food and Nutrition in Autistic Adults: Knowledge Gaps and Future Perspectives (2025).** PMC **PMC12073154**. Extends the food-selectivity/sensory-processing discussion into adulthood and emphasizes restricted repertoires and aversion to sensory food characteristics.

---

## 16. Integration rule

Do **not** promote this note into the frozen foundation merely because the analogy is compelling.

The next verdict-changing probe is:

> Demonstrate a case in which repeated exposure produces improved nonverbal, transferable decomposition of a stimulus family **without requiring either reduced aversive intensity or increased liking**.

That result would separate representational unfolding from the two easiest rivals — habituation and hedonic reweighting — and would justify treating acquired taste as evidence for toolkit-shape acquisition rather than merely as a preference change.

Until then:

$$
\boxed{\text{Representational unfolding: CONJECTURED, experimentally reachable.}}
$$

The durable intuition to preserve is:

> **The beer need not become less bitter. The mind can become large enough that bitter is no longer the whole beer.**
