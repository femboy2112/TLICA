# Born Good?

## Moral Priors, Developmental Attractors, and the Boolean Baby Incident

**Status:** Author-originated TLICA research note, 2026-08-13. **UNVERIFIED** as an empirical model. This is not a foundation amendment, not a completed application paper, and not a claim that developmental psychology has established that humans are "born good." It records a sharpened conjecture, the logical correction that produced it, its fit with the existing architecture, rival hypotheses, and verdict-changing probes.

**TLICA dependencies:** Foundation v5.3.3, especially File 2 §§3–4 (developmental acquisition and Modes A/B/C) and File 3 §8 (substrate, focus, and imprinting); *The Cold Frame and Its Sources* v0.4.3; *Agency Architecture* v0.3.0.

---

## 0. The question and the corrected answer

The originating intuition was:

> People are born good; maleficent outcomes usually arise from the combination of environment and substrate. The many conspicuously bad people we encounter in history and public life may distort our estimate of the underlying distribution because bad outcomes leave unusually visible records.

The intuition contains something worth preserving, but its first formulation compresses too much. The strongest defensible version is not:

\[
\text{human at birth} \Longrightarrow \text{morally good}.
\]

It is closer to:

\[
\boxed{
\text{mixed substrate priors}
+\text{developmental environment}
+\text{imprinting history}
\longrightarrow
\text{path-dependent moral configuration}
}
\]

with the further conjecture that, under a sufficiently supportive ordinary social ecology, **prosocial configurations may form a comparatively broad or deep developmental attractor**.

This preserves the motivating insight while discarding the false binary. A newborn need not be morally good, morally bad, or even morally neutral in the sense of a completed moral agent. The newborn may instead possess an unequally weighted collection of capacities and response-priors from which moral agency is later constructed: attachment, distress sensitivity, social orientation, imitation, reciprocity, defensive aggression, dominance-seeking, coalition formation, threat detection, curiosity, and the capacity to model and route other subjects. None of those basis elements is itself a virtue or vice. Their developmental organization matters.

The resulting thesis is therefore:

> **Humans may be born with mixed social and self-preservational priors inside an architecture for acquired selfhood. Prosociality may be a natural developmental attractor under supportive conditions without being an innate moral essence. Many severely harmful adult configurations may be better explained by substrate × environment × history interactions than by an inborn evil essence.**

That thesis is plausible and TLICA-compatible. It is not yet established.

---

## 1. The Boolean Baby Incident

The correction arrived when the author noticed that the question had been posed as though "good" and "bad" exhausted the state space.

Let

\[
G(x) := \text{“}x\text{ is born good”}
\]

and

\[
B(x) := \text{“}x\text{ is born bad.”}
\]

Classical excluded middle gives:

\[
G(x) \lor \neg G(x).
\]

It does **not** give:

\[
G(x) \lor B(x),
\]

unless one separately proves that

\[
B(x) \equiv \neg G(x).
\]

That equivalence was silently imported. The actual mistake was therefore not merely "using the law of excluded middle." It was treating a substantive rival predicate as the exact Boolean complement of another predicate. From

\[
\neg G(x)
\]

one cannot infer

\[
B(x).
\]

The negation of "born good" includes many possibilities: morally unformed, motivationally mixed, prosocial in one domain and defensive in another, equipped with latent capacities but no stable moral organization, or too developmentally incomplete for the predicate to apply cleanly at all.

### 1.1 The authorized roast

TLICA was built, in large part, to stop people from collapsing distinct dimensions into one dial. It separates contact, truth-indistinguishability, identity-correlation, source-map adequacy, probe availability, toolkit closure, modeling, routing, ownership, responsibility, and accountability.

Its author then briefly represented the moral developmental state space of *Homo sapiens* as:

```text
bool baby_is_good;
```

The architecture devoted hundreds of pages to explaining why a hallucination, an anesthetized limb, and depersonalization cannot be represented on one axis. Five minutes later, the species received one bit. This is magnificent.

