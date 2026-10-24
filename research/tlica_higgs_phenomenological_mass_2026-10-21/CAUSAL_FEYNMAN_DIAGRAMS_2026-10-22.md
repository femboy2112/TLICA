# TLICA–HIGGS IV — Actual causal Feynman diagrams for a bounded stochastic field model

**Dated:** 2026-10-22. **Origin:** Leah's TLICA–HIGGS, boson-excitation, coupled-field, and PCE/$\Pi$ discussion; assistant mathematical implementation. 
**Status:** **DISCLOSED** conditional finite Gaussian/Wick expansion, exact first-order coefficient and causal-diagram weights; numerical witness **OBSERVED**; TLICA-to-human mapping **CONJECTURED / UNVERIFIED**. 
**Scope:** Diagrammatics for **classical stochastic responses**, not literal quantum particles, conscious quantum fields, or moral diagnoses. Foundation untouched. 
**Figure:** [causal_feynman_diagrams.svg](causal_feynman_diagrams.svg) — actual source-editable vector diagram with corresponding formulas.
**Test witness:** [causal_diagram_witness.py](causal_diagram_witness.py), 16 unit tests executed locally; no human data.

## 0. Why these really are diagrams, not illustrations

A Feynman-type diagram is meaningful mathematically if:
1. An action, Gaussian reference system, and expansion parameter are specified.
2. Every line has a defined propagator/covariance and orientation/type.
3. Every vertex comes from a specific non-Gaussian interaction term and has a coefficient.
4. Wick pairings generate each topology with the correct combinatorial/symmetry factor.
5. Diagram weights sum to coefficients of a declared observable's perturbative expansion, verified independently if possible.
6. The formal result is not silently promoted to an empirical claim about an unmeasured psychological field.

Classical stochastic dynamics support these diagram techniques; the Martin–Siggia–Rose / Janssen–De Dominicis (MSRJD) response functional is established prior art.

