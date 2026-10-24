# Formal sketch — context boundaries and authority-defaulted transport

**Status:** research-level definitions and conditional mathematical observations. **Not** an empirical cognitive law, a validated structural equation model, or a new TLICA primitive.

## 1. Distinguish environment, observer, and the paper's claims

An actual social environment at time $t$ is $E_t$; indexed observers $i$ have toolkits $K_{i,t}$, local models $M_{i,u,t}$ in context $u$, and multiple nonexchangeable margins of slack $L_{i,t}$. The environment need not correspond to the observer's representation.

The paper uses a context index category $\mathcal C$ only after specifying objects (situated contexts, questions, evidence interfaces) and arrows (admissible shifts between them). Mere analogy among contexts does not supply a category, functor, or natural transformation.

A local model $M_{i,u,t}$ is a structured hypothesis/state used to answer questions in context $u$. It may be well calibrated for its local task even if the observer lacks a warranted way to carry its claims into context $v$.

Represent a candidate cross-context route by $r:u\leadsto v$, with opportunity/cost vector $c_i(r,t)$ and admissible resource/safety vector $L_i(t)$.

$$
\mathcal R_{i,t}^{\rm feasible}(u,v)
=\{r\in\mathcal R_{i,t}(u,v):c_i(r,t)\preceq L_i(t)\}.
$$

The order $\preceq$ is componentwise **only among quantities of the same kind**. Money, agency, time, and attention have no natural common addition unit.

**Conditional fact (set inclusion):** fixing route costs and other conditions, if $L'_i\preceq L_i$, then $\mathcal R_i^{\rm feasible}(L'_i)\subseteq\mathcal R_i^{\rm feasible}(L_i)$. This is immediate from the definition, not experimental proof that socioeconomic scarcity causes any particular reasoning deficit.

A route can be **conceivable but unaffordable**, **available but not recognized**, or **not constructible under the current toolkit**. These must not be merged. With TLICA diagnostics, $\phi$ is toolkit-relative truth indistinguishability and its pathway state, $\sigma$ tracks source-map adequacy, $\mu$ tracks probe availability, and $\rho$ identity coupling; none is the same as slack, authority deference, or felt intensity.

## 2. Distinguish the local models from their bridge

Consider two context-dependent propositions:

$$
P:\ \text{Noncompliance here risks loss of income};
\quad
Q:\ \text{Adults ought to honor legitimate obligations}.
$$

The purported global conclusion is:

$$
R:\ \text{This particular imposed rule is legitimate and immune to question}.
$$

The entailment $P,Q\models R$ **does not hold** without additional premises. A one-world countervaluation with $P=1,Q=1,R=0$ refutes it, assuming ordinary propositional semantics. This is a narrow disclosed logical result, not proof that the workplace rule is in fact illegitimate.

The actual missing bridge might be, for example:

$$
B:\ \text{Every enforced work condition is a legitimate adult obligation}.
$$

If the reasoning uses $B$, the argument can be formally valid but $B$ is a separately contestable premise. This is the sense of **authority at the boundary**. The fault, when present, is an unexamined rule connecting correct local knowledge to a global norm.

Let $T_{uv}^{\rm warranted}$ be the bridge justified by relevant data/assumptions, when defined. Let $A_{uv}^{\rm inherited}$ denote an internalized or culturally supplied authority-compatible bridge. The conjecture is conditional substitution:

$$
\mathcal R_{i,t}^{\rm feasible}(u,v)\ \text{inadequate}
\quad\Longrightarrow_{\rm sometimes}\quad
\widehat T_{i,uv,t}=A_{i,uv,t}^{\rm inherited}.
$$

The arrow tagged "sometimes" is a **causal hypothesis**. The premise does not logically force the substitution, and the inherited bridge may happen to be correct.

## 3. Local compatibility and the limits of sheaf language

For a genuinely declared atlas of domains $U_i$, local sections $s_i$ and overlap identifications $g_{ij}$, a globally consistent glued object requires compatible restrictions on overlaps. Where transition maps are appropriate isomorphisms on triple overlaps, one familiar condition is

$$
g_{jk}\circ g_{ij}=g_{ik}.
$$

