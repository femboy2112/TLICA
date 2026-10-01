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
