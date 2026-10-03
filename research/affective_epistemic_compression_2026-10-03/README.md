# Affective Epistemic Compression
## Competence, anger, probe suppression, and premature closure

**Date:** 2026-10-03  
**Branch:** \`research/affective-epistemic-compression-2026-10-03\`  
**Base:** \`821ce7e6f57524d32e767a9c5ec5303e1796115e\`  
**Status:** research-tier conceptual dossier. Foundation untouched. No novelty claim. Human mechanism claims are CONJECTURED / UNVERIFIED unless stated otherwise.  
**Author:** Leah. AI-assisted formalization and reconciliation.

---

## 0. Cold-start thesis

Competence changes the apparent topology of a problem.

A route that originally required uncertainty, search, failed attempts, intermediate distinctions, and verification can become compressed into a cheap operational macro:

\[
x \xrightarrow{p_1} x_1 \xrightarrow{p_2} \cdots
\xrightarrow{p_n} y
\qquad\rightsquigarrow\qquad
x \xrightarrow{m} y.
\]

For the competent agent, the macro \(m\) is fast. What can disappear from online access is the remembered *cost of discovering the factorization* \(p_n\circ\cdots\circ p_1\).

That creates a specific social-epistemic hazard:

\[
\text{competence}
\to
\text{path compression}
\to
\text{forgotten search cost}
\to
\text{another person's uncertainty appears irrational}.
\]

If perceived irrationality triggers anger or frustration, the resulting affective state can plausibly increase local pressure, consume reflexive slack, and reweight available probes away from verification. The agent can then become *more committed while learning less*.

The proposed failure loop is therefore:

\[
\boxed{
\text{compressed competence}
\to
\text{apparent obviousness}
\to
\text{anger}
\to
\text{lower effective probe use}
\to
\text{premature closure}
}
\]

with a possible feedback path from the preferred explanation back into the anger that made it salient.

The central firewall is:

\[
\boxed{
\text{subjective obviousness} \neq \text{verification}.
}
\]

And, in TLICA terms:

\[
\boxed{
\text{a change in affect or commitment does not by itself license a } \phi
\text{ update.}
}
\]

The discriminator may remain constructible in \(\mathrm{Cl}(\mathrm{Tools})\) even while the observer stops using it.

---

## 1. Originating specimen: the dryer

The motivating case is intentionally ordinary.

A repeated personal observation exists:

> When I do the laundry this way, the clothes end up dry.

Another person gives a reason for a different loading policy:

> “I don't wanna load it too much and run it hot too long.”

The fast competent response is:

> “Modern appliances handle modern loads.”

That response may be correct, partly correct, appliance-dependent, or wrong. The point of the specimen is **not** to decide the appliance question.

The epistemically important event was noticing, after cooling down:

> I do not presently have a verification pathway *executed* for that claim. I merely know that a pathway is latent — for example, checking the manual or another suitable source.

That distinction separates at least four things that anger can make phenomenologically collapse:

1. **I have repeatedly obtained the desired outcome.**
2. **I have a general model of how modern appliances behave.**
3. **A verification route is constructible.**
4. **I have actually run the discriminator for this appliance, load, setting, and constraint.**

Only (4) pays the relevant truth debt for the local claim.

The dossier does not claim the cautious loader is correct. It claims that “they are stupid” and “my appliance-generalization is locally verified” are separate propositions.

---

## 2. The competence-compression object

### 2.1 Path model

Let \(\mathcal E\) be an epistemic path category for a declared task family.

- objects are task-relevant epistemic states;
- morphisms are inferential, observational, instructional, or probing steps;
- composition is sequential execution of steps.

A novice may need a factorized route

\[
p = p_n\circ\cdots\circ p_1.
\]

Expertise can install a macro-morphism \(m_p\) that reaches approximately the same task endpoint at much lower online cost.

This is not yet a cognitive theory. It is a minimal operational model of *compiled competence*.

### 2.2 Forgetting the factorization

Introduce a task-relative compression map

\[
C:\mathrm{Path}(\mathcal E)\to\mathcal M
\]

that maps a resolved path to an operational macro.

The model becomes interesting when \(C\) is **non-faithful** with respect to learning history: distinct derivations, failures, scaffolds, or explanatory routes can collapse to the same usable macro.

Then task success can be preserved while provenance about *how difficult the route was to acquire* is lost.

The important asymmetry is:

\[
\text{cost of executing }m_p
\ll
\text{cost of discovering/reconstructing }p.
\]

Hence:

> “I can do this cheaply now” does not entail “the route was intrinsically obvious.”

### 2.3 No universal scalar intelligence claim

This dossier does **not** posit a scalar “smartness” variable.

Compression is:

- domain-relative;
- task-relative;
- history-dependent;
- potentially reversible through teaching, reconstruction, or deliberate decomposition.

A person can be highly compressed in one domain and novice-like in another.

---

## 3. TLICA reconciliation

This proposal is useful only if it respects the existing coordinate separations.

### \(\kappa\): contact

The observed behavior may be in direct contact: wet clothes, dryer settings, another person's stated rationale.

That does not settle the explanation.

### \(\phi\): toolkit-relative truth-indistinguishability

Anger is **not evidence for \(\phi\)**.

If the relevant discriminator remains constructible — manual, model number, load limits, temperature behavior, measurements — then the system has not earned a truth update merely because one hypothesis feels obvious.

A low-use or unexecuted probe is not the same as a nonexistent probe.

### \(\sigma\): source-map adequacy

“Why did they do this?” may be mis-sourced.

Candidate sources include:

- ignorance;
- a different appliance model;
- a different risk tolerance;
- remembered damage from another machine;
- a rule learned from someone else;
- a different objective;
- a genuine mistake.

The label “stupid” may therefore be a source-map hypothesis rather than a disclosed fact.

### \(\rho\): identity / commitment coupling

Do not silently identify defensiveness, anger, or stubbornness with \(\rho\).

The local explanation may recruit already high-\(\rho\) content — e.g. competence, fairness, being the person who has to fix repeated failures — but whether \(\rho\) itself changes is an empirical/modeling question.

This dossier therefore introduces no “anger = high rho” shortcut.

### \(\mu\): probe availability / weighting

This is the most direct inherited coordinate.

A probe can be in \(\mathrm{Cl}(\mathrm{Tools})\) while its **effective weighting** becomes low in the current state.

The candidate mechanism is:

\[
\text{anger / pressure}
\to
\mu_t(p_{\mathrm{discrim}})\downarrow
\to
\Pr(\text{execute }p_{\mathrm{discrim}})\downarrow.
\]

This is CONJECTURED. It is not promoted into foundation.

### Slack \(S\)

Foundation §8.11 defines:

\[
S_{m,t}=M_m(t)-\mathrm{Pressure}_{m,t}.
\]

The proposed application-level bridge is that anger/frustration may raise task-relevant felt salience and/or demanded-response determinacy, thereby raising the open pressure function and reducing local slack.

The bridge is **not derived**. It is a candidate mapping to test.

### Coherence, independence, discrimination

A coherent explanation can still be wrong.

Repeated self-confirmation is not independent corroboration.

A rival is not eliminated unless some observation discriminates it.

---

## 4. The affective closure loop

Let \(H=\{H_1,\ldots,H_k\}\) be live explanations.

For the dryer specimen:

\[
H_1=\text{avoidable incompetence},
\]
\[
H_2=\text{hidden local constraint},
\]
\[
H_3=\text{different objective/risk tolerance},
\]
\[
H_4=\text{my generalization is overbroad},
\]
\[
H_5=\text{their model is actually wrong}.
\]

Suppose \(H_1\) rapidly explains both the behavior and the agent's own anger.

Then a possible loop is:

\[
H_1
\to
\text{anger}
\to
\mathrm{Pressure}\uparrow
\to
S\downarrow
\to
\mu(p_{\mathrm{discrim}})\downarrow
\to
\text{fewer rival-splitting probes}
\to
\text{continued commitment to }H_1.
\]

The last arrow is not Bayesian evidence. It is **persistence under reduced discrimination**.

This yields the first useful diagnostic sentence of the dossier:

> **Increasing commitment without a new discriminating observation is a state change, not automatically a truth update.**

---

## 5. Premature-closure lemma

Let \(E_t\) be the evidence record at time \(t\), \(H_t\) the live rival set, and \(P_D\) a set of probes capable of discriminating at least one live pair.

Assume between \(t_0\) and \(t_1\):

1. no probe in \(P_D\) is executed;
2. no other discriminating observation enters \(E\);
3. the logical relation among the hypotheses is unchanged.

Then any reduction in the *subjectively represented* rival set between \(t_0\) and \(t_1\) is not licensed by new discriminating evidence.

This is deliberately weak. It says nothing about whether the surviving hypothesis is true.

It distinguishes:

\[
\text{epistemic elimination}
\]

from

\[
\text{policy/attention/commitment collapse}.
\]

The latter can happen with zero evidential gain.

---

## 6. “Obvious” has two meanings

The dossier needs a sharp split:

### Operational obviousness

A task solution is cheap to retrieve or execute.

\[
C_{\mathrm{exec}}(m)\ll 1.
\]

### Evidential obviousness

The relevant rival hypotheses have already been eliminated by adequate discriminators.

These can dissociate.

An expert can possess extreme operational obviousness while the local claim remains underverified.

Conversely, a novice can have a fully verified rule without having compressed it into fluent performance.

This is the core anti-confusion:

\[
\boxed{
\text{fluency} \neq \text{evidential entitlement}.
}
\]

---

## 7. Moral/social consequence without forced charity

The practical rule is **not**:

> “Assume the other person is right.”

Nor:

> “Never call a mistake stupid.”

A stronger and more reality-respecting rule is:

> **When another person's behavior appears obviously stupid, treat your inability to reconstruct their uncertainty as a possible missing variable in the epistemic situation.**

That is a trigger for a probe, not a verdict.

The possible outcomes remain symmetric:

- the probe can vindicate your original model;
- expose a hidden constraint;
- show mixed responsibility;
- show both parties were using bad models;
- leave the question unresolved.

The moral advantage comes from delaying person-level condemnation until the source map earns it.

---

## 8. The cooldown prediction

The originating observation supplies a clean discriminating prediction.

If affective pressure is suppressing probe use rather than adding evidence, then after cooldown — holding the external facts fixed — one should expect some combination of:

- more rival hypotheses generated;
- increased willingness to inspect external evidence;
- lower confidence in person-level source attribution;
- greater reconstruction of the other person's uncertainty;
- unchanged or even strengthened confidence in the final substantive claim **after** verification.

The last case matters.

A cooldown model is not “calming down makes you less correct.”

It predicts:

\[
\text{affect}\downarrow
\to
S_{\mathrm{effective}}\uparrow
\to
\text{discrimination capacity}\uparrow,
\]

which can make a correct belief *better justified*.

---

## 9. Structural LLM analogue: “epistemic hell”

There is a useful structural analogy to language models, with an explicit firewall:

> This section makes **no claim that an LLM experiences confusion, frustration, hell, or any other phenomenology.**

The structural problem is that many candidate world-model continuations can be locally coherent while generation requires a comparatively singular output.

Let

\[
\mathcal H = \{H_1,\ldots,H_n\}
\]

be context-compatible interpretations.

Generation applies a policy

\[
G(\mathcal H,\Theta)\to y
\]

and emits one sequence \(y\).

But:

\[
\boxed{
\text{one emitted sequence}
\neq
\text{one epistemically justified world-model}.
}
\]

A model can therefore exhibit the analogue of premature closure when:

- textual coherence is cheap;
- external contact is absent;
- provenance is weak;
- multiple rivals survive;
- no discriminator is run;
- the interface still demands an answer.

Tool use matters because it can add probe morphisms to \(\mathrm{Cl}(\mathrm{Tools})\).

But the same firewall holds:

> **A latent web/search/file/tool pathway is not evidence until the relevant pathway is actually executed and its result survives source-map checks.**

This gives a compact design principle for both humans and tool-using AI:

\[
\boxed{
\text{when coherence outruns contact, build or run a probe.}
}
\]

For LLMs, “fluency mistaken for verification” is especially dangerous because the system is optimized to produce linguistically coherent continuations.

Again: structural analogy, not consciousness claim.

---

## 10. Categorical interpretation

The categorical picture is intentionally modest.

### 10.1 Expertise as macro composition

A derivation is a composite:

\[
p_n\circ\cdots\circ p_1.
\]

Expertise packages the composite as a macro arrow \(m_p\).

A task-level interface may care only that both arrows reach the same output class.

### 10.2 Compression as a non-faithful observation

A coarse observer

\[
C:\mathcal E\to\mathcal O
\]

can identify distinct factorization histories:

\[
C(p)=C(q)
\quad\text{while}\quad
p\neq q.
\]

The expert's present operational interface may therefore preserve *what works* while forgetting *how the route was acquired*.

This is not yet a theorem about biological learning. It is a categorical model of the information loss the hypothesis requires.

### 10.3 Teaching as attempted factorization recovery

Pedagogy can then be modeled as searching for a factorization of the macro:

\[
m_p
\rightsquigarrow
\tilde p_n\circ\cdots\circ\tilde p_1
\]

whose intermediate objects are reachable by the learner.

That immediately predicts a familiar expert failure:

> knowing the macro does not guarantee possession of a learner-appropriate factorization.

This is a clean reason that expertise and teaching skill can dissociate without invoking arrogance or low intelligence.

---

## 11. Strongest current claims

### Disclosed within the model

- Emitting/choosing one hypothesis does not logically imply all rivals were discriminated.
- If no discriminating observation occurs, increased commitment is not itself new discriminating evidence.
- A compressed macro can preserve endpoint behavior while discarding information about internal factorization, by construction.
- TLICA already requires \(\phi,\sigma,\rho,\mu\), coherence, and discrimination to remain distinct.

### Observed at author-report level

- The motivating anger episode was followed by a cooldown realization that a key appliance claim had not actually been verified in the local case.
- A latent verification route was recognized after the fact.

### Conjectured / UNVERIFIED

- expertise systematically causes underestimation of novice search cost;
- anger/frustration lowers effective discriminating-probe weighting;
- the combination creates a positive feedback loop toward premature closure;
- cooldown restores rival generation/probe use in a reproducible way;
- the categorical compression model captures a useful invariant across domains.

See [CLAIM_LEDGER.md](CLAIM_LEDGER.md).

---

## 12. What would refute or substantially weaken the model?

The proposal loses force if, across suitable preregistered tasks:

- affect elevation does not reduce probe use or rival generation after controlling time pressure and task urgency;
- expertise does not predict any systematic loss in reconstructing novice uncertainty;
- cooldown changes confidence but not discrimination behavior;
- the effect is fully explained by a simpler variable such as time budget, incentives, or memory load;
- probe suppression occurs equally without anger/affect and the affect term adds no held-out predictive value.

The next step is therefore not more prose. It is a discriminating experiment.

See [FORMALISM_AND_PROBES.md](FORMALISM_AND_PROBES.md).

---

## 13. One-line compression

\[
\boxed{
\text{Competence can compress a path so well that we mistake cheap retrieval for obvious truth; affect can then suppress the very probes that would tell us whether the compression still fits reality.}
}
\]