The incident is retained rather than edited away because it is methodologically useful. A framework earns trust partly by catching the compression errors of its own author. The embarrassing moment is therefore a negative control that passed: the architecture objected when its own multidimensional discipline was violated.

---

## 2. Three different claims hidden inside “born good”

The phrase "born good" can name at least three non-equivalent hypotheses.

### 2.1 Moral-essence hypothesis

A person begins life already possessing a morally good essence or settled moral character.

This is the strongest reading and the least compatible with TLICA's developmental account. The cogito anchors an I, but the lived profile, verification toolkit, identity integrations, developed orders of willing, referent models, and stable action dispositions are acquired. A newborn may have morally relevant substrate parameters; that does not amount to a completed moral character.

### 2.2 Early-prior hypothesis

Human newborns or young infants possess early biases toward some socially relevant patterns: social approach, distress, helping, affiliation, fairness, or agents who facilitate rather than obstruct goals.

This is an empirical claim. Some findings support early prosocial sensitivities, but the evidential picture is mixed and task-dependent. Even a robust early preference would establish a **prior**, not goodness. Looking longer at helping than hindering is not equivalent to owning a moral norm, acting from it under cost, generalizing it across in-groups and out-groups, or sustaining it when accountability disappears.

### 2.3 Developmental-attractor hypothesis

Given ordinary human substrate priors and sufficiently supportive conditions, developmental dynamics tend to produce configurations involving attachment, reciprocity, concern for other subjects, cooperative norm-learning, and aversion to unprovoked harm.

This is the most promising version. It says neither that moral character is present at birth nor that environment writes on a blank slate. It says the developmental landscape may be structured so that some configurations are easier to enter, more self-stabilizing, or more recoverable than others.

The research program should therefore replace the vague question

\[
\text{“Are humans born good?”}
\]

with the sharper question

\[
\text{“What morally relevant priors exist, and what attractor landscape do substrate, environment, and history jointly induce?”}
\]

---

## 3. TLICA translation: morality as a developed configuration

TLICA already supplies the central causal grammar.

The architecture begins with an indexed I, not a fully populated autobiographical or moral self. The lived self is acquired through contact, focus, imprinting, and Modes A, C, and later B. Focus capacity and other substrate parameters are inherited rather than chosen. Ambient regularities can be written into the substrate through osmotic imprinting without explicit attention, endorsement, or verification. The verification toolkit is learned through encounter. Early development therefore happens substantially **to** the I before the I can direct itself.

A schematic moral-development map can be written as:

\[
\mathcal{M}_{m,t}
=
\mathcal{F}
\bigl(
S_m,
P_{m,0},
E_{m,0:t},
H_{m,0:t},
\mathrm{Cl}(\mathrm{Tools}_{m,t}),
\lambda_{T\to R,m,t},
\eta_{m,0:t}
\bigr),
\]

where:

- \(S_m\) is the inherited substrate of I \(m\), including bodily and cognitive constraints;
- \(P_{m,0}\) is the minimally developed initial profile rather than a completed moral identity;
- \(E_{m,0:t}\) is the encountered developmental environment;
- \(H_{m,0:t}\) is the path-dependent history of contact, reinforcement, injury, care, identification, differentiation, and recovery;
- \(\mathrm{Cl}(\mathrm{Tools}_{m,t})\) is the current verification-tool closure;
- \(\lambda_{T\to R,m,t}\) is the developed coupling between modeling another subject and routing that subject into affective significance;
- \(\eta_{m,0:t}\) stands for stochastic or presently unmodeled variation.

This equation is **schematic application-level notation**, not a new foundation primitive and not a claim that the function \(\mathcal{F}\) is known.

### 3.1 Moral configuration is not one score

The output \(\mathcal{M}_{m,t}\) should not be collapsed into a scalar "goodness" value. At minimum, morally relevant structure includes distinct questions:

1. **Model fidelity:** Is the other represented as a full I-bearing subject, or as a thinned object, role, obstacle, or symbol?
2. **Routing:** Does the modeled other's disruption register in the agent's own affective and preservation-relevant configuration?
3. **Coupling:** How reliably does accurate modeling recruit routing across referent classes and under load?
4. **Identity placement:** How deeply are reciprocal or universalizing norms integrated into \(\rho\), and do they survive flattening of social accountability?
5. **Source-map adequacy:** Are beliefs about the target and situation correctly sourced, or merely high-\(\phi\) inside a defective source map?
6. **Agency:** Were live options constructible, available, selectable, and implementable? Was ownership intact? Was sourcehood compromised?
7. **Scope:** Does concern generalize beyond kin, allies, in-group members, or socially rewarded cases?
8. **Behavior under cost:** Does the configuration survive temptation, threat, anonymity, exhaustion, and conflict between preservation rankings?

A person can be strong on some axes and weak on others. One can model accurately and route weakly; route intensely over a distorted model; hold a norm instrumentally but not constitutively; care deeply for an in-group while treating an out-group as a thinned referent; commit harm under constrained agency; or perform good behavior for bad reasons. No single moral bit captures these dissociations.

---

## 4. Mixed priors rather than a blank slate or an evil seed

The revised model rejects two symmetric simplifications.

### 4.1 Not a blank slate

Substrate matters. Infants differ in activity, affective gain, task orientation, irritability, sensory thresholds, attention, fear response, approach tendencies, and regulatory capacity. These differences change which events seize focus, how intensely events are registered, what patterns are reinforced, and what developmental environments the child subsequently evokes or selects.

TLICA therefore predicts neither identical developmental starting points nor uniform response to the same nominal environment. Environment is always environment-as-contacted-through-a-substrate.

### 4.2 Not an evil seed

A harmful outcome does not require an intrinsic malevolent essence. Several routes already exist within TLICA:

- an inherited substrate parameter makes some regulation or routing operations unusually difficult;
- early Mode A differentiation occurs under chronic threat, producing defensive boundaries and hostile priors;
- osmotic imprinting installs associations before reflective access exists;
- identity-correlation integrates a local code whose application is internally coherent but externally destructive;
- the modeling channel is source-compromised;
- referent-thinning leaves the routing channel little to route;
- accumulated load produces state-to-trait conversion in coupling;
- agency is narrowed by fear, coercion, addiction-like capture, learned helplessness, or live-option failure;
- a highly moral agent faithfully acts on a culturally thinned or falsely sourced model of the target.

None of this removes accountability or denies that some people repeatedly choose severe harm. It changes the explanatory target. The question becomes not "Where is the evil substance?" but "What configuration produced this action, which parts were unauthored, which parts were owned, what could have discriminated or redirected the path, and what responsibility or accountability follows now?"

### 4.3 Goodness as a basin, not a substance

Define a provisional prosocial basin \(\mathcal{A}_P\) as a family of configurations in which:

- other subjects are modeled with adequate thickness and source fidelity;
- modeling ordinarily recruits routing;
- reciprocal or universalizing norms are sufficiently integrated to survive ordinary reductions in external surveillance;
- the agent can construct and implement non-harmful live options under normal load;
- the configuration generalizes beyond a narrow protected class;
- repair remains possible after local failure.

To call \(\mathcal{A}_P\) an **attractor** is to make a dynamical conjecture: nearby developmental states may tend to move toward or remain within this family under supportive feedback. It does not imply inevitability, global stability, or moral perfection. A basin can be shallow, domain-specific, punctured by stress, or exited after cumulative load. Different substrates may experience different basin geometries under the same environment.

The serious hypothesis is therefore not "goodness is the default setting." It is:

> **For a large region of ordinary human substrate × environment space, mutually prosocial organization may be easier to stabilize than persistent generalized maleficence.**

That is a claim about developmental geometry and population distributions, not essence.

---

## 5. Is the prevalence of “bad people” a survivorship bias?

The motivating statistical intuition is real, but **survivorship bias** is not the most precise label.

Survivorship bias usually concerns cases that remain observable after a selection process while cases that disappeared are omitted. Here the more direct problem is a combination of:

