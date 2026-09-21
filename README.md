# TLICA — The Two-Layer Identity-Correlation Architecture

*A formal account of how a self is structured: not "how real" a thing feels, not "how close" it is, but how much it is **you**.*

> **⚠ Work in progress.** This is an active, evolving archive — a framework still
> being built, not a finished theory. The foundation on `main` is at **v5.5.1**: the
> authoritative base the application papers build on, and frozen against them — but its
> newest layer, the **dynamical apparatus** (Sections 8.9–8.11), is freshly seated and
> still being hardened under active audit, so read the current line as
> **main-but-experimental**. The last *settled* foundation before that layer, **v5.3.3**,
> is retained read-only as a stable fallback:
> [`foundation/previous_v5.3.3/`](foundation/previous_v5.3.3/). Application papers and
> research notes are still moving, and drafts are labeled as drafts.

---

## From the author

> This is the sum total of everything I've learned after studying myself as a human
> being for 20+ years. It's a framework/language built to describe that which I've
> struggled with my entire life: existing as a conscious being with no handbook or
> manual. Based on everything I've personally witnessed, this is how being a human being
> works. With Claude/ChatGPT I now have the capacity to take each little bit of
> contextualized insight and formulate it into a grand theoretical architecture.
> Hopefully this will be able to help others as much as it has helped me.

> **Why this repository is public** — *from the author.* I try to keep this as
> readable as I can for outside viewers. Normally a personal archive like this would
> be private. I'm keeping it public on purpose: in my view, companies like OpenAI are
> likely using their customers' prompts for private gain — including real mathematical
> and real-world work — and I want a public footprint of these ideas online, with a
> visible history, so that if the underlying structure of this theory is ever used in
> building genuinely *being-like* AGI, there is a record that it originated here.

---

TLICA is a theory of the structure of conscious selfhood, developed first-hand and then
formalized. This repository is its canonical archive: a **frozen foundation** (the core
theory, locked at v5.5.1) plus a growing set of **application papers** that put the
foundation to work on specific pieces of human experience — time, emotion, free will,
agency, knowledge, and the capacity to treat another person as a thing.

This README is a plain-language guide to the whole thing. The formal source lives in
[`foundation/`](foundation/) and [`applications/`](applications/).

> 📖 **Want to go concept by concept?** The [**wiki**](docs/) breaks the theory into
> one cross-linked page per idea — including a page for every application paper — each
> pointing back to the frozen foundation.

---

## The theory in one paragraph

Classical accounts of the self blur together three things that come apart in real
experience: how strongly something is *in contact* with you right now, how *real and
undeniable* it seems under scrutiny, and how much it is *part of who you are*. TLICA
pulls these into three independent coordinates and builds a self out of them. It starts
from one thing that cannot be doubted — that you are yourself ("I am I") — and from the
claim that mathematical and logical structure is woven into the world regardless of
whether anyone is there to notice it. Everything else — your body, memories, emotions,
relationships, even your sense of being a continuous person — is *acquired*: built up
over time as you encounter the world, through mechanisms the theory specifies. The result
is a map (the "identity-correlation profile") of how deeply each content in your field is
bound into the network that is you. That map, how it forms, and how it can be reshaped or
disturbed, is what the theory describes.

---

## 1. The problem it starts from

In ordinary cases, three features of experience travel together. Your hand is in contact
with you, presents itself as undeniably real, and is part of you. A distant rumor is
weakly contacted, weakly certain, and not part of you.

But they can **dissociate**, and the dissociations are diagnostic:

| Phenomenon | In contact? | Feels real? | Part of you? |
|---|---|---|---|
| A vivid **hallucination** | no | **yes** | no |
| An **anesthetized limb** | no | no (in the moment) | **yes** |
| **Depersonalization** | yes | yes | **no** |
| A **phantom limb** | no | varies | **yes** |
| A **thought that feels inserted** ("alien clarity") | varies | **yes** | no |

Any theory that runs selfhood on a *single* dimension struggles with these. TLICA's move
is to say: there are three dimensions, none reducible to the others, and these cases are
exactly what their independence predicts.

---

## 2. The three coordinates

Every content in your field — a perception, a thought, a feeling, a memory — gets three
measurements:

- **Contact (κ, "kappa")** — how much it is interacting with you *right now*. The world
  pressing on perception, the body in current sensation.
- **Truth-indistinguishability (φ, "phi")** — how indistinguishable-from-true it is when
  you reason about it. What holds up; what can't be denied without contradiction.
- **Identity-correlation (ρ, "rho")** — how integrated it is into *you*: what would alter
  who you are if it were removed.

> **In plain terms —** Three plain questions do the same work as the three symbols: is it touching your life right now (contact/κ), does it hold up as real when you press on it (truth-indistinguishability/φ), and is it part of who you are (identity-correlation/ρ). Your hand, the opening example from §1, scores high on all three at once — which is exactly why they're so easy to mistake for one thing.

