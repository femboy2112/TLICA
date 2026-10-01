# Categorical Cybernetics Pressure Test

## The closest prior art changes the preferred target

**Date:** 2026-10-01  
**Status:** primary-source pressure update to the Semantic Optics program. External mathematical descriptions are source-supported; TLICA placement remains **CONJECTURED / UNVERIFIED**.

---

# 1. Result

The closest external framework located so far is not bare categorical optics.

It is:

\[
\boxed{
\mathbf{Para}\bigl(\mathbf{Optic}(-)\bigr)
}
\]

as developed in **categorical cybernetics**.

Capucci, Gavranović, Hedges, and Rischel explicitly construct parametrised optics for systems that interact bidirectionally with both an environment and a controller. Their framework treats parameters/coparameters and optic residuals as private agent state/memory, supports reparametrisation, and interprets the construction as dynamical systems steered by agents.

Primary source:

- Matteo Capucci, Bruno Gavranović, Jules Hedges, Eigil Fjeldgren Rischel, *Towards Foundations of Categorical Cybernetics*, arXiv:2105.06332, revised 2022.  
  https://arxiv.org/abs/2105.06332

This materially changes our prior-art map.

The naive claim:

> “Semantic Optics needs an optic plus a new TLICA controller/fiber.”

is now too broad as a novelty-shaped idea.

A substantial part of that shell already exists.

The research question narrows to:

> **Can TLICA's observer-state semantics be instantiated as a particular parametrisation / controller / selection layer inside categorical cybernetics, and what genuinely additional structure remains after that reduction?**

That is a stronger research program.

---

# 2. The existing categorical construction

The paper combines:

\[
\mathbf{Para}(-)
\]

with:

\[
\mathbf{Optic}(-)
\]

to obtain parametrised optics.

A parametrised optic has parameter and coparameter objects:

\[
(P,Q)
\]

and an optic-shaped process represented schematically by:

\[
v:P\bullet X\to M\bullet Y,
\]

\[
u:M\bullet Y'\to Q\bullet X'.
\]

Thus the forward process depends on a parameter state \(P\), while the backward process can return an update/change in \(Q\).

The framework interprets:

- the horizontal optic as a dynamical **arena/protocol**;
- vertical parameter wires as agents/control;
- reparametrisations as agency dynamics;
- residuals and parameters together as private agent state/memory.

This is extremely close to the object Semantic Optics was independently converging toward.

---

# 3. Revised candidate placement of TLICA

The earlier dossier considered three locations for TLICA:

1. the process inserted in the optic hole;
2. a decoration/fiber over optic interfaces;
3. state absorbed into a richer base category.

Categorical cybernetics adds a fourth, and now preferred, candidate:

\[
\boxed{
\text{TLICA observer state}
\longleftrightarrow
\text{parameter/coparameter semantics of a parametrised optic}.
}
\]

Write a schematic TLICA observer state:

\[
\Theta
=
(H,B,\mathrm{Foc},\kappa,\phi,\sigma,\rho,\mu,\tau_O,C,\ldots).
\]

The candidate is **not** to treat this heterogeneous structure as one numerical parameter.

Instead, seek a parameter category:

\[
\mathcal M_\Theta
\]

whose objects/morphisms encode only those aspects of observer state that actually reparametrise a given semantic interface.

Then a Semantic Optic may take the form:

\[
\widetilde\omega_\Theta
\in
\mathbf{Para}_{\circledast}
\bigl(
\mathbf{Optic}_{\bullet,\bullet}(\mathcal C,\mathcal D)
\bigr).
\]

This is now the leading formal target.

---

# 4. Why this is better than an ad hoc fiber

The \(\mathbf{Para}\) construction already supplies:

- typed parameters;
- composition of parameterised morphisms;
- reparametrisation;
- 2-cells between parameterisations;
- monoidal composition under suitable conditions.

So before inventing:

\[
p:\mathsf{TOpt}\to\mathsf{Optic}
\]

as a bespoke fibration, we should first test whether:

\[
\mathbf{Para}(\mathbf{Optic})
\]

already does the required work.

The generic fibred/Grothendieck construction remains useful only for TLICA structure not naturally expressible through \(\mathbf{Para}\), or for explaining how different observer-state fibers vary across interface types.

---

# 5. The strongest conceptual match

The categorical-cybernetics paper says parametrised optics model cybernetic systems—dynamical systems steered by agents—and that agents act in the world and receive feedback through the two actegorical directions.

For Semantic Optics, that becomes:

\[
\text{observer/actor parameter state}
\to
\text{world-facing action/exposure}
\to
\text{environment}
\to
\text{returned evidence/objective}
\to
\text{observer-state update}.
\]

This is almost exactly the closed semantic-optics loop:

\[
x_t
\to
y_t
\to
\widehat z_t
\to
a_t
\to
x_{t+1}
\]

once the observer state itself is made dynamic:

\[
\Theta_t
\to
\Theta_{t+1}.
\]

The categorical-cybernetics framework therefore appears to own much of the **compositional dynamics**.

TLICA's candidate distinctive contribution is more likely the **internal semantic typing of \(\Theta\)** and the probe/source/identity distinctions governing its updates.

---

# 6. Revised “Categorical Optics + TLICA deviation”

The previous generic equation was:

\[
\widetilde\omega
=
(\omega,\delta_\omega).
\]

The prior-art-adjusted candidate is now:

\[
\boxed{
\mathsf{TLICAOptics}
\stackrel{?}{\hookrightarrow}
\mathbf{Para}_{\Theta}
\bigl(
\mathbf{Optic}(\mathcal C,\mathcal D)
\bigr).
}
\]

Or, under a stronger moonshot:

\[
\boxed{
\mathsf{TLICAOptics}_0
\simeq
\mathsf{CyberOptics}_{\Theta,0}
}
\]

on a declared subdomain.

Then “TLICA deviation” is not generic extra decoration.

It is more precisely one of:

1. **parameter-state refinement** relative to a coarser parametrised optic;
2. **reparametrisation** between observer-state descriptions;
3. **controller-selection difference** inside the same optic arena;
4. **residual epistemic structure** not represented by the categorical-cybernetic baseline;
5. **probe/source semantics** attached to or constraining parameter updates.

This is substantially more disciplined.

---

# 7. A candidate coarse-to-rich diagram

Let:

\[
\mathsf O
=
\mathbf{Optic}_{\bullet,\bullet}(\mathcal C,\mathcal D).
\]

Let:

\[
\mathsf{CO}
=
\mathbf{Para}_{\circledast}(\mathsf O)
\]

be the categorical-cybernetic parametrised optic category/bicategory.

Let:

\[
\mathsf{TCO}
\]

be a future TLICA-typed restriction/refinement in which parameter objects satisfy TLICA-specific typing and update constraints.

Then seek:

\[
\mathsf{TCO}
\overset{U}{\longrightarrow}
\mathsf{CO}
\overset{V}{\longrightarrow}
\mathsf O.
\]

Interpretation:

- \(V\) forgets parameters/control and leaves the bidirectional arena;
- \(U\) forgets TLICA-specific semantics but leaves generic parametrised cybernetic structure.

The **TLICA deviation** relative to categorical cybernetics is whatever is lost under \(U\), not whatever is lost under the much coarser \(V\).

This is a more informative decomposition.

---

# 8. What might survive as genuinely TLICA-specific?

Current candidates:

## 8.1 Probe-closure semantics

A structured relation among:

\[
\mu,
\quad
\mathrm{Cl}(\mathrm{Tools}),
\quad
\phi,
\]

and a restricted probe category.

Categorical cybernetics supplies parametrised dynamics, but not automatically the TLICA distinction between:

- no constructible verification path;
- available but low-weight probe;
- source-map defect;
- identity-coupled resistance.

## 8.2 Source-map semantics

\[
\sigma
\]

is not merely hidden state.

It is a structured attribution from content to putative source, with adequacy separately audited.

A generic parameter object does not automatically encode the difference between:

\[
\text{correct evidence, wrong source}
\]

and:

\[
\text{wrong evidence, correct source}.
\]

## 8.3 Identity/commitment coupling

\[
\rho
\]

can alter stakes and update dynamics without being evidence of truth.

Again, generic parameter state does not enforce that firewall.

## 8.4 Toolkit-relative representation

The same optic arena can be interpreted through distinct learned bases:

\[
B_i\neq B_j.
\]

The TLICA program may contribute a typed account of how those bases affect decoder/controller structure.

## 8.5 Restricted-Yoneda probe adequacy

The density/nerve bridge may provide a formal account of when a probe family is structurally adequate to distinguish objects.

This currently looks more distinctive than the bare feedback architecture.

---

# 9. Parametrisation versus fiber: not rivals

The earlier fibred idea should not simply be deleted.

The \(\mathbf{Para}\) construction itself has fibrational behavior: reparametrisations track changes of parameter space.

The open question becomes:

> does TLICA need only parametrisation, or an indexed family of different parameter categories over different semantic interfaces?

If the latter, the Grothendieck/fibred layer returns **above** categorical cybernetics rather than replacing it.

Possible hierarchy:

\[
\boxed{
\text{optic}
\subset
\text{parametrised optic / cybernetic arena}
\subset
\text{TLICA-indexed semantic cybernetics}.
}
\]

This is cleaner than the original ad hoc fiber proposal.

---

# 10. Reparametrisation may be the right home for “deviation”

A parametrised morphism can be reparametrised along:

\[
r:M'\to M.
\]

That means some apparent TLICA deviations may be maps between observer-state parameterisations rather than differences inside one coordinate system.

This is important.

If two TLICA models of an observer are related by a lawful reparametrisation and induce the same externally relevant cybernetic behavior, then their difference may be representational.

This gives a mature categorical version of:

\[
\text{gauge-like TLICA deviation}.
\]

If no lawful reparametrisation exists and their full compositional profiles differ, the distinction may be structurally real.

Yoneda can then test the total categorical objects.

---

# 11. Connection to active inference

Toby St. Clere Smithe's *Compositional Active Inference I* introduces Bayesian lenses and statistical games and proves that Bayesian inversions compose in a lens pattern.

Primary source:

- Toby St. Clere Smithe, *Compositional Active Inference I: Bayesian Lenses. Statistical Games*, arXiv:2109.04461  
  https://arxiv.org/abs/2109.04461

This establishes a nearby compositional formalism where:

- forward generative processes;
- backward inference;
- optimization objectives;

are kept together.

TLICA should therefore be compared not only with bare Bayesian lenses but with the larger active-inference/statistical-game machinery.

No reduction of TLICA to active inference is claimed.

---

# 12. Cyber Kittens pressure

Smithe's earlier *Cyber Kittens* defines a categorical cybernetic system as a dynamical realisation of a generalized open game and explicitly builds on Bayesian updates composing optically.

Primary source:

- Toby St. Clere Smithe, *Cyber Kittens, or Some First Steps Towards Categorical Cybernetics*, arXiv:2101.10483  
  https://arxiv.org/abs/2101.10483

This further narrows any novelty claim around:

> “bidirectional observer/controller dynamics can be modeled categorically.”

That territory is already occupied.

The Semantic Optics contribution, if any, has to be in its **specific semantic decomposition and cross-family empirical application**, not that generic discovery.

---

# 13. Revised moonshot

The original moonshot:

\[
\mathsf{TLICAOptics}
\simeq
\mathsf{Optic}
\]

is now probably the wrong target.

A more plausible ladder is:

### M1 — realization

Construct:

\[
F:
\mathsf{TLICAOptics}
\to
\mathbf{Para}(\mathbf{Optic}).
\]

### M2 — full/faithful embedding

Prove \(F\) full and faithful on a declared subcategory.

### M3 — essential image

Characterize exactly which categorical-cybernetic systems satisfy TLICA's semantic constraints.

### M4 — equivalence on that image

\[
\mathsf{TLICAOptics}_0
\simeq
\mathsf{CyberOptics}_{\mathrm{TLICA\text{-}admissible}}.
\]

### M5 — Yoneda/restricted-Yoneda certification

Show that the equivalence preserves complete compositional profiles and that practical probe subcategories recover the distinctions claimed by TLICA.

This is both stronger and less tautological.

---

# 14. The granularized-instantiation hypothesis, revised

The phrase:

> “TLICA is a granularized instantiation of categorical optics”

should now become:

> **TLICA Semantic Optics may be a semantically constrained, observer-indexed instantiation of parametrised categorical optics / categorical cybernetics, where TLICA supplies a finer internal factorization of agent parameter state and epistemic probe structure than the generic categorical framework requires.**

Symbolically:

\[
\boxed{
\mathsf{TLICAOptics}
\stackrel{?}{\simeq}
\mathsf{CyberOptics}^{\mathrm{TLICA}}
\subseteq
\mathbf{Para}(\mathbf{Optic}).
}
\]

This is the current preferred moonshot.

---

# 15. New falsifiers introduced by the prior art

The bridge weakens if:

1. TLICA's observer state cannot be made into composable parameter objects;
2. TLICA updates violate reparametrisation/coherence laws required by \(\mathbf{Para}\);
3. the semantic distinction between source, probe, identity, and contact adds no held-out predictive value beyond generic parametrised optics;
4. every TLICA-specific object can be absorbed trivially into parameter state without changing any theorem or observable discriminator;
5. a different categorical-cybernetic formalism maps the phenomena more naturally with less bespoke machinery.

The last two are especially important.

---

# 16. Current prior-art-adjusted verdict

### Established externally

- categorical cybernetics already formalizes bidirectional environment/controller interaction;
- parametrised optics are its central construction;
- parameters, residuals, private state/memory, feedback, and reparametrisation are existing machinery.

### Still open

- whether TLICA observer state can be typed naturally as those parameters;
- whether TLICA contributes nonredundant semantic constraints;
- whether restricted Yoneda/density genuinely maps onto toolkit/probe adequacy;
- whether a full/faithful TLICA embedding exists;
- whether any categorical equivalence can be earned.

### Research consequence

The program has become **harder to claim as novel and easier to make rigorous**.

That is a net improvement.
