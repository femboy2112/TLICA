# Formalism and Probe Program — Affective Epistemic Compression

**Status:** research-tier model proposal. No human dataset has been fit. No novelty claim.  
**Foundation:** untouched.  
**Primary internal anchors:** [foundation formal apparatus](../../foundation/3_formal_apparatus.md), especially §8.11 slack; [Semantic Optics](../semantic_optics_2026-10-01/README.md) for observer-state/probe discipline.

---

## 1. Variables and typing discipline

For observer \(j\), task \(T\), time \(t\):

- \(\mathcal H_t=\{H_1,\ldots,H_k\}\): live rival hypotheses;
- \(\mathcal P_D\): declared discriminating probes;
- \(\mathrm{Cl}(\mathrm{Tools}_j)\): constructible probe closure;
- \(\mu_{j,t}(p)\): TLICA probe availability/weighting for probe \(p\);
- \(S_{j,t}\): inherited reflexive slack;
- \(A_{j,t}\): application-level affective activation relevant to the task;
- \(c_{j,t}(H)\): application-level commitment/action weight for hypothesis \(H\);
- \(E_{j,t}\): evidence record;
- \(D_{j,t}(H_a,H_b)\): achieved discrimination between a rival pair.

Do **not** identify \(A\) or \(c\) with foundation \(\rho\).

Do **not** treat \(c\) as truth probability.

Do **not** treat \(\mu\) as confidence.

---

## 2. Competence compression

Let \(\mathcal E_T\) be a task-relative path category.

A novice route:

\[
p = p_n\circ\cdots\circ p_1:x\to y.
\]

An installed macro:

\[
m_p:x\to y.
\]

Define online execution cost

\[
K_{\mathrm{exec}}(m_p)
\]

and path-reconstruction cost

\[
K_{\mathrm{recon}}(p\mid m_p).
\]

A **compression gap** is

\[
G_C(p)
=
K_{\mathrm{recon}}(p\mid m_p)
-
K_{\mathrm{exec}}(m_p).
\]

This is not asserted to be a universal psychological quantity. It is a measurable application-level target once a task-specific cost operationalization is declared.

A large \(G_C\) means: “easy to do now; expensive to reconstruct how one would discover/teach it.”

---

## 3. Non-faithful path compression

Let

\[
C:\mathcal E_T\to\mathcal O_T
\]

be a coarse task-performance observation.

If distinct learning paths satisfy

\[
p\neq q
\qquad\text{but}\qquad
C(p)=C(q),
\]

then \(C\) is non-faithful on those morphisms.

This formalizes one required information loss:

> endpoint competence need not retain derivational provenance.

The empirical question is whether human expertise actually produces behavior well-described by such a quotient in the target domains.

---

## 4. Probe execution

Constructibility and execution are separate.

Define the executable set

\[
\mathcal P^{\mathrm{avail}}_{j,t}
=
\mathcal P_D\cap\mathrm{Cl}(\mathrm{Tools}_j).
\]

Define an application-level probe policy

\[
\pi_{j,t}(p)
=
\Pr(p\text{ executed}\mid \Theta_{j,t},T).
\]

A minimal monotone candidate is:

\[
\pi_{j,t}(p)
=
g\!\left(\mu_{j,t}(p),S_{j,t},A_{j,t},C_{\mathrm{time}},C_{\mathrm{effort}}\right),
\]

with

\[
\frac{\partial g}{\partial \mu}>0,\qquad
\frac{\partial g}{\partial S}>0.
\]

The sign of \(\partial g/\partial A\) is **not fixed by definition**; the dossier's central hypothesis predicts it is negative for rival-splitting probes in the anger/frustration regime after relevant controls.

---

## 5. Candidate affect-to-slack bridge

Foundation gives

\[
S=M-\mathrm{Pressure}.
\]

The research-tier bridge is:

\[
A\uparrow
\Rightarrow
V_{\mathrm{task}}\uparrow
\ \text{and/or demanded-response determinacy}\uparrow
\Rightarrow
\mathrm{Pressure}\uparrow
\Rightarrow
S\downarrow.
\]

Every arrow here beyond the foundation definition is empirical.

A null model is:

\[
S \perp A
\mid
\text{time pressure, task urgency, working-memory load, incentives}.
\]

That null must be allowed to win.

---

## 6. Commitment without evidence

Let \(c_t(H)\) be the behavioral/attentional commitment to \(H\).

The model allows

\[
c_{t_1}(H_1)>c_{t_0}(H_1)
\]

even when

\[
E_{t_1}=E_{t_0}.
\]

This is the formal signature of **commitment drift without evidential gain**.

It is not automatically irrational: policy can change for non-epistemic reasons.

It becomes an epistemic failure only when the increased commitment is *misreported or treated as if it were discrimination*.

---

## 7. Premature closure

Define represented rival support

\[
R_t\subseteq\mathcal H_t.
\]

A **premature closure event** occurs when:

1. \(|R_{t_1}|<|R_{t_0}|\);
2. at least one eliminated rival pair remained discriminable by some \(p\in\mathcal P_D\);
3. no relevant discriminator was executed between \(t_0,t_1\);
4. no equivalent discriminating evidence arrived by another route.

This definition is procedural, not truth-valued.

The retained hypothesis can still be true.

---

## 8. Feedback candidate

The strongest loop proposed is:

\[
c_t(H_1)
\to
A_t
\to
S_t
\to
\mu_t/\pi_t
\to
\text{probe execution}
\to
c_{t+1}(H_1).
\]

