# Affective Yoneda — typed formalism and finite categorical witness

**Date:** 2026-11-07  
**Status:** mathematical identities below are **Disclosed** under their stated hypotheses. The mapping to lived interpersonal understanding is **CONJECTURED / UNVERIFIED**.  
**Dependency:** [research seed and boundaries](README.md). No foundation amendment.

## 1. The typed semantic-transport problem

Let $A,B$ be two communicators. Their representational spaces $\mathcal R_A,\mathcal R_B$ need not coincide. A communication task $\tau$ fixes a target set $I_\tau$ of *declared observables/invariants*, with comparison maps

$$
q_A:\mathcal R_A\longrightarrow I_\tau,
\qquad
q_B:\mathcal R_B\longrightarrow I_\tau.
$$

Let $\mathcal U$ be observable expressions, $\mathcal C_{AB,t}$ the dyad's hypothesized common-ground state at time $t$, and $\mathcal S$ the apparent sender/source label available to the recipient. A schematic, fallible interface is

$$
E_A:\mathcal R_A\times\mathcal C_{AB,t}\longrightarrow\mathcal U,
$$

$$
D_B:\mathcal U\times\mathcal S\times\mathcal C_{AB,t}
\longrightarrow\mathcal R_B.
$$

The task-relative reconstruction criterion for $m_A\in\mathcal R_A$ is

$$
q_B\bigl(D_B(E_A(m_A,c),s_A,c)\bigr)=q_A(m_A).
$$

This is **not** equality of private representations; the comparison is well-typed because both sides lie in $I_\tau$. Depending on task, the outcome could be a relation, an intended emotional valence, a counterfactual prediction, a constraint, or a participant-correctable interpretation. Neither $q_A$ nor $q_B$ is a measurement of qualia. In an empirical setting they require explicit operationalization and source checking.

The same external expression $u$ can have different readings as $s$ or $c$ varies:

$$
D_B(u,s_A,c_1)\ne D_B(u,s_X,c_1),
\qquad
D_B(u,s_A,c_1)\ne D_B(u,s_A,c_2).
$$

These inequalities are **possible effects to test**, not asserted universal laws. Apparent source, source authenticity, and actual intention must be distinguished; inaccurate source attribution can create a confident but false interpretation.

## 2. Conditional-information statement, with its exact scope

For *finite-valued, jointly distributed* variables $M$ (task-annotated intended content), $U$ (observed expression), $S$ (apparent source), and $C$ (relevant common-ground/context annotation), standard Shannon identities give

$$
H(M\mid U)-H(M\mid U,S,C)
=I(M;S,C\mid U)\ge 0.
$$

**Disclosed:** conditioning on additional variables cannot increase *expected* conditional entropy for this fixed joint distribution. It may increase uncertainty in a particular case $(u,s,c)$, and it need not improve a biased decoder's accuracy. The identity does not establish that interpersonal memories are accurately shared, that either party knows the other's first-person life, or that any distinctive *affective Yoneda* mechanism exists. Correlated bad priors can make both parties more confident and more wrong.

No information is created from nothing. Any compression of an utterance relative to its reconstructed relational content is enabled by information already held in the recipient's state and by the conditions under which messages are generated.

## 3. What exactly would be Yoneda-shaped?

Choose **explicitly** a locally small category $\mathcal M$ of candidate meaning structures and meaning-preserving transformations. Such a category has **not** yet been constructed for TLICA interpersonal semantics. Choose a subcategory of admissible probes

$$
i:\mathcal P_{AB,t}\hookrightarrow\mathcal M.
$$

The *candidate* restricted Yoneda nerve of $X\in\mathcal M$ is

$$
N_{AB,t}(X)=\mathcal M(i-,X):
\mathcal P_{AB,t}^{\mathrm{op}}\longrightarrow\mathbf{Set}.
$$

The standard full Yoneda embedding $y(X)=\mathcal M(-,X)$ is full and faithful. A restricted nerve $N_i$ is full and faithful **if and only if** $i$ is dense, under the standard categorical definition of density.

Consequences *within the declared mathematical category*:

1. If $i$ is dense, a natural isomorphism $N_i(X)\cong N_i(Y)$ implies $X\cong Y$.
2. If $i$ is not dense, reconstructability is not certified; some categories/probe sets have collisions (explicit witness below). Failure of density does **not** automatically imply an object-level collision for every category.
3. Full faithfulness never establishes that $\mathcal M$ exhausts reality or that actual people can enumerate all probes or certify the naturality of a psychological profile.

**Open bridge obligation:** define the observation/probe assignment from actual dialogue episodes into $\mathcal M$; show that composition and source/meaning types are respected; establish what the empirical decoder really estimates. Without that, Yoneda supplies a rigorous *comparison language* rather than an explanatory theorem of intimacy.

