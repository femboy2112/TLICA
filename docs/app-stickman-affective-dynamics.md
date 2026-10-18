# Stickman

[← Applications overview](applications.md) · [Wiki home](README.md) · Source: [`applications/stickman_affective_dynamics_v0_1_0.md`](../applications/stickman_affective_dynamics_v0_1_0.md) · **v0.1.0 · draft · UNVERIFIED**

> **Draft (v0.1.0).** An application-level *proposal*: take TLICA's account of affect and
> give its non-reflective, bodily layer an **equation of motion** — then ask how much of
> ordinary "common sense" falls out of that motion before any thinking is added. It adds
> **no new foundation primitive** and does not touch the frozen core. The human and
> affective mechanisms it describes are the author's **conjectured model**, not established
> science. Its central thesis and its novelty are explicitly held at **UNVERIFIED**: no
> human dataset has been fit, no cross-population invariance has been shown, and no claim of
> originality is made.

> **What it is careful NOT to claim.** Not that emotion literally has mass. Not that the
> executable toy on the branch is evidence about real people. Not that the fancier
> "inertial" model beats the plain one — it does not, yet. Not that biology explains all
> behavior. The strongest honest status here is *"the discriminator exists,"* observed once,
> in a synthetic toy.

---

## The one-sentence version

Picture a stick figure. Not a mind with plans and principles — just a living body that a
situation reaches out and *shoves*. The shove changes how the body feels, which changes
what it's ready to do, which tips it into one coarse kind of action. The paper's own
governing sentence is blunt about this:

> **Stickman is pushed before it chooses.**

Stickman is a deliberately **lossy** model of a human being. Its job is *not* to represent
personality, deliberation, moral reasoning, long-horizon planning, or reflective agency. It
keeps only the substrate-mediated affective dynamics needed to answer one narrow question:

> Given a minimally specified living human substrate and a context that couples to it, what
> coarse response-shape should occur most often across ordinary human populations?

> **In plain terms —** Most models of a person start with a little reasoner inside and ask
> what it decides. Stickman starts one floor down, with the body getting pushed around, and
> asks how far you can get *before* you have to add a reasoner at all.

---

## Running Differentiated Affect backward

Stickman is built on top of one existing TLICA application: [Differentiated
Affect](app-differentiated-affect.md). That paper's key move is that emotions are not
primitive labels but **configurations** — structured operations on the lived "I" that
perturb things like salience, action-readiness, profile stability, and embodied state. It
sorts affect into five clusters: connection / extension, self / reflexive evaluation,
threat / preservation, boundary / encounter, and embodied / somatic.

*Differentiated Affect* runs forward: **TLICA structure → affect configuration → named
affect family** ("that configuration is what we call fear"). Stickman asks for the reverse,
operational program:

`context → structural perturbation → affective trajectory → action-readiness → response basin → colloquial gloss`

The final gloss — "obviously, pull your hand away" — is **not** part of the body's dynamics.
It is our *linguistic compression* of the trajectory that usually happens. The empirical
content lives in the middle arrows, never in the catchphrase at the end.

> **In plain terms —** "Common sense" might not be a library of propositions everyone has
> memorized. It might be the *shadow in language* cast by what a very small dynamical animal
> reliably does when the world leans on it. The paper's framing research question is exactly
> that: **how much ordinary common sense is the linguistic shadow of population-stable
> attractors in substrate-mediated affective dynamics, before reflective agency is added?**

### The bridge: action-readiness

The foundation already states that somatic (bodily) processing keeps features like
intensity, valence, **action-tendency**, and broad affective tone while losing propositional
detail. That observation is the bridge from a *taxonomy of feelings* to a *mechanics*.
Instead of reading "fear = an emotion label," Stickman asks whether a fear-like
configuration can be a **region of state space whose flow biases the body toward a family of
coarse actions**. Anger-like boundary activation becomes a deformation of response-readiness,
not a dictionary entry.

Stickman does not import the whole taxonomy. It takes a **primitive candidate subspace** —
embodied, threat, boundary, and primitive extension/attachment affects — and initially
*excludes* the self/reflexive cluster (guilt, shame, articulated embarrassment), because
those can require self-modeling or learned meaning that Stickman is specifically designed
not to contain. That the primitive subspace is the right cut is marked **Conjectured**, not
settled; which pieces survive has to be *earned experimentally*, not chosen because they
sound psychologically natural.

---

## State, context, and the refusal to name axes

