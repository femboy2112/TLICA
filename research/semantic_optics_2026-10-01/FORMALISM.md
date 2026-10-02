# Formalism — Semantic Optics

**Status:** research-tier candidate formalism. Sections marked **Disclosed** are direct mathematics inside the declared model. Cross-domain interpretations remain **Conjectured / UNVERIFIED**.

---

# 1. Recover the object

Fix:

- a task / decision boundary \(\tau\);
- a current proper situation \(x\in\mathcal W_\tau\);
- an observer \(j\);
- an observer state \(\Theta_j\);
- an observation interface;
- a response channel.

The complete semantic-optics loop is:

\[
x_t
\xrightarrow{O_{j,\tau}}
y_{j,t}
\xrightarrow{D_{j,\tau}(-;\Theta_{j,t})}
\widehat z_{j,t}
\xrightarrow{\pi_{j,\tau}}
a_{j,t}
\xrightarrow{F_\tau}
x_{t+1}.
\]

The one-way observer map is:

\[
\Omega_{j,\tau}
=
D_{j,\tau}\circ O_{j,\tau}.
\]

This is only the front half of the full dynamics.

---

# 2. Types

## 2.1 Proper situation

\[
\mathcal W_\tau
\]

is a declared task-relative state domain.

It should contain whatever proper-state distinctions the research question requires.

No claim is made that any observer can inspect all coordinates of \(\mathcal W_\tau\).

## 2.2 Evidence space

\[
\mathcal Y_{j,\tau}
\]

contains what observer \(j\) can receive through the declared interface.

An observation/exposure map is:

\[
O_{j,\tau}:
\mathcal W_\tau
\to
\mathcal Y_{j,\tau}.
\]

This map may be deterministic, stochastic, lossy, history-dependent, or controlled by another actor.

## 2.3 Interpretation space

\[
\mathcal Z_{j,\tau}
\]

contains the task-relative relational objects the observer can reconstruct.

The decoder is:

\[
D_{j,\tau}:
\mathcal Y_{j,\tau}\times\Theta_j
\to
\mathcal Z_{j,\tau}.
\]

## 2.4 Response space

\[
\mathcal A_{j,\tau}
\]

contains available responses.

The response policy is:

\[
\pi_{j,\tau}:
\mathcal Z_{j,\tau}
\to
\mathcal A_{j,\tau}.
\]

More generally \(\pi\) may also depend on observer state, value structure, role constraints, and uncertainty.

## 2.5 World update

\[
F_\tau:
\mathcal W_\tau\times\mathcal A_{j,\tau}
\to
\mathcal W_\tau
\]

or, when multiple actors are active,

\[
F_\tau:
\mathcal W_\tau\times
\prod_j\mathcal A_{j,\tau}
\to
\mathcal W_\tau.
\]

---

# 3. TLICA observer state

Do not compress TLICA diagnostics into one parameter.

Use a structured observer state:

\[
\Theta_j
=
(
H_j,
B_j,
\mathrm{Foc}_j,
\kappa_j,
\phi_j,
\sigma_j,
\rho_j,
\mu_j,
\tau_{O,j},
C_j,
\ldots
).
\]

This is schematic.

Each component keeps its existing type:

- \(H_j\): relevant history;
- \(B_j\): conceptual / perceptual / verificational toolkit;
- \(\mathrm{Foc}_j\): focus allocation;
- \(\kappa_j\): contact profile;
- \(\phi_j\): toolkit-relative truth-indistinguishability/pathway state;
- \(\sigma_j\): source mapping and its separately audited adequacy;
- \(\rho_j\): identity / commitment integration;
- \(\mu_j\): probe availability/weighting;
- \(\tau_{O,j}\): application-level observer update timescale;
- \(C_j\): current context.

There is **no universal scalar map**

\[
\Theta_j\mapsto q\in\mathbb R
\]

asserted here.

---

# 4. Observer-relative equivalence and quotient

Fix a task-relative comparison relation \(\equiv_\tau\) on reconstructed objects.

Define:

\[
x_1\sim_{j,\tau}^{\Omega}x_2
\iff
\Omega_{j,\tau}(x_1)
\equiv_\tau
\Omega_{j,\tau}(x_2).
\]

If \(\sim_{j,\tau}^{\Omega}\) is reflexive, symmetric, and transitive, then the optic quotient exists:

\[
\mathcal Q_{j,\tau}^{\Omega}
=
\mathcal W_\tau/\!\sim_{j,\tau}^{\Omega}.
\]

**Disclosed:** this is a genuine quotient once the relation is an equivalence relation.

**Warning:** approximate similarity is not automatically transitive. If the task uses a tolerance relation, cluster, cover, pseudometric ball, or fuzzy relation, quotient notation is not licensed until transitivity is established.

---

# 5. Optic collapse and splitting

## 5.1 Collapse

\[
x_1\neq x_2
\]

but

\[
x_1\sim_{j,\tau}^{\Omega}x_2.
\]

The observer interface cannot distinguish the task-relevant difference.

## 5.2 Splitting

For a fixed state \(x\),

\[
\Omega_{i,\tau}(x)
\not\equiv_\tau
\Omega_{j,\tau}(x).
\]

Different observer states produce different reconstructions.

Collapse is many-world-to-one-observer-object.

Splitting is one-world-to-many-observer-objects.

---

# 6. Categorical optic core

Let \((\mathcal C,\otimes,I)\) be a symmetric monoidal category.

A standard optic from \((S,S')\) to \((A,A')\) is:

\[
\operatorname{Optic}_{\mathcal C}
\bigl((S,S'),(A,A')\bigr)
=
\int^{M\in\mathcal C}
\mathcal C(S,M\otimes A)
\times
\mathcal C(M\otimes A',S').
\]

Choose a representative:

\[
l:S\to M\otimes A,
\]

\[
r:M\otimes A'\to S'.
\]

Semantic reading:

\[
S=\text{current proper state},
\]

\[
A=\text{exposed evidence},
\]

\[
M=\text{hidden residual context},
\]

\[
A'=\text{returned observer response},
\]

\[
S'=\text{updated proper state}.
\]

Write:

\[
\omega=[M,l,r].
\]

---

# 7. Closing the optic with an observer

Let:

\[
c_{\Theta_j}:A\to A'
\]

be the observer/controller process.

In the simplest deterministic case:

\[
c_{\Theta_j}
=
\pi_j\circ D_j.
\]

Close the optic:

\[
\operatorname{cl}_{\Theta_j}(\omega)
=
r
\circ
(\mathrm{id}_M\otimes c_{\Theta_j})
\circ
l
:
S\to S'.
\]

This is the central factorization:

\[
\boxed{
\text{world/interface optic}
+
\text{observer controller}
\to
\text{closed world transition}.
}
\]

The plus sign here is diagrammatic composition, not arithmetic addition.

---

# 8. Proposition — residual-representation invariance

Suppose two representatives of the same optic are related by:

\[
f:M\to N
\]

with:

\[
l'=(f\otimes A)\circ l
\]

and:

\[
r=r'\circ(f\otimes A').
\]

For any:

\[
c:A\to A',
\]

we have:

\[
r\circ(\mathrm{id}_M\otimes c)\circ l
=
r'\circ(\mathrm{id}_N\otimes c)\circ l'.
\]

## Proof

By substitution:

\[
\begin{aligned}
r\circ(\mathrm{id}_M\otimes c)\circ l
&=
r'\circ(f\otimes A')\circ(\mathrm{id}_M\otimes c)\circ l\\
&=
r'\circ(\mathrm{id}_N\otimes c)\circ(f\otimes A)\circ l\\
&=
r'\circ(\mathrm{id}_N\otimes c)\circ l'.
\end{aligned}
\]

The middle equality is bifunctoriality/naturality of \(\otimes\).

\(\square\)

**Status: Disclosed inside the standard optic construction.**

---

# 9. Why this theorem matters

The hidden residual may admit multiple equivalent encodings.

A semantic-optics theory should not assign different closed behavior merely because the scratch-space representation was changed along the coend equivalence.