- **severity-weighted ascertainment:** extreme harm is more likely to enter legal, clinical, journalistic, and historical records;
- **historical trace bias:** destructive agents leave unusually durable institutional and narrative traces;
- **availability bias:** vivid harmful cases are easier to recall than ordinary decent lives;
- **denominator neglect:** the number of conspicuously harmful people is noticed without comparison to the full population at risk;
- **outcome-conditioned sampling:** explanations are built from people already selected for a malignant outcome;
- **cost asymmetry:** one destructive agent can affect thousands or millions, making prevalence and impact easy to confuse.

Metaphorically, the terrible cases "survive the filter" into collective memory. Formally, **visibility-conditioned selection bias** or **severity-weighted ascertainment bias** is cleaner.

The ordinary person who works, loves several people imperfectly, helps occasionally, causes limited damage, and dies without founding a dictatorship or serial-killer documentary contributes little to the archive. This makes cultural memory a deeply non-random sample of moral development.

But the bias claim cannot itself establish that most people are good. It only blocks an invalid inference:

\[
\text{many visible malignant cases}
\centernot\Longrightarrow
\text{malignancy is the modal human developmental outcome}.
\]

A base-rate claim requires representative prospective data, explicit outcome definitions, and separate measurement of frequency, severity, persistence, and reach.

---

## 6. What the empirical record presently permits

The evidence does not justify "humans are born good." It does justify taking early social/prosocial priors seriously while maintaining strong uncertainty about their interpretation and robustness.

### 6.1 Early helping exists, but it is not birth and not moral essence

Warneken and Tomasello reported spontaneous instrumental helping in young children, including helping an adult retrieve out-of-reach objects. This supports the presence of early-emerging helping capacities. It does not show that newborns possess settled moral character, that helping generalizes across domains, or that the behavior survives substantial cost and conflict.

### 6.2 The classic helper–hinderer result is not a secure foundation

Hamlin, Wynn, and Bloom reported that 6- and 10-month-old infants preferred helpful over hindering agents in the hill paradigm. That study strongly shaped the "moral baby" literature.

A large preregistered ManyBabies coordinated replication later tested 1,018 infants across 37 laboratories, with 567 infants included in the analysis. In the social condition, 49.34% preferred the helper—indistinguishable from chance. The clean conclusion is not that infants lack all prosocial priors. It is that this famous behavioral paradigm does not presently warrant high confidence in a robust helper preference of the originally estimated kind.

### 6.3 Newborn attention is genuinely interesting and still not goodness

Geraci and colleagues reported that 5-day-old newborns looked longer at prosocial than antisocial interactions in three experiments, including a preregistered partial replication. The result is unusually relevant because postnatal experience is extremely limited.

However:

- the experiments used small samples;
- preferential attention can reflect salience, predictability, approach orientation, or social alignment rather than moral approval;
- an attentional bias is not a norm, identity commitment, costly action disposition, or generalized moral character;
- prenatal and immediate postnatal learning are not literally zero.

This is evidence for an early socially relevant prior, not disclosure of innate goodness.

### 6.4 Social experience appears to refine moral-role inference

Zeng, Gill, and Sommerville found that 12- to 24-month-old infants formed some cross-situation moral-role expectations involving aggressors, victims, and protectors. Their exploratory analyses also associated stronger differentiation with sibling and daycare experience. This pattern fits a mixed model: early capacities plus developmental sharpening through social contact.

### 6.5 Substrate and environment both matter for aggression and antisocial trajectories

A genetically informed longitudinal twin study linked developmental changes in early temperament dimensions to aggression at age seven through both genetic and nonshared environmental variance. Other longitudinal work finds that persistent antisocial trajectories are associated with combinations of temperament or neurocognitive risk, parenting, peer environment, adversity, and developmental feedback.

No responsible synthesis of this literature supports either "environment alone creates bad people" or "bad people are simply born that way." The live empirical family is interactional, developmental, and heterogeneous.

---

## 7. Rival hypotheses and discriminating predictions

The preferred framing should compete against explicit rivals rather than absorbing every result after the fact.