Stickman's fast state is written `q`. Slower parameters `θ` collect gains, damping,
thresholds, learned substrate associations, and developmental state — ordinary biological
variation. Crucially, `θ` is **not personality in disguise**; it is the parameterization
needed so that normal human variation does not get promoted to a brand-new state variable
every time.

At v0.1.0 the paper deliberately **refuses to canonize a coordinate chart** for the state
space. Naming five psychologically attractive axes and declaring them minimal would quietly
defeat the project. Which coordinates actually matter is a **model-selection problem**, to be
discovered by ablation — a variable earns its place only if removing it destroys the model's
ability to match real response patterns.

### Context is forcing, not instruction

The world `w` is richer than Stickman. An upstream perceptual map `Π_perc` turns world state
into a **perceived, substrate-relevant context** `c`. Stickman receives `c`, not raw reality,
and `c` becomes a generalized forcing on the state.

This split is load-bearing. If a complicated social scene arrives already labeled
"dangerous," Stickman is allowed to model what *perceived* danger does to the body. It does
**not** thereby explain how the scene got classified as dangerous in the first place — and if
the context parser has to secretly encode "what the person will do," then Stickman has become
a renamed lookup table (that is failure mode **F6**, below).

> **In plain terms —** Keep two jobs separate. Figuring out *that* something is a threat is
> hard perception-and-meaning work Stickman doesn't claim to do. Stickman only claims the
> next step: once the body registers "threat," here is how it moves.

---

## Two rival equations of motion

The paper proposes two dynamical families and insists the *simpler one wins by default*.

**The conservative null — overdamped flow.** A first-order, dissipative, noisy system: the
state slides downhill on an affective/regulatory "potential" `V`, pushed by context forcing,
jostled by biological noise. In compact form, `Γ·q̇ = −∇V(q;c) + B·u_c(t) + Σ·ξ(t)`. This is
deliberately close *in spirit* to the foundation's own relaxational baseline law
`ḃ = γ(f − b)` — but Stickman's `q` is **not** silently identified with the foundation's
baseline `b`, field-reading `f`, or identity-coupling `ρ`. (See [the self in
motion](the-self-in-motion.md) for the driven baseline and slack that Stickman borrows the
*spirit* of while keeping its own objects.)

**The stronger candidate — dissipative Lagrangian mechanics.** The author's motivating
hunch is that affect may have enough persistence and directional carry to warrant a
mechanics-style treatment. The weakest serious version is **Lagrange–d'Alembert with Rayleigh
dissipation**, which for constant coefficients reduces to a familiar damped-oscillator shape:

`M·q̈ + Γ·q̇ + K·q = B·u_c(t) + Ξ(t)`

Here `M` is the dangerous term. It is **not literal kilograms** and not a claim that emotion
has physical inertia. It is a *phenomenological* second-order parameter standing for any
persistence a first-order state of the same dimension can't capture. The paper's own words:
`M` is **"guilty until proven useful."** And the overdamped null is simply this model's
limit when inertia is negligible (`M·q̈ ≈ 0`), so Stickman never has to decide up front which
story is true — the simple one is nested inside the fancy one.

> **In plain terms —** The real question is never the metaphysical "does emotion have mass?"
> It is the predictive one: **does adding an inertial coordinate give a lower-complexity or
> better-generalizing fit than a plain overdamped model with the same capacity?** If not, you
> set `M = 0` and throw the mechanics away.

---

## The toy: a discriminator, nothing more

The branch ships a small standard-library program,
`research/stickman_affective_dynamics_2026-09-26/stickman_dynamics_demo.py`, and it does
**exactly one thing**. Give both models a single positive forcing pulse (on for a moment,
then off). The matched first-order relaxation rises, then relaxes monotonically back down
and **never crosses to the other side**. A chosen underdamped second-order system can
**overshoot and cross the baseline** after the pulse ends.

The executed run on 2026-09-26 recorded **7/7 checks passed**, with:

- overdamped peak ≈ `0.2163016047`, post-pulse minimum ≈ `7.14063×10⁻⁵`, **no** post-pulse
  sign reversal;
- inertial peak ≈ `0.3508772102`, post-pulse minimum ≈ `−0.2361654441`, sign reversal
  **present**, first crossing to the opposite side at `t = 2.106`.

That yields a **precommitted discriminator**: if, after controlling for delayed external
forcing, hidden slow state, and measurement lag, real affect trajectories show reproducible
overshoot/phase-reversal structure that a matched first-order rival cannot reproduce at equal
predictive complexity, the inertial term earns its keep. Otherwise it is dropped.

