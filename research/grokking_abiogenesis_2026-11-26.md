# Grokking Abiogenesis
## Recursive differential toolkit closure and observer-relative semantic rarity

**Origin:** Leah, 2026-11-26 conversation; formal synthesis and experimental specification assisted by ChatGPT. **Status:** research-tier, v0.1, CONJECTURED / UNVERIFIED as a general learning mechanism. No change to the frozen foundation. No empirical run or human-mechanism validation is claimed.

## 1. Authorial seed

Learning begins with few tools and high friction. Individual tools are discovered, practiced, mastered, and rendered cheap. A growth spurt follows as earlier knowledge makes new learning easier. Eventually almost everything within the constructed network of actions is easy, yet progress beyond it stalls. The next growth level opens when the learner discovers a causally relevant differential: what one mastered tool does to another, or what applying one makes the other capable of doing. Newly mastered compositions become tools in their own right.

The second hypothesis concerns the often prolonged, variable interval after a model fits its training data but before it generalizes: the training distribution was not designed around the learner's current toolkit. A semantic witness for its next missing tool relation may be exceptionally rare, appear as noise relative to its current representation, or be absent as an explicit example. Optimization can follow many low-training-loss trajectories until a productive internal configuration is reached. A viable circuit then develops, competes, stabilizes and participates in further tool formation. The author calls this **grokking abiogenesis**.

The analogy concerns the emergence of reusable computational organization, not chemistry, biological life, consciousness, intention, or a universal stochastic mechanism. A model does not literally decide to search for a semantic witness. "Saturation" means an observed plateau on a specified distribution, not exhaustion of all information or zero gradient.

## 2. Continuity with TLICA

- [Access and development, sections 3.2–3.3](../foundation/2_access_and_development.md): verification-tool imprinting, shadow encounter, compositional action, and self-encounter. A structure can leave a shadow before the observer can distinguish it.
- [The First Atomic Connection](grokking_as_toolkit_closure_2026-08-29.md): existing distinction between local coverage and global closure, four gates (constructibility, identifiability, accessibility, dominance), bridge-gauge theorem, P11 nested grokking, and P12 targeted bridges.
- [Existing bridge protocol](grokking_toolkit_closure_experiment_protocol_2026-08-29.md): degree-matched graph repair, corruption controls, cross-component transfer.
- [Recursive Epistemic Ratchet](recursive_epistemic_ratchet_2026-10-02.md): epistemic compilation, affordance versus derivational possession. The individual-scale analogue is a validated composition becoming cheap enough to be used as an atom in a later operation.

The present note gives the already-proposed atomic connection a candidate operational form. It does not claim that every bridge is a derivative or that all grokking creates a new route.

## 3. Toolkit and differential

Let T_n be a set of typed, partial operations with explicit domains, costs and semantics. Cl_A(T_n) is their closure under declared admissible operations A. Keep unrestricted expressibility, discovered routes, resource-bounded accessibility and deployed behavior separate.

For compatible A and B on a common state space, define a finite response:

```text
Delta_B A(x) = A(B(x)) - A(x)
C_AB(x) = B(A(x)) - A(B(x))
```

The differences require a common additive output space and defined compositions. For nonnumeric outputs use paired observations, equality/prediction tests or a declared transport; do not subtract arbitrary embeddings. Order dependence is a possible signal, not a requirement or proof of a useful mechanism. For smooth y and perturbation x + epsilon*z(x), the first variation is Dy(x)[z(x)], with an O(epsilon^2) remainder only under suitable second-derivative bounds. For intervention claims fix context, intervention, readout and horizon rather than inferring causality from association.

Example: A(x)=x+a and B(x)=b*x. B(A(x))-A(B(x))=a*(b-1), independent of x. That relation supports transfer across x but does not imply every pair has a compact useful law. Addition by a and addition by b commute yet yield useful composites.

A candidate recursive learning operator is:

```text
T_(n+1) = T_n union Compile(Verify(Discover(T_n, residuals, probes)))
```

Discovery proposes typed relations; verification certifies the scoped behavior; compilation preserves semantics, domains, uncertainty, provenance, and invalidation conditions. No candidate gains authority merely by insertion. Actual registration can be rejected or revoked. If a composite was already expressible, the unrestricted closure may remain unchanged; a cheaper verified implementation can strictly enlarge the bounded closure at fixed compute budget. When transport or primitives truly change, the expressible closure may expand too.

## 4. Semantic rarity is relational, not intrinsic to a datum

Fix a target bridge R, observer/toolkit state s, source distribution D, and a preregistered detector for whether an example disambiguates R against named rivals. The useful-witness probability is relative to R, s, D, and the detector. The same datum can discriminate after a tool is mastered but be ineffective beforehand. This is not a truth probability or a new TLICA coordinate.