| Hypothesis | Initial state | Role of environment | Expected evidence |
|---|---|---|---|
| **H1: Innate-good essence** | Settled good moral orientation | Mainly preserves or corrupts it | Robust newborn moral preferences across paradigms; strong cross-context invariance; early measures predict later moral conduct with limited mediation |
| **H2: Moral blank slate** | No morally relevant priors | Constructs nearly all moral organization | Little reliable newborn selectivity after low-level controls; large environmental effects; weak substrate-linked heterogeneity |
| **H3: Mixed priors + developmental attractors** | Uneven social, affiliative, defensive, aggressive, and regulatory priors | Shapes basin geometry and path through interaction with substrate | Some early social/prosocial biases, some failures and task sensitivity; strong developmental sharpening; gene/environment interplay; path dependence and multiple routes to similar behavior |
| **H4: Selfish/hostile default** | Predominantly self-protective or exploitative orientation | Socializes agents into cooperation | Early antisocial/self-favoring behavior should dominate when controls and costs are matched; prosocial conduct should track surveillance and reinforcement more than deep integration |

The current record appears most compatible with **H3**, but that is a provisional dominance claim, not a final verdict.

### 7.1 Predictions specific to the TLICA attractor model

1. **Prior–character dissociation.** Newborn or infant social preferences will predict later behavior only weakly unless mediated by profile development, toolkit acquisition, routing, identity placement, and environment.
2. **Substrate-dependent plasticity.** The same caregiving or social intervention will produce heterogeneous effects conditional on attention, affective gain, regulation, and contact structure.
3. **Modeling–routing dissociation.** Some harmful agents will accurately model others while routing them weakly; others will route strongly over a distorted or thinned model. The same outward behavior will therefore require different repairs.
4. **Load-induced state-to-trait conversion.** Repeated apparent betrayal, threat, or unresolved frame-decoherence will predict durable reductions in other-routing for a subset of high-coupling agents.
5. **Deep-placement resilience.** Prosocial norms held at high identity-correlation will survive anonymity and reduced external accountability better than shallow instrumental norms, though source-compromised models can still redirect them toward harm.
6. **Visibility correction.** Representative longitudinal samples will contain a much larger mass of low-harm or transient-harm trajectories than historical or forensic samples suggest, while a smaller persistent group will account for disproportionate harm.
7. **Repair specificity.** Model-thinning, routing attenuation, live-option failure, and constitutive norm absence will respond differently to re-thickening, affective contact, agency repair, and accountability structures.

---

## 8. Verdict-changing probes

### Probe A: preregistered newborn multi-paradigm battery

**Question:** Is there a domain-general early prosocial prior, or only task-specific attention effects?

Test the same newborns across several tightly controlled paradigms: approach/avoidance, helping/hindering, distress responsiveness, biological alignment, and non-social motion controls. Require independent stimulus sets and blinded coding.

- **Pass for H1:** a common latent prosocial factor appears across paradigms and survives low-level controls.
- **Pass for H2:** effects collapse under controls and show no cross-task coherence.
- **Pass for H3:** some early selectivity survives, but it is heterogeneous, task-sensitive, and better described as socially relevant priors than completed morality.
- **Ambiguous:** looking-time effects occur without convergence with physiological or later behavioral measures.

### Probe B: longitudinal substrate × environment map

Begin in infancy and repeatedly measure:

- temperament, regulation, attention, sensory and affective gain;
- caregiving responsiveness, threat, instability, social density, and peer ecology;
- modeling fidelity, routing, norm placement, source-map adequacy, and agency conditions;
- helping, aggression, fairness, deception, out-group generalization, and repair behavior.

Fit rival causal structures before outcome data are inspected. The crucial discriminator is whether prosocial outcomes are best explained by an innate stable trait, environment alone, or interactional developmental paths with hysteresis.

### Probe C: modeling-versus-routing intervention

Construct cases with matched target facts but independently manipulate:

1. the detail and subjecthood of the target model;
2. affective routing/contact;
3. accountability visibility;
4. cognitive load.

