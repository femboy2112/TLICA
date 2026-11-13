# Trust, contact, integration, and the emergence of verification

**Status:** research formalism for future integration, 2026-11-12. The frozen foundation is not amended. TF-1 through TF-3 are elementary mathematical propositions under explicit assumptions; TW-1 and TW-2 are designed finite mechanisms. None is a psychological validation of TLICA.

**Authorial target:** contact supplies recurrent encounters with contextual signal/object relations; integration changes how those encounters are interpreted, acted upon, and selected. Their operating coupling can develop the tools through which a content acquires a natural, toolkit-relative verification profile. Trust is a candidate mechanism governing uptake and delegation within that loop.

**Pins:** [foundation 1, Sections 2.3 and 2.7–2.9](../../foundation/1_foundations.md), [foundation 2, Section 4](../../foundation/2_access_and_development.md), and [foundation 3, Sections 6–8](../../foundation/3_formal_apparatus.md). The [executable witness](finite_witness.py) supplies finite calibration cases and raw JSON. Exact live-render observations and their scope are recorded in the [validation record](VALIDATION.md).

## 1. What is coupled

The foundation explicitly distinguishes formal non-reducibility from dynamic entanglement. Leah's coupling claim concerns the operating development of an observer. It should not be replaced with the weaker claim that two isolated numerical readouts determine a third.

Three distinctions make that operating proposal precise:

1. **Current contact and contact history differ.** The foundation's current contact is $\kappa_{m,t}(n)=\chi_m(t,n)$. A history of contextual encounters, actions, signals, and persistence cues contains information not recoverable from one current contact value.
2. **The relational structure exceeds its summaries.** The directed historical graphs $G^{m,k}_t$ generate mode-specific integration capacities and the profile $\vec\rho^m_t$. A scalar projection can discard source identity, path arrangement, integration mode, and temporal order. Even the full collection of max-flow readouts need not identify its generating graphs.
3. **Constructibility and execution differ.** A verification pathway being constructible makes Tier-3 $\phi$ applicable. It does not certify that the pathway was executed successfully or that its empirical premises were independently checked. A tacit capacity may eventually support such a pathway; familiarity alone is not a construction certificate.

Preserve the existing convention:

```math
\phi_{m,t}(x)=1-n_{m,t}(x)\delta-\epsilon_{m,t}(x),
\qquad
\epsilon_{m,t}(x)=\int_{Q^m_t}(1-q(x))\,d\mu^m_t(q).
```

The cogito's $1-\delta$ is a structural placement in an ordered field with a positive infinitesimal. It is not a confidence estimate, a measured failure rate, or a floating-point number close to one. The empirical term $\epsilon$, conditional depth, probes, and probe weighting retain their foundation meanings. Neither accuracy on a benchmark nor willingness to delegate is automatically $\phi$.

If no pathway is constructible, $\phi$ remains undefined. Contact and integration can nevertheless develop: this is already the foundation's osmotic-imprinting case. The constructive research question is how those changes sometimes make a new verification pathway available.

## 2. A candidate developmental mechanism

An outside description of an encounter may record the actual source, object, context, intervention, emitted signal, and later object state. The observer ordinarily receives only mediated observations and persistence cues. Its inferred source assignment, written here as $\widehat\sigma$, is an internal hypothesis; it is not the foundation's actual outside-perspective source map $\sigma$.

Let $\widehat E_t$ denote the observer-accessible event record, including its context and provenance estimates. The following schematic is a **proposed applied update family**, not a newly derived foundation law:

$$
(G_t,\mathsf{Tools}_t,\widehat E_t)
\xrightarrow{\mathcal U_{\mathsf{Tr}}}
(G_{t+1},\mathsf{Tools}_{t+1},\mathsf{Foc}_{t+1}).
$$

The resulting graphs determine integration readouts. The available tools determine possible pathways and probes. Focus and contact enter the foundation's existing weighting map:

$$
\mu^m_t=\Lambda^\mu_m(\mathsf{Foc}^m_t,\kappa^{\mathrm{out}}_{m,t},Q^m_t).
$$

Thus actual contact can affect the observer through mediated encounters; integrated structure can influence attention and action; those choices change later encounters and tool development. Where a pathway becomes constructible, the existing evaluation machinery supplies its $\phi$ profile. Repeated contact does not merely increase a number: it may teach a new contextual distinction, change a persistence model, or make a previously unavailable comparison possible.

This family needs concrete update rules before it predicts anything. In particular, an observer's updater cannot simply read the true source map from outside. A good applied implementation must represent source uncertainty and retain failed as well as successful encounters.

## 3. Trust as scoped routing and delegation

Use $\mathsf{Tr}_{m\leftarrow j}^{d,c,t}$ for a proposed trust configuration concerning source/person $j$, domain $d$, context $c$, and time $t$. This is a typed configuration, not a replacement coordinate and not one universal score. The symbol $\tau$ is already used for temperature in the foundation and is not repurposed.

The configuration distinguishes three operational effects:

- **Uptake:** which claims or interpretations from the source enter the working model, and with what provenance and provisional status.
- **Action delegation:** which actions may be guided or performed through the source, with what scope and revocation conditions.
- **Probe policy:** which questions, alternative sources, and independent checks are sought, deferred, or omitted.

Human interpersonal trust can also involve expected competence, goodwill, or fidelity to commitments. Trusting environmental regularity need not attribute intentions to reality. Predictability, trustworthy intentions, reliance caused by lack of alternatives, and permission to act must remain distinguishable.

This makes the power connection operational: permitting a source to guide interpretation, action, or probe selection gives it an influence channel. Unnoticed influence can occur because that channel is smoothly integrated into ordinary activity. Smoothness alone does not identify trust, truth, consent, or good intentions. A predictable opponent and a trusted expert who challenges one's assumptions separate these possibilities.

“Trust is a derivative form of truth” is retained as an **operative metaphor**: an epistemic orientation becomes a disposition to act, delegate, and look. A literal derivative requires a specified response map and perturbation. If a policy is differentiable in a source signal $s_j$, one could study

$$
J_{m\leftarrow j}=D_{s_j}\pi_m(H,s_j;\mathsf{Tr}).
$$

Here $H$ is the observer-accessible history and $\pi_m$ is the specified response policy. This is response sensitivity, not truth's derivative. For discrete policies, use finite controlled changes instead. To attribute influence specifically to trust, vary the trust routing while controlling message content, opportunities, and coercive constraints. A large response alone cannot isolate its cause.

## 4. TF-1: when an integrated representation determines a current assessment

Let $\mathcal H$ be a declared class of admissible histories/model states, and let $R:\mathcal H\to\mathcal Z$ be a proposed representation. Fix a content, evaluation convention, and toolkit-relative target

```math
F:\mathcal H\to\{\bot\}\sqcup\mathbb K,
```

where $\bot$ marks undefined $\phi$ and otherwise $F$ is its value. The disjoint-union notation ensures undefined is not numerical zero. This is a mathematical target; it need not be directly known to the observer.

**TF-1 — static representation sufficiency.** There exists a function $f$ on $R(\mathcal H)$ satisfying $F=f\circ R$ if and only if