**Literature:**
- U. C. Täuber, *Critical Dynamics*, ch. 4, dynamic perturbation theory, [Cambridge University Press](https://www.cambridge.org/core/books/abs/critical-dynamics/dynamic-perturbation-theory/2414E9C2C6CD391B2AE522F255A8B9A9).
- Lin and Lindsey (2018), [Feynman diagram combinatorics from Gaussian integrals](https://arxiv.org/abs/1809.02900).
- Zhang (2026), [sft-wick: diagram expansions in stochastic field theories](https://arxiv.org/abs/2606.19480).
- [TLICA's existing coupled-field proposal](COUPLED_FIELD_ECOLOGY_AND_ABDUCTIVE_RECON_2026-10-22.md) and [the PCE/$\Pi$ definitions](../../docs/the-two-prerogatives.md).

## 1. Phenomenological bridge contract: what gets to enter the source

In TLICA, $\rho$ represents structural identity-correlation while $\Pi$ is the distinct *preservation ranking* used with the prerogative of continued existence (PCE). Neither is a numerical truth probability or a field phase. A situation-dependent projection of expected continuations through a justified $\Pi$ ranking can produce a **candidate source** $J_\Pi(t)$, *if* an operational map has been independently declared and verified.

$$
  (E,G,\Pi)\xrightarrow{\mathcal J_{\rm observation}}J_\Pi(t)
    \xrightarrow{\mathrm{response\ dynamics}}q(t).
$$

The arrow $\mathcal J_{\rm observation}$ is **not yet instantiated** by the actual TLICA foundation. For the mathematical toy we supply arbitrary known $J(t)$ instead, and attach the $\Pi$ label only to illustrate a later possible interface. This prevents a bogus quantum propagator labeled $\Pi$, as if a priority ordering were a physical boson.

**Not transported:** objective normative truth, spirituality as a quantum phase, Higgs particles, electroweak symmetry breaking, cognitive data, a unique preserved self, or literal spacetime locality of social situations.

## 2. Minimal stochastic dynamical theory

Choose one scalar fast response $q_t$ (the multi-mode extension is later), parameters $K>0,D>0,u\ge0$, an externally specified deterministic drive $J(t)$, and Brownian motion $W_t$:

$$
\boxed{dq_t=\left[-Kq_t-\frac{u}{3!}q_t^3+J(t)\right]dt+\sqrt{2D}\,dW_t.}
\tag{1}
$$

The drift derives from a stable quartic potential for constant $J$:
$$
U_J(q)=\frac12 Kq^2+\frac{u}{4!}q^4-Jq,
\qquad-\partial_q U_J=-Kq-\frac{u}{3!}q^3+J.
$$

In the TLICA analogy: the coefficient $K$ may be a conditional effective background gap; $J$ is the declared environmental input; $q$ is the measured response mode; $D$ represents ordinary stochastic variation; $u$ measures nonlinear response coupling. These quantities are not measured in the author or other humans.

At $u=0$ with the Ornstein–Uhlenbeck process initialized in its stationary fluctuations, its mean and covariance are:
$$
m_0(t)=\int_{-\infty}^t ds\,R_0(t,s)J(s),\qquad
R_0(t,s)=\mathbf 1_{t>s}e^{-K(t-s)},\qquad
C_0(t,s)=\frac{D}{K}e^{-K|t-s|}.
\tag{2}
$$
The Itô endpoint convention sets $R_0(t,t)=0$. The free connected covariance $C_0$ is **not** a second response propagator.

## 3. Finite model first: the actual Wick combinatorics are exact

For time step $\delta>0$, Gaussian increments $\zeta_n\sim\mathcal N(0,1)$ independent, and $0<K\delta<2$, define:
$$
q_{n+1}=(1-K\delta)q_n+\delta J_n
-\delta\frac{u}{6}q_n^3+\sqrt{2D\delta}\,\zeta_n.
\tag{3}
$$

On a **finite** time lattice and fixed initial data, every $q_n(u)$ is a polynomial in $u$ and the finitely many Gaussian inputs; every fixed-order coefficient of its expectation is a finite sum of Gaussian moments. Gaussian Wick/Isserlis pairing rules are exact here. This is a mathematically controlled foundation for diagram *coefficients*, rather than a claim that the full infinite continuum expansion converges.

The $u=0$ process has Gaussian mean $m_{0,n}$ and variance $v_{0,n}$. Directly differentiating (3) with respect to $u$ at $u=0$ gives:
$$
m_{1,n+1}=(1-K\delta)m_{1,n}
-\frac{\delta}{6}\big(m_{0,n}^3+3m_{0,n}v_{0,n}\big),
\quad
m_{1,n}:=\left.\partial_u \mathbb E[q_n(u)]\right|_{u=0}.
\tag{4}
$$
This is a finite first-order **tree plus contraction loop** decomposition.

## 4. Continuous causal diagrams: exact first-order coefficient

Duhamel's integral solution of (1) reads:
$$
q(t)=q_0(t)-\frac{u}{6}\int_{-\infty}^t ds\, R_0(t,s)q(s)^3.
$$
Expanding to first order in $u$:
$$
\mathbb E[q(t)]
=m_0(t)-\frac{u}{6}\int_{-\infty}^t ds\,
R_0(t,s)\mathbb E_0[q_0(s)^3]+O(u^2).
$$
For Gaussian $q_0=m_0+\zeta$:
$$
\mathbb E_0[q_0(s)^3]=m_0(s)^3+3m_0(s)C_0(s,s).
$$

Hence
$$
\boxed{
\mathbb E[q(t)]
=m_0(t)
-\underbrace{\frac{u}{6}\int_{-\infty}^t ds\,R_0(t,s)m_0(s)^3}_{\text{tree}}
-\underbrace{\frac{u}{2}\int_{-\infty}^t ds\,R_0(t,s)m_0(s)C_0(s,s)}_{\text{one covariance tadpole loop}}
+O(u^2).
}
\tag{5}
$$

The factor $3$ is the number of pairings of two out of the three Gaussian legs leaving one leg attached to the mean. It cancels $3!=6$ down to $1/2$. The picture labeled **tadpole** is a genuine Wick contraction attached to a nonlinear vertex. It is **not quantum pair creation**, nor evidence of literal Higgs bosons in consciousness.

**Diagram rules:**
- External source insertion: measured/declared $J(s)$, integrated over its time.
- Directed retarded line: $R_0(t,s)$, zero if $t\le s$.
- Undirected covariance contraction: $C_0(t,s)$.
- Nonlinear dynamic vertex: one response field plus three response-mode legs, arising from the $u q^3/6$ drift; expansion contributes negative sign $-u/6$.
- Sum over allowable Gaussian pairings, respecting vertex causality and Itô convention; integrate each internal vertex time.

The formal MSRJD response functional for this additive-noise model can be written, with a properly chosen response-field contour,
$$
S[q,\hat q]
=\int dt\left[\hat q(\dot q+Kq+\tfrac{u}{6}q^3-J)-D\hat q^2\right].
$$
At the Gaussian reference level the only nonzero connected bare pairings are $\langle q(t)\hat q(s)\rangle_0=R_0(t,s)$ and $\langle q(t)q(s)\rangle_{0,c}=C_0(t,s)$; $\langle\hat q\hat q\rangle_0=0$. Causal response-only closed loops vanish under Itô time ordering. The finite recursion (3) is the safer primary definition for this dossier.

## 5. Actual independent consistency check: equilibrium Gibbs density

For constant $J$, a stationary density exists for $K>0,u\ge0,D>0$:
$$
p_J(q)=Z_J^{-1}\exp\left[-\frac{Kq^2/2+u q^4/24-Jq}{D}\right].
\tag{6}
$$

Using an **independent static quadrature and Gaussian moment expansion** rather than the dynamic diagrams, the expected stationary response is:
$$
\boxed{
\langle q\rangle_J
=\frac JK-\frac{u J^3}{6K^4}-\frac{u JD}{2K^3}+O(u^2).
}
\tag{7}
$$

The same result follows from (5) with constant $m_0=J/K$, $C_0(s,s)=D/K$, and $\int_0^\infty e^{-Ks}ds=1/K$.

For a small probe around $J=0$, the susceptibility is
$$
\chi:=\left.\frac{\partial\langle q\rangle_J}{\partial J}\right|_{J=0}
=\frac1K-\frac{uD}{2K^3}+O(u^2).
\tag{8}
$$
A second, static route uses the exact equilibrium identity
$$
\chi=\frac{\mathrm{Var}_{J=0}(q)}{D}
$$
and expands the Gibbs variance in $u$, recovering (8). No quantum calculation is needed.

**Concrete preregistered toy sample:** for $J=0.45,K=1.8,D=0.6$, static numerical integration gives:

| $u$ | Numerical equilibrium mean | First-order diagram result | Absolute error |
|---:|---:|---:|---:|
| 0.08 | 0.248073759 | 0.248032407 | 0.000041352 |
| 0.04 | 0.249026712 | 0.249016204 | 0.000010508 |
| 0.02 | 0.249510751 | 0.249508102 | 0.000002649 |

The error falls approximately fourfold as $u$ halves, consistent with omitted $O(u^2)$ effects. These numbers were calculated locally during this task and reproduced by the witness code; this is **one mathematical model checked along two analytic/computational routes**, not independent empirical confirmation.

## 6. What the diagram would mean phenomenologically—**if** grounded

- **A source $J_\Pi$:** a recorded encounter whose relation to preservation-priority $\Pi$ has been operationalized. It is not evidence of universal moral rightness.
- **A directed response line:** traceable earlier-to-later effect, conditional on a declared causal observation model.
- **A branching tree:** nonlinear combination of multiple inputs through one response mode. For illustration: several individually manageable obligations combine to change a decision's response.
- **A covariance loop:** the *variance of the baseline stochastic process* contributes to the mean effect; identical mean context can produce a different average response when background variance differs.
- **A new external slow-imprinting node:** **not yet permitted** as an internal propagator until a stochastic transition and observation process for $G$ or $\Pi$ are explicitly defined.

**Key boundary:** observing the same graphical topology in the model and in a story about a person is not evidence the model is causally correct. A loop is a Gaussian fluctuation contraction, not proof of an unconscious recursive self-justification; any such interpretation demands a discriminating probe.

## 7. Predictive and falsification obligations

**Conditional mathematical prediction:** at weak positive $u$, in this model, larger $D$ decreases small-signal susceptibility (8); if $D=0$ the first-order **noise tadpole term** vanishes, while deterministic tree effects at nonzero $J$ remain.

**Rivals for actual cognition:** ordinary decision threshold shifts, attention constraints, reward learning, direct memory effects, unrecorded material stakes, fatigue/arousal, and non-Gaussian noise. All may generate qualitatively similar observations without a cubic response field.

**Controls:**
1. Null $u=0$: exactly Ornstein–Uhlenbeck; both interaction diagrams absent.
2. Null $J=0$: mean remains zero under symmetric scalar potential, even when variance exists; **fluctuations alone do not create a nonzero mean in this symmetric toy**.
3. Null $D=0$: tadpole disappears, deterministic tree remains for $J\ne0$.
4. Sign mutation $J\mapsto-J$: mean changes sign due potential symmetry.
5. Positive control: Gaussian $\mathbb E[(m+z)^3]=m^3+3m\,\mathrm{Var}(z)$.
6. Negative control: shift the Wick contraction multiplicity; independently checked stationary susceptibility must then fail.
7. Time-order control: $R_0(t,s)=0$ for $t\le s$.
8. Finite-lattice versus static-Gibbs calculations: compare weak-$u$ coefficients.
9. Fresh holdout context/referent only after $\mathcal J_\Pi$ becomes measurable.

**Pass (math):** correct Wick multiplicities, causal structure, finite Gaussian coefficient and matching independent equilibrium expansion.
**Fail (math):** mismatched coefficient, noncausal response, or wrong noise-zero limit.
**Ambiguous (empirical):** inability to identify external source, $\Pi$ map, noise, interaction order, or distinct response modes.

## 8. TLICA compatibility and next target

[The Two Prerogatives](../../docs/the-two-prerogatives.md): $\Pi$ is not $\rho$; PtCns (frame consistency) and PCE (preservation ranking) can diverge. Nothing in the present mathematical work measures either, predicts self-sacrifice, or modifies the foundational baseline dynamics $\dot b=\gamma(f-b)$.

Next build an explicitly typed **two-mode** model (for instance, relational integrity and institutional compliance) with:
- independently measured sources $J_i$;
- cross-response kernel $R_{ij}$;
- noise covariance $C_{ij}$;
- cubic vertex tensor $u_{ijkl}$;
- a frozen historical versus current $\Pi$-ranking label;
- new holdout predictions discriminating external-source paths from endogenous loop corrections.

Only then seek evidence of phenomenological *orientations* and consequences; never call a physical phase or a quantum amplitude what is merely an unmeasured value preference.

**Status conclusion:** Yes: these are authentic Feynman-type causal/Wick diagrams with calculable amplitudes for a **defined classical stochastic model**. No: their measured reality as a theory of minds or institutions has not been established. That split is the point of the research dossier.
