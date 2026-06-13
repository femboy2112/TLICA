# TLICA — The Two-Layer Identity-Correlation Architecture

*A formal account of how a self is structured: not "how real" a thing feels, not "how close" it is, but how much it is **you**.*

This repository is the canonical archive of the architecture and its application
papers. The foundation is **frozen at v5.3.3**; the application papers build on it
at varying levels of maturity. This README is a plain-language guide to the whole
theory. The formal source is in [`foundation/`](foundation/) and
[`applications/`](applications/).

> 📖 **Want to go concept by concept?** The [**wiki**](docs/) breaks the theory into
> one cross-linked page per idea, each pointing back to the frozen foundation.

---

## The theory in one paragraph

Classical accounts of the self blur together three things that come apart in real
experience: how strongly something is *in contact* with you right now, how *real
and undeniable* it seems under scrutiny, and how much it is *part of who you are*.
TLICA pulls these into three independent coordinates and builds a self out of them.
It starts from one thing that cannot be doubted — that you are yourself ("I am I") —
and from the claim that mathematical and logical structure is woven into the world
regardless of whether anyone is there to notice it. Everything else — your body,
memories, emotions, relationships, even your sense of being a continuous person — is
*acquired*: built up over time as you encounter the world, through mechanisms the
theory specifies. The result is a map (the "identity-correlation profile") of how
intensely each content in your field is bound into the network that is you. That map,
and the way it can be reshaped or disturbed, is what the theory describes.

---

## 1. The problem it starts from

In ordinary cases, three features of experience travel together. Your hand is in
contact with you, presents itself as undeniably real, and is part of you. A distant
rumor is weakly contacted, weakly certain, and not part of you.

But they can **dissociate**, and the dissociations are diagnostic:

| Phenomenon | In contact? | Feels real? | Part of you? |
|---|---|---|---|
| A vivid **hallucination** | no | **yes** | no |
| An **anesthetized limb** | no | no (in the moment) | **yes** |
| **Depersonalization** | yes | yes | **no** |
| A **phantom limb** | no | varies | **yes** |
| A **thought that feels inserted** ("alien clarity") | varies | **yes** | no |

Any theory that runs selfhood on a *single* dimension struggles with these. TLICA's
move is to say: there are three dimensions, none reducible to the others, and these
cases are exactly what their independence predicts.

---

## 2. The three coordinates

Every content in your field — a perception, a thought, a feeling, a memory — gets
three measurements:

- **Contact (κ, "kappa")** — how much it is interacting with you *right now*. The
  world pressing on perception, the body in current sensation.
- **Truth-indistinguishability (φ, "phi")** — how indistinguishable-from-true it is
  when you reason about it. What holds up; what can't be denied without contradiction.
- **Identity-correlation (ρ, "rho")** — how integrated it is into *you*: what would
  alter who you are if it were removed.

The headline claim is that these are **formally independent** (you can change one in
the model while holding the other two fixed) but **dynamically entangled** (in a
living mind they constantly influence each other — sustained contact tends to build
integration over time, strong integration biases what grabs your attention, and so
on). "Independent" means *not definable in terms of each other*, not *statistically
uncorrelated*. Most of the time they line up; the interesting cases are when they
don't.

Identity-correlation (ρ) is the coordinate the theory is really about. It is defined
as **flow through a network rooted at you**: each content's ρ measures how much
"you-ness" can reach it across the historically-built web of integrations. The
complete picture of these values across your whole field — the **identity-correlation
profile** — is the theory's single most important object. Not any one value, but the
*shape* of the whole map.

---

## 3. The two layers

The architecture splits everything into two layers.

- **The intrinsic layer** — mathematics, logic, and reason. The theory treats these
  as *in re*: real in the structure of the world, true whether or not any mind verifies
  them. (When a river pushes one stone next to another, there are now two stones,
  whether or not anyone counts.) This is a **naturalist** realism — the world contains
  structure minds can encounter — not the stronger Platonist claim about a separate
  realm of abstract objects.
- **The asymptotic layer** — *everything else*: every content in your field, conscious
  or unconscious, that does not hold by reason alone.

Between them sits **the cogito**. "I am I" is taken as a starting postulate, not a
proof — any attempt to deny that you exist presupposes the you doing the denying. It
is the single indexed instance of universal reflexivity ("x = x"), and so it sits one
step away from pure universality: the theory writes this position as **φ = 1 − δ**,
infinitesimally short of intrinsic truth, closer than anything else you'll ever hold.
Crucially, the cogito buys you *only* your own self-identity — no body, no memories,
no abilities. All of that has to be acquired.

---

## 4. Where the self comes from

There is no fully-formed self at the moment the cogito is anchored. Two developmental
stories run in parallel.

