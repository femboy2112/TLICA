# Sources and Prior-Art Pressure — Semantic Optics

**Date:** 2026-10-01  
**Status:** source map for a research-tier bridge. No novelty claim is made.

The current program has two source families:

1. **external categorical/compositional literature**;
2. **existing TLICA repository ancestors**.

The point is not to collect adjacent words. It is to identify which mathematical structures already exist and which TLICA claims are genuinely extra.

---

# A. External categorical/compositional literature

## A1. Mitchell Riley — Categories of Optics

Mitchell Riley, *Categories of Optics* (2018).  
arXiv:1809.00738  
https://arxiv.org/abs/1809.00738

### Load-bearing facts used here

- lenses are a special case of a general optic construction;
- a general optic is represented by a forward map and backward map with residual \(M\);
- optics compose;
- the residual is quotiented by a coend relation;
- the construction has a universal property;
- lawfulness is separable from mere optic existence;
- Yoneda/coend reduction is used internally to recover concrete lens representations.

### Why relevant

This is the base source for:

\[
l:S\to M\otimes A,
\qquad
r:M\otimes A'\to S'.
\]

The semantic-optics project maps:

\[
S\leftrightarrow\text{proper state},
\quad
A\leftrightarrow\text{available evidence},
\quad
M\leftrightarrow\text{hidden residual context},
\quad
A'\leftrightarrow\text{returned response},
\quad
S'\leftrightarrow\text{updated state}.
\]

### What it does NOT establish

- TLICA is an optic;
- humans satisfy optic laws;
- TLICA optics is equivalent to Riley's optic category.

---

## A2. Clarke et al. — Profunctor Optics, a Categorical Update

Bryce Clarke, Derek Elkins, Jeremy Gibbons, Fosco Loregian, Bartosz Milewski, Emily Pillmore, Mario Román,  
*Profunctor Optics, a Categorical Update*. Compositionality 6 (2024).  
arXiv:2001.07488  
https://arxiv.org/abs/2001.07488  
DOI: https://doi.org/10.32408/compositionality-6-1

### Load-bearing facts

- mixed optics;
- enriched optics;
- generalized Tambara modules;
- alternative profunctor representation;
- category structure for mixed enriched optics.

### Why relevant

Semantic optics may require different mathematical categories for:

- world state;
- evidence;
- interpretation;
- response.

This source prevents premature forcing into homogeneous \(\mathbf{Set}\) optics.

---

## A3. Toby St. Clere Smithe — Bayesian Updates Compose Optically

Toby St. Clere Smithe, *Bayesian Updates Compose Optically* (2020).  
arXiv:2006.01631  
https://arxiv.org/abs/2006.01631

### Load-bearing facts

- Bayesian inversion composes according to a lens-like structure;
- inversion is treated as state-dependent;
- fibred-category machinery is central.

### Why relevant

Semantic optics includes an inference problem:

\[
\text{world}\to\text{evidence}
\]

followed by an observer reconstructing hidden structure.

Bayesian lenses supply a principled inference baseline without licensing the claim that TLICA observers are Bayesian.

---

## A4. Braithwaite, Hedges, St Clere Smithe — Compositional Structure of Bayesian Inference

Dylan Braithwaite, Jules Hedges, Toby St Clere Smithe,  
*The Compositional Structure of Bayesian Inference* (2023).  
arXiv:2305.06112  
https://arxiv.org/abs/2305.06112

### Relevance

A later general treatment of Bayesian inversion in categories of Markov kernels, again emphasizing state-dependent morphisms and functorial/compositional inference.

Useful for a future stochastic Semantic Optics layer.

---

## A5. Ghani et al. — Compositional Game Theory

Neil Ghani, Jules Hedges, Viktor Winschel, Philipp Zahn,  
*Compositional game theory* (2016).  
arXiv:1603.04641  
https://arxiv.org/abs/1603.04641

### Load-bearing facts

- open games are morphisms of a symmetric monoidal category;
- games are defined relative to an environment;
- information/feedback flows compose;
- Nash/off-equilibrium behavior can be represented compositionally.

### Why relevant

Political optics, reputation management, comedy, performance, and ordinary social action can be strategic: actors anticipate how an observer will decode and respond.

This is a strategic layer beyond a bare optic.

---

## A6. Bolt, Hedges, Zahn — Bayesian Open Games