Measure whether harmful choice is repaired by re-thickening the model, restoring routing, reopening live options, or changing social cost. A single undifferentiated "empathy" theory predicts less repair-specificity than the TLICA decomposition.

### Probe D: the archive-denominator audit

Compare four samples:

- historical biographies selected for prominence;
- legal/forensic records selected for harm;
- clinical records selected for dysfunction;
- representative longitudinal population cohorts.

Estimate the distributions of harmful behavior by frequency, severity, persistence, and number of people affected. This directly tests whether public intuition confuses the visibility and reach of extreme cases with their population prevalence.

### Probe E: hostile-regime moral persistence

Measure behavior when external accountability, in-group approval, material reward, and reputational consequences are independently removed. Test whether identity placement, model fidelity, and routing predict which prosocial commitments survive.

The result could falsify a flattering version of the attractor hypothesis. If apparently deep prosocial commitments evaporate broadly under modest cost or anonymity, then "supportive conditions produce robust goodness" is too strong and must be narrowed.

---

## 9. Ethical consequence: explanation without exoneration

The substrate–environment framing creates a predictable moral anxiety: if nobody chose their starting substrate or early environment, does responsibility disappear?

TLICA already blocks that collapse. Ownership, responsibility, accountability, sourcehood, and desert are distinct. A harmful action may be genuinely owned while its upstream developmental sources were unauthored. Responsibility may be reduced along one axis and preserved along another. Accountability for containment, repair, restitution, treatment, or future risk can remain even where ultimate desert is weakened.

The point of developmental explanation is not to pronounce everyone innocent. It is to locate leverage accurately.

- If the failure is model-thinning, punishment alone may increase thinning while re-thickening may restore contact.
- If the failure is severed routing, factual education alone may leave the decisive channel untouched.
- If the failure is source-compromised but deeply moral action, moral condemnation may strengthen the destructive frame.
- If the failure is live-option construction, demanding a choice the agent cannot represent is not an intervention.
- If the failure is stable predatory preference plus intact agency, protection and accountability may dominate rehabilitation hopes.

A theory that says "environment did it" and stops is as structurally coarse as a theory that says "evil did it." The task is decomposition.

---

## 10. Claim ledger

### Disclosed within the stated formal boundary

- The law of excluded middle gives \(G\lor\neg G\), not \(G\lor B\).
- "Not born good" does not entail "born bad."
- TLICA's existing architecture treats the lived self, toolkit, identity integrations, and many agency structures as developmentally acquired rather than fully present at birth.
- A one-dimensional moral birth predicate discards distinctions the architecture requires.

### Corroborated, with scope limits

- Early helping and socially relevant infant responses have been observed in multiple paradigms.
- The classic helper–hinderer hill preference failed a large coordinated replication, so it should not carry the innate-goodness thesis.
- Recent newborn work provides evidence of early preferential attention to prosocial interactions, but not settled moral character.
- Longitudinal and genetically informed work supports heterogeneous substrate and environmental contributions to aggression and antisocial development.

### Conjectured

- Prosocial organization is a comparatively broad developmental attractor under sufficiently supportive conditions.
- Persistent generalized maleficence occupies a smaller population basin than its cultural visibility suggests.
- TLICA's modeling/routing/source-map/identity-placement decomposition will predict intervention specificity better than scalar empathy or goodness measures.

### UNVERIFIED

- The exact dimensions and geometry of the proposed moral attractor landscape.
- Whether a common early prosocial factor exists across newborn paradigms.
- Whether TLICA variables add predictive value beyond established developmental, attachment, temperament, social-learning, and personality models.

### Dark; the missing lamp

- A validated measure that distinguishes genuinely moral newborn sensitivity from lower-level social attention without requiring capacities newborns do not possess.
- A longitudinal dataset that jointly measures early substrate, environment, TLICA-relevant intermediate structure, and adult moral behavior.
- A representative denominator for "bad people" under an explicit, non-circular definition of badness.

---

## 11. Author questions for the next pass