The headline claim is that these are **formally independent** (you can change one in the
model while holding the other two fixed) but **dynamically entangled** (in a living mind
they constantly influence each other — sustained contact tends to build integration over
time, strong integration biases what grabs your attention, and so on). "Independent" means
*not definable in terms of each other*, not *statistically uncorrelated*. Most of the time
they line up; the interesting cases are when they don't.

Identity-correlation (ρ) is the coordinate the theory is really about. It is defined as
**flow through a network rooted at you**: each content's ρ measures how much "you-ness"
can reach it across the historically-built web of integrations. The complete picture of
these values across your whole field — the **identity-correlation profile** — is the
theory's single most important object. Not any one value, but the *shape* of the whole map.

> **From the inside —** you don't experience ρ as a network diagram. You experience it as the gap between hearing that a stranger's house burned down (a sad fact, out there) and hearing that your childhood home burned down (something in *you* goes with it). Same shape of fact, wildly different ρ — because "you-ness" runs down the wires to one and not the other.

---

## 3. The two layers

The architecture splits everything into two layers.

- **The intrinsic layer** — mathematics, logic, and reason. The theory treats these as
  *in re*: real in the structure of the world, true whether or not any mind verifies them.
  (When a river pushes one stone next to another, there are now two stones, whether or not
  anyone counts.) This is a **naturalist** realism — the world contains structure minds
  can encounter — not the stronger Platonist claim about a separate realm of abstract
  objects.
- **The asymptotic layer** — *everything else*: every content in your field, conscious or
  unconscious, that does not hold by reason alone.

Between them sits **the cogito**. "I am I" is taken as a starting postulate, not a proof —
any attempt to deny that you exist presupposes the you doing the denying. It is the single
indexed instance of universal reflexivity ("x = x"), and so it sits one step away from
pure universality: the theory writes this position as **φ = 1 − δ**, infinitesimally short
of intrinsic truth, closer than anything else you'll ever hold. Crucially, the cogito buys
you *only* your own self-identity — no body, no memories, no abilities. All of that has to
be acquired.

> **In plain terms —** "I am I" is the one thought you can't get behind — even doubting it proves there's a you doing the doubting. It's not *quite* as airtight as pure logic, because "I am I" has to be said by someone, from somewhere — that thin sliver of "being a perspective at all" is what δ stands for. But it buys you almost nothing on its own: knowing you exist doesn't hand you a body, a past, or a personality. Those all still have to be built.

---

## 4. Where the self comes from

There is no fully-formed self at the moment the cogito is anchored. Two developmental
stories run in parallel.

**Access — how you reach intrinsic structure.** You aren't born able to reason; you build
the toolkit. Through interaction with a world that *instantiates* logical and mathematical
structure, you acquire **verification tools** — object permanence (the lived form of
reflexivity), cause-and-effect (the lived form of implication), then modal, hypothetical,
and inductive reasoning. These come in an order set by **temporal scale**: short-timescale
patterns first, each tool unlocking the ability to perceive longer, slower ones (the
"developmental escalator"). Tools are acquired through three kinds of encounter: **direct**
(perceiving structure in the world), **shadow** (recognizing structure through its
consequences — e.g. Newton seeing the apple's fall and the moon's orbit as one law), and
**self-encounter** (turning reason on your own reasoning).

**Emergence — how the lived self forms.** The self itself is built by three **modes** of
development. These are *response-types*, not predictors — the theory says what each mode
*does*, not which one will fire for a given encounter:

- **Mode A — Adversarial differentiation.** Encountering something "other" enough draws a
  boundary. This is what creates an I/not-I distinction in the first place. It carries the
  **prerogative of consistency**: your own frame is the implicit standard against which the
  discrepant thing registers as discrepant.
- **Mode C — Positive identification.** Encountering something that registers as
  *continuous with you* folds it inside the boundary. This is how most of the self gets
  populated. (When candy is taken from a baby, the baby grieves a loss *of self* — the
  candy had been positively identified as part of the proto-self, before a firm boundary
  existed to exclude it.)
- **Mode B — Reflexive meta-reasoning.** You turn attention on your own structure. This
  can't happen at the very beginning — there has to be something accumulated to reflect on
  — and once available it *refines* the whole.

> **From the inside —** Mode A is the flinch: someone cuts you off in traffic and for a second "you" and "them" snap into sharp relief. Mode C is the melt: someone becomes so folded into your life that "my day" quietly includes what happened to them. Mode B is catching yourself mid-flinch or mid-melt and asking *why* — turning the same equipment back on itself.

A consequence the theory takes seriously: **early development happens *to* you, not *by*
you.** Before the capacity for self-direction exists, the patterns being laid down are
products of a substrate you didn't choose and an environment you didn't control.

