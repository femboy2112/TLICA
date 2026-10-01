# Probe Program — Semantic Optics

**Status:** preregistration-style research plan. No human or empirical probe in this file has been run.

The program is designed to split:

- interface effects;
- observer/controller effects;
- feedback effects;
- categorical-representation artifacts;
- genuine TLICA-specific structure.

---

# P0. Acceptance criteria before data

For every probe declare in advance:

- object domain;
- task boundary \(\tau\);
- base optic/interface;
- observer state manipulation;
- response measure;
- proper-state invariant;
- pass;
- fail;
- ambiguous;
- mutation controls;
- provenance.

No fitted example may also serve as the confirming holdout.

---

# P1. Base-optic / observer-state factorial

## Question

Can the effects of interface and observer state be separated?

Construct:

\[
\omega_1,\omega_2
\]

and:

\[
\Theta_1,\Theta_2.
\]

Run all four cells:

\[
(\omega_1,\Theta_1),
(\omega_1,\Theta_2),
(\omega_2,\Theta_1),
(\omega_2,\Theta_2).
\]

Measure reconstructed object and response.

## PASS

Both:

- interface manipulations matter;
- observer state matters;

and the full cell matrix is needed to predict outcomes.

## FAIL for TLICA fiber necessity

Observer-state condition adds no held-out predictive information once the base optic is known.

## AMBIGUOUS

Observer state matters only because it changed exposure \(A\), confounding optic and controller.

---

# P2. Residual-invariance mutation

## Question

Does the semantic implementation respect the categorical optic coend equivalence?

Construct two residual encodings related by a declared residual morphism:

\[
f:M\to N.
\]

Ensure they represent the same optic.

Close both with the same controller:

\[
c.
\]

## PASS

Closed outputs agree exactly / up to declared target equivalence.

## FAIL

The implementation leaks residual encoding into external semantics.

This kills the claim that it factors through the optic quotient.

---

# P3. Composition test

## Question

Does multi-stage semantic composition agree with categorical optic composition?

Build:

\[
\omega_1,
\omega_2,
c.
\]

Compare:

1. compose optics first, then close;
2. explicitly execute the two stages.

## PASS

Outputs agree on every finite fixture cell.

## FAIL

The proposed bridge is not functorial / not compositional.

This is a load-bearing failure.

---

# P4. Faithfulness counterexample search

## Question

Does the bridge collapse distinct TLICA morphisms?

Enumerate a finite \(\mathsf T_{\mathrm{toy}}\).

For:

\[
f\neq g,
\]

search for:

\[
F(f)=F(g).
\]

## PASS for faithfulness

No collisions over the exhaustive finite domain.

## FAIL

Explicit collision found.

Then localize which TLICA distinction the base optics forgets.

---

# P5. Fullness counterexample search

Enumerate target optic morphisms:

\[
h:F(X)\to F(Y).
\]

Search whether every \(h\) has a TLICA preimage.

## PASS

Every target morphism has a preimage in the declared finite domain.

## FAIL

Find the smallest optic behavior TLICA cannot realize.

This may indicate either:

- substantive TLICA constraint;
- incomplete TLICA formalization.

---

# P6. Essential-image test

Enumerate optic objects in the finite target.

Classify:

- represented;
- isomorphic to represented;
- outside essential image.

A proper essential image would support the “granularized subfamily” interpretation without requiring global equivalence.

---

# P7. Restricted-Yoneda collision

## Question

Can current probes collapse distinct objects?

Choose a probe family:

\[
\mathcal P.
\]

Compute:

\[
N_{\mathcal P}(X)
=
\mathcal C(i-,X).
\]

Search for:

\[
X\not\cong Y
\]

but:

\[
N_{\mathcal P}(X)
\cong
N_{\mathcal P}(Y).
\]

The included finite demo already supplies one construction-level witness.

---

# P8. Lamp search

Starting from a restricted-Yoneda collision, search for minimal additional probe set:

\[
\mathcal L
\]

such that:

\[
N_{\mathcal P\cup\mathcal L}(X)
\not\cong
N_{\mathcal P\cup\mathcal L}(Y).
\]

