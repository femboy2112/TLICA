# Formalism: Local Frame Updates, Salience Reachability, and Provenance

**Status:** candidate model with narrow, conditional mathematical results; empirical psychology **UNVERIFIED**.  
**Scope:** an observation-model proposal over TLICA's existing machinery, not a new foundational law.

## 1. Type discipline

Use the following *application-level* variables, not additional foundation coordinates.

| Object | Type | Meaning |
|---|---|---|
| $W_t$ | external world state | Reality against which propositions and consequences can be checked |
| $c_t$ | context | Cues, roles, task scaffolding, opportunities, constraints |
| $K_t$ | represented content plus source pointers | What propositions and memories are represented, not necessarily recalled now |
| $r_t(x,c)$ | retrieval/access relation | Whether/how content $x$ can enter the present working model under context $c$ |
| $w_t(x,c)$ | salience assignment | Felt/action-driving priority of represented content |
| $J_t$ | interpretation map | How represented evidence, models, and memories are given significance |
| $g_t$ | goal/commitment structure | Current long- and short-horizon valuation structure |
| $\pi_t$ | action/focus policy | How live alternatives influence responses |
| $H_t$ | accessible provenance | Current *representation* of earlier inputs and frame transitions |
| $\ell_t$ | typed family of margins | Time, emotional tolerance, control budget, opportunity, etc. |

A candidate frame is $F_t=(K_t,r_t,w_t,J_t,g_t,\pi_t)$; a larger modeled cognitive state is $X_t=(F_t,H_t,\ell_t)$. External observations enter via $o_t=\mathrm{Obs}(W_t,c_t)$.

All of $r,w,J,g,\pi$ are *candidate* coordinates for modeling a phenomenon. They have no default empirical estimator and should not be conflated with each other or with TLICA's $\kappa,\varphi,\sigma,\rho,\mu$. In particular, $\varphi$ is toolkit-relative truth-indistinguishability/pathway state, *not* how compelling an idea feels; $\sigma$ is source-map adequacy, *not* affective salience.

An abstract update law may be written

$$
X_{t+1} = U(X_t,o_t,a_t), \qquad a_t\sim\pi_t(\cdot\mid X_t,c_t).
$$

It states only that the future represented state may depend on the present, input, and action. This equation does **not** specify a neural mechanism or prove one exists.

## 2. The access/activation factorization

For content $x$ and target act $a$, define distinguishable predicates:

$$
P_t(x)=\text{content available somewhere in the repertoire},
$$
$$
A_t(x\mid c)=\text{content effectively available for current reasoning},
$$
$$
D_t(a\mid x,c)=\text{an actionable route to }a\text{ has been recruited}.
$$

The implication $P_t(x)\Rightarrow A_t(x\mid c)$ is *not* assumed; nor is $A_t(x\mid c)\Rightarrow D_t(a\mid x,c)$. Here $P_t$ is a possession predicate and must **not** be mistaken for the frozen TLICA identity-correlation profile $P_{m,t}$.

A candidate salience threshold for task $i$ is

$$
q_i(t,c)=v_i+u_i(t,c)+z_i(c)-b_i(F_t,c),
\quad
\text{initiate when } q_i(t,c)\ge\theta_i.
$$

The terms are respectively value, urgency, contextual support, and opposing commitments/cost. This deliberately simplified model is *not unique*: negative expected value, deficient action scaffolding, avoidance learning, and context-dependent executive recruitment can all fit similar initiation curves.

One important consequence is conceptual: high initial problem-solving ability does not imply reliable initiation; high end-of-deadline performance does not imply adequate capacity to schedule *multiple* tasks. A queue becomes infeasible when its feasible working windows admit no schedule meeting the deadlines. That scheduling statement is exact conditional on task durations/windows; the cognitive causes of those windows are hypotheses.

## 3. Local frame changes and authorization drift

Let $\mathcal F$ be a chosen family of frames. Declare a directed relation:

$$
F_i \xrightarrow[\mathrm{loc}]{u_i} F_{i+1}
\quad\Longleftrightarrow\quad
L(F_i,u_i,F_{i+1})=1.
$$