**Substrate, focus, and imprinting.** You have a finite, substrate-set **focus capacity**
you cannot choose. Contents reach you through pathways of increasing mediation, each lossy:
**first-order** (raw salience capture — sharp), **second-order** (cognitive mediation —
thoughts, structured), **third-order** (somatic-then-cognitive — emotions, sensations,
often *intense but fuzzy*: a panic attack screams "something is terribly wrong" without
specifying what). Running underneath all of it is **osmotic imprinting**: substrate-level
pattern formation by sheer repeated co-occurrence, always operating, requiring no attention
— the main engine of "I don't know why I feel this way about X."

> **In plain terms —** think of three ways the world gets into you, each more filtered than the last: a jolt from the world arrives clean and sharp (a bang, your own name, a stab of pain grabbing your attention), thoughts arrive a little processed but with words attached, and emotions arrive loudest but blurriest — a panic attack is a five-alarm siren with no address on it. Underneath all three, a slower process is always running: osmotic imprinting is why you can dread a certain tone of voice for years without ever being able to say what taught you to.

---

## 5. What the theory explains

Because the profile has a *shape*, disturbances of the self are **shape disturbances**, not
"too little self" or "too much":

- **Boundary and dissociation cases** (the table in §1) fall out directly from coordinate
  independence.
- **Conditions often classed as mental illness** are characteristic *profile shapes* — e.g.
  depression as a collapse and narrowing of the network, plus, in severe cases, a
  *functional* collapse of the partition between the I and its contents (depressive thoughts
  come to be treated as *who you are* rather than things you *have*). The theory is
  explicitly **descriptive, not prescriptive**: many such patterns originate inside a
  developmental window — or under situational overwhelm like trauma — where conscious
  direction could not have overridden the substrate. It does not moralize them.
- **Self-sacrifice** (a parent dying for a child) is handled without breaking the rule that
  only the core self has ρ = 1. ρ measures *integration*, not *what you'd preserve*. A second
  structural feature — the **prerogative of continued existence** — governs action under
  existential pressure. It is not the §4 *prerogative of consistency* (which makes your own frame the implicit standard a discrepant thing registers against); the two prerogatives are kept formally distinct.

---

## 6. The reach: application papers

The foundation is deliberately a *foundation*. Its power is meant to show in application —
and the standard each paper holds itself to is that the phenomenon should **fall out of the
existing apparatus**, with no new architectural commitments. So far:

- **Temporal phenomenology** *(complete)* — Why subjective time accelerates with age, what
  the felt "now" is, and why the past feels concrete while the future feels thin. All three
  come from one idea already in the foundation: a fixed mental **bandwidth** that an
  ever-growing self must spend more and more of on *integration*, leaving less for raw
  input. The "now" is the moment the world is actually being written into you; the past is
  *actual* imprinting, the future only *projected*.

- **Differentiated affect** *(complete)* — Starts by defining **love** structurally (folding
  another into the self so deeply that their loss is damage to *you*), then derives the whole
  emotional taxonomy as variations, losses, threats, and failures of that configuration:
  grief, fear, devotion, jealousy; **guilt vs. shame vs. embarrassment** (the same operation
  at different *scopes*); anxiety, dread, hope, despair; anger, disgust, awe, hate; pain,
  pleasure, trauma activation. Emotions become classifiable by *structural operators* rather
  than by their ordinary names.

- **Free will** *(draft)* — Replaces the single contested property "free will" with **six
  structural conditions** of free choice. The account is neutral on whether the universe is
  deterministic; what matters is whether the conditions are met. It separates **owning** a
  choice from where the choice was **sourced** — which is what makes manipulation genuinely
  hard.

- **Agency architecture** *(draft)* — The companion to *Free Will*. Takes free choice as the
  canonical case and derives everything else — akrasia, compulsion, addiction, ADHD-like
  gaps, learned helplessness, flow, mastery, manipulation — as structural variations. Builds
  the apparatus for **responsibility** (ownership / responsibility / accountability, never
  zero-sum) and reads the famous experiments (Libet, Wegner) as tests of much narrower things
  than "free will."

- **Out of the cave** *(early draft)* — Derives Plato's allegory of the cave from the
  foundation as a theory of **epistemic closure**. Escape is real, but every escape is ascent
  to a *larger cave*, never an exit from cave-hood. Re-diagnoses the prisoners' error: not
  false belief, but a systematically wrong *source-map* — "correctly ordered and wrongly
  sourced."

- **The Cave's Lagrange Points** *(first draft)* — A companion to *Out of the Cave* about
  **constriction** rather than closure: what happens when the cave cannot be made wider. It
  names two ordinary collapse directions — shrinking the self to fit the constraint, or
  shrinking the constraint into a defeatable enemy — and a third, sustainable configuration,
  **dual-fidelity integration**, using the physics of Lagrange points (unstable points you
  must actively station-keep; stable points you can orbit) as the guiding analogy, limits and
  all. Exploratory; its predictions are UNVERIFIED.