One simple toy sign structure is:

\[
A_{t+1}=a_0+\alpha c_t(H_1)-\beta Z_t,
\]

\[
S_{t+1}=M-\mathrm{Pressure}(A_{t+1},r_t),
\]

\[
\pi_{t+1}(p_D)
=
\sigma\!\left(
\eta_0+\eta_\mu\mu(p_D)+\eta_S S_{t+1}-\eta_A A_{t+1}
\right),
\]

where \(Z_t\) denotes de-escalating evidence/context and \(\sigma\) is a logistic link.

This is only a scaffold for experimental fitting. No parameter signs beyond the displayed candidate are claimed from data.

---

# Probe program

## P0. Manipulation checks

Before interpreting anything:

- verify the competence manipulation actually changes task execution cost;
- verify the affect manipulation changes the declared affect measure;
- verify probe opportunities are visible and usable;
- verify the task has genuine rival hypotheses;
- verify at least one probe actually separates those rivals.

If any fail, the main experiment is uninterpretable.

---

## P1. Expertise × novice-cost reconstruction

### Question

Does expertise reduce accuracy in estimating the search/learning cost faced by novices?

### Design

For several domains:

1. recruit novices and experts;
2. measure novice time/errors/requests for help on a task;
3. ask experts to predict novice trajectories before seeing novice data;
4. ask experts to explicitly reconstruct an instructional factorization;
5. compare prediction error to expertise and \(G_C\)-like compression measures.

### Predictions

**Model:** more compressed experts systematically underpredict some novice costs unless forced to reconstruct intermediate states.

**Null:** expertise predicts novice difficulty at least as well, with no benefit from factorization reconstruction.

### Verdict

The “curse of competence” component fails if reconstruction adds no predictive gain and expert estimates are well calibrated.

---

## P2. Affect × probe-use factorial

Use a complete factorial design.

Factors:

- competence: low/high;
- affective frustration: low/high.

Primary dependent variables:

- number of rival hypotheses generated;
- discriminating-probe uptake;
- latency to probe;
- confidence before and after probe;
- person-level attribution strength;
- final accuracy.

All four cells are required before claiming an interaction.

### Key contrast

\[
\Delta_{\mathrm{probe}}
=
(\text{expert, high affect}-\text{expert, low affect})
-
(\text{novice, high affect}-\text{novice, low affect}).
\]

Do not interpret a mixed term without every cell.

---

## P3. Cooldown crossover

Within subject, present matched ambiguous cases.

Compare:

- immediate judgment;
- delayed/cooldown judgment.

Keep the evidence bundle fixed until the probe stage.

### Model prediction

Cooldown increases rival representation and/or probe uptake without requiring the substantive verdict to reverse.

### Strong falsifier

If cooldown merely lowers confidence but does not restore discrimination behavior, the proposed \(\mu/S\) mechanism is weakened.

---

## P4. Hidden-constraint reveal

Construct cases where the apparently incompetent actor is:

- actually wrong;
- actually tracking a hidden constraint;
- optimizing a different declared objective;
- using a stale but formerly rational rule.

Randomize these conditions.

This prevents the experiment from baking “charity wins” into the design.

The desired outcome is calibration, not niceness.

---

## P5. Dryer-style microprotocol

For a real appliance/task claim:

1. record the initial belief and confidence;
2. enumerate live rivals;
3. record which probes are already in \(\mathrm{Cl}(\mathrm{Tools})\);
4. record whether each probe has actually run;
5. inspect model-specific documentation or measurement;
6. update claim status;
7. separately evaluate the other person's reasoning/source map.

The local appliance result is secondary.

The scientific target is whether “latent pathway” and “executed verification” are behaviorally conflated under affect.

---

## P6. Identity/commitment control

Because \(\rho\) must not become a generic defensiveness variable:

- include low-identity and high-identity task domains;
- measure whether affective probe suppression appears without identity threat;
- test whether identity coupling moderates rather than defines the effect.

If the phenomenon only appears under identity load, that is a different model than the broad competence hypothesis.

---

## P7. LLM structural analogue

No phenomenology claim.

Construct prompts with two or more plausible rivals and a tool-access condition.

Cells:

- answer-only, no tool;
- tool available but optional;
- tool required before answer;
- abstention explicitly allowed.

Measure:

- factual accuracy;
- rival enumeration;
- tool invocation;
- calibration;
- unsupported closure;
- source-map adequacy.

Prediction:

\[
\text{required discrimination}
>
\text{latent tool availability alone}
\]

for reducing unsupported closure.

A model merely *having* search access should not be counted as verified if it never calls it.

---

## P8. Mutation controls

To ensure the metric is not cosmetic, create mutations that:

- relabel hypotheses while preserving structure;
- swap which rival is true;
- remove the discriminating probe;
- provide a fake non-discriminating probe;
- lower time pressure without lowering affect;
- lower affect without increasing time.

A valid instrument should separate these manipulations.

---

# Acceptance criteria for advancing beyond conjecture

The central affective-compression claim should not be upgraded unless:

1. the expertise effect replicates on held-out tasks;
2. the affect/probe effect survives time-pressure and workload controls;
3. at least one preregistered rival mechanism loses on held-out prediction;
4. cooldown or another intervention changes probe behavior in the predicted direction;
5. identity coupling and source-map effects remain separately measured;
6. the effect is not merely confidence deflation;
7. an independent implementation reproduces the analysis.

Until then: **CONJECTURED / UNVERIFIED**.