Joe Bolt, Jules Hedges, Philipp Zahn,  
*Bayesian open games* (2019).  
arXiv:1910.03656  
https://arxiv.org/abs/1910.03656

### Load-bearing facts

The framework extends open games toward:

- stochastic environments;
- stochastic choices;
- incomplete information.

### Why relevant

Many optics settings are explicitly incomplete-information interactions.

---

## A7. Hedges — Coherence for Lenses and Open Games

Jules Hedges, *Coherence for lenses and open games* (2017).  
arXiv:1704.02230  
https://arxiv.org/abs/1704.02230

### Relevance

Identifies teleological categorical structure underlying lenses/open games.

Useful prior art for future-directed bidirectional interactions.

No identification with TLICA's existential prerogatives is claimed.

---

## A8. Capucci et al. — Fibrational Construction for Optics

Matteo Capucci, Bruno Gavranović, Abdullah Malik, Francisco Rios, Jonathan Weinberger,  
*On a fibrational construction for optics, lenses, and Dialectica categories* (2024).  
arXiv:2403.16388  
https://arxiv.org/abs/2403.16388

### Load-bearing fact

Optic/lens constructions can be understood through towers of Grothendieck fibrations.

### Why relevant

This is direct prior art for the proposed:

\[
p:\mathsf{TOpt}\to\mathsf{Optic}
\]

fibred/decorated decomposition.

---

## A9. Grothendieck construction / indexed categories

Reference overview:

- https://ncatlab.org/nlab/show/Grothendieck+fibration
- https://ncatlab.org/nlab/show/indexed+category
- https://ncatlab.org/nlab/show/Grothendieck+construction+for+monoidal+categories

### Load-bearing fact

An indexed category:

\[
\mathcal D:\mathcal B^{op}\to\mathbf{Cat}
\]

corresponds to a category fibred over \(\mathcal B\).

This supplies the generic mathematics for:

\[
\text{base interface}
+
\text{state living over that interface}.
\]

---

## A10. Restricted Yoneda / density

Reference overview:

- https://ncatlab.org/nlab/show/Yoneda%20embedding
- https://ncatlab.org/nlab/show/restricted+Yoneda+embedding
- https://ncatlab.org/nlab/show/nerve
- https://ncatlab.org/nlab/show/dense+functor

### Load-bearing fact

For:

\[
i:\mathcal P\to\mathcal C,
\]

the restricted nerve:

\[
N_i(X)=\mathcal C(i-,X)
\]

is fully faithful iff \(i\) is dense.

### Why relevant

This is the strongest formal neighbor of TLICA's “available probes may not distinguish live rivals.”

It does not automatically equal \(\mu\) or \(\phi\).

---

## A11. Fong — Decorated Cospans

Brendan Fong, *Decorated Cospans* (2015).  
arXiv:1502.00872  
https://arxiv.org/abs/1502.00872

### Relevance

Established applied-category pattern:

\[
\text{compositional interface}
+
\text{functorial extra structure}.
\]

Not an optic theorem, but useful design prior art.

---

## A12. Baez, Courser, Vasilakopoulou — Structured vs Decorated Cospans

John C. Baez, Kenny Courser, Christina Vasilakopoulou,  
*Structured versus Decorated Cospans* (2021).  
arXiv:2101.09363  
https://arxiv.org/abs/2101.09363

### Relevance

Under suitable conditions, decorated and structured forms can become equivalent through a Grothendieck category.

This directly motivates the question:

> could TLICA state be represented either as optic decoration or absorbed into a richer base category?

---

## A13. Capucci et al. — Towards Foundations of Categorical Cybernetics

Matteo Capucci, Bruno Gavranović, Jules Hedges, Eigil Fjeldgren Rischel,  
*Towards Foundations of Categorical Cybernetics* (2022 revision).  
arXiv:2105.06332  
https://arxiv.org/abs/2105.06332

### Load-bearing facts

- explicitly models processes interacting bidirectionally with environment and controller;
- combines \(\mathbf{Para}(-)\) with \(\mathbf{Optic}(-)\);
- makes parametrised optics the central construction;
- interprets parameter/coparameter and residual structure as private state/memory;
- uses reparametrisation to represent agency dynamics.

### Research impact

This is the **closest prior art located so far**. It shifts the preferred target from “bare optic + invented TLICA fiber” to a TLICA-typed region of parametrised optics / categorical cybernetics.