It is not justified to assume psychological boundaries are invertible, that their overlaps are physical intersections, or that all of an observer's propositions form sections of a sheaf. A more modest formulation uses **partial, directed transports** and asks for coherence on paths where both compositions are meaningful.

A loop discrepancy, $T_{ki}\circ T_{jk}\circ T_{ij}\neq\mathrm{id}$, is a *formal inconsistency within an explicitly specified transport model*; it is not intrinsically a psychological pathology. Some contexts have legitimately noncommuting updates because time, evidence, and state change. Order dependence is not an error without a declared invariance requirement.

A "global frame" in the paper may mean an *inhabited impression of coherence* or a dynamically stable collection of locally applicable rules. That is weaker than a mathematically valid global section. Confusing these senses would reproduce the very ontology error the paper criticizes.

### 3.1. Routing, core dependence and perceived existential threat (2026-10-11)

The initial transport notation omitted a vital distinction: choosing a **different route** and challenging the **organizing roots** of the frame are different operations. Let $p:u\leadsto v$ be one sequence of partial transport maps; when it fails or is disputed, a person may choose $p':u\leadsto w\leadsto v$. This can involve an authority-derived map and still leave every central commitment untouched. Its warrant depends on the authority's actual competence and the validity of the composed inference, not on the presence of deference.

Let $R_i$ be a separately identified set of central commitments and $e\rightsquigarrow r$ a declared relation indicating that the current justification of $r\in R_i$ relies on bridge $e$. For a challenge to edges $E(q)$, define the potential rejustification obligations:

$$
\mathcal D_i(q)=\{r\in R_i:\exists e\in E(q),\ e\rightsquigarrow r\}.
$$

A nonempty $\mathcal D_i(q)$ means such commitments may require renewed support **if the challenge succeeds**; it does *not* imply that they are false. The person's perceived set $\widehat{\mathcal D}_i(q)$ may differ from the actual support relation. "Core" must be elicited independently of reaction intensity, or the experiment becomes circular. High TLICA $\rho$ can concern the relevant represented contents; it must not be equated to graph edge centrality or strong emotion.

This yields orthogonal distinctions: authority included in $p'$ yes/no; root implication yes/no; warrant of $p'$ valid/invalid; current threat present/absent; affect intense/mild. **Cross-domain movement alone is not the distinguishing criterion**. See [routing/root correction](ROUTING_AND_ROOT_IMPLICATION.md).

### 3.2. Recipient-relative polarity and path-indexed decoding (2026-10-11)

Avoid importing electrostatic sign conventions into psychology. For two observers $A,B$, let an encoded input $\mathrm{Enc}_A(m)$ travel through a shared channel and be partially decoded along an available recipient route $p$:

$$
z_{B,p,t}=\mathrm{Dec}_{B,p,t}(\mathrm{Enc}_A(m)).
$$

Define $\nu_{B,u,t}(z)$ as a *candidate* self-referential valence and $\alpha_{B,u,t}(z)$ as attentional capture, both context- and state-indexed; $\rho_B(z)$ remains TLICA identity correlation. They are not one scalar. Different paths may recover different semantics, or the same semantics with different valence. In particular,

$$
\nu_A(m)>0,\ \nu_B(z_{B,p,t})<0
$$

is possible even when both accurately understand the same externally testable proposition. A sign difference alone neither establishes semantic distortion nor disproves the claim. Signed coupling on a graph, positive/negative affective valuation, and dynamical attraction/repulsion must remain separately typed. A negatively valenced content can still capture attention or participate in a stable learned response.

Meaningful comparison of signs across A/B requires an operationally common referent and validated semantic transport; no ungrounded basis transport or "phase" is inferred. Nonlinear/path-dependent routing does not suffice to demonstrate mathematical chaos. Details, counterexamples and falsifiers: [FIELD_POLARITY_AND_TRANSPORT.md](FIELD_POLARITY_AND_TRANSPORT.md).

### 3.3. Fast scattering, slow reconstruction, and the limits of moving-zero spectra

Let $x_t$ be the currently active interpretive state and $G_t$ the slower structure supplying conditional response paths. One candidate discrete model is