Separate:
- **Evidential rarity:** discriminating observations are sparse in D.
- **Representational rarity:** the learner seldom occupies states capable of decoding the witness.
- **Compositional rarity:** the necessary tools rarely interact productively despite being present.
- **True underdetermination:** competing relations agree on all accessible observations. No more repetitions of those observations distinguish them absent a new probe or justified prior.

Explicit semantic examples are not necessary: a learner can infer a new algorithm from a collection of observations without ever seeing an example of that algorithm itself. A fixed dataset can support delayed discovery as weights, alignment and optimizer state change. A correct bridge can already exist without being behaviorally dominant.

## 5. First passage and nested timescales

Model a training trajectory (parameters, optimizer state, and sampler state) as S_t; define a predeclared functional nucleation region N_R by validated ability to exploit the relation, not by retrospectively picking a high-accuracy checkpoint. Let tau_R be the first observed entry into N_R. This can be transient: define a separate sustained-access threshold.

For independent constant-probability trials, the waiting time is geometric with mean 1/p. Real training has history-dependent hazard h_t = Pr(tau_R=t given tau_R>=t); survival is the product of (1-h_t) over prior steps, and the mean is the sum of survival probabilities when finite. Variable seed-dependent times alone establish neither independent trials nor random escape.

Distinguish:
1. local mastery and coverage saturation (preconditions to a particular bridge, not necessarily all tasks);
2. first candidate bridge or pre-nucleation;
3. constructible, identifiable and accessible route (the earlier manuscript's t_star);
4. circuit growth/alignment;
5. dominance and behavioral disclosure (t_grok);
6. stability, hostile transfer and compilation (t_sat);
7. repeat at a higher scale.

Nucleation-limited, growth-limited, and dominance-limited runs may coexist. Nested sigmoids are a qualitative prediction, not a universal shape. Fixed closure can saturate; an obstruction can be a pathway, probe, access, or proven boundary, not a demand for arbitrary additional training. Full-batch deterministic dynamics can traverse a productive route without SGD noise, so noise is not required by this framework.

## 6. Empirical constraints and competing explanations

- [Power et al., 2022](https://arxiv.org/abs/2201.02177): delayed generalization on small algorithmic datasets after overfitting, with dependence on dataset size. Not evidence for semantic rarity by itself.
- [Nanda et al., 2023](https://arxiv.org/abs/2301.05217): modular-addition Fourier computation, gradual circuit formation followed by cleanup. This directly constrains the pure random-walk story: internal progress can precede behavioral change. The learned algorithm was not supplied as an explicit procedure.
- [Ersoy and Wiesner, 2026 preprint](https://arxiv.org/abs/2606.17120): engineered metastable regimes in linear deep networks with noise-driven escape and reported Arrhenius scaling. Relevant to stochastic nucleation, not evidence for universal semantic bridge rarity.

Other live rivals: optimizer/regularizer selects an already accessible generalizer; gradual representational alignment; direct rule induction without a new compositional primitive; sample-size or difficulty effects; changed interface/cost rather than new computation. Do not count these papers as independent verification of the proposed human mechanism.

## 7. Discriminating program

First reproduce the existing opaque modular-addition bridge experiment. Then branch paired, locally mastered checkpoints into a complete bridge-exposure (valid versus matched redundant) by exploration (low versus high noise) factorial, with a fixed-data full-batch arm, corrupted bridge arm, dense positive and random-label negative controls. Match training examples/tokens, update count, optimizer settings except the intended intervention, and report actual compute. Do not use test examples for training, probe tuning, bridge choice or timing thresholds. Distinguish deliberate novel evidence from reweighting an existing witness; the former tests identifiability, the latter discovery/access.

Predeclare t_star, circuit progress, t_grok, t_sat, right censoring, nested-depth holdouts, mutation/ablation tests and selection criteria. Split pilot seeds, confirmatory seeds, and secret task-generator families. Track local competence, cross-family/depth transfer, source correctness, resource cost, and distinct hazards. Report paired checkpoint results and uncertainty, not only successful runs.

Prediction: if evidence rarity matters, valid bridges should shorten first-access time relative to matched redundant/corrupt ones under matched exploration; if state exploration dominates, changing noise/order at fixed information may suffice; if dominance dominates, a usable circuit should predate the behavioral event and regularization should change deployment without earlier first access. If explicit bridge compilation only changes inference cost, classify it as bounded access, not weight-space grokking. Falsify the general rare-semantic-witness claim if matched controls explain the observed delays without bridge dependence. Ambiguous or uncalibrated results remain UNVERIFIED.

For human analogues use consented, bounded opaque-symbol learning tasks, no clinical or intelligence diagnosis, matched local mastery, transfer before subjective aha ratings, independent assessment and a separate ethics/protocol review.

## 8. TLICA diagnostics and ledger

Keep contact kappa, truth-indistinguishability/pathway phi, source-map sigma, commitment/identity rho, probe availability mu, tool closure, independence, coherence and discrimination separate. Undefined phi is no constructible path, not falsehood. High phi can coexist with wrong sigma; a felt insight or high rho is not validation. No human coordinate is attributed to a language model merely because a circuit transfers.

| Claim | Status | Boundary / next probe |
|---|---|---|
| Nested grokking and tool-on-tool learning as general developmental mechanism | CONJECTURED | Nested-depth transfer and selective bridge intervention |
| Differential and order examples | DISCLOSED by direct algebra | Compatible state/output domain only |
| Geometric waiting-time example | DISCLOSED under iid constant hazard | Not an empirical optimizer law |
| Observer-relative semantic rarity causes prolonged grokking | CONJECTURED | Paired bridge-by-exploration experiment |
| Stochastic escape as universal explanation | NOT ESTABLISHED | Deterministic and dominance rivals |
| Compiled validated tools expand bounded capability | CONDITIONAL | Define cost and exhibit strict witness |
| Human and neural mechanism identity | UNVERIFIED | Independent human and model studies; potentially inaccessible microscopic comparison |
| Autonomous recursive capability improvement | UNVERIFIED | Matched-budget frozen-weight benchmark and mutation controls |

## 9. Preservation and handoff

This is an additive continuation, not a replacement of the August manuscript, not an application registration, and not a foundation amendment. The companion formal direction is causal observation, finite response and predictive completion in Observational SUCC ([Liber Secundus](https://github.com/femboy2112/SUCC/blob/main/docs/principia_observatoris/02_causality_geometry.md)). A downstream implementation should begin with exact toy sources and reversible pure tools, then test frozen-weight orchestration separately from learned circuit formation. No experiment, local repository gate, or rendered math check was executed in preparing this note.

## 10. Authorial extension: emergent observational basis and the two stagnations (2026-11-26)

Leah's further observation: both the no-tools beginning and the high-mastery plateau are instances of being stuck. The sigmoid staircase suggests a frame-change interpretation: a rare combination of existing tools exposes a causally novel direction in their correlated future history; "we have constructed a basis through emergence."

The load-bearing refinement is **basis emergence through mixed causal observation**, rather than the literal shape of a graph. At the beginning, few useful instruments exist. At saturation, available instruments may predict every familiar history while leaving orthogonal or quotient directions unresolved. No 90-degree rotation follows from plotting learning curves; a rotation of coordinates within an existing span cannot disclose new information. But if a newly executable observation l is outside the old observational span W, its class in the quotient is nonzero. Under a declared positive-definite metric, subtract its projection onto W: the nonzero residual is orthogonal to W by construction. This is the precise conditional sense of a new 90-degree direction. It does not establish physical or statistical independence or a universal neural geometry.

The SUCC companion's addendum GA-06–08 gives an exact example: with x=(x1,x2,x3,x4), two commuting causal tools can disclose x1+x2 and x1+x3 individually, while their composite discloses x1+x2+x3+x4. No number of repetitions of either tool alone distinguishes x4. The complete four-cell contrast isolates x4, a new observable coordinate. A matched additive control has the same pure histories and orthogonal first-order directions but no novel mixed dimension. A nonzero mixed contrast can also be entirely in the old span. Thus tool orthogonality alone is not sufficient, noncommutativity is not necessary, and novelty is relative to the actual observable domain.

More strongly, a constructed Boolean-lattice family with m commuting primitives and a 2^m-dimensional hidden carrier has exact accessible rank sum of binomial(m,j) over j=0..k at support depth k. All lower-order histories may be solved before a mixed history reveals a higher-order basis coordinate. This is a rigorous existence model of nested developmental boundaries, not evidence that human cognition or neural optimization has this carrier, this dimension growth, or a literal staircase of phase rotations.

The proposed learning event now has a stronger possible criterion: local mastery; a valid bridge in causal history; a novel functional direction relative to the current accessible span or rival partition; reliable transfer; and eventual deployment/compilation. A bridge may already be expressible in unrestricted closure but absent from accessible routes. Distinguish observational rank from expressive power, cost and evidence. If the old space is invariant under all admissible actions and observations, no composition can escape it; new access, representation, evidence or action is needed. High performance on a lattice is not proof of global saturation.

Empirical extension: matched locally mastered checkpoints; valid mixed witness versus additive/null, corrupt, and nonzero-in-span controls; require new functional discrimination/transfer, not merely a large mixed contrast or a hidden-state decoder. Separate genuinely new evidence from fixed-data access, and compare optimization noise, growth and dominance as before. Where no linear output space is declared, use rival partitions instead of an invented metric. GA-06–08 are scoped mathematical deductions in SUCC, with standalone exact finite checks; the learning interpretation is CONJECTURED and no neural/human experiment, full TLICA validation or visual math check has run. No foundation change or new TLICA coordinate.