> **In plain terms —** A finite toy can prove that the two models are *tellable apart* in
> principle. It cannot say which one humans actually are. The source states this flatly, and
> so does this page: the 7/7 result is **Observed in a synthetic witness only — no human
> inference.**

---

## Common sense, with an honest "no answer"

For a reference population, each admissible parameter setting and starting state produces a
trajectory, which projects to a coarse response. Average over the population and you get a
**response distribution** `P(r | c)`: how often each coarse response shows up.

Common sense is then defined as the **modal (most common) response** — but *only when it
dominates*. Let `r₁` be the top response and `Δ` be its lead over the runner-up. If `Δ`
clears a predeclared margin `δ_CS`, Stickman emits `r₁` as the common-sense answer. If it
doesn't, Stickman emits `⊥` — **no dominant common-sense response**.

That abstention is the point. The model must be allowed to say *ordinary people genuinely
divide here*, rather than hallucinating a consensus that isn't there. (This is a **definition**,
not a claim that anyone consciously computes population statistics in their head.)

> **In plain terms —** "Common sense" gets a precise, local meaning: the response most normal
> people's bodies tip into under this context — *and only when most of them really do agree*.
> Where the crowd splits, the honest output is "there is no common-sense answer here."

---

## Population-invariant without pretending we're identical

"Population-invariant" must **not** mean every culture, age band, and physiology gives
identical numbers. The defensible target is **conditional structural invariance**: once you
condition on the biologically relevant state and substrate-relevant context, the *population
label* should add little predictive information — informally, `I(R ; P | X_bio, c) ≈ 0`.
A response belongs in **core Stickman** only if it passes that test on held-out data.
Population-specific thresholds and gains are explicitly allowed; what's claimed is a *shared
structure with varying parameters*, implemented hierarchically. If population membership stays
strongly predictive after the controls, the effect isn't discarded — it just lives **outside**
the invariant core. This is marked a **Conjectured operational definition**.

A categorical restatement (Stickman as Markov kernels in **Stoch**, context segments
composing, a behavioral readout kernel) is offered as a *valid representation* whose extra
explanatory payoff is **Conjectured** — the source bars "categorical ornament" that buys no
new composition, invariant, or test.

---

## The scope ladder — and the walls

Stickman is meant to start where the body's signal is loudest and move outward only after
passing held-out probes. For how these tiers sit against TLICA's A/B/C development picture,
see [modes of development](modes-of-development.md).

- **Tier 0 — reflex arcs:** nociceptive withdrawal, blink/startle, postural correction,
  orienting to sudden salient stimuli.
- **Tier 1 — interoceptive regulation:** air hunger, hunger/thirst, thermoregulation, sleep
  pressure, bladder/bowel urgency.
- **Tier 2 — acute defensive affect:** imminent threat, looming collision, peripersonal-space
  invasion, acute pain, sudden loss of stability.
- **Tier 3 — primitive social-affective coupling:** abrupt boundary violation, proximity
  threat, protection of a strongly routed attachment target, simple affiliative repair. *This
  is where the project gets interesting and dangerous to overclaim* — success in Tiers 0–2
  does **not** license Tier 3.
- **Tier 4 — explicitly excluded from base Stickman:** articulated guilt/shame, complex
  jealousy, explicit norm reasoning, strategic deception, reputation management, long-horizon
  planning, counterfactual self-narrative, moral justification. These need richer structure
  and are candidates for *StickmanPlus*, not the biological core.

The choice of reflex and interoceptive tiers as the calibration ground is **Corroborated** as
a research-design choice by established external literatures (interoception/allostasis,
withdrawal reflex, defensive behavior, sleep loss, air hunger) — but the *exact Stickman
mapping onto them remains UNVERIFIED*.

> **In plain terms —** Start with "you yank your hand off a hot stove," where the body plainly
> does the work. Earn your way up one rung at a time. The moment the model needs culture,
> language, or relationship-stories to predict a response, you've found the wall where
> reflective cognition becomes necessary — and finding that wall cleanly is itself a result.

### StickmanPlus, and where Mode B actually begins

If base Stickman fails in a systematic way, **StickmanPlus** adds the *smallest* model that
earns itself: first a one-step action→outcome projection ("move away → threat decreases"), then
one more composition. Neither is automatically [Mode B](the-self-in-motion.md). TLICA reserves
Mode B for **reflexive meta-reasoning** — the "I" taking its *own* response-generating structure
as an object ("why am I being pulled toward this response?") and reweighting it. Calling every
prediction "Mode B" would be exactly the kind of semantic drift the archive's [glossary](glossary.md)
and [two-layer](two-layers.md) discipline exist to prevent.

