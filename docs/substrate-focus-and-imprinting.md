# Substrate, Focus & Imprinting

[← Wiki home](README.md) · Source: [File 3, §8](../foundation/3_formal_apparatus.md)

---

The [profile](identity-correlation-profile.md) doesn't form in a vacuum. It's shaped by a
**substrate** you didn't choose, a finite **focus** you allocate within hard limits, and
several **imprinting** mechanisms that write contents into the network. This page covers
the machinery — how raw experience gets *into* you, and why the way it gets in shapes how
it feels once it's there.

> **In plain terms —** you are not a blank slate that picks what to take in. You arrive
> with a fixed-size attention, a body and brain you didn't design, and several different
> channels through which the world leaves marks on you. This page is about those channels.

A quick orientation to the **substrate** itself. Formally the substrate for a given I is
written `S_m = (B_m, E_m, χ_m)` — three parts: `B_m` **(the body)**, a piece of the world
you can't step outside of; `E_m` **(the environing contents you're embedded in)**; and
`χ_m` **(the contact map)** — *how strongly each thing is currently in live contact with
you*. "Substrate" is just the Latin for *what lies underneath* — the standing equipment
(body, brain, sensory apparatus, the world you're soaked in) that does the processing
before anything ever reaches the part of you that says "I." You never inspect it directly;
you only ever receive its output.

> **In plain terms —** "substrate" = the under-layer. It's the machinery (body, brain,
> surroundings) that catches the world, chews it up, and hands you the result. You don't
> get the world raw; you get the substrate's version of it.

## Substrate-bound focus

Your **focus capacity** — how much you can hold in attention at once — is set by your
substrate and **you cannot choose it**. In the formalism this is the map `M_m(t)`
(your maximum number of focus-slots at time *t*), and it's fixed by the substrate through
an unspecified function `Γ^M_m` (gamma-em — "whatever rule the substrate uses to set your
capacity"). The theory deliberately leaves *how* the substrate sets it open; what it
commits to is that the capacity is **inherited, not chosen**: written tersely,
`î_m ↛ M_m(t)` — "the I has no arrow into its own capacity," i.e. wanting more attention
does not give you more attention.

You can *allocate* focus among available contents, but only within that inherited bound:
`|Foc_t| ≤ M_m(t)` — the number of things you're holding in attention can never exceed
your slot-count. **Foc (focus)** is simply *what you're currently attending to* — the
spotlight, not the stage.

> **In plain terms —** you have a fixed number of attention-slots. You can point them at
> whatever you like, but you can't will yourself more of them. The ceiling came with the
> body.

> **From the inside —** it's the feeling of "I can only think about so much at once." When
> five things need you and you can hold maybe two, that wall you hit is `M_m` — and no
> amount of trying makes the wall move.

Focus allocation has two drivers that shift in balance over development. Formally
`Foc_t = Foc_t[contact-driven] ⊕ Foc_t[self-directed]` — the ⊕ just means your attention
is a *blend* of two sources whose weighting changes as you grow:

- **Contact-driven** — salient things in the world grab focus from outside. Dominant
  early, when there's little internal structure to direct from. (A newborn doesn't *decide*
  to look at the bright thing; the bright thing takes the look.)