$$
x_{t+1}=T_{G_t}(x_t,q_t,E_t),\qquad
G_{t+1}=G_t+\varepsilon I(G_t,q_t,E_t)+J(G_t,x_t,q_t,L_t,H_t).
$$

Here $I$ stands for incremental imprinting and $J$ for a potentially larger but not automatically thresholded structural update. No additive biological law, scalar conserved emotional energy or mandatory sharp plasticity gate is asserted.

The elementary double-well $V(x;a)=(x^2-1)^2+ax$ admits a barrier crossing while $a$ stays constant. Its landscape instead undergoes a fold when $|a|=8/(3\sqrt3)$. This **discloses** a conceptual difference between *state-space basin switches* and *structural parameter changes*, but it does not identify actual cognitive attractors.

A family $F_{G_t}(z)$ can have moving zeros as $G_t$ changes. However, spectra need not identify response dynamics. For $A_0=0_{2\times2}$ and $A_1=\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)$, both characteristic polynomials are $z^2$, whereas $e^{A_0}(0,1)^T=(0,1)^T$ and $e^{A_1}(0,1)^T=(1,1)^T$. Thus **zero multiset equality is insufficient to infer equality of state evolution**. Comparing moving zeros also demands gauge/normalization fixed independently of the data.

The author's analogical "finite ↔ Archimedean" halves are developmental acquisition/proto-structure and self-relative load/global relational coupling, *not* actual arithmetic places. They supply no RH positivity or prime–Gamma closure. Formal stress tests, mathematical countermodels and sources: [SCATTERING_AND_FIELD_RECONSTRUCTION.md](SCATTERING_AND_FIELD_RECONSTRUCTION.md).

### 3.4. Justificatory dependency is not affective resistance (2026-10-11)

Choose a finite *represented* premise set $E_G$, commitments $R_G$, and a family $\mathcal J_G(r)$ of sufficient supports for each $r$. Define $\mathrm{Sup}_G(r\mid E)=1$ if some $J\in\mathcal J_G(r)$ is contained in $E$. For challenged bridge $e$, define the loss-of-warrant set

$$
\mathcal D_G(e)=
\{r\in R_G:\mathrm{Sup}_G(r\mid E_G)=1,\
\mathrm{Sup}_G(r\mid E_G\setminus\{e\})=0\}.
$$

This describes **represented justification debt conditional on removing $e$**, not actual falsity. Additional legitimate support may protect a commitment even if the challenged premise was used frequently. The observer's perceived threat $\widehat{\mathcal D}_{G,t}(e\mid q)$ may be larger or smaller than $\mathcal D_G(e)$, varying with message delivery, source recognition and active context.

Thus distinguish (i) actual world truth; (ii) represented current justifications; (iii) perceived implications; (iv) self-identity coupling $\rho$; (v) affective activation; (vi) feasible reconstruction paths under current slack. These are not generally equivalent or proportional.

The author's earlier inverse-age phrasing and later age-dependent/proportional phrasing are retained at provenance level; no sign or proportionality is assigned to age without further observation. A formative event's onset, eventual consolidation, frequency and integration are separate. See [FOUNDATIONAL_REPAIR_BURDEN.md](FOUNDATIONAL_REPAIR_BURDEN.md), including a finite redundancy control with 10 verified assertions.

## 4. Formation, activation, interpretation and action

Separate five stages:

$$
\text{environmental event/sequence}\rightarrow
\text{learned association}\rightarrow
\text{later cue activation}\rightarrow
\text{interpretation}\rightarrow
\text{behavior}.
$$

They need not occur in that order in every model; this is a bookkeeping factorization. The key is that the resulting objects are not identical.

The development-stage association can couple a boundary probe $q_{uv}$ with a sanction signal $H$, yielding an internal expectation $p(H\mid q_{uv},\text{history})$. It does **not** logically license $p(\neg\text{valid}(q_{uv})\mid H)=1$. Treating social cost as epistemic falsification is the candidate *calibration error*.

TLICA's osmotic imprinting provides a possible substrate-level channel without assuming all conditioning is explicit. The author reports a later mismatch between explicit, independently tested beliefs and residual reaction; this is **observed as report**, while the pathway that produced it remains unverified.