This is a real compatibility check:

\[
\boxed{
\text{equivalent residual encoding}
\Rightarrow
\text{same closed external behavior}.
}
\]

Any TLICA bridge that violates this has not factored through the optic quotient.

---

# 10. Composition

Let:

\[
\omega_1:
(R,R')
\rightsquigarrow
(S,S')
\]

and:

\[
\omega_2:
(S,S')
\rightsquigarrow
(A,A')
\]

be optics.

Categorical optics compose by plugging one open diagram into the other.

The residuals combine monoidally.

Semantic interpretation:

> a multi-stage observation interface should be composable without flattening every hidden intermediate state into one global bespoke map.

Examples:

\[
\text{politician}
\to
\text{press}
\to
\text{clip}
\to
\text{viewer},
\]

\[
\text{actor}
\to
\text{camera}
\to
\text{edit}
\to
\text{audience},
\]

\[
\text{employee}
\to
\text{manager}
\to
\text{policy record}
\to
\text{HR}.
\]

The categorical composition law is inherited if the semantic bridge is genuine.

That inheritance is a future discriminator.

---

# 11. Mixed optics

The forward and backward channels may require different categories.

Let:

- \(\mathcal M\) be a monoidal category of residual contexts;
- \(\mathcal C\) and \(\mathcal D\) be \(\mathcal M\)-actegories.

A mixed optic has hom-object:

\[
\int^{M\in\mathcal M}
\mathcal C(S,M\bullet A)
\times
\mathcal D(M\ast B,T).
\]

This may be preferable when:

- observations are stochastic but actions deterministic;
- meanings live in a different semantic category than physical states;
- institutional responses are typed procedures;
- internal observer state requires enrichment.

No specific mixed category is chosen yet.

---

# 12. Stochastic extension

A deterministic decoder is too weak for many applications.

A likely extension is:

\[
D_j:
Y
\rightsquigarrow
Z
\]

as a Markov kernel or stochastic morphism.

Then:

\[
\pi_j:
Z
\rightsquigarrow
A'
\]

may also be stochastic.

The composite controller:

\[
c_{\Theta_j}
:
A
\rightsquigarrow
A'
\]

should live in a category admitting the relevant composition.

Bayesian lenses provide one candidate formalism when the decoder is explicitly inferential.

TLICA does not currently commit to Bayesian optimality.

---

# 13. Strategic extension

An actor may choose the presentation itself.

Let:

\[
g_u:S\to S_u
\]

be an intervention or presentation policy.

Then the actor may optimize:

\[
u^\star
\in
\arg\max_u
V\left(
\operatorname{cl}_{\Theta_j}(\omega_u)(S)
\right),
\]

or more specifically some desired observer response.

This enters open-game territory.

The observer optic alone is not a game-theoretic solution concept.

---

# 14. Pure optics steering

Let:

\[
R_\tau:S\to K
\]

extract the declared proper-state invariant.

An intervention \(u\) is task-pure optic steering when:

\[
R_\tau(g_u(s))=R_\tau(s)
\]

but:

\[
\Omega_{j,\tau}(g_u(s))
\not\equiv_\tau
\Omega_{j,\tau}(s).
\]

This is the minimal formal definition.

It does not tell us whether the intervention is:

- benign clarification;
- theater;
- PR;
- framing;
- politeness;
- deception;
- propaganda.

Those require independent normative and factual analysis.

---

# 15. Optic fidelity versus favorability

Define a declared task-relevant reference map:

\[
R_\tau:
S\to K.
\]

Suppose there is a transport:

\[
T_j:K\to Z_j.
\]

Then a reconstruction defect can be defined if \(Z_j\) has a comparison structure:

\[
E_{j,\tau}(s)
=
d_j\left(
\Omega_{j,\tau}(s),
T_j(R_\tau(s))
\right).
\]

This is an application-level metric, not a foundation quantity.

Favorability is a different functional:

\[
U_j:
Z_j\to\mathbb R.
\]

Thus one can have:

\[
E\text{ low},\quad U\text{ low},
\]

or:

\[
E\text{ high},\quad U\text{ high}.
\]

Truth and favorability are not ordered.

---

# 16. Optic robustness

For contexts \(c\) and observers \(j\), define a family:

\[
\Omega_{j,c,\tau}.
\]

Robustness asks how much the decoded relation moves under declared perturbations:

\[
\operatorname{Rob}(x)
=
\operatorname{Dispersion}
\left\{
\Omega_{j,c,\tau}(x)
\right\}_{j,c}.
\]

No particular scalar dispersion is privileged.

Cross-context invariance may be structural rather than numerical.

---

# 17. Manipulability

A candidate manipulability functional is:

\[
\operatorname{Manip}_{j,\tau}(x,z^\star)
=
\inf_u
\operatorname{Cost}(u)
\]

subject to:

\[
R_\tau(g_u(x))
=
R_\tau(x)
\]

and:

\[
\Omega_{j,\tau}(g_u(x))
\equiv_\tau
z^\star.
\]

This asks:

> how cheaply can the reconstruction be moved to a target while the declared proper-state invariant is preserved?

This can be finite, infinite, or undefined.

It is not a moral score.

---

# 18. Optic adversarial examples

A semantic adversarial example is a pair:

\[
x,x'
\]

such that the declared proper-state relation is small / invariant:

\[
R_\tau(x)\approx R_\tau(x')
\]

but observer reconstruction changes strongly:

\[
\Omega_j(x)\not\approx\Omega_j(x').
\]

Conversely, an occlusion pair has large proper-state difference with small optic difference.

These are natural probe targets.

---

# 19. Restricted Yoneda formalization

Let \(\mathcal C\) be the candidate semantic-optics category.

Let:

\[
i:\mathcal P\to\mathcal C
\]

be a probe functor.

Define the restricted nerve:

\[
N_i:
\mathcal C
\to
[\mathcal P^{op},\mathbf{Set}]
\]

by:

\[
N_i(X)
=
\mathcal C(i-,X).
\]

If \(i\) is dense:

\[
N_i
\]

is full and faithful.

Then the probe signatures preserve all morphism-level structure of \(\mathcal C\).

If \(i\) is not dense, the restricted probe language can be too weak.

---

# 20. Probe collision

Call \(X,Y\) a \(\mathcal P\)-collision when:

\[
X\not\cong Y
\]

but:

\[
N_i(X)\cong N_i(Y).
\]

This formalizes:

> distinct objects remain indistinguishable under the current probe family.

A new probe family:

\[
i':\mathcal P'\to\mathcal C
\]

resolves the collision if:

\[
N_{i'}(X)\not\cong N_{i'}(Y).
\]

This is the exact mathematical pattern exercised by the finite demo.

---

# 21. Relationship to \(\mu\)

Do **not** identify:

\[
\mu
=
\mathcal P.
\]

A better decomposition is:

- \(\mathcal P\): declared universe of probe objects/morphisms in the model;
- \(\mu_j\): observer-relative availability/weighting over some of those probes;
- \(\mathrm{Cl}(\mathrm{Tools}_j)\): closure of constructible probing operations;
- \(N_{\mathcal P_j}\): restricted nerve induced by accessible probes.

Then:

\[
\mathcal P_j
\subseteq
\mathcal P
\]

is an application-level bridge object.

This could make TLICA's probe discipline categorically legible without collapsing the existing diagnostics.

---

# 22. Relationship to \(\phi\)

Do **not** identify:

\[
\phi=N_{\mathcal P}.
\]

A possible bridge is narrower:

> a pair of contents that current tools cannot discriminate may correspond, in one formalization, to objects with identical restricted probe signatures over the currently constructible probe subcategory.

But:

- \(\phi\) has its own existing definition and pathway semantics;
- restricted Yoneda is a category-level representation theorem.

Any equivalence between them must be proved, not named.

---

# 23. Relationship to \(\sigma\)

\(\sigma\) concerns source mapping / provenance attribution.

Semantic optics separates:

\[
\text{evidence generation}
\]

from:

\[
\text{source attribution}.
\]

Two observers can receive the same \(y\) but map it to different presumed sources.

Thus \(\sigma\) naturally affects \(D_j\), but:

\[
\sigma
\neq
O_j.
\]

And:

\[
\text{optic fidelity}
\neq
\sigma\text{-adequacy}.
\]

One can accurately decode the presented evidence while mis-sourcing it.

---

# 24. Relationship to \(\rho\)

Identity/commitment coupling can alter:

- salience;
- response thresholds;
- search effort;
- acceptance/rejection of reconstructions;
- the cost of updating.

But:

\[
\rho
\not\Rightarrow
\text{accuracy}.
\]

High coupling is not evidence that an optic reconstruction is correct.

---

# 25. Relationship to semantic wake

Semantic wake is naturally represented as closed-loop accumulation.

At each step:

\[
x_t
\to
y_t
\to
\widehat z_t
\to
a_t
\to
x_{t+1}.
\]

Observer lag means:

\[
\Theta_{j,t}
\]

is itself updated slower than the world/interface changes.

A more complete dynamics therefore includes:

\[
\Theta_{j,t+1}
=
G_j(
\Theta_{j,t},
y_t,
\widehat z_t,
a_t,
x_{t+1}
).
\]

Now wake drag can be modeled as the accumulated consequence of repeated reconstruction error / lag.

This remains application-level and unverified.

---

# 26. Relationship to cinema

Cinema factors naturally into a composite optic chain.

A rough decomposition:

\[
\omega_{\text{acting}}
\circ
\omega_{\text{camera}}
\circ
\omega_{\text{edit}}
\circ
\omega_{\text{display}}.
\]

The viewer controller closes the final hole.

The compositional question is whether the semantic invariants preserved by the composed optic match those recovered by the viewer.

This is a sharper version of the earlier cinema diagram.

---

# 27. Relationship to Kaufman

Kaufman may alter not only the exposed view but the observer's selection among decoder families.

Introduce a decoder index:

\[
k\in K_j.
\]

Then:

\[
D_{j,k}:Y\to Z.
\]

A Kaufmanesque event can make:

\[
p(k\mid y)
\]

unstable or multimodal.

The observer must infer both:

1. the event content;
2. which decoder/frame applies.

This is a higher-order optics problem.

---

# 28. Relationship to institutions

A distributed institution can contain causal support in residual \(M\) while exposing only local \(A\).

An external observer acts on \(A\).

The institutional update then combines:

\[
M
\]

with the returned response.

This is one of the cleanest direct readings of the optic residual.

---

# 29. Relationship to reputation

A reputation is a compressed observer-side object built from a behavioral trace.

Different generators can collapse:

\[
x_1\neq x_2,
\qquad
\Omega_j(x_1)=\Omega_j(x_2).
\]

The appropriate repair is not necessarily “observe more of the same behavior.”

One may need a field-changing probe.

This directly matches *Cold Frame*'s varied-condition requirement.

---

# 30. Boundaries

This formalism does **not** establish:

- that every social interaction is literally an optic in one fixed category;
- that humans are Bayesian;
- that the correct base category is \(\mathbf{Set}\);
- that observer state is fully captured by TLICA;
- that TLICA is equivalent to categorical optics;
- that all hidden causal structure belongs in the optic residual;
- that every interpretive failure is a projection failure;
- that optics has one moral valence;
- that a restricted probe family corresponds exactly to \(\mu\) or \(\phi\);
- that Yoneda provides empirical truth;
- that representational equivalence implies phenomenological identity.

---

# 31. Immediate proof program

The next formal tasks are:

1. define a small \(\mathsf{SOpt}\) independently;
2. prove it is a category;
3. define a candidate functor into mixed categorical optics;
4. prove closure is well-defined under residual equivalence;
5. define observer decorations;
6. determine whether the decorated total category is a Grothendieck construction;
7. characterize the forgetful functor;
8. build a nontrivial full/faithful finite example;
9. build a counterexample to fullness or faithfulness under a too-coarse bridge;
10. test restricted-nerve density on finite models.

Only after these are complete should the Yoneda equivalence claim be upgraded.