$$
R(h)=R(h')\quad\Longrightarrow\quad F(h)=F(h')
\qquad(h,h'\in\mathcal H).
$$

**Proof.** If $F=f\circ R$, equal representations give equal targets. Conversely, when the implication holds, assign $f(z)=F(h)$ for any history with $R(h)=z$. Constancy on that fibre makes the assignment well-defined. This proves the equivalence.

The criterion respects the strongest charitable coupling proposal: a sufficiently rich contact/integration representation could determine the assessment. The actual work is to specify that representation and establish sufficiency. Merely including the answer as a field would satisfy the theorem vacuously and supply no developmental explanation.

The script gives histories sharing current contact and a scalar integration projection while differing in pathway availability or probe scores. Those lossy summaries fail. A representation retaining the declared evaluation inputs succeeds for this fixture. This is not a refutation of coupling, nor proof that all real histories admit a compact sufficient representation.

## 5. TF-2: present sufficiency does not establish dynamic closure

Suppose a deterministic extension law $D(h,a,u)$ maps history $h$, action $a$, and declared exogenous input $u$ to a successor history. Require the state domain to contain these successors.

**TF-2 — deterministic transition sufficiency.** A representation-level update $\overline D$ satisfying

$$
R(D(h,a,u))=\overline D(R(h),a,u)
$$

exists if and only if equal representation fibres have equal successors under the same action/input:

$$
R(h)=R(h')\quad\Longrightarrow\quad
R(D(h,a,u))=R(D(h',a,u)).
$$

**Proof.** Apply TF-1's well-definedness argument separately for each fixed action/input. When this holds and the current assessment also factors through $R$, induction gives the corresponding assessment along any fixed admissible input/action sequence. For stochastic dynamics the analogous requirement concerns the conditional law of the successor representation; if future observations are part of the claimed simulator, their joint law must also be preserved.

The witness uses a four-state domain consisting of a hidden bit and a revealed-state flag. Its two displayed initial histories both have the flag unset and current readout zero. Under the same `reveal` action, their successor readouts are zero and one. The present readout factors through itself, but its value does not close the dynamics. Retaining the hidden bit repairs this particular fixture. The script separately checks that both declared actions keep every state inside the four-state domain.

Consequently, “the full integrated form generates future $\phi$” requires more than matching current values. A proposed compression must preserve the action-conditioned distinctions relevant to later contact, tool growth, and assessment. This condition identifies a testable missing requirement; it does not prohibit such a model.

## 6. TF-3: repetition, persistence, and new information

Let $\Omega$ be a finite candidate-world set. A deterministic observation map $O_q$ represents a specified probe, context, time convention, and provenance. For an observation history $D$, define its surviving worlds:

```math
S(D)=\{\omega\in\Omega:O_q(\omega)=y
\text{ for every }(q,y)\in D\}.
```

**TF-3 — identical deterministic constraints are idempotent.** If $(q,y)$ is already in $D$, then

```math
S(D\cup\{(q,y)\})=S(D).
```

**Proof.** The added condition is already required by the defining conjunction. It removes no additional world.

The scope matters. A fresh noisy measurement, a new context, an elapsed-time persistence check, or an intervention can impose a different constraint. Repetition can also change the learner's integration or toolkit even when this outside deterministic candidate set does not shrink. Moreover, repeated presentation may change probe weighting, so TF-3 does **not** prove unchanged $\phi$.

The witness repeats one identical constraint 32 times, then contrasts a fresh discriminating context. A contradictory “duplicate” is detected as inconsistency. This distinguishes learning through recurrent contextual contact from counting recycled evidence as independent confirmation.

## 7. TW-1: observation selection can conceal contextual failure

The deterministic fixture contains eight externally specified events. In two familiar-context events an object persists; in six changed-context events it does not. A signal always predicts persistence. A policy observes only the familiar contexts.

| Evaluation set | Correct predictions | Exact accuracy |
| --- | --- | --- |
| Selected familiar events | 2 of 2 | 1 |
| Externally selected disjoint holdout | 0 of 6 | 0 |
| Entire specified eight-event population | 2 of 8 | 1/4 |

**TW-1** discloses a possible feedback failure: accurate selected encounters do not establish accuracy outside the selected context. The holdout is selected independently of the observer's policy; no statistical independence or IID sampling assumption is asserted. These fractions are empirical accuracy in a known finite fixture, not $\phi$, $\rho$, or confidence that the world is true.

A truthful predictor passes everywhere; an inverted-truth predictor fails everywhere. A context-invariant null population removes the selection gap. Reusing training events as a “holdout” is rejected by provenance checks, and inverting the signal reverses the signed gap.

For an application, keep latent target-domain reliability distinct from its observed estimate. The target distribution, success condition, and source identity must be declared. Agreement inside an endogenous observation policy estimates a different quantity from performance under an independently specified distribution.

## 8. TW-2: a complete contact-access by integration-selection contrast

Begin with four binary candidate worlds and one prior observation fixing the first bit. Two worlds survive. The contact-access intervention makes a second-context probe available; the integration-selection intervention supplies a specified model-linked rule to choose that novel probe when accessible. Without that rule, the policy repeats the familiar probe. The rule is hand-coded: learning or imprinting it is outside this simulation.

The outcome $Y$ is the reduction in unresolved candidate pairs. It is a discrimination diagnostic, not a truth probability or a $\phi$ value.

| New contact access | Integrated novel-probe selection | Selected probe | $Y$ |
| --- | --- | --- | --- |
| 0 | 0 | Familiar | 0 |
| 0 | 1 | Familiar, only available probe | 0 |
| 1 | 0 | Familiar | 0 |
| 1 | 1 | New context | 1 |

All four cells are evaluated before the interaction is formed:

$$
Y_{11}-Y_{10}-Y_{01}+Y_{00}=1.
$$

**TW-2** is a constructive example of complementary access and specified model-linked selection: a distinction becomes available and the observer's policy selects it. It does not measure the foundation's $\kappa$ or graph-derived $\rho$, and it does not establish a universal multiplication law or simulate developmental learning. The complementarity was engineered, not discovered in human data.

A null makes the purportedly new probe duplicate the familiar one: all gains vanish. A mutation makes the policy select the new probe whenever accessible regardless of the integration intervention: access still helps, but the interaction becomes zero. The script emits all four cells for each regime and rejects an incomplete factorial contrast.

## 9. Next discriminating study

The next application should compare two live explanations: contact/integration develops transferable contextual verification, or it primarily strengthens selection of already-confirming encounters. Use known signal/object-persistence relations, predeclare a context shift, and retain the raw source and action history.

Measure separately: accessible versus chosen probes, source-attribution errors, demonstrable pathway construction, executions and their results, task performance, and scoped reliance. Do not infer graph-derived $\rho$ from a confidence questionnaire or assign $\phi$ from success frequency. If graph updates are modeled, specify the edge evidence and integration modes before interpreting max-flow readouts.

**Pass for the stronger mechanism:** with preregistered criteria, the coupled development condition constructs and uses a transferable discriminating procedure and improves performance on externally selected contexts. **Failure of that claim:** benefits remain confined to self-selected contexts while the proposed transfer procedure fails. **Ambiguous:** the interventions also change available information, cost, or task skill in unseparated ways; the study then has not isolated the claimed mechanism.

The exact witness tests implement only their stated finite outcomes. Human-effect magnitudes, developmental update laws, the relationship between interpersonal trust and environmental reliance, and faithful measurement of integration remain **UNVERIFIED**.

## 10. Reproduction and interpretation

From the repository root:

```bash
python3 research/trust_kappa_rho_phi_2026-11-12/finite_witness.py
python3 research/trust_kappa_rho_phi_2026-11-12/finite_witness.py --json
```

The script uses standard-library rational arithmetic and deterministic enumeration. JSON includes raw fixture events, surviving worlds, fibre collisions, all factorial cells, mutation results, and each named check. It creates no result files. Its positive, negative, null, and mutation controls establish the specified instrument behavior; they do not convert these designed examples into independent empirical evidence.

The future integration target is therefore concrete: implement a source-aware developmental update in which contextual contact and historical integration jointly shape tools and choices, then test whether the resulting verification gains survive changed contexts and independent observation policies.