---

## A14. Smithe — Cyber Kittens

Toby St. Clere Smithe,  
*Cyber Kittens, or Some First Steps Towards Categorical Cybernetics* (2021).  
arXiv:2101.10483  
https://arxiv.org/abs/2101.10483

### Load-bearing facts

- defines categorical cybernetic systems as dynamical realisations of generalized open games;
- emphasizes compositional bidirectional structure;
- builds on Bayesian updates composing optically.

### Research impact

Further blocks any novelty claim for generic “bidirectional agent/world feedback as categorical optics.”

---

## A15. Smithe — Compositional Active Inference I

Toby St. Clere Smithe,  
*Compositional Active Inference I: Bayesian Lenses. Statistical Games* (2022 revision).  
arXiv:2109.04461  
https://arxiv.org/abs/2109.04461

### Load-bearing facts

- Bayesian lenses characterize exact Bayesian-inference bidirectionality;
- Bayesian inversions compose;
- statistical games formalize objectives for approximate inference;
- the framework is aimed toward compositional active inference.

### Research impact

Semantic Optics must distinguish TLICA-specific observer semantics from already-existing compositional inference/objective machinery.

---

## A16. Hedges & Sakamoto — Reinforcement Learning in Categorical Cybernetics

Jules Hedges, Ryo Sakamoto,  
*Reinforcement Learning in Categorical Cybernetics* (2024).  
arXiv:2404.02688

### Relevance

Shows the categorical-cybernetics/parametrised-optics line is an active program extending into reinforcement learning. This strengthens the requirement to compare TLICA against the existing cybernetic stack rather than claiming a new generic control architecture.

---

## A17. Smithe — Structured Active Inference

Toby St. Clere Smithe,  
*Structured Active Inference* (2024).  
arXiv:2406.07577

### Load-bearing facts

The work uses categorical systems theory to cast generative models as systems “on an interface,” treats agents as controllers dual to those models, and develops structured/changing interfaces and typed policies.

### Research impact

This further narrows the candidate TLICA contribution: generic system/interface/controller compositionality is prior art. The interesting question is whether TLICA's internal semantic/probe/source decomposition earns additional explanatory or predictive value.

---

## A18. Hefford & Comfort — Coend Optics for Quantum Combs

James Hefford, Cole Comfort,  
*Coend Optics for Quantum Combs* (2022).  
arXiv:2205.09027  
https://arxiv.org/abs/2205.09027

### Load-bearing facts

The paper compares:

- an **intensional** definition of 1-combs as coend optics;
- an **extensional** definition obtained by quotienting operational behavior on lower-order maps.

It constructs a **full, bijective-on-objects quotient functor** from the intensional to the extensional category and gives sufficient conditions for that functor to become an isomorphism.

### Research impact

This is exceptionally close in abstract shape to the Semantic Optics fork:

\[
\text{rich/intensional semantics}
\to
\text{operational quotient}.
\]

The application domain is quantum combs, not TLICA, but it establishes that intensional-versus-extensional quotienting is already serious optic-theory territory. Semantic Optics should frame “TLICA delta” as a candidate kernel/quotient question rather than claim novelty for the pattern.

---

## A19. Brunetti, Fredenhagen, Verch — Generally Covariant Locality Principle

Romeo Brunetti, Klaus Fredenhagen, Rainer Verch,  
*The generally covariant locality principle — A new paradigm for local quantum physics* (2001/2003).  
arXiv:math-ph/0112041  
https://arxiv.org/abs/math-ph/0112041

### Load-bearing facts

- locally covariant QFT is formulated as a covariant functor from globally hyperbolic spacetimes with admissible embeddings to unital *-algebras with injective morphisms;
- ordinary Haag–Kastler nets are recovered as a special case;
- locally covariant fields are natural transformations.

### Research impact

This is strong prior art for the Semantic Optics locality claim that the same physical structure must transport coherently through admissible local embeddings, and for using commuting naturality squares rather than verbal “same local physics” claims.

---

## A20. Haag–Kastler local nets / isotony and causal locality

Foundational framework: Rudolf Haag and Daniel Kastler, *An Algebraic Approach to Quantum Field Theory* (1964).

Modern summary used in this round:
https://qft.org/mathematical-qft/algebraic-locally-covariant-qft/haag-kastler-nets-locality/