Optimization target:

\[
\min|\mathcal L|
\]

or minimal probe cost.

This is the formal “name the lamp” program.

---

# P9. Density test

For finite categories, exhaustive-check whether the restricted nerve is full and faithful.

Do not infer density from point separation alone.

Need:

- faithfulness on morphisms;
- fullness of natural transformations.

If finite, enumerate every relevant natural transformation.

---

# P10. TLICA fiber ablation

Take the observer state bundle:

\[
\Theta
=
(H,B,\mathrm{Foc},\kappa,\phi,\sigma,\rho,\mu,\tau_O,\ldots).
\]

Ablate one family at a time.

Examples:

\[
\Theta\setminus\sigma,
\]

\[
\Theta\setminus\mu,
\]

\[
\Theta\setminus\rho.
\]

Evaluate held-out predictive/discriminative change.

## Goal

Find the smallest decoration that improves prediction beyond the bare optic/controller baseline.

No component is protected from deletion.

---

# P11. Source-map vs exposure discriminator

Hold available evidence fixed.

Manipulate only source attribution.

Question:

> can \(\sigma\)-related changes alter reconstruction/response without changing the base exposure optic?

If yes, that supports source state living in the controller/fiber rather than solely in \(l\).

---

# P12. Probe-availability vs evidence discriminator

Hold evidence and source attribution fixed.

Change which checking operations are available.

If interpretation diverges only after probe access changes, this is evidence for a \(\mu\)/toolkit contribution rather than an exposure contribution.

---

# P13. Identity-coupling discriminator

Hold evidence, source map, and probe access fixed.

Manipulate or stratify by declared commitment relevance.

Measure:

- update resistance;
- search effort;
- response policy;

separately from accuracy.

This tests whether \(\rho\)-like structure changes controller dynamics without being treated as truth evidence.

---

# P14. Observer-update timescale

Hold content family fixed.

Vary presentation/update frequency.

Test Semantic Wake prediction:

\[
\tau_A/\tau_O.
\]

Measure:

- reconstruction lag;
- apparent inconsistency;
- trust updates;
- rule/escalation responses.

This is an application probe on top of the optic framework.

---

# P15. Optic-pure steering

Declare invariant:

\[
R_\tau.
\]

Construct interventions \(u\) such that:

\[
R_\tau(F(x,u))=R_\tau(x).
\]

Search for changes in:

\[
\Omega_j(F(x,u)).
\]

This directly tests “optics changed while the declared task-relevant reality did not.”

Negative control:

interventions that change neither invariant nor reconstruction.

Positive control:

intervention that changes both.

---

# P16. Reality change without optics change

Construct:

\[
x,x'
\]

with:

\[
R_\tau(x)\neq R_\tau(x')
\]

but:

\[
\Omega_j(x)\equiv_\tau\Omega_j(x').
\]

This is the inverse problem.

It tests whether the interface is blind to a load-bearing proper-state difference.

---

# P17. Bayesian baseline deviation

For a domain with a defensible Bayesian generative model:

1. compute Bayesian inverse;
2. measure actual/experimental observer reconstruction;
3. compare with TLICA-parameterized reconstruction.

Use:

- calibration;
- predictive loss;
- held-out evidence;
- qualitative error class.

Do not call a non-Bayesian response irrational by definition.

---

# P18. Natural-transformation deviation

If baseline and TLICA controller families are functors:

\[
C_0,C_T:\mathcal I\to\mathcal E,
\]

test whether a natural transformation:

\[
\eta:C_0\Rightarrow C_T
\]

exists.

If only pointwise mappings exist but naturality fails, “TLICA deviation” is not compositional in the proposed sense.

---

# P19. Dynamic fiber state

Test whether:

\[
\Theta_{t+1}
\]

depends on interaction history in a way that cannot be represented by a static fiber.

If yes, upgrade to a dynamical/indexed-state model.

Potential specimen:

- reputation learning;
- semantic wake;
- repeated comedy audience calibration;
- political/media repeated exposure.

---

# P20. Cross-family holdout

Fit the abstract formalism using only:

- cinema;
- institutions;
- semantic wake.

Hold out:

- reputation;
- comedy;
- politics.

Then predict what the optic/fiber decomposition says the failure loci should be.

If the mapping must be rewritten domain-by-domain, the umbrella is too weak.

---

# P21. Hostile cross-family case

Actively seek a domain where:

- another entity interprets a situation;
- consequences follow;

but:

\[
S\to M\otimes A,\quad M\otimes A'\to S'
\]

is an obviously poor decomposition.

A strong counterexample is more valuable than another compatible example.

---

# P22. Tautology detector

Try two base categories:

## Minimal independent base

Objects/morphisms defined without TLICA.

## TLICA-saturated base

Objects contain full TLICA state.

If equivalence only succeeds in the saturated construction, downgrade the result to **encoding**, not explanatory equivalence.

---

# P23. Yoneda-equivalence anti-cheat suite

A claimed equivalence must provide:

- explicit object map;
- explicit morphism map;
- identity preservation;
- composition preservation;
- full;
- faithful;
- essential-surjectivity witness or bounded essential-image declaration;
- inverse/quasi-inverse when claimed;
- natural isomorphisms;
- probe-profile correspondence.

No prose substitute.

---

# P24. Mutation controls

For any finite bridge implementation, include mutants:

1. swap two observer decorations;
2. delete residual;
3. leak residual into exposed evidence;
4. break backward update;
5. break identity;
6. reverse one composition;
7. collapse two distinct probes;
8. add a fake probe that carries no new information.

The test suite should kill every semantic mutant designed to violate the claimed law.

---

# P25. Parametrised-optic bridge

Construct a finite parameter category:

\[
\mathcal M_\Theta
\]

independently of the desired equivalence.

Define TLICA observer/controller instances as parametrised optics in:

\[
\mathbf{Para}_{\circledast}(\mathbf{Optic}).
\]

Test:

- parameter composition;
- reparametrisation;
- identity;
- monoidal combination where claimed;
- whether the same TLICA distinction survives lawful reparametrisation.

## PASS

The mapped observer dynamics compose and reparametrise according to the existing categorical-cybernetics laws.

## FAIL

A minimal TLICA update cannot be represented without violating the \(\mathbf{Para}\) typing/coherence.

---

# P26. Generic-cybernetics ablation

Fit/predict with a generic parametrised-optic model first.

Then add TLICA-specific distinctions:

- source-map state;
- probe availability/closure;
- identity coupling;
- toolkit-relative truth/pathway state.

Use held-out cases.

## PASS for nonredundant TLICA refinement

The TLICA-typed model improves declared held-out discrimination/prediction or correctly localizes failures the generic model merges.

## FAIL

The generic parametrised-optic state predicts equally well and the TLICA decomposition adds no operational distinction.

This is now the highest-value prior-art-adjusted discriminator.

---

# P27. Reparametrisation/gauge test

Choose two observer parameterisations believed to describe the same operational state.

Construct:

\[
r:\Theta'\to\Theta.
\]

Test whether the reparametrised optic induces the same declared external behavior.

If yes, candidate gauge redundancy.

If no, the parameter difference is Yoneda/behavior visible or the proposed reparametrisation is invalid.

---

# P28. Active-inference comparator

Where a defensible generative model exists, compare:

1. generic Bayesian lens / statistical-game baseline;
2. generic parametrised-optic cybernetic baseline;
3. TLICA-typed parameter model.

Do not interpret “best predictive fit” as ontology proof.

The goal is to determine what, if anything, TLICA contributes beyond existing compositional inference/control machinery.

---

# P29. Claim promotion ladder

A result can move from:

**UNVERIFIED**

to:

**Observed (finite construction)**

only after the script runs.

It can move to:

**Disclosed (formal)**

only with a proof in the declared model.

It can move toward:

**Corroborated**

only after:

- independent implementations;
- provenance separation;
- held-out domains;
- primary-source prior-art audit.

No same-model rerun counts as independence.