1. What is the minimal operational definition of a prosocial attractor that does not smuggle moral conclusions into the measurement?
2. Is "good" best decomposed by harm, reciprocity, truth-respecting agency, referent thickness, scope of concern, or a conjunction of these?
3. Which components belong to the foundation, and which must remain application-level moral psychology?
4. Does the attractor metaphor require a formal state-transition model, or is it currently only a disciplined analogy?
5. What would count as evidence that some substrate configurations begin outside the reachable basin of ordinary prosocial development?
6. How should prenatal experience be represented when discussing "born" rather than "early appearing" traits?
7. Can the archive-denominator claim be measured without defining goodness as mere absence of criminality?
8. What distinguishes a morally good configuration from socially cooperative behavior that remains parochial, conformist, or cruel to excluded referents?
9. Does a high-coupling agent with a defective source map belong inside or outside the prosocial basin?
10. What intervention would most cleanly separate referent-thinning from low routing, shallow norm placement, and constrained agency?

---

## 12. Provisional synthesis

The original sentence—"people are born good, and environment plus substrate produces bad outcomes"—was directionally sensitive to a real asymmetry but formally overcompressed.

The stronger reconstruction is:

> A human being is born neither as a completed saint nor as a completed monster. The newborn arrives with a substrate containing mixed, unequally weighted social, defensive, affiliative, aggressive, regulatory, and attentional priors. The lived self and its moral organization are then built through contact, imprinting, identification, differentiation, toolkit acquisition, modeling, routing, and agency development. Under supportive conditions, prosocial organization may be a natural and comparatively stable attractor. Under other substrate–environment histories, the same architecture can yield defensive, thinned, exploitative, parochial, or persistently harmful configurations. Extreme harmful outcomes are likely overrepresented in cultural memory because their consequences and records are disproportionate, but this visibility bias does not by itself establish the population base rate of goodness.

Or, in the technically exact language demanded by the incident:

\[
\neg\texttt{baby\_is\_good}
\;\not\Rightarrow\;
\texttt{baby\_is\_evil}.
\]

The baby was never a Boolean. The theorist briefly was.

---

## References

1. Hamlin, J. K., Wynn, K., & Bloom, P. (2007). Social evaluation by preverbal infants. *Nature, 450*, 557–559. https://doi.org/10.1038/nature06288
2. Lucca, K., Yuen, F., Wang, Y., et al. (ManyBabies4 Consortium). (2025). Infants' social evaluation of helpers and hinderers: A large-scale, multi-lab, coordinated replication study. *Developmental Science, 28*(1), e13581. https://doi.org/10.1111/desc.13581
3. Geraci, A., Surian, L., Tina, L. G., et al. (2025). Human newborns spontaneously attend to prosocial interactions. *Nature Communications, 16*, 6304. https://doi.org/10.1038/s41467-025-61517-3
4. Warneken, F., & Tomasello, M. (2006). Altruistic helping in human infants and young chimpanzees. *Science, 311*(5765), 1301–1303. https://doi.org/10.1126/science.1121448
5. Zeng, N. J., Gill, I. K., & Sommerville, J. A. (2026). Infants make moral character inferences in multi-agent social interactions. *Communications Psychology, 4*, 51. https://doi.org/10.1038/s44271-026-00417-8
6. Penichet, E. N., Beam, C. R., Luczak, S. E., & Davis, D. W. (2025). A genetically informed longitudinal study of early-life temperament and childhood aggression. *Development and Psychopathology, 37*(2), 779–801. https://doi.org/10.1017/S0954579424000634
7. Moffitt, T. E., & Caspi, A. (2001). Childhood predictors differentiate life-course persistent and adolescence-limited antisocial pathways among males and females. *Development and Psychopathology, 13*(2), 355–375. https://doi.org/10.1017/S0954579401002097
8. Aguilar, B., Sroufe, L. A., Egeland, B., & Carlson, E. (2000). Distinguishing the early-onset/persistent and adolescence-onset antisocial behavior types: From birth to 16 years. *Development and Psychopathology, 12*(2), 109–132. https://doi.org/10.1017/S0954579400002017
