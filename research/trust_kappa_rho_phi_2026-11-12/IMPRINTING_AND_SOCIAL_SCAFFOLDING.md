# Osmotic imprinting and the world as a learning scaffold

**Status:** author-requested research addendum, 2026-11-12. This develops the contact–integration–trust proposal for future integration; it does not amend the frozen foundation. **IS-1** below is a restricted mathematical proposition. The developmental and social mechanisms remain proposals requiring application-specific evidence.

**Read with:** [author seed](AUTHOR_SEED.md), [formalism and probes](FORMALISM_AND_PROBES.md), [source reconciliation](SOURCES_AND_RECONCILIATION.md), and [claim ledger](CLAIM_LEDGER.md).

## 1. Contact prepares the learner before the learner can explain it

Leah's addition is substantial: the contact–integration loop includes ambient formation of the observer's capacities, not only deliberate encounters followed by explicit evaluation. A person can acquire expectations about persistence, social roles, and reliable signals before possessing a verbal account of those expectations.

This already has a precise architectural home. [Foundation 3, §8.7](../../foundation/3_formal_apparatus.md) defines osmotic imprinting as substrate-level pattern formation through repeated ambient co-occurrence, without requiring attention to the association or a constructed verification pathway. It distinguishes formation from later activation and an operating mechanism from a measurable durable update. Signal strength, recurrence, plasticity, and available bandwidth matter; their update rates are not specified.

κ therefore belongs on the contact side of this developmental account. It is neither the imprinting process itself nor a count of exposures. Contextual contact histories provide occasions for the substrate to acquire associations; accumulated structure then influences interpretation, action, and subsequent contact. An association can be durable without being source-resolved or correct.

Section 8.4 already places source-mediated contact within the coefficients of a **focus-driven** graph update. That is evidence of architectural compatibility, not a completed law of purely osmotic learning. Section 8.11 makes a closer connection: osmotic contact and self-directed Mode B both write the slow structure $G$. The shared-structure relation between integration and world-reading is explicitly **Posit G**, not an established psychological theorem.

[Foundation 2, §3.2](../../foundation/2_access_and_development.md) supplies the next step: ambient proto-patterns can become accessible and be refined into deployable verification tools. This is where the proposal reaches φ. A felt expectation may precede constructible verification; it does not acquire defined φ merely by becoming strong. The cogito's structural $1-\delta$ remains unchanged throughout this development.

## 2. Preserve the ideal observer thesis by specifying its space

The author's strong thesis is that an indefinitely resourced local observer could learn the entire relevant space perfectly, while actual humans remain unfinished and resource-limited. Treat this as an **ideal-limit proposal** whose “within reason” clause supplies real mathematical conditions.

The target must be declared. Two world models that produce identical outputs under every reachable admissible probe cannot be separated by longer computation alone. Perfect mapping can mean recovering the world up to that observational equivalence. A stronger ontological identification requires a separating instrument, rather than just additional repetitions of the existing observations.

**IS-1 — restricted identification by accumulated observations.** Let $\mathcal H$ be a finite or countable hypothesis class containing the actual target $h_*$. Assume:

1. The target is stationary over the experiment, or the hypotheses already describe its complete relevant trajectory.
2. There is a countable, effectively schedulable family of reachable probes with deterministic, correctly predicted outputs $O_q(h)$. The learner can evaluate consistency and retain its observations.
3. Every rival $h\neq h_*$ is separated from $h_*$ by at least one such probe.
4. The schedule eventually executes each required probe. Executions provide accurate records and do not destroy access to subsequent required tests or change an unmodeled target.

Define the surviving hypotheses after $t$ observations:

```math
V_t=\{h\in\mathcal H:O_{q_s}(h)=O_{q_s}(h_*)\text{ for all }s\leq t\}.
```

Then:

```math
\bigcap_{t\geq 1}V_t=\{h_*\}.
```

**Proof.** Correct observations never remove $h_*$. Each rival has a separating probe; the schedule executes it at some finite step, at which that rival is removed. Hence precisely the target survives the intersection. For a finite hypothesis class, the maximum of the finitely many required elimination times is finite, so the version space becomes a singleton. This is completion relative to the declared realizable class, not proof that the class exhausts reality.

For a countable class, a singleton limiting intersection need not yield a finite certificate. Consider the all-zero binary sequence alongside sequences having exactly one `1` at an arbitrary position. Query positions in order when the truth is all-zero. Every particular rival is eventually eliminated, but after any finite stage an unqueried position supports another rival. The intersection is exact while no finite version space is a singleton. IS-1 proves this version-space statement; it does not supply a general learning algorithm whose output is guaranteed to stabilize or announce completion.

Unlimited resources thus remove some computational and sampling bottlenecks under stated conditions. They do not supply identifiability, reachability, correct model-class specification, or stationarity by themselves. No stochastic convergence theorem is claimed here; noisy learning requires its own observation and consistency assumptions.

## 3. Finite learners can put part of the learning process into the world