## 5. Boundary gain is not a truth meter

For comparable, suitably normalized prompts $q_a,q_b$, define an operational response contrast

$$
\Delta_R=R(q_b)-R(q_a),
$$

where $R$ is a declared measured response variable (e.g. self-rated distress or response latency). A conditional **boundary gain** diagnostic compares this contrast for cross-compartment and within-compartment pairs that are matched on topic, threat, and cognitive difficulty.

One can describe local gain as $\|\Delta_R\|/\mathrm d(q_a,q_b)$ **only** if prompt distance $\mathrm d$ and response norm are independently operationalized. Otherwise use raw contrasts; metaphors about sharpness are not measured derivatives.

Affective response $I$, propositional assent $E$, and observable compliance $C$ are separately measured:

$$
I\ \not\equiv\ E\ \not\equiv\ C.
$$

The distinction does not imply conditional statistical independence.

## 6. Developmental law as a family of rival functions

Let $a_{uv}$ be estimated age/window of **consolidation** (not necessarily age of first event), $\ell_{uv}$ self-relative formation load, $n_{uv}$ repeated exposure, $r_{uv}(t)$ subsequent learning, $\rho_{uv}(t)$ identity relevance, and $z_t$ the present context. Let $I_{uv}(t;q)$ be measured affective response conditional on a probe.

$$
\mathbb E[I_{uv}\mid q,t]=
F(a_{uv},\ell_{uv},n_{uv},r_{uv}(t),\rho_{uv}(t),z_t,q).
$$

**Author's initial monotonic conjecture** (all else held constant):

$$
\partial_a\mathbb E[I]<0,\qquad
\partial_\ell\mathbb E[I]>0.
$$

These are *conjectured signs*, not calibrated derivative estimates; a strict $I\propto \ell/a$ is not justified, is undefined at $a=0$, and imposes unjustified units, scale, and universal monotonicity.

Competing possibilities include nonlinear sensitive windows, threshold interactions, a zero age effect conditional on self-relative load, exposure-dependent reversals, and self-report recall bias. Age may be embedded in load definition; incremental predictive value must be measured without double counting.

The word "solidified" itself requires an operational choice: developmental point, interval, asymptotic consolidation, or repeated partial updates. Different choices induce distinct testable models.

## 7. Coupled observer–institution dynamics

Let $X_t$ encode the distributed social microstate: indexed agents, relations, norms, incentives, and records. Let $H_t$ be a task-relative institutional macrostate derived from $X_t$ using the existing distributed-realization model.

A general, uncalibrated social dynamics is:

$$
X_{t+1}=F(X_t,\{a_i(X_t,E_t)\}_i,E_t),\qquad H_t=\Pi_{\mathcal T}(X_t).
$$

Some agents' actions $a_i$ may incorporate boundary-defaulted transports and sanctions; others may be dissident, unpersuaded, or simply pragmatic. If $F$ supports stable or metastable authority-compatible patterns, institutional pressure and inherited boundary defaults can reinforce each other.

Calling this an *attractor* requires choosing a state space, topology, evolution rule, and stability/basin criterion. **No such empirical attractor has been demonstrated here**. The population loop in the manuscript is a hypothesis, not a theorem about equilibrium.

A real intervention can change feasible routes (material slack), learned transports (education/reflection), actual sanction policies (institutional reform), or information interfaces (visibility). A purely psychological reframing cannot automatically remove a real external constraint.

## 8. Diagnostic rather than ideological classification

For one observer and one boundary, distinguish:

- **Compliance** under threat;
- **Authority warrant** actually believed or inferred;
- **Affective activation** when challenged;
- **Enforcement toward peers** after external sanction is removed;
- **Availability and validity of explicit cross-domain justification**;
- **Formation and source-map uncertainty**;
- **Context and identity coupling**.

No one scalar "bootlicker" or "ontological defect" score is defensible. Even apparent boundary-reactivity is compatible with a correct model reacting to a harmful confrontation.

**Verdict:** countervaluation in §2 and slack set-inclusion in §1 are valid inside their declared formal boundaries. Every proposed causal link from childhood/social dependence to specific observed population behavior is **CONJECTURED / UNVERIFIED**.