- **The Cold Frame and Its Sources** *(draft)* — Splits the fused notion of "empathy" into two
  operations: a **modeling channel** (building an accurate model of another as a real person) and
  a **routing channel** (their state actually *landing* on you), coupled by a variable λ. From
  this one move it addresses psychopathy (intact modeling, severed routing — *not* an absence of
  feeling), the "cold frame," and how *ordinary* moral people can commit atrocity by faithfully
  caring — over a model of a group that culture has *thinned* at the source, so they feel not
  cruel but correct. It closes on a hard meta-ethical claim: a morality can be genuinely binding
  even though where you land on it is undeserved.

- **The Self-Applied Architecture** *(draft prose — full first draft)* — The theory turned on its own author.
  Where the others apply the apparatus to an abstract phenomenon, this one reconstructs a single
  **lived trajectory** — the author's own — as a profile shaped by two unauthored substrate roots
  (an execution/focus constraint and a high-gain affective parameter), running through a
  destabilization engine, three idealizations, addiction, and recovery. It is autobiographical and
  candid about hard material (taken as *given*, not diagnosed), and it carries a built-in firewall
  against reading one's own life as a flattering arc. Its meta-ethical core is the cold frame's,
  reached from the inside: accountability survives even where desert and credit do not.

- **This Is Water** *(first draft)* — A bridge from David Foster Wallace's "This Is Water" to
  the architecture: a theory of **truth-respecting choice**. It isolates the moment
  self-knowledge becomes *causally active* in a real episode — before the choice closes — as an
  "epistemic-to-agential transport," and adds guardrails for when that transport respects the
  evidence. Deliberately modest: it supplies machinery, not a theory of Truth or a derivation of
  right action, and says so.

- **Shared Reality, Divergent Maps** *(first draft)* — Turns the apparatus on democratic
  politics. It reads a citizen's sense of a candidate — their "vibe" — literally, as a
  compressed, affectively-weighted model of the world that candidate seems to embody, and models
  culture war as a case where people share a vocabulary while decoding different worlds
  (**semantic interoperability** falling as within-group bandwidth rises). Its proposed repair is
  not civility or splitting the difference but **constraint-closed compromise**: each side must
  inherit the downstream obligations of its own principles and permanently absorb the strongest
  surviving concern its rival makes vivid. Extends *This Is Water*; exploratory, and its formal
  model is UNVERIFIED.

- **Choice as Endogenous Filter Application** *(first draft)* — A conservative *refinement* of
  *Free Will* and *Agency Architecture*: choosing is not selecting a point from a ready-made menu
  but the endogenous application of a **filter** to the field of live possibilities — the
  self-directed deformation of focus *is* the choice, with no hidden chooser behind it. Discrete
  options survive as a valid coarse-grained (*quotient*) description rather than an error;
  **perceptual momentum** — how strongly the current trajectory resists reweighting — sets how much
  bodily leverage a small chosen shift carries. It adds no new foundation machinery; its
  phenomenological predictions are UNVERIFIED.

- **This Ontology Is Really Moreish** *(publication-hardened v1.0; supersedes v0.2.9)* — an author-derived structural
  self-application, read as a control architecture. A "moreish" failure mode arises when three
  locally-valid **sensors** — adversarial epistemic skepticism (*Underground Super Hans*),
  present-reward demand (*Pavlov's Veruca*), and sacrificial moral seriousness (*the Jesus/WWJD
  ideal*) — are each promoted to a global **governor**. It names the **Greedy Integral Problem**
  (maximizing each moment locally need not maximize a life whose moments are dynamically coupled
  through state) and the **epistemic ratchet** (lived resonance can install a rule that later
  suffering cannot symmetrically remove), and proposes the corrective as an adaptive feedback
  policy that preserves option value, keeps distress as telemetry, and refuses to assign the self
  zero weight. It adds no new foundation machinery; the formal skeleton is schematic and the
  autobiographical claims are UNVERIFIED.

- **When the Map Becomes a Mandate** *(first draft; AI-assisted, author review pending)* — the
  theory turned outward onto a **documentary case**: attention, institutional abstraction, and
  moral authorization in the writings of Ted Kaczynski. Not a derivation of a phenomenon but a
  *source-critical application*, and pointedly **not a diagnosis, an endorsement, or a validated
  causal biography**. Its spine is one distinction held rigidly apart: **explanation, practical
  evaluation, and moral authorization** are separable even as they interact — a real constraint
  does not identify its cause, identifying a cause does not license a remedy, and predicting an
  effect does not confer permission to impose it on a nonconsenting person. It carries four
  **conditional formal results** (identity-weight ρ is not itself a force on the baseline law;
  rejecting an alternative is not being unable to represent it; a task-preserving institutional
  quotient can discard ethically load-bearing facts; descriptive premises do not entail a
  permission without a normative bridge) and six **documentary conclusions** at explicit scopes —
  while keeping **six rival explanations live** and every causal claim CONJECTURED / UNVERIFIED. It
  adds no foundation machinery, imports no clinical or risk-profiling content, and does not
  transport the TLICA author's own history onto its subject. Provenance: the retained
  [Phase 1 dossier](research/kaczynski_focus_closure_2026-09-15/README.md).