Actual development does not enjoy that ideal observer's conditions. A finite observer acts while its model is incomplete, inherits an environment it did not choose, and must reuse tools whose full derivations it does not possess. The foundation already locates early development largely on the contact-driven side rather than treating it as the learner's deliberate design.

Operationally, humans are thermodynamically open systems: they exchange matter and energy with their surroundings. For the present argument, the consequential feature is the capacity to act on an external environment and encounter the enduring effects. Material and energetic exchange enables this process; it is not an entropy argument proving epistemic progress.

The proposed causal chain has several necessary links: action leaves a usable external trace; another learner encounters that trace; its interpretation survives contextual change; learning is retained and can guide later activity. A physical trace alone does not establish any of those later links.

An illustrative organization can encode a successful procedure in its tools, layout, labels, demonstrations, and role assignments. Its next member then encounters a structured learning environment instead of independently rediscovering every distinction. Formation can be explicit through instruction and osmotic through everyday participation.

The archive's [recursive epistemic ratchet](../../docs/recursive-epistemic-ratchet.md), especially “Epistemic compilation” and “Osmotic inheritance,” already states this mechanism: inherited infrastructure makes a capability usable before its derivation is personally reconstructed. This is a direct integration site for the present proposal, rather than independent empirical confirmation. Boyd, Richerson, and Henrich's [2011 cultural-niche account](https://pmc.ncbi.nlm.nih.gov/articles/PMC3131818/) supplies relevant primary literature on cumulative socially acquired practices; it also explains why cheaper imitation alone need not improve population adaptation.

## 4. Make “learning commutes” a typed claim

Fix two contexts $c,d$, the relevant task, learner starting conditions, learning protocol, and admissible experience bundles. Write:

```math
L_c:E_c\to M_c,\qquad L_d:E_d\to M_d,
```

where $E_c$ contains learning experiences in context $c$ and $M_c$ contains the resulting task models. Let experience translation and model translation be:

```math
T_E:E_c\to E_d,\qquad T_M:M_c\to M_d.
```

Exact commutation means:

```math
T_M\circ L_c=L_d\circ T_E.
```

Learning in the first context and transporting the result then agrees with translating the experience and learning in the second. These types prevent “transport” from sliding between copied words, usable skills, institutional authority, and preserved understanding. A stochastic learning rule would require a corresponding distributional formulation; it is not automatically a deterministic map.

Standardized units, role conventions, shared interfaces, and reproducible demonstrations are candidate ways to reduce the discrepancy between those routes. Making it feel trivial to the recipient may require substantial prior work to align contexts. The archive's [cultural interoperability work](../../docs/cultural-interoperability.md) provides existing distinctions between transported observations, preserved relations, and intervention-level agreement.

When an application justifies a metric or task-specific pseudometric on $M_d$, approximate commutation can be measured by:

```math
\eta(e)=d_{M_d}\big(T_M(L_c(e)),L_d(T_E(e))\big).
```

For example, disagreement on a declared family of task predictions defines a pseudometric when distinct models can agree on every measured task. The task family and weights must be declared. Small discrepancy on that family does not establish equivalence outside it, and no metric is inferred merely from naming a transport.

## 5. The same route can carry useful knowledge and persistent error

Commutation is a portability condition. It does not certify correctness. An exact negative control is immediate: let each learning map always return its context's version of the same false model, and let $T_M$ carry one version to the other. Both routes agree for every experience, although the model fails an external test.

This preserves the author's central point that low-friction social inheritance can transport both good and bad models. A recipient can inherit a powerful instrument, a useful shortcut, a mistaken assumption, or an obsolete rule through the same reliable channel. Trust in the channel, source provenance, task fit, and independently tested content must therefore remain distinct.

The [existing finite witness](finite_witness.py) already illustrates one relevant boundary: observations selected by a model can all succeed while an externally selected context set fails. It does not simulate cultural transmission, but supplies a controlled reason to test transport against changed contexts rather than only against familiar examples.

Reduced learning or transport cost also does not establish optimality. An optimization claim needs an objective, admissible designs, error costs, and accounting for construction, maintenance, revision, and exclusion of alternatives. “Optimal learning” is retained as the author's design ambition, not announced as a consequence of openness or standardization.

## 6. Standing on the shoulders of giants becomes a concrete research target

The proposed advantage is cumulative external preparation: earlier observers modify an environment so later observers inherit useful distinctions, tools, and affordances with less repeated discovery. The world can carry part of a derivation's operational consequences while individual learners continue developing.

The next discriminating application should compare unprepared and scaffolded learning environments across two contexts. Measure learning cost, transport discrepancy, external task accuracy, source recovery, and revision after a deliberate context change separately. Include a faithfully transported false rule as a negative control and an irrelevant formatting change as a null control.

Evidence for the stronger proposal would show transferable capability, reduced total relevant cost, and retained correction under context change. Faster agreement alone would establish easier transmission. The developmental rates, social benefits, and any optimum remain **UNVERIFIED** until that work is done. The resulting framework connects κ, osmotic imprinting, integration, trust, and shared infrastructure without treating a socially coherent model as automatically true.