And there is **no slack variable** in base Stickman. Fatigue, sleep deprivation, hunger, and
pain change the trajectory *directly*, by moving the substrate state — not through a
control-budget term. If a later layer needs slack to predict reflective override, that belongs
in the added agency layer, not the body.

---

## How it fails (on purpose)

The paper lists seven ways the program *fails usefully*, because a model that can't fail
explains nothing:

- **F1 — No stable minimal quotient:** prediction keeps needing an ever-growing list of
  semantic/cultural variables even in primitive contexts.
- **F2 — Population invariance fails:** population label stays strongly predictive after the
  controls; the "core" response gets demoted to population-specific structure.
- **F3 — Affect adds nothing:** a direct stimulus→response model matches or beats the
  affective-state model on held-out data.
- **F4 — Lagrangian inertia loses:** the overdamped or generic model predicts as well at lower
  complexity; set `M = 0`.
- **F5 — Basins are post-hoc:** response classes invented *after* seeing the data explain
  nothing; the quotient must be frozen first.
- **F6 — The context parser does all the work:** `Π_perc` has to encode the answer; Stickman is
  a renamed lookup table.
- **F7 — Social extension fails:** it works for reflex/interoception and breaks on social
  "common sense." *That outcome is acceptable* — it locates the boundary.

The minimum empirical program (Stages A–E) would calibrate on established low-level responses,
compare four preregistered rivals on **held-out** prediction (direct stimulus→response,
overdamped Stickman, inertial Stickman, and a matched-capacity generic state-space model), test
transport across a second domain, and only then, carefully, touch low-stakes social cases. None
of this has been run on human data yet.

---

## Claim-status summary

The source keeps a strict ledger. Carried faithfully:

**Settled within the paper's own boundaries (Disclosed / Derived / Observed):**
- *Differentiated Affect* treats affect as structural configuration including action-readiness;
  the foundation supplies substrate mediation and a driven dissipative baseline dynamics; and
  action-priority dynamics under pressure are an explicitly **open** application problem the
  foundation itself names — all **Disclosed from repository text**.
- Inside the proposed mathematics: the overdamped model is a limiting case of the second-order
  candidate; context-conditioned transitions compose as Markov kernels; a response-preserving
  quotient and a margin-gated "common sense with abstention" are well-defined — **Derived /
  Disclosed as definitions**.
- The pulse discriminator (first-order no reversal; chosen underdamped system reverses sign,
  7/7 checks) is **Observed in the executed finite toy only**, synthetic parameters, **no human
  inference**.

**Conjectured (the author's model, not established fact):**
- that the primitive (embodied/threat/boundary/attachment) subspace is the right minimal cut;
- that the overdamped null and the conditional-invariance criterion are the right methodological
  choices;
- the load-bearing thesis that a substantial fraction of colloquial common sense is
  substrate-affective rather than reflective.

**UNVERIFIED:**
- that human affect needs an inertial term (the Lagrangian candidate is **not privileged** over
  the overdamped null);
- that a stable, low-dimensional, cross-population Stickman quotient exists;
- that broad common sense can be recovered from it; that primitive social responses stay inside
  the substrate-only closure;
- and **novelty** — Stickman is not established as new relative to control-theoretic allostasis
  models, active inference, appraisal dynamics, or computational ethology, and *no novelty claim
  is made*.

The honest overall position, in the source's words: the **formal research object is coherent and
cold-startable**, the **main empirical thesis remains UNVERIFIED**, and the toy has paid only
"one small piece of truth debt" — it shows the inertia question has a concrete, falsifiable
signature in *one* controlled construction.

> **Foundation untouched.** Stickman is an application-level draft (author: Leah, AI-assisted
> formulation). It adds no coordinate, rewrites none of TLICA's three coordinates, and does not
> alter the meaning of Mode A/B/C. The frozen foundation (v5.5.2) is **untouched**.

---

*Full manuscript: [`applications/stickman_affective_dynamics_v0_1_0.md`](../applications/stickman_affective_dynamics_v0_1_0.md).
Research support package — formalism, probe ladder, claim ledger, and the executable witness:
[research/stickman_affective_dynamics_2026-09-26/](../research/stickman_affective_dynamics_2026-09-26/README.md).
Donor theory: [Differentiated Affect](app-differentiated-affect.md).*

If the program ever works, a surprising amount of "what any normal person would obviously do"
may turn out not to be a library of propositions at all — but the linguistic shadow cast by a
very small dynamical animal.