### Load-bearing facts

- regions are assigned local observable algebras;
- isotony: \(O_1\subset O_2\Rightarrow \mathcal A(O_1)\subseteq\mathcal A(O_2)\);
- spacelike-separated local algebras obey Einstein-causality/locality constraints;
- covariance transports local algebras under spacetime symmetries.

### Research impact

This supplies an established physical “locality net” model that is not a single linear nesting chain.

---

## A21. Abramsky & Brandenburger — sheaf-theoretic contextuality

Samson Abramsky, Adam Brandenburger,  
*The Sheaf-Theoretic Structure of Non-Locality and Contextuality* (2011).  
arXiv:1102.0264  
https://arxiv.org/abs/1102.0264

### Load-bearing facts

- measurement contexts form a cover;
- local data are handled sheaf-theoretically;
- contextuality/nonlocality correspond to obstructions to global sections.

### Research impact

This blocks the naive inference:

\[
\text{every local context is coherent}
\Rightarrow
\text{one global hidden assignment exists}.
\]

It motivates separating **restriction/local support** from **global gluing**.

---

## A22. Relativistic frame covariance / overlapping charts

Useful source:
Markus Pössel, Einstein Online, *…that all coordinate systems are created equal*  
https://www.einstein-online.info/en/spotlight/covariance/

Additional geometry reference:
H. S. Reall, *General Relativity* lecture notes, manifold/chart section.

### Load-bearing facts

- different observers/charts assign different coordinate values to the same events;
- lawful transition maps relate overlapping descriptions;
- physical laws are formulated covariantly rather than by demanding identical coordinates.

### Research impact

This directly supports the user's distinction:

> the mathematics/relations agree, while simultaneity, coordinate values, energy/momentum components, etc. need not.

---

## A23. Yoneda, generalized elements, and representable identity

Standard references:

- Yoneda lemma / full faithfulness / uniqueness of representing objects:
  https://ncatlab.org/nlab/show/Yoneda+lemma
- generalized elements:
  https://ncatlab.org/nlab/show/generalized+element

### Load-bearing facts

For \(f:A\to B\), Yoneda transports every generalized element \(x:C\to A\) by:

\[
x\mapsto f\circ x.
\]

Moreover:

\[
A\cong B
\iff
y(A)\cong y(B).
\]

### Research impact

This is the exact object-level form1/form2 theorem. Invertible forms correspond to invertible Yoneda transport of every probe.

---

## A24. Adjunctions and adjoint equivalences

Standard references:

- adjunction as natural hom-set bijection:
  https://ncatlab.org/nlab/show/adjoint+functor
- adjoint equivalence:
  https://ncatlab.org/nlab/show/adjoint+equivalence
- equivalence of categories / quasi-inverses:
  https://stacks.math.columbia.edu/download/categories.pdf

### Load-bearing facts

An adjunction:

\[
F\dashv G
\]

is equivalently a natural family:

\[
\mathcal B(Fc,d)
\cong
\mathcal A(c,Gd).
\]

An adjoint equivalence is an adjunction whose unit and counit are natural isomorphisms.

### Research impact

This supplies the exact context-level forward/backward-form structure, and distinguishes reversible hom-form transport from reversible object/context transport.

---

## A25. Kan extension and presheaf context transport

References:

- https://ncatlab.org/nlab/show/Kan+extension
- https://ncatlab.org/nlab/show/functoriality+of+categories+of+presheaves

### Load-bearing facts

For a functor \(F\), precomposition on presheaves has left/right Kan-extension adjoints under standard hypotheses:

\[
F_!
\dashv
F^\*
\dashv
F_*.
\]

Left Kan extension transports representables compatibly:

\[
F_!(y(c))
\cong
y(Fc).
\]

### Research impact

This supplies a canonical transport mechanism not only for objects, but for their full Yoneda/presheaf profiles across locality/scale contexts.

---

# B. Existing TLICA repository ancestors

These are **project-shared provenance**, not independent corroboration.

---

## B1. Shared Reality, Divergent Maps

Path:

\[
\texttt{applications/shared\_reality\_divergent\_maps\_v0\_2\_0.md}
\]

Key inherited object:

\[
\text{world-state}
\to
\text{learned representation}
\]

with candidate “vibe” defined as a decoded, affectively weighted model rather than truth.

