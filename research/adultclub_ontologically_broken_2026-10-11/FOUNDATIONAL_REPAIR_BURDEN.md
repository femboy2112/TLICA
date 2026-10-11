# Foundational repair depth: why some ideas enter peripheral space and others implicate the self

**The AdultClub™️ Is Ontologically Broken — research extension, 2026-10-11.**
**Provenance:** Leah's author-origin account is quoted exactly in [AUTHOR_RECORD.md](AUTHOR_RECORD.md); formalization, counterexamples and empirical conditions are assistant-authored.
**Status:** conditional mathematical definitions and a finite witness; psychological mechanisms, developmental gradients and individual interpretations **CONJECTURED / UNVERIFIED**.
**Foundation status:** TLICA unchanged; this is application-level research. No diagnosis of any person from defensiveness, no literal physical force or universal plasticity law.

## 1. The author's proposed geometry

The author distinguishes a weakly connected, self-peripheral representation from a relation deeply integrated into the construction of the self. Both can provoke defensive reactions depending on how the message is communicated, but a challenge to foundational construction is carried through a denser set of personally meaningful associations, making it more difficult to land as a calmly inspectable candidate revision.

This sharpens the existing [root implication](ROUTING_AND_ROOT_IMPLICATION.md) and [scattering/field update](SCATTERING_AND_FIELD_RECONSTRUCTION.md) notes. The new object is **counterfactual reconstruction burden**: *which currently justified commitments would need independent rejustification if a questioned inferential bridge failed?*

**Essential qualifications:**
- A peripheral claim can be intensely defended because of present insult, pressure, threat, or misunderstood intent.
- A foundational challenge can be calmly inspected, welcomed, or used for generative revision.
- The same content can elicit different response patterns under different delivery conditions without altering its propositional truth.
- An early-onset pattern can become deeply integrated, but so can an adult-acquired belief; an early learned event can remain peripheral.
- Event age, age of boundary consolidation, years of rehearsal, self-relative load at acquisition, TLICA identity coupling, existing alternatives and current slack are different explanatory variables.
- The author's earlier "inversely proportional to age" and current "proportional to age of onset" phrasings are preserved without silently asserting contradictory mathematical signs. The present research treats *developmental timing as a hypothesized moderator* pending a specifically declared functional form.

## 2. Justificatory dependencies, not mere graph degree

Define an observer's **represented** premise/evidence set \(E_G\) and currently endorsed claims \(R_G\). For each \(r\in R_G\), specify a family \(\mathcal J_G(r)\) of locally considered sufficient support sets. This is a chosen truth-maintenance representation, not an objective certificate of truth.

Define **represented warrantedness**

\[
\operatorname{Sup}_G(r\mid E)=1
\iff \exists J\in\mathcal J_G(r): J\subseteq E.
\]

For an inferential premise or bridge \(e\in E_G\), define the *current loss-of-support set*:

\[
\mathcal D_G(e)=
\{r\in R_G: \operatorname{Sup}_G(r\mid E_G)=1,\ 
\operatorname{Sup}_G(r\mid E_G\setminus\{e\})=0\}.
\]

A claim appearing in \(\mathcal D_G(e)\) is **not proved false**. Its currently represented justificatory routes have become inadequate under removal of \(e\), and new evidence could restore support. If a legitimate independent support route was already available, that claim does *not* enter \(\mathcal D_G(e)\).

This improves on simply counting arrows emanating from an edge: a heavily referenced relation can be epistemically redundant, while one apparently isolated relation can be extraordinarily self-relevant.

Define an optional task-relative diagnostic \(B_G(e)=\sum_{r\in\mathcal D_G(e)}w(r)\) only if the importance weights \(w\), their units, elicitation and interpretation are independently specified. **Do not identify \(B\) with TLICA \(\rho\), emotional intensity, a psychological energy quantity, or the moral worth of a belief.** Set size alone is a transparent baseline.