- **Self-directed** — accumulated lived-I structure directs focus from inside. Grows as
  the self grows. (An adult can choose to stay with a dull tax form because a built-up
  sense of *who I am and what I'm doing* holds the spotlight in place.) The shift from
  outside-driven to inside-driven is gradual and **never complete** — the world can always
  still grab you.

> **In plain terms —** early on, the world points your attention. As you build up a self,
> you start pointing it yourself. That handover happens slowly and never fully finishes —
> a sudden bang will still steal the spotlight from you at sixty.

## The three orders of imprinting

**Imprinting** is the general name for *the world leaving a mark on you* — any process by
which a content gets written in. Contents reach you through pathways of increasing
**mediation** (number of substrate stages they pass through) — and every stage is
**lossy** (it compresses the signal, keeping some features and throwing the rest away).
The "order" of a content is its *dominant* pathway. Formally this is the **mediation
depth** `D_{m,t}(x)` — "how many substrate layers content *x* had to cross to reach you." It isn't
a new coordinate alongside κ/φ/ρ; it's just a label for which route a content took. Most
real contents mix all three orders, with one dominant.

- **First-order (D = 1) — salience capture.** Pathway: **world → salience-gating → focus.**
  A loud bang grabs your attention. Minimally mediated, so **sharp**. (Not *unmediated* —
  the signal still passes through substrate, through the startle and novelty-detection
  machinery; it's just the shortest path. The theory is firm that nothing reaches you raw.)
  *Everyday cases:* a door slams and your head turns; a pain-spike yanks attention to your
  ankle; you catch your own name across a noisy room.
- **Second-order (D = 2) — cognitive mediation.** Pathway:
  **world → cognitive substrate → I.** These are **thoughts.** The brain takes bits of the
  world — a remark, a memory, a situation — and works them into representational form
  before they reach you. They carry propositional structure ("that person insulted me"),
  which makes them **clear** and easy to run reason-tests on — well-suited for
  φ-placement (slotting into your verification system, where **φ** is the coordinate for
  *can-I-trace-and-check-this-source?*). *Everyday cases:* "I should leave soon." "What did
  she mean by that?" "This proof needs f to be continuous." Note thoughts are
  *meta-cognitive* — commentary the brain makes *about* the world, never the world itself.
- **Third-order (D = 3) — somatic-then-cognitive mediation.** Pathway:
  **world → body → cognitive substrate → I.** These are **emotions and sensations.** Two
  compression stages have run by the time they reach you — the body squeezes the original
  signal into intensity/valence/action-tendency, then the brain squeezes *that* into
  felt-content — so they tend to be **intense but fuzzy**. *Everyday cases:* dread before
  a meeting; a wave of grief; unplaceable hunger or fatigue; a mood you can't pin to a
  cause.

> **In plain terms —** three doors the world comes in by. Door 1 (a startle) is short and
> crisp. Door 2 (a thought) is longer but arrives with words attached. Door 3 (a feeling)
> is the longest — it's been squeezed twice, so it hits hard but shows up without a
> note explaining itself.

> **From the inside —** the difference between *"a bang — I flinched"* (sharp), *"he meant
> that as an insult"* (clear, checkable), and *"I just feel awful and I can't say why"*
> (loud, but wordless). Same person, three different delivery routes.

**Orders are dominant pathways, not boxes.** A single moment can be third-order dominant
(a knot of unease) with a second-order thought riding along ("it's about tomorrow") that
points first-order attention at the calendar. One content, one main route, contributions
from the others.

> **Intensity is not clarity.** A panic attack is maximal intensity with near-zero
> information density — "something is terribly wrong" without saying what. It is fully
> conscious, high κ, source-opaque, undefined φ. Fuzziness means *low explicit
> information density / low source-resolution*, not low intensity, and not "less
> conscious." (Trained interoception, expert somatic awareness, and contemplative
> practice can make third-order content unusually sharp — the rule is a *tendency*, not a
> law.)

Here the symbols, in plain dress: **κ (kappa, contact)** — *how live/present a content is
to you right now*; panic is high-κ, it's blaringly present. **φ (phi, truth-indistinguishability)**
— *whether you can trace where it came from and check it*; panic is undefined-φ, you can't
source it. So "intense but unverifiable" is exactly high-κ-plus-undefined-φ.

> **In plain terms —** loud is not the same as legible. A feeling can be deafening and
> still tell you nothing about itself. Don't mistake "I feel this strongly" for "I
> understand this clearly" — they're separate dials.

A useful corollary: **thoughts can trigger emotions.** A second-order thought about a
frightening possibility activates the body; the body's response is compressed back into
affect that reaches you via the third-order pathway — formally
`cognitive content → somatic activation → cognitive integration → I (as affect)` — which
is why anticipatory anxiety or grief arrives forceful but with its original reasoning no
longer attached. (Mood spillover, the dread that outlasts the thought that started it, and
emotionally-coloured memory all run on this same loop.)

> **From the inside —** you think one worried thought, and twenty minutes later you're
> still anxious but can't remember what set it off. The thought poked the body; the body's
> answer came back as a feeling with the receipt torn off.

## Osmotic imprinting

Underneath all the focus-driven machinery runs a different mechanism entirely:
**osmotic imprinting** — substrate-level pattern formation by sheer **repeated
co-occurrence in ambient experience**. The word *osmotic* is borrowed from osmosis, where
a substance seeps across a membrane on its own, no pump required: here a pattern seeps into
the substrate just from being *around* it enough times. It requires **no focus, no
verification, no mode operation** — you don't have to notice it, check it, or work at it.
**Pavlov's dog** is the pure case: bell-and-food co-occur, and the bell alone later
triggers the food-response. The dog never "decided" anything.

> **In plain terms —** osmotic = soaked-in. Some things mark you not because you studied
> them but because you stood next to them often enough. It's learning-by-marination.

Key properties:

- **Always operating.** The substrate is continuously patterned by what surrounds you —
  a constant **tug-of-war between focus and ambient exposure**. High focus narrows ambient
  intake but never seals it; rest, mind-wandering, and sleep raise it. Even total sensory
  deprivation doesn't stop it — your own proprioception, interoception and inner chatter
  are still "ambient" and still pattern you. ("Always operating" means the mechanism stays
  *online* — not that every moment produces a durable update; the soak-rate can drop near
  zero when there's little to soak in.)
- **Imprinting vs. activation are distinct.** *Imprinting* is the substrate forming the
  association (the soaking-in); *activation* is an imprinted pattern firing later (a smell
  triggers anxiety; an accent triggers a guarded posture). Activation can be conscious or
  entirely pre-conscious, and doesn't require you to recognize what's being triggered.
- **It's the engine of "I don't know why I feel this way about X."** That sentence is the
  signature of osmotic activation: the feeling is fully available (conscious), but its
  source-pathway stays opaque (undefined φ). Implicit attitudes, attachment patterns,
  trauma-cue responses, aesthetic dispositions, absorbed cultural and linguistic
  patterns — largely osmotic. Many become
  [unconscious-operative or conscious-fuzzy](two-layers.md) contents.
- **It runs mostly on the first- and third-order substrates.** Repeated co-occurrence
  re-tunes your **salience gates** (the first-order door — what now jumps out at you) and
  your **somatic-affective associations** (the third-order door — what now makes your body
  brace). It's the structural form of both Pavlovian conditioning and trauma-cue dynamics.
- **It seeds verification tools too** — populating the substrate with **proto-tools**
  (rough pattern-templates that aren't yet explicit reasoning tools): counting that
  happened *around* you before you could count, grammar you heard before you could parse
  it. These [later become explicit tools](access-to-intrinsic-structure.md). The
  developmental signature is "I had a sense of it before I could put it into words" — the
  substrate held the pattern by osmosis; the words came afterward.

> **From the inside —** you walk into a kitchen, catch a particular smell, and your chest
> tightens before any memory loads. Nobody taught you that on purpose; you just lived near
> the pairing long enough that the smell now carries the dread by itself. That's osmotic
> imprinting firing.

Osmotic imprinting is **transverse**: not a fifth kind of imprinting, but a substrate-level
process running *underneath* the four kinds below. Each of the four can have an osmotic
variant (something integrating by repeated exposure) and a non-osmotic variant (something
integrated by deliberate work).

## The four kinds of imprinting

All governed by the focus-and-contact dynamics above. Each is "imprinting" in the sense of
*writing a lasting change into the network*, but they write into different things:

1. **Content imprinting** — a content's **ρ rising as it integrates into the network.**
   **ρ (rho, identity-correlation)** is, in plain terms, *how much of you is bound up in a
   thing — the stuff whose loss would actually change who you are.* So content imprinting
   is something growing into part of you. *Example:* a hobby that was once just a passing
   activity becoming "who I am."
2. **Contact imprinting** — changes in **contact relationships (κ)**: how live your
   connection to something is, strengthening or fading. *Example:* a friend you now see
   daily moving from background to foreground of your life.
3. **Verification-tool imprinting** — acquiring **reasoning tools through encounter**: new
   ways of checking and tracing things, picked up by running into them. *Example:* learning
   what a controlled comparison is, and now being able to test claims you couldn't before.
4. **Mode-development imprinting** — the actualization of **Modes A, B, and C** (the I's
   developing capacities for distanced self-relation). *Example:* the slow arrival of being
   able to step back and watch your own reactions instead of just having them.

> **In plain terms —** four different kinds of lasting mark: things becoming part of you
> (ρ), connections heating up or cooling (κ), new mental tools, and new self-handling
> abilities. Osmotic imprinting can quietly drive any of the four before you ever notice
> it happening.

## Why this isn't "anything goes"

The architecture leaves several functions open — note the unspecified maps `Γ^M_m`
(capacity-setting), `Λ^μ_m` (lambda-mu — how focus and contact set which contents get
probed), and `𝒜/ℬ` (the update-strength rules). It deliberately does *not* say exactly
how the substrate sets capacity, or how focus shapes a given update. But the
**dependencies are fixed**: substrate determines capacity; focus shapes probing and
updating; contact shapes weighting and imprinting. The specific empirical content — the
actual numbers and rates — is application-level work, to be filled in by conditioning
research, attachment theory, trauma research and the like. The *structure* of the
dependencies is the theory's commitment; the dials are left for science to set.

> **In plain terms —** the theory says *what depends on what* without pretending to know
> the exact formulas. "Your body sets your attention-ceiling" is a firm claim; "and here's
> the precise equation for it" is not — that's left open on purpose, not hand-waved.

---

*Next: [The Two Prerogatives](the-two-prerogatives.md) · [Profile-Shape Disturbances](profile-shape-disturbances.md)*