See the [applications wiki](docs/applications.md) for fuller treatments. Drafts are marked
as drafts; the foundation they rest on is frozen.

---

## 7. What it deliberately does *not* claim

The theory is careful about its own edges:

- It is **not a theory of consciousness.** Consciousness — that there is an I with a field at
  all — is *presupposed*, not explained. Identity-correlation is a structure *within*
  consciousness; ρ is **not** a measure of "how conscious" something is.
- **It does not rank people by selfhood.** No global, shared self; each instance is anchored
  to one perspective. The theory is *form-invariant* (anyone can build it for themselves) but
  single-perspective.
- It is **honest about its limits.** Whether other minds actually exist, what the world is
  like independent of you, and where your contents really come from are all acknowledged as
  unknowable from inside a single perspective. They are named as posits or as out of scope,
  not smuggled in.

It is also **translatable** into many prior frameworks (self-model theory, predictive
processing, phenomenology, no-self traditions, attachment theory, classical conditioning)
without depending on any of them — and it marks where it genuinely *conflicts* with others
(Humean bundle theory, eliminativism about the self, fictionalism about mathematics) rather
than papering over it.

---

## 8. Status

TLICA is **a foundation in active development, not a finished theory.** The foundation
(Files 0–5) is frozen at v5.5.1 so application papers have a stable base — though its
newest layer, the **dynamical apparatus** (Sections 8.9–8.11), is still being hardened
under audit and is best read as **main-but-experimental**; the last settled foundation before
it, **v5.3.3**, is retained read-only at
[`foundation/previous_v5.3.3/`](foundation/previous_v5.3.3/). A v6 consolidation
is anticipated once enough refinements accumulate. The work was developed iteratively,
grounded in the author's direct phenomenological access to her own structure and refined
under repeated adversarial pressure — a process the theory regards as continuous with its own
account of how minds acquire and refine understanding.

---

## 9. The documents

### Foundation (v5.5.1 — current; frozen, main-but-experimental)

> **Version note.** The v5.4.x–v5.5.x line seats a new **dynamical apparatus** (Sections 8.9–8.11) that is
> still being hardened under active audit — authoritative and frozen for the application
> papers, but experimental. For the last *settled* foundation before that layer, the **v5.3.3**
> files are retained read-only at
> [`foundation/previous_v5.3.3/`](foundation/previous_v5.3.3/): the same core architecture
> (coordinates, modes, cogito) without the motion/dynamics layer.

Read in order; each file builds on the previous. Start with the reading guide.

| File | Document | Contents |
|---|---|---|
| 0 | [`0_reading_guide.md`](foundation/0_reading_guide.md) | Reading guide and overview |
| 1 | [`1_foundations.md`](foundation/1_foundations.md) | Preface, abstracts, introduction, foundational commitments |
| 2 | [`2_access_and_development.md`](foundation/2_access_and_development.md) | Access to the intrinsic layer; modes of I-development |
| 3 | [`3_formal_apparatus.md`](foundation/3_formal_apparatus.md) | Shell walkthrough, asymptotic field, the three coordinates, substrate/focus/dynamics |
| 4 | [`4_derived_concepts_and_predictions.md`](foundation/4_derived_concepts_and_predictions.md) | Other I's, derived concepts, boundary phenomena, predictions and exclusions |
| 5 | [`5_translations_open_problems_conclusion.md`](foundation/5_translations_open_problems_conclusion.md) | Translations and tensions, open problems, conclusion, appendix |

**Where to start, by reader:**
- *New, want the whole thing* — read Files 1 → 2 → 3 → 4 → 5 in order.
- *Just the compressed view (~3000 words)* — the long abstract in File 1, then the appendix
  in File 5, then the predictions in File 4.
- *Coming from another framework* — File 1, then the translations in File 5, then back to
  2–4 as needed.
- *Want it in plain language first* — start with the [wiki](docs/).

### Application papers

Each applies the frozen foundation to a specific phenomenon. Plain-language summaries are in
the [applications wiki](docs/applications.md).