For an *actual*, not just currently represented, minimum reconstruction cost, one would need an independently justified update metric \(d\) and conditions specifying admissible revised models:

\[
C_G^*(e)=\inf_{\substack{G'\ \mathrm{admissible}\\G'\models\neg e\\G'\ \mathrm{honors\ retained\ evidence}}}d(G,G').
\]

Without operational definitions of admissibility, evidence and \(d\), this is a research target, **not a measured quantity**. The infimum can be undefined if there is no admissible repair or if the metric is not supplied.

## 3. Exact toy — authority bridge versus peripheral norm

Let the currently available represented premises be:

\[
E=\{b,h,p,k,d,j,r\},
\]

where \(b\) is a rule-to-legitimacy bridge, \(h\) past-cost context, \(p\) a peer norm, \(k\) demonstrated expert competence, \(d\) an independently sufficient justification, \(j\) rent due, and \(r\) a peripheral dress rule.

Define support families (each semicolon separates *alternative* complete sufficient support sets):

| Claim | Currently represented sufficient routes |
|---|---|
| Deference defines maturity | \(\{b\}\) |
| Past suffering was necessary | \(\{b,h\}\) |
| Questioning is irresponsible | \(\{b,p\}\) |
| An accountant is credible | \(\{b\};\{k\}\) |
| A particular rule might be justified | \(\{b\};\{d\}\) |
| Rent is due | \(\{j\}\) |
| Dress rule applies | \(\{r\}\) |

Refuting the *peripheral* \(r\) removes represented support from one claim. Refuting the *apparently foundational* \(b\) removes support from three claims, **not five**: expert competence \(k\) and a case-specific justification \(d\) provide independent routes. If those alternatives are independently unavailable, removing \(b\) causes five claims to lose their represented support.

This is a conditional mathematical contrast; none of the listed claims is asserted to be true, and the toy contains no empirical individuals or measurements.

The standard-library [finite_support_dependency.py](finite_support_dependency.py) reproduces the construction with **ten deterministic checks, locally passed 2026-10-11**. A robust finding in actual cognition would require independently eliciting dependencies *before* presenting the challenging question.

## 4. What the observer *perceives* can differ from the support graph

The real supports, the observer's represented supports and the observer's immediate estimate of a challenge's implications can differ:

\[
\mathcal D^{\rm actual}(e)
\quad \ne\quad \mathcal D_G(e)
\quad\ne\quad\widehat{\mathcal D}_{G,t}(e\mid q)
\]

in general.

A speaker might carefully question \(b\) while explicitly preserving \(h,p,k,d,j,r\). A listener could still infer, "if this is wrong, everything I am is wrong" and assign a much larger \(\widehat{\mathcal D}\) than the challenge entails.

Conversely, a listener may initially *underestimate* the ramifications of a very influential structural error.

A challenge can be phrased respectfully, abrasively, vaguely, indirectly, or as a personal attack. **Delivery modulates perceived stakes and present threat**; it does not itself supply or revoke the logical support of the underlying claim.

This explains why the phenomenological descriptor "nerve-hitting" should track the observer's **response to a perceived dependency challenge**, without allowing the response to certify the correctness of the source model.

## 5. The conditional behavioral hypothesis

Let \(a_e\) denote age of first acquisition, \(a_e^{\rm con}\) age/window of consolidation, \(\ell_e\) self-relative formation load, \(n_e\) repetition/rehearsal, \(\rho_e\) self-coupling of relevant represented contents, \(S_t\) current slack margins and \(q\) the delivery/probe.

A general uncalibrated hypothesis is

\[
I_t(q)=F(\widehat{\mathcal D}_{G,t}(e\mid q),\
a_e,a_e^{\rm con},\ell_e,n_e,\rho_e,S_t,\text{current threat},\text{context}).
\]

Here \(I\) is an operationalized response variable chosen by a study (e.g. self-rated affect). No scalar conserved emotional energy, differentiable \(F\), monotonicity, or proportional age law is established.

**Proposed dominant mechanism, not yet established:** when an observer experiences a question as destabilizing multiple highly self-coupled commitments without feasible repair routes, defensive rerouting may become comparatively available while carefully reconsidering the relevant bridge is costly.

**Important counterhypothesis:** a consolidated, strongly connected schema may make contradiction *more* detectable and support *better* updating when reliable information and adequate conditions exist. This is empirically plausible: Richter et al. (2019) found more updating of inconsistent material after consolidation in their human spatial-schema paradigm. Frank et al. (2018) found more attention to some unexpected schema components but worse integration than congruent material, illustrating that attention and incorporation can diverge. Neither study validates this self-foundation account.

Therefore distinguish **cost of reconstruction**, **capacity to recognize error**, **affective response**, **defensive/repair policy**, and **lasting structural update** as five separate quantities.

## 6. Discriminating design and falsifiers

Create low-stakes learned logical/social-rule networks with objectively calibrated dependency structures. Predeclare equivalent incoming challenges to high-dependency vs low-dependency relations, with parallel deliveries that preserve semantic content while manipulating perceived interpersonal threat in ethically appropriate ways.

Measure *before the challenge* which claims participants think depend on each rule, and whether independent supports are known and accessible. Afterward measure literal comprehension, how many commitments participants believe are implicated, response intensity, whether they use an alternative route, whether they rejustify claims, and retention/generalization on novel problems after a delay.

Run a full factorial with **dependency load** (high/low), **independent justified backup** (present/absent), and **delivery** (supportive/neutral versus antagonistic but nonthreatening) only if these are independently manipulated and all eight cells observed. Age of onset cannot be randomized ethically in a real developmental history; treat it as a separate longitudinal observational moderator, distinct from acquisition order in lab training.

**Favors this mechanism:** dependency/backup structure adds robust out-of-sample predictive power for perceived root implication and response/repair choices beyond offensiveness, difficulty, cognitive load and generic identity threat.

**Refutes or sharply weakens it:** objectively similar responses regardless of independently elicited dependency/backup structure after calibrating question difficulty and affective communication; or purely antagonistic wording explains every measured effect.

**Ambiguous:** participants infer differently worded propositions, the dependency structure was only inferred from their reaction, the perceived supports fail to match task calibration, or no follow-up establishes sustained revision.

**Controls:** positive valid inference and genuine warranted criticism, neutral matched-content questions, incorrect authority-based inference, low-stakes familiar schemas, high-degree-but-redundant support mutants, and blind raters. Verify the manipulation before inferring cognitive architecture.

## 7. Empirical provenance and limitations

- [Richter et al., 2019, *Scientific Reports*](https://doi.org/10.1038/s41598-019-39468-9): consolidated prior schema could *facilitate* learning from inconsistency in a controlled task, constraining simple integration-as-resistance claims.
- [Frank et al., 2018, *Learning & Memory*](https://doi.org/10.1101/lm.047738.118): in their event-memory tasks, incongruence increased some attentional measures while typically hindering integration compared with congruence.
- [Schaefer, Cheng and Dunn, 2022, *Lancet Psychiatry*](https://doi.org/10.1016/S2215-0366(22)00362-5): systematic review of childhood maltreatment studies found no consistent sensitive timing window across the most studied outcomes. This is a distinct population, exposure and outcome; it constrains universal age-effect rhetoric rather than directly testing the present model.

None of these establishes the psychological reality or universality of TLICA's model-dependency object. They are heterogeneous constraints, not votes.

**Verdict:** the relation between *perceived root threat*, *actual support dependence*, *developmental history*, *delivery* and *ability to reconstruct* is an excellent falsifiable target. But a person's strong response alone identifies none of these causes.

> **The difficulty of receiving an idea may depend less on its propositional complexity than on the amount of one's inhabited reality that appears to require reconstruction if the idea is true.**
