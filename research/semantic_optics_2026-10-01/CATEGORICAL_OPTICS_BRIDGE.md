# Categorical Optics Bridge

## Primary-source pressure test of the semantic-optics idea

**Status:** literature bridge. Mathematical descriptions of cited optic constructions are source-supported. The TLICA mappings are **Conjectured** until formal functors are built.

---

# 1. Research question

Does the ordinary/social meaning of “optics” merely resemble categorical optics, or is there enough structural correspondence to justify treating categorical optics as the mathematical backbone of Semantic Optics?

The answer from this round is:

> **There is a nontrivial structural match at the level of typed bidirectional interfaces, residual context, composition, and hole-filling.**

That does **not** yet establish categorical equivalence.

---

# 2. Riley 2018 — the base optic

Primary source:

Mitchell Riley, *Categories of Optics*, arXiv:1809.00738  
https://arxiv.org/abs/1809.00738

Riley begins from concrete lenses:

\[
\mathrm{Get}:S\to A,
\]

\[
\mathrm{Put}:S\times A'\to S'.
\]

He then generalizes to optics in an arbitrary symmetric monoidal category.

For pairs \((S,S')\) and \((A,A')\):

\[
\operatorname{Optic}_{\mathcal C}
((S,S'),(A,A'))
=
\int^{M\in\mathcal C}
\mathcal C(S,M\otimes A)
\times
\mathcal C(M\otimes A',S').
\]

A representative is:

\[
l:S\to M\otimes A,
\]

\[
r:M\otimes A'\to S'.
\]