| Document | Layer | Version | Status | What it does |
|---|---|---|---|---|
| [`6_temporal_phenomenology.md`](applications/6_temporal_phenomenology.md) | 6 | v1.0 | Complete | Subjective time, the "now," past/future asymmetry |
| [`differentiated_affect_v1_0_2.md`](applications/differentiated_affect_v1_0_2.md) | 7 | v1.0.2 | Complete | The emotions, derived from the structure of love |
| [`free_will_v0_3_0.md`](applications/free_will_v0_3_0.md) | 8A | v0.3.0 | Draft | Free choice as six structural conditions |
| [`agency_architecture_v0_3_0.md`](applications/agency_architecture_v0_3_0.md) | 8B | v0.3.0 | Draft | The taxonomy of agency, attribution, and the experiments |
| [`out_of_the_cave_v0_1_2.md`](applications/out_of_the_cave_v0_1_2.md) | — | v0.1.2 | Early draft | Plato's cave as a theory of epistemic closure |
| [`caves_lagrange_points_v0_1_0.md`](applications/caves_lagrange_points_v0_1_0.md) | — | v0.1.0 | First draft | Lagrange-point dynamics: constriction and dual-fidelity integration |
| [`this_is_water_truth_respecting_choice_v0_1_0.md`](applications/this_is_water_truth_respecting_choice_v0_1_0.md) | — | v0.1.0 | First draft | Wallace's "This Is Water" as epistemic-to-agential transport |
| [`shared_reality_divergent_maps_v0_2_0.md`](applications/shared_reality_divergent_maps_v0_2_0.md) | — | v0.2.0 | First draft | Politics as contested representations; semantic interoperability and constraint-closed compromise |
| [`choice_as_filter_v0_1_0.md`](applications/choice_as_filter_v0_1_0.md) | — | v0.1.0 | First draft | Choice as endogenous filter application; perceptual momentum; discrete options as filter quotients — a conservative refinement of *Free Will* / *Agency Architecture* |
| [`moreish_ontology_v1_0.md`](applications/moreish_ontology_v1_0.md) | — | v1.0.1 | Publication-hardened (frozen preprint; supersedes v0.2.9) | A "moreish" failure mode as a control architecture: three sensors (skepticism, present-reward, sacrificial morality) that break when promoted to governors; the Greedy Integral Problem and the epistemic ratchet — an author-derived self-application. v1.0 adds a method/claim-boundary section, an adjacent-literature/novelty boundary, the costume-party developmental root (§2.5), and a full reference apparatus; the prior first-final-draft [`moreish_ontology_v0_2_9.md`](applications/moreish_ontology_v0_2_9.md) is retained |
| [`when_the_map_becomes_a_mandate_v0_1_0.md`](applications/when_the_map_becomes_a_mandate_v0_1_0.md) | — | v0.1.0 | First draft (AI-assisted; review pending) | Documentary/case application to Ted Kaczynski's writings: separating explanation, practical evaluation, and moral authorization; four conditional formal results + six scoped documentary conclusions; six rivals live. **Not a diagnosis or validated causal biography**; causal reconstruction CONJECTURED / UNVERIFIED |
| [`cold_frame_v0_4_3.md`](applications/cold_frame_v0_4_3.md) | — | v0.4.3 | Draft (closed prose) | Modeling vs. routing; the "cold frame" and its three sources |
| [`cold_frame_v0_3_0.md`](applications/cold_frame_v0_3_0.md) | — | v0.3.0 | Superseded prose | Prior draft (pre-close; §4.5 still skeleton) |
| [`cold_frame_v0_2_0.md`](applications/cold_frame_v0_2_0.md) | — | v0.2.0 | Superseded prose | Prior draft of *The Cold Frame* (pre-φ-gap) |
| [`referent_routing_v0_1_6.md`](applications/referent_routing_v0_1_6.md) | — | v0.1.6 | Superseded skeleton | Pre-prose predecessor of *The Cold Frame* |
| [`self_applied_architecture_prose_draft_v0_1.md`](applications/self_applied_architecture_prose_draft_v0_1.md) | — | v0.1 | Draft prose (full first draft) | The theory applied to one lived trajectory; method, all four arcs, master-patterns + appendices |
| [`self_applied_architecture_v0_8.md`](applications/self_applied_architecture_v0_8.md) | — | v0.8 | Working doc (pre-prose) | Full frozen architecture behind the prose draft |
| [`self_applied_architecture_v0_6.md`](applications/self_applied_architecture_v0_6.md) | — | v0.6 | Working doc (pre-prose) | Earlier architecture-freeze skeleton |

### Research notes (exploratory — dated, un-versioned)

Beyond the finished application papers, an exploratory tier of working notes lives in
[`research/`](research/) — raw derivations and dossiers, author-derived and typically
**UNVERIFIED** as empirical models. They are dated rather than versioned and are *not* part
of the frozen foundation. [`research/README.md`](research/README.md) is the research tier's
full front page; the most developed threads are surfaced below. First, the grokking /
toolkit-closure dossier, which has a full plain-language wiki page:

| Document | Date | Status | What it does |
|---|---|---|---|
| [`grokking_as_toolkit_closure_2026-08-29.md`](research/grokking_as_toolkit_closure_2026-08-29.md) | 2026-08-29 | Research paper — **CONJECTURED** | Reads **grokking** (a learner's delayed jump from *memorizing* cases to *generalizing* the rule behind them) through the theory's own developmental vocabulary. It separates the moment a global understanding first becomes **constructible** (t★) from the later moment it actually **takes over behavior** (t_grok), proves an exact gauge obstruction that leaves disconnected evidence unidentifiable, and defines "nerf-grokking" (when the global route is blocked, unbuildable, or permanently subordinate). **Foundation impact: none.** |
| [`grokking_toolkit_closure_experiment_protocol_2026-08-29.md`](research/grokking_toolkit_closure_experiment_protocol_2026-08-29.md) | 2026-08-29 | Protocol — **UNRUN** | Preregisterable bridge-topology experiment that would test the account by changing only the connectivity of the evidence while holding sample count fixed; all outcomes explicitly **UNRUN / UNVERIFIED**. |

A plain-language walkthrough of the grokking dossier lives at
[docs/grokking-toolkit-closure.md](docs/grokking-toolkit-closure.md).

**Actualization / recognition dossier (2026-09-07 – 2026-09-09).** A connected cluster from one
long conversation on how a person inhabits an activity, how particularity survives being
modelled, and the ethics of turning people into operators. All **research-tier, v0.1.0,
foundation untouched**, each with its own claim ledger and a finite-model demo (the demos are
shared across the papers, so they are *not* independent corroboration; person-level claims stay
UNVERIFIED):

- [**The Geometry of Actualization**](research/geometry_of_actualization_2026-09-07/README.md) (Bataille, Dostoevsky, Wallace) — the field contains the self; the same coarse agency machinery sustains absorbed work and instrumental labor, plus immersion / correctable-commitment and traversability / steerable-commitment continuations.
- [**Depth Without Capture**](research/actualization_recognition_2026-09-09/README.md) — recognition as faithful *bounded* reconstruction of what is expressed, not a demand for a duplicate person; a predictable person keeps full moral standing.
- [**Inside Out and Reflected**](research/idubbbz_hyde_paper_2026-09-09/README.md) (iDubbbz, Sam Hyde) — norm-referenced adjudication vs. protocol-disrupting inquiry as two nonexclusive allocations of normative authority; explicitly *not* a mathematical duality.
- [**A Post-Mortem of the Four Horsemen**](research/four_horsemen_postmortem_2026-09-09/README.md) — *warrant substitution* (crediting success under one acceptance criterion as warrant under another) across Hitchens, Dennett, Dawkins, and Harris; narrows or withdraws the symmetric personal diagnoses the conversation began with.

**Math-justification program (the dynamical substrate).** An extension-layer effort to *earn*
the literal correspondence of TLICA's borrowed motion-words (momentum, reachability, …) rather
than merely assert it — the "dimensional analysis, not equality" discipline made rigorous.
Foundation untouched.

- [`dynamical_substrate_axioms_2026-09-08.md`](research/dynamical_substrate_axioms_2026-09-08.md) — Round 0: the minimal dynamical-substrate axioms (A1–A5) a motion-word can be earned *against*.
- [`substrate_round1_reachability_momentum_2026-09-08.md`](research/substrate_round1_reachability_momentum_2026-09-08.md) — Round 1: *reachability* core **Derived** (its exact-partition headline **Refuted**); *momentum* shape **Derived**, literal `p = mv` **Refuted** — a downgrade to shape-only that is the rigor working, not failing.

**Intergenerational conflict dossier (2026-09-10).** A standalone research draft on a proposed
failure mode of coercive policy: defeating present adversaries through conduct that helps
*reproduce* future ones. **Research-tier, v0.1.0, foundation untouched**; its psychological,
strategic, and historical mechanisms are **CONJECTURED / UNVERIFIED**, carried with a full source
and claim ledger and an author-intent record that keeps what is *proposed* separate from what is
*proved*:

- [**The Children of Our Enemies**](research/children_of_our_enemies_2026-09-10/README.md) —
  *inherited conflict, goal-relative slack, and the conditions of durable victory.* Understanding
  and empathy are treated as **situated, resource-bounded tasks** (goal-relative *slack*), not one
  capacity a policy can demand while removing the room to perform it; "hearts and minds" is rebuilt
  as **equal-standing, reciprocal discovery** of acceptable outcomes — listening that can change the
  mission — rather than indoctrination; and divergent cultural projects are modelled as **alternative
  operators** in a shared system. Its motivating examples (Israel–Palestine, the U.S. Civil War) are
  used *without* assigning collective guilt, equating sides, or adjudicating any current operation.
  The one piece that is genuinely *proved* rather than conjectured is a synthetic **switched-system
  counterexample** (§9): two update maps each individually contractive, whose average is also
  contractive, yet whose alternation **expands** — machine-checked by a standard-library script (13
  exact-arithmetic checks; largest eigenvalue of the alternation `(131 + 9√181)/200 ≈ 1.26 > 1`,
  independently reproduced). It establishes a mathematical *possibility*, **not** a claim about any
  real society.

**Distributed institutional realization (2026-09-15, v0.2).** A candidate *future* application
paper on how socially real structures — governments, courts, firms, offices, procedures — can be
causally effective through indexed people, typed relations, artifacts, and records **without** being
reduced to a document or reified into an unindexed group mind. **Research-tier, v0.2.0, foundation
untouched**; carried with a claim ledger, an audit reconciling it against `main`, and a
falsification plan:

- [**Distributed Institutional Realization**](research/distributed_institutional_realization_2026-09-15/README.md) —
  *institutional macrostates, local discontinuity, and social structure without a group mind.* v0.2's
  load-bearing repair: the institution is not the map `𝕽_t(P,R,D,S)=I_t` (which risked being the
  inputs renamed) but the **task-relative quotient** `I_t^T=[X_t]_{~_T}` of the micro-realization
  `X_t=(P_t,R_t,D_t)` — the equivalence class of realizations that answer a declared task the same
  way — with the situational field kept external and entering only at activation. Every "the
  institution did X" must still expand into an indexed path through real people and things, and its
  central phenomenological move is unchanged (**Conjectured**): behavior can look **locally abrupt**
  when the distributed support for it sat outside the observer's frame until it activated there (an
  observability claim, explicitly *not* the truism "hidden causes exist"). Comes with **two executed**
  standard-library toy models: a **NEW quotient demo** (12 self-checks) in which six distinct
  micro-realizations collapse to three macrostates and the response map factors through the quotient
  *exactly* on all 36 cells — the **formal** half of C-006, executed, showing the institution object
  is genuinely smaller than the raw list — and the badge-door demo (14 self-checks), whose
  role-substitution and ρ-inertness results are now honestly relabeled **construction-level** (the
  code is built role-relative and never reads ρ) and whose grid is relabeled a **pipeline trace**.
  What stays **UNVERIFIED**: whether such institutional quotients are *useful* in real domains (the
  empirical half of C-006) and whether the account out-predicts existing network / distributed-
  cognition / role / social-ontology accounts (C-025). Plain-language wiki page:
  [docs/distributed-institutional-realization.md](docs/distributed-institutional-realization.md).