## 4. Disclosed finite witness: words alone versus relationships

Take $\mathcal G$ to be the category of **finite directed multigraphs**. An object $G$ has sets $V_G$ (vertices) and $E_G$ (edges), with maps

$$
s_G,t_G:E_G\longrightarrow V_G.
$$

A morphism consists of vertex and edge functions commuting with source and target. Let $P_V$ be the graph with one vertex and no edges. Let $P_E$ be the graph with two distinct vertices and one directed edge between them. There are precisely two endpoint inclusions $P_V\to P_E$.

For any graph $G$,

$$
\mathcal G(P_V,G)\cong V_G,
\qquad
\mathcal G(P_E,G)\cong E_G.
$$

The two endpoint inclusions induce precisely $s_G$ and $t_G$ when the Hom functor is evaluated contravariantly.

**Theorem (graph probe reconstruction).** For the full probe subcategory $\mathcal P$ on objects $P_V,P_E$, the restricted nerve

$$
N_{\mathcal P}:\mathcal G\longrightarrow
[\mathcal P^{\mathrm{op}},\mathbf{Set}]
$$

is full and faithful.

**Proof.** A natural transformation $N_{\mathcal P}(G)\to N_{\mathcal P}(H)$ has a component on $P_V$, namely a function $f_V:V_G\to V_H$, and a component on $P_E$, namely a function $f_E:E_G\to E_H$. Naturality for the two endpoint inclusions forces

$$
f_Vs_G=s_Hf_E,\qquad f_Vt_G=t_Hf_E.
$$

Thus the components constitute exactly a graph morphism $G\to H$. Conversely every graph morphism induces these components and satisfies naturality. These assignments are mutually inverse and compose correctly. Therefore the comparison on Hom sets is bijective. **QED.**

**Hostile counterexample to a vertex-only probe family.** Let $X$ have two vertices and one edge from the first to the second; let $Y$ have the same two vertices but no edges. They are not isomorphic as graphs, yet their profiles under the full subcategory containing only $P_V$ are isomorphic: both expose a two-element vertex set. The additional edge probe $P_E$ distinguishes them because

$$
|\mathcal G(P_E,X)|=1,\qquad
|\mathcal G(P_E,Y)|=0.
$$

**Interpretation, not theorem of mind:** a vocabulary-only interface can preserve terms while losing their relational composition. Additional probes asking how meanings connect can split that collision. The graph theorem does **not** show that relational tests determine the actual private content of another person; it illustrates the formal mechanism a future TLICA account would need.

## 5. Coherence under *novel* transformations

The discriminating intuition is not mere recall of a familiar expression. Suppose context transformation $\alpha:c\to c'$ has declared action $T^I_\alpha:I_\tau\to I_{\tau'}$ on the relevant task invariants. Let $(u,c)$ and $(u',c')$ be a documented pair of utterance-context trials intended to express related meanings. One proposed coherence test is

$$
q_B^{\tau'}D_B(u',s_A,c')
\ \stackrel{?}{=}\ 
T^I_\alpha\!\left(q_B^\tau D_B(u,s_A,c)\right),
$$

with the same relationship checked against Alice's *independently elicited* intended invariant. The symbol $T^I_\alpha$ must be **declared before scoring**; arbitrary after-the-fact interpretation is not transport. Test novel transformations of the expression, role, tone, stakes, or context, while checking which transformations *should* preserve versus change the invariant.

Successful coherence on a finite set of tests does **not** establish naturality over an infinite category. What it can establish is transfer within a measured probe closure, conditional on valid source attribution and on the chosen coding of the intended invariant.

## 6. Mathematical debt and false shortcuts

- **Category gap:** specify objects, morphisms, composition, identities, admissible contexts, and the observer map; do not use the word *Yoneda* as a substitute.
- **Probe gap:** test whether partner-specific probes outperform generic linguistic or frequency-based probes on *held-out* relational transformations.
- **Source gap:** mutual familiarity, affect, common ground, and accurate intention attribution may be confounded; acquire participant-corrected targets, sender controls, and a source ledger.
- **Boundary:** no categorical density claim can prove another person's consciousness, identical qualia, or metaphysical exhaustiveness.
- **Non-collapses:** restricted-nerve adequacy is not TLICA's $\mu$; categorical isomorphism is not $\phi$; mutual confidence is not $\sigma$; interpersonal significance is not evidence of correctness.

**Working recommendation:** retain "Affective Yoneda" as a memorable hypothesis label. Promote the categorical language only when the typed semantic category, probe assignment, and an empirical advantage over established common-ground accounts are demonstrated.