The predicate $L$ denotes a *local authorization judgement* made under the current frame. It need not be objective, ethical, predictive, or globally consistent. Crucially, $L$ can depend on $F_i$, including its salience and criterion of acceptability.

Define separately:

- $I(F)$: declared fixed invariant;
- $G(F_0,F_n)$: endpoint acceptability relative to a frozen initial guard;
- $E(W_t,a_t)$: independent evidence/consequence evaluation, which can be UNKNOWN;
- $\mathrm{Reach}_L(F_0,F_n)$: existence of a finite $L$-legal path.

### Proposition P1 (fixed-invariant closure)

If $I(F_i)=I(F_{i+1})$ for all $0\le i<n$, then $I(F_0)=I(F_n)$.

**Proof:** transitivity of equality (or induction on path length). QED.

**Interpretation:** genuine preservation of one fixed invariant cannot be bypassed by a clever factorization of steps. Apparent bypass means "legal" was something other than that invariant, the invariant's semantics changed, or some intermediate step violated it.

### Counterexample C1 (local adjacency is weaker than global guard)

Let $\mathcal F=\{0,1,2,3,4\}$ encode an *illustrative* warning-salience level. Declare $L(i,j)=1$ whenever $|i-j|\le1$. Declare the fixed initial guard $G(4,j)=1$ only when $j\ge3$.

There is no direct legal move from $4$ to $0$, but

$$
4\to3\to2\to1\to0
$$

is entirely locally legal while $G(4,0)=0$. This proves **only** that a bound on the size of each transition is not the same as a bound on total drift. It is not evidence that human reasoning implements this sequence.

### Counterexample C2 (path existence without direct edge)

For a directed graph with edges $A\to B$ and $B\to C$, but no edge $A\to C$, $C$ is reachable from $A$ without being directly adjacent. This is the minimal rigorous content of the "traverse a wall by a different path" analogy. No literal quantum process, barrier violation, or discontinuity follows.

### Rival explanations for apparent "illegal" changes

1. A previously unreachable endpoint becomes reachable through intermediate reweighting (true path gap).
2. The agent's **standard of justification** changes during traversal (authorization drift).
3. Available evidence changes genuinely, warranting a frame revision.
4. Retrieval suppression makes older objections hard to reconstruct, creating false apparent consent.
5. The frame never contained a valid prohibition; only an exaggerated perceived cost.

The proposed mechanism has content only if an experiment can separate these.

## 4. Long-timescale provenance compression

Let a full history be $h=(F_0,u_1,o_1,\ldots,u_n,o_n,F_n)$. An accessible summary is

$$
H_n=C(h).
$$

### Proposition P2 (non-invertible summary)

If $C(h_a)=C(h_b)$ for some $h_a\ne h_b$, then no function receiving **only** $C(h)$ can recover the unique original history for both $h_a$ and $h_b$.

**Proof:** if a right-inverse $R$ recovered both, then $R(C(h_a))=h_a$ and $R(C(h_b))=h_b$; equal inputs would have unequal outputs. Contradiction. QED.

**Boundary:** outside records, new observations, or extra memory channels may disambiguate the histories. P2 asserts inability from the chosen summary **alone**, not permanent or universal amnesia.

### Three recoveries that must not be collapsed

- $N$: narrative reconstruction ("I can explain how I got there").
- $V$: phenomenological reinstatement ("the earlier concerns again feel urgent").
- $B$: behavioral reversibility ("I can make decisions as I would have under the former frame").

An agent may have high $N$ and low $V$ or $B$. This is a proposed separation, not an established factor structure. Claims of "reversibility" must name which one was measured.

A candidate evolution in which $C$ becomes coarser with time is a **hypothesis**. Biological memory does not obey a demonstrated universal monotone hierarchy complete → boundary → fadeout. Reconsolidation, rehearsal, external cues, and fresh learning can all change later access.

## 5. Two timelines of affect

Consider an event $e$ and three distinct processes:

$$
A(t)=\text{subjective emotional activation},
\quad J_t=\text{interpretation},
\quad \pi_t=\text{action propensity}.
$$

Candidate explanation R1 reduces $dA/dt$ while preserving eventual emotional peak. Candidate R2 leaves $A(t)$ broadly unchanged but weakens or delays its effect on $\pi_t$. Candidate R3 gates generalization from one event to the entire $J_t$ (local state update rather than global frame update).

These are not separable by simply asking whether an event "felt slower." None is tied to a named treatment or brain structure here. *Identification requires measurements capable of distinguishing them.*

## 6. Slack and correction latency

The frozen foundation's narrower slack is

$$
S_{m,t}=M_m(t)-\mathrm{Pressure}_{m,t},
$$

with the reflexive gate explicitly **posited**, not deduced ([File 3 §8.11](../../foundation/3_formal_apparatus.md)). This dossier must not overwrite it.

For the wider phenomenological construct use a typed collection

$$
\ell_t=(\ell_t^{\mathrm{time}},
\ell_t^{\mathrm{control}},
\ell_t^{\mathrm{affect}},
\ell_t^{\mathrm{external\ support}},\ldots).
$$

These are **not fungible**, not one truth/moral score, and not claimed to add new TLICA foundation coordinates.

A candidate relation is

$$
\mathrm{LatencyToCorrection}\sim
f(\ell_t,\mathrm{anomaly\ salience},\mathrm{source\ quality},\mathrm{commitment\ coupling}).
$$

No sign or monotonicity of $f$ is established. One possible observation is that low slack yields short-run defensiveness but later revision, whereas high slack enables co-representation and faster revision. A rival is that low slack alters **observable expression** only, with similar eventual belief updates. Another is that salient anomalies sometimes cause *stronger rationalization* rather than correction.

**A detected contradiction is not a proof of learning.** Measure held-out calibration changes, not just the existence of a satisfying new story.

## 7. Identity as a compatible family, not a single active configuration

For contexts $c\in\mathcal C$, let $F_c$ be local realizations and $T_{c\to d}$ candidate partial transports between context-relative representations. They need not be total or invertible.

A condition for global consistency could be

$$
T_{d\to e}\circ T_{c\to d}
\approx T_{c\to e}
$$

on their **common defined domain**, with a declared observational tolerance and loss report. We have not established that these maps exist, satisfy a cocycle, form a groupoid, or glue to a unique global identity.

Categorical/Yoneda/sheaf vocabulary is **proposed research language only** until objects, morphisms, observation functors, and commuting diagrams are specified. Treat the model of identity as a family of compatible local descriptions, not evidence of literal multiple persons.

## 8. Coherence trap and epistemic guard

Consider the causal sketch

$$
\text{active frame}\to
\text{salience/retrieval selection}\to
\text{observed support}\to
\text{reinforced frame}.
$$

Both accurate and inaccurate models may exhibit this loop. Correction quality therefore requires evidence outside the loop and a nontrivial alternative explanation.

Keep separate:

$$
\underbrace{\mathrm{Coherence}}_{\text{internal consistency}},
\quad
\underbrace{\mathrm{Resonance}}_{\text{felt self-fit}},
\quad
\underbrace{\mathrm{Calibration}}_{\text{prediction versus world}},
\quad
\underbrace{\mathrm{Provenance}}_{\text{recoverability of sources and paths}}.
$$

An epistemic abstention state $\mathrm{UNRESOLVED}$ is an **actionable policy output**, not a metaphysical truth value. "Do not play" is legitimate when no safe, warranted move exists **and** the costs of deferral are acceptable; otherwise collect a new observation, use a reversible action, or seek external review.

## 9. Falsifiability and limits

The mathematical propositions above are elementary and conditional. Nothing about them proves the human psychological hypotheses. The model must predict new discriminations under held-out contexts and adverse controls, or be reduced to a useful vocabulary.

Read next: [PROBES.md](PROBES.md), [CLAIM_LEDGER.md](CLAIM_LEDGER.md), [SOURCES_AND_RECONCILIATION.md](SOURCES_AND_RECONCILIATION.md).