### Access — how you reach intrinsic structure
You aren't born able to reason; you build the toolkit. Through interaction with a
world that *instantiates* logical and mathematical structure, you acquire **verification
tools** — object permanence (the lived form of reflexivity), cause-and-effect (the
lived form of implication), then modal, hypothetical, and inductive reasoning. These
come in an order set by **temporal scale**: short-timescale patterns first, and each
tool unlocks the ability to perceive longer, slower ones (the "developmental
escalator"). Tools are acquired through three kinds of encounter: **direct**
(perceiving structure in the world), **shadow** (recognizing structure through its
consequences — e.g. Newton seeing the apple's fall and the moon's orbit as one law),
and **self-encounter** (turning reason on your own reasoning).

### Emergence — how the lived self forms
The self itself is built by three **modes** of development. These are *response-types*,
not predictors — the theory says what each mode *does*, not which one will fire for a
given encounter:

- **Mode A — Adversarial differentiation.** Encountering something "other" enough draws
  a boundary. This is what creates an I/not-I distinction in the first place. It carries
  the **prerogative of consistency**: your own frame is the implicit standard against
  which the discrepant thing registers as discrepant.
- **Mode C — Positive identification.** Encountering something that registers as
  *continuous with you* folds it inside the boundary. This is how most of the self gets
  populated. (When candy is taken from a baby, the baby grieves a loss *of self* — the
  candy had been positively identified as part of the proto-self, before a firm boundary
  existed to exclude it.)
- **Mode B — Reflexive meta-reasoning.** You turn attention on your own structure. This
  can't happen at the very beginning — there has to be something accumulated to reflect
  on — and once available it *refines* the whole.

A consequence the theory takes seriously: **early development happens *to* you, not
*by* you.** Before the capacity for self-direction exists, the patterns being laid down
are products of a substrate you didn't choose and an environment you didn't control.

### Substrate, focus, and imprinting
You have a finite, substrate-set **focus capacity** you cannot choose. Contents reach
you through pathways of increasing mediation, each lossy:

- **First-order** — raw salience capture (a loud bang grabs attention). Sharp.
- **Second-order** — cognitive mediation (thoughts). Structured, easy to reason about.
- **Third-order** — somatic-then-cognitive mediation (emotions, sensations). Often
  *intense but fuzzy* — high information loss means a panic attack screams "something is
  terribly wrong" without specifying what.

Running underneath all of this is **osmotic imprinting**: substrate-level pattern
formation by sheer repeated co-occurrence, always operating, requiring no attention and
no verification (Pavlov's dog is the pure case). It is the main engine of "I don't know
why I feel this way about X" — associations laid down below the level you can inspect.

---

## 5. What the theory explains

Because the profile has a *shape*, disturbances of the self are **shape disturbances**,
not "too little self" or "too much":

- **Boundary and dissociation cases** (the table in §1) fall out directly from
  coordinate independence.
- **Conditions often classed as mental illness** are characteristic *profile shapes* —
  e.g. depression as a collapse and narrowing of the network, plus, in severe cases, a
  *functional* collapse of the partition between the I and its contents (depressive
  thoughts come to be treated as *who you are* rather than things you *have*). The theory
  is explicitly **descriptive, not prescriptive**: many such patterns originate inside a
  developmental window — or under situational overwhelm like trauma — where conscious
  direction could not have overridden the substrate. It does not moralize them.
- **Self-sacrifice** (a parent dying for a child) is handled without breaking the rule
  that only the core self has ρ = 1. ρ measures *integration*, not *what you'd preserve*.
  A second structural feature — the **prerogative of continued existence** — governs
  action under existential pressure, and the two prerogatives are kept formally distinct.

---

## 6. What it deliberately does *not* claim

The theory is careful about its own edges:

- It is **not a theory of consciousness.** Consciousness — that there is an I with a
  field at all — is *presupposed*, not explained. Identity-correlation is a structure
  *within* consciousness; ρ is **not** a measure of "how conscious" something is.
- **It does not rank people by selfhood.** No global, shared self; each instance is
  anchored to one perspective. The theory is *form-invariant* (anyone can build it for
  themselves) but single-perspective.
- It is **honest about its limits.** Whether other minds actually exist, what the world
  is like independent of you, and where your contents really come from are all
  acknowledged as unknowable from inside a single perspective. They are named as posits
  or as out of scope, not smuggled in.

It is also **translatable** into many prior frameworks (self-model theory, predictive
processing, phenomenology, no-self traditions, attachment theory, classical conditioning)
without depending on any of them — and it marks where it genuinely *conflicts* with
others (Humean bundle theory, eliminativism about the self, fictionalism about
mathematics) rather than papering over it.

---

## 7. Status

TLICA is **a foundation in active development, not a finished theory.** The foundation
(Files 0–5) is frozen at v5.3.3 so application papers have a stable base; a v6
consolidation is anticipated once enough refinements accumulate. The work was developed
iteratively, grounded in the author's direct phenomenological access to her own
structure and refined under repeated adversarial pressure.

---

## 8. The documents

### Foundation (v5.3.3 — frozen)

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
- *Just the compressed view (~3000 words)* — the long abstract in File 1, then the
  appendix in File 5, then the predictions in File 4.
- *Coming from another framework* — File 1, then the translations in File 5, then back
  to 2–4 as needed.

### Application papers

Each applies the frozen foundation to a specific phenomenon.

| Document | Layer | Version | Status |
|---|---|---|---|
| [`6_temporal_phenomenology.md`](applications/6_temporal_phenomenology.md) | 6 — First application | v1.0 | Complete |
| [`differentiated_affect_v1_0_2.md`](applications/differentiated_affect_v1_0_2.md) | 7 — Second application | v1.0.2 | Complete |
| [`free_will_v0_3_0.md`](applications/free_will_v0_3_0.md) | 8 — Third application (split A) | v0.3.0 | Draft |
| [`agency_architecture_v0_3_0.md`](applications/agency_architecture_v0_3_0.md) | 8 — Third application (split B) | v0.3.0 | Draft; companion to *Free Will* |
| [`out_of_the_cave_v0_1_2.md`](applications/out_of_the_cave_v0_1_2.md) | Application | v0.1.2 | Early draft |
| [`referent_routing_v0_1_6.md`](applications/referent_routing_v0_1_6.md) | Working doc | v0.1.6 | Pre-prose skeleton |

---

## Conventions

- The foundation set is frozen at v5.3.3. Changes to foundation files are errata-level
  unless a v6 consolidation is declared.
- Application papers cite the foundation by section and file (e.g. "Section 8.5, File 3").
- Version numbers live in document filenames so superseded versions can be retained
  alongside their successors when needed.

*More documents are forthcoming and will be filed under `applications/` (or a new
top-level directory if a distinct document class emerges).*