**Research method — phenomenology → analogy → model → probe (2026-09-15).** A note about *how the
work is made*, not a claim about selfhood: the project uses an explicit analogy-to-model loop in
which a phenomenological pattern may suggest a source analogy, but the analogy is only a candidate
generator. The transported structure must be **declared** (a bridge contract stating what maps and
what explicitly does not), formalized, driven **outside** its motivating cases, and exposed to a
discriminating probe — including **Refuted** as an allowed outcome — before it earns empirical
warrant: *analogy proposes, mathematics propagates, reality supplies warrant.* It adds **no**
foundation coordinate, mode, or law; that using it explicitly improves research generally is
**UNVERIFIED**. [Dossier](research/phenomenology_analogy_model_probe_loop_2026-09-15/README.md) ·
[plain-language page](docs/research-method.md).

**Quiet Quitting Manifesto — recovered work and history (2026-09-16).** A self-contained
**historical archive** of Leah's *Ethical Quiet Quitting Manifesto* (written with disclosed AI
assistance) — **not** an application paper and **not** a validated workplace model, kept readable
without any TLICA knowledge. **Research-tier, foundation untouched**; carried with a claim ledger, a
retrospective theory bridge, a provenance record, and a repeatable byte-integrity check:

- [**The Quiet Quitting Manifesto**](research/quiet_quitting_manifesto_2026-09-16/README.md) —
  *competent, safe, honest work while withdrawing the unowned excess an institution has folded into
  "normal," after a material, persistent mismatch and failed or unavailable repair.* Eleven manuscript
  versions recovered as a **branching** edit history: v1.4 the voice-preserving parent, v2.0 a
  **rejected** rewrite (not promoted by its larger number), a preliminary v1.5 rejected for false
  worker/employer symmetry, the v1.5.3 checkpoint, and the latest-recovered v1.5.4 (which adds an
  autobiographical genealogy without retroactively certifying earlier conduct). Preserves the narrow
  scope of *quiet quitting proper* (distinct from ordinary boundaries, collective pressure, and
  outright refusal), the **equal-worth / unequal-power** asymmetry, and the "fuck-it factor"
  acute-triage construct as **proposed**, not proven. File recovery is substantial (86 source paths,
  SHA-256 verified); conversation recovery is **partial** and explicitly bounded. The current TLICA
  reading is an appended **retrospective** map, not validation — operational slack ≠ reflexive slack,
  and no coordinate derives the ethics. Plain-language wiki page:
  [docs/quiet-quitting-manifesto.md](docs/quiet-quitting-manifesto.md).

These notes are more technical than the [wiki](docs/) and carry their empirical claims as
UNVERIFIED. The frozen foundation (v5.5.1) is untouched by all of them.

---

## Conventions

- The foundation set is frozen at v5.5.1. Changes to foundation files are errata-level unless
  a v6 consolidation is declared.
- Application papers cite the foundation by section and file (e.g. "Section 8.5, File 3").
- Version numbers live in document filenames so superseded versions can be retained alongside
  their successors when needed.

*More documents are forthcoming and will be filed under `applications/` (or a new top-level
directory if a distinct document class emerges).*