Riley describes \(M\) as temporary “scratch space”: information retained from \(S\) so that \(S'\) can later be reconstructed.

This is the first load-bearing bridge.

---

# 3. Semantic reading of the residual

The semantic-optics interpretation is:

\[
S
=
\text{full current situation},
\]

\[
A
=
\text{evidence exposed to the observer},
\]

\[
M
=
\text{causal/contextual support not exposed at the interface},
\]

\[
A'
=
\text{returned observer response},
\]

\[
S'
=
\text{updated proper situation}.
\]

Then:

\[
l:S\to M\otimes A
\]

is an **exposure split**.

It says:

> from the proper state, produce an observer-facing view while carrying forward hidden residual state.

And:

\[
r:M\otimes A'\to S'
\]

is the **return/update** map.

It says:

> recombine the hidden context with what came back from the observer to produce the next world-state.

This is strikingly close to the intended object:

\[
\text{world}
\to
\text{observable interface}
\to
\text{observer response}
\to
\text{world}.
\]

---

# 4. Why the coend quotient matters socially

The residual \(M\) is not part of the external identity of the optic.

Different residual factorizations can represent the same optic.

This is exactly what we want if two implementations carry the same task-relevant hidden support but encode it differently.

The optic quotient therefore supplies a useful firewall:

\[
\boxed{
\text{hidden representation choice}
\neq
\text{observable interface identity}.
}
\]

This resonates with the repository's repeated distinction between:

- implementation path;
- task-relative macrostate;
- local projection;
- exposed evidence.

But the equivalence relation is the categorical coend relation, not TLICA's existing quotient machinery.

---

# 5. Hole-filling is the strongest bridge

Riley's string-diagram interpretation treats an optic as an open diagram with a hole.

Given:

\[
\omega=[M,l,r]
\]

and a process:

\[
c:A\to A',
\]

the closed composite is:

\[
r\circ(\mathrm{id}_M\otimes c)\circ l.
\]

This suggests a disciplined separation:

\[
\boxed{
\text{categorical optic}
=
\text{interface/context}
}
\]

while:

\[
\boxed{
\text{TLICA observer/controller}
=
\text{process inserted into the hole}.
}
\]

This is currently more plausible than the stronger statement:

> TLICA itself is the optic.

TLICA's variables describe the state and constraints of the interpreting/acting I.

The optic describes the bidirectional environment/interface in which such a process is inserted.

---

# 6. Riley's Yoneda reductions

Riley explicitly uses coend calculus and “Ninja Yoneda” / Yoneda reduction.

For ordinary lenses in a cartesian category, the optic coend reduces to the familiar Get/Put representation using Yoneda reduction.

This is important for the moonshot for two reasons:

1. Yoneda is **already structurally active inside optic representation theory**; it is not an alien theorem being attached after the fact.
2. However, Riley's Yoneda reductions establish representation isomorphisms **within the optic theory**. They do not imply that TLICA and optics are categorically equivalent.

This distinction is load-bearing.

---

# 7. Lawfulness is separate from existence

Riley distinguishes general optics from **lawful** optics.

The semantic-optics bridge should initially target the general optic category.

Why?

Human interpretation can be:

- inconsistent;
- path-dependent;
- source-defective;
- manipulative;
- state-dependent;
- non-idempotent.

It would be premature to import lens-law analogues as psychological laws.

A later program can ask which social/cognitive interfaces satisfy useful lawfulness conditions.

---

# 8. Clarke et al. — mixed and enriched optics

Primary source:

Bryce Clarke, Derek Elkins, Jeremy Gibbons, Fosco Loregian, Bartosz Milewski, Emily Pillmore, Mario Román,  
*Profunctor Optics, a Categorical Update*, Compositionality 6 (2024), arXiv:2001.07488  
https://arxiv.org/abs/2001.07488

The paper generalizes optics to mixed and enriched settings.

For an acting monoidal category \(\mathcal M\), with \(\mathcal M\)-actegories \(\mathcal C,\mathcal D\):

\[
\operatorname{Optic}
((S,T),(A,B))
=
\int^{M\in\mathcal M}
\mathcal C(S,M\bullet A)
\times
\mathcal D(M\ast B,T).
\]

This matters because a semantic optic's forward and backward channels need not be homogeneous.

Potentially:

- forward channel: stochastic observation;
- internal channel: inference;
- backward channel: discrete action;
- world update: institutional / physical transition.

A mixed optic can represent different mathematical types on the two legs.

---

# 9. Profunctor representation

Clarke et al. connect mixed optics to generalized Tambara modules / profunctor representations.

The relevance is not implementation convenience.

It suggests:

> one optic can admit multiple equivalent representations, and composition can be studied through a representation theorem rather than through one concrete tuple encoding.

This is directly relevant to the proposed Yoneda program.

A future TLICA bridge should therefore distinguish:

- concrete semantic-optic tuples;
- categorical optic equivalence classes;
- profunctor/Tambara representation;
- TLICA decorations.

If two of those are conflated, apparent “equivalence” may be only a change of encoding.

---

# 10. Bayesian Updates Compose Optically

Primary source:

Toby St. Clere Smithe, *Bayesian Updates Compose Optically*, arXiv:2006.01631  
https://arxiv.org/abs/2006.01631

The paper's central result is that Bayesian inversion of a composite process can itself be composed from component inversions, and that the relevant compositional structure is lens-like.

It treats Bayesian inversion as a state-dependent morphism in a fibred category.

This is a major neighboring result for semantic optics.

Semantic optics also has:

- a forward evidence-generating process;
- an observer who must reconstruct hidden structure;
- a backward response/update.

But no inference should be made that TLICA is Bayesian.

The correct use is as a comparator:

\[
\text{TLICA decoder}
\quad
\text{vs}
\quad
\text{Bayesian inversion baseline}.
\]

---

# 11. Why Bayesian lenses matter to the deviation idea

Suppose:

\[
D^{B}
\]

is a Bayesian inverse and:

\[
D^\Theta
\]

is a TLICA-parameterized decoder.

A future experiment might compare them.

But the “deviation”:

\[
\Delta^\Theta
\]

cannot be written as subtraction unless the codomain carries an additive structure.

Safer:

\[
\Delta^\Theta
=
\operatorname{Compare}
(D^\Theta,D^B).
\]

Possible comparison objects include:

- natural transformation;
- divergence;
- metric defect;
- calibration curve;
- fiber position;
- likelihood-ratio residual;
- qualitative failure class.

The baseline must be declared.

---

# 12. Bayesian open games

Primary source:

Joe Bolt, Jules Hedges, Philipp Zahn, *Bayesian open games*, arXiv:1910.03656  
https://arxiv.org/abs/1910.03656

The paper extends compositional game theory to:

- stochastic environments;
- stochastic choices;
- incomplete information.

This is directly relevant to political and social optics.

In many semantic-optics problems, an actor anticipates:

\[
\Omega_j(x)
\]

and chooses a move partly for its effect on observer response.

That is strategic, not merely perceptual.

The open-game literature is therefore a serious candidate for the **strategic layer above the optic**, rather than something the semantic-optics project should recreate from scratch.

---

# 13. Compositional Game Theory

Primary source:

Neil Ghani, Jules Hedges, Viktor Winschel, Philipp Zahn, *Compositional game theory*, arXiv:1603.04641  
https://arxiv.org/abs/1603.04641

Open games are morphisms in a symmetric monoidal category and compose into larger games.

They are explicitly modeled relative to an environment and return environment-relevant information.

This is structurally adjacent to:

\[
\text{agent}
\leftrightarrow
\text{observer/environment}.
\]

But open games add equilibrium / preference machinery not assumed by TLICA.

---

# 14. Coherence for lenses and open games

Primary source:

Jules Hedges, *Coherence for lenses and open games*, arXiv:1704.02230  
https://arxiv.org/abs/1704.02230

Hedges identifies a teleological categorical structure with counit-like behavior but no corresponding units.

Riley later proves a universal property in which the optic construction freely adds counits to a suitable setting.

This is relevant because social/cognitive interactions are naturally future-directed and response-sensitive.

Still:

\[
\text{teleological category}
\neq
\text{TLICA prerogative of continued existence}.
\]

No conceptual identification is claimed.

---

# 15. Fibrational optics

Primary source:

Matteo Capucci, Bruno Gavranović, Abdullah Malik, Francisco Rios, Jonathan Weinberger,  
*On a fibrational construction for optics, lenses, and Dialectica categories*, arXiv:2403.16388  
https://arxiv.org/abs/2403.16388

The paper gives an overarching fibrational construction for optics/lenses.

This matters strongly for the proposed TLICA-deviation formulation.

If TLICA state varies over interface type, the right construction may be:

\[
p:\mathsf{TOpt}\to\mathsf{Optic}
\]

as a fibration or related total category.

Then observer/toolkit/history structure lives in the fiber over the base interface.

This is mathematically much cleaner than inventing an untyped additive correction.

---

# 16. Grothendieck construction

Reference overview:

https://ncatlab.org/nlab/show/Grothendieck+fibration  
https://ncatlab.org/nlab/show/indexed+category

An indexed category:

\[
\mathcal D:
\mathcal B^{op}
\to
\mathbf{Cat}
\]

is equivalent, under the Grothendieck construction, to a category fibred over \(\mathcal B\).

The total category has objects schematically:

\[
(b,\delta),
\qquad
\delta\in\mathcal D(b).
\]

This is exactly the generic form wanted for:

\[
\boxed{
\text{base optic}
+
\text{TLICA-specific state}
}
\]

provided the indexing and reindexing laws can actually be defined.

---

# 17. Decorated structures as precedent

Primary neighboring source:

Brendan Fong, *Decorated Cospans*, arXiv:1502.00872  
https://arxiv.org/abs/1502.00872

Decorated cospans show a mature applied-category pattern:

> keep a compositional base interface object, then attach structured extra data via a functor.

This is not itself an optic theorem.

It is precedent for the strategy:

\[
\text{compositional shell}
+
\text{typed decoration}.
\]

---

# 18. Structured vs decorated cospans

Primary source:

John C. Baez, Kenny Courser, Christina Vasilakopoulou,  
*Structured versus Decorated Cospans*, arXiv:2101.09363  
https://arxiv.org/abs/2101.09363

Under suitable conditions, structured and decorated constructions can become isomorphic after passing through a Grothendieck category.

This is highly relevant to a future semantic-optics question:

> is TLICA best represented as an explicit decoration over optics, or can the same information be absorbed into a richer base category so that the result becomes an ordinary optic there?

That is exactly one route by which “TLICA is a granularized instantiation of categorical optics” could become literal.

But doing so can also become tautological if the base category is engineered merely to encode TLICA verbatim.

---

# 19. The anti-tautology constraint

A bad proof would proceed:

1. define a base category whose objects literally contain every TLICA state;
2. define optics over it;
3. observe that TLICA can be encoded;
4. announce equivalence.

That demonstrates representability, not explanatory reduction.

The bridge only earns scientific value if:

- the categorical structure is independently motivated;
- the mapping preserves pre-existing TLICA distinctions;
- nontrivial composition laws are inherited;
- some TLICA distinctions are shown redundant, necessary, or impossible;
- the mapping predicts failures/collisions not inserted by construction.

---

# 20. Strongest current bridge diagram

Current candidate:

\[
\begin{array}{ccc}
\mathsf{TLICA\ observer\ state}
& \longrightarrow &
c_{\Theta}:A\to A'
\\[4pt]
& &
\downarrow \text{plug into hole}
\\[4pt]
\mathsf{Categorical\ optic}
& \ni &
\omega=[M,l,r]
\\[4pt]
& &
\downarrow
\\[4pt]
& &
\operatorname{cl}_\Theta(\omega):S\to S'.
\end{array}
\]

An alternative packaging is:

\[
p:\mathsf{TOpt}\to\mathsf{Optic}
\]

with TLICA state in the fibers.

These are not yet proven equivalent formulations.

---

# 21. Candidate interpretations ranked by mathematical commitment

## I. Optic-as-shell

Lowest commitment.

Categorical optic provides interface; TLICA supplies hole process.

Current best-supported reading.

## II. TLICA-decorated optic

Observer state is structured decoration/fiber over optic interfaces.

Strongly plausible from fibrational literature.

## III. TLICA as optic in a richer base category

Absorb observer state into objects/residuals of a richer category.

Possible, but high tautology risk.

## IV. Equivalence of categories

Construct:

\[
F:\mathsf{TOpt}\to\mathsf{Optic}_{\mathcal C}
\]

and prove full, faithful, essentially surjective.

Moonshot.

## V. Yoneda-certified equivalence

Additionally match representable/restricted probe profiles in a way that demonstrates the equivalence from compositional observations.

Strongest target.

---

# 22. Categorical cybernetics — closest prior art

Primary source:

Matteo Capucci, Bruno Gavranović, Jules Hedges, Eigil Fjeldgren Rischel, *Towards Foundations of Categorical Cybernetics*, arXiv:2105.06332  
https://arxiv.org/abs/2105.06332

This source materially tightens the bridge.

The authors explicitly combine:

\[
\mathbf{Para}(-)
\]

and:

\[
\mathbf{Optic}(-)
\]

to obtain parametrised optics for bidirectional dynamical systems steered by agents.

A parametrised optic includes parameter/coparameter objects \((P,Q)\) and maps schematically:

\[
v:P\bullet X\to M\bullet Y,
\]

\[
u:M\bullet Y'\to Q\bullet X'.
\]

The paper interprets parameters/coparameters and residuals as private agent state/memory and reparametrisations as agency dynamics.

This is closer to Semantic Optics than a generic optic-plus-fiber construction.

The preferred target is now:

\[
\boxed{
\mathsf{TLICAOptics}
\stackrel{?}{\hookrightarrow}
\mathbf{Para}(\mathbf{Optic})
}
\]

with TLICA supplying candidate semantics/constraints on the parameter state rather than inventing the generic controller architecture.

Detailed pressure analysis: [CATEGORICAL_CYBERNETICS_PRESSURE.md](CATEGORICAL_CYBERNETICS_PRESSURE.md).

---

# 23. Current conclusion

The literature does not collapse the project.

It strengthens it.

There is already a mature hierarchy:

\[
\text{lenses}
\subset
\text{optics}
\leftrightarrow
\text{profunctor/Tambara representations},
\]

with extensions toward:

\[
\text{mixed/enriched optics},
\]

\[
\text{Bayesian lenses},
\]

\[
\text{fibrational optics},
\]

\[
\text{open games}.
\]

The semantic-optics program should therefore attempt to **land inside this ecosystem**, not build a parallel vocabulary.

The open question is not:

> “Can we make TLICA sound categorical?”

It is:

> **Which existing categorical object, if any, carries exactly the observer-interface structure TLICA needs, and what additional structure remains after the strongest honest reduction?**