Semantic Optics generalizes the interface structure behind that political application.

---

## B2. Semantic Wake Drag

Path:

\[
\texttt{research/semantic\_wake\_drag\_2026-09-26/}
\]

Key inherited objects:

- receiver-side reconstruction;
- local projection;
- observer update timescale \(\tau_O\);
- action/communication/observer mismatch;
- legibility \(\neq\) truth.

Semantic Optics subsumes the observer-interface half while preserving wake-specific timescale dynamics.

---

## B3. Distributed Institutional Realization

Path:

\[
\texttt{research/distributed\_institutional\_realization\_2026-09-15/}
\]

Key inherited claim:

> apparent local discontinuity can be the projection of distributed causal structure onto an insufficient local frame.

This is the clearest repository precursor to the optic residual \(M\).

---

## B4. Cold Frame / Referent Routing

Paths:

\[
\texttt{applications/cold\_frame\_*}
\]

and:

\[
\texttt{applications/referent\_routing\_*}
\]

Key inherited result:

Different inner structures can produce behaviorally identical outward conduct under a fixed field.

This is a direct optic-collapse specimen.

---

## B5. Cultural Realness Atlas

Path:

\[
\texttt{research/cultural\_realness\_atlas\_2026-09-22/}
\]

Key inherited object:

declared fact-preserving transports between annotated relational structures.

This may eventually supply a typed transport between observer meaning-spaces.

---

## B6. Self-Applied Architecture

Paths:

\[
\texttt{applications/self\_applied\_architecture\_*}
\]

Key inherited art thesis:

> art can instantiate an internal map in external form for receiver-side reconstruction.

Cinema and Semantic Optics refine the interface operators inside this claim.

---

## B7. Cinema as Self-Coupled Meaning-Space Reconstruction

Path:

\[
\texttt{research/cinema\_self\_coupled\_meaning\_space\_2026-10-01/}
\]

This is the immediate parent specimen.

It supplied:

- acting as generative re-realization;
- camera/edit as projection operator;
- viewer reconstruction;
- Kaufman/Cohen/Nicholson cases;
- the first explicit self-coupled loop.

Semantic Optics is the umbrella generalization.

---

## B8. Out of the Cave

Path:

\[
\texttt{applications/out\_of\_the\_cave\_v0\_1\_2.md}
\]

Relevant distinction:

- source map;
- probe availability;
- cave-internal discrimination;
- source-error despite high truth-indistinguishability.

Semantic Optics must preserve these distinctions rather than calling all interpretive error “bad optics.”

---

# C. Prior-art pressure summary

## Existing theory already owns

- categorical optic composition;
- residual/coend equivalence;
- profunctor/Tambara representations;
- mixed/enriched optics;
- Bayesian lens composition;
- open games;
- fibrational optic constructions;
- Grothendieck/indexed decoration patterns;
- Yoneda/restricted Yoneda/density.

## TLICA may contribute, if the bridge survives

- a particular structured observer-state decomposition;
- separation of contact, truth-indistinguishability, source map, identity coupling, and probe availability inside an optic/controller;
- a cross-family application synthesis connecting politics, institutions, cinema, reputation, comedy, and semantic wake;
- a toolkit-relative restricted-probe interpretation;
- empirical hypotheses about how observer state changes closure behavior.

These are **not novelty claims**.

They are candidate contributions requiring literature comparison and probes.

---

# D. Most dangerous prior-art failure modes

1. **Reinventing Bayesian lenses** while calling the result TLICA optics.
2. **Reinventing open games** for strategic observer response.
3. **Reinventing profunctor optics** as a “new bidirectional interface.”
4. **Calling a Grothendieck fiber a TLICA invention.**
5. **Using Yoneda as philosophical decoration** instead of proving full/faithful properties.
6. **Making the base category so TLICA-specific that equivalence becomes tautological.**

The repository should treat any of these as a failed research round, not a branding issue.

---

# E. Source status

The external literature above was freshly checked in this research round.

No source located here claims:

> TLICA is categorical optics.

No novelty claim is made.

The next literature pass should target:

- categorical cybernetics;
- open dynamical systems with lenses/optics;
- active inference / Bayesian lens applications;
- statistical games;
- double categories of open systems;
- representation learning under categorical observation interfaces;
- categorical system identification / tomography.

That flank remains open.
