# The Three Coordinates

[← Wiki home](README.md) · Source: [File 3, §7](../foundation/3_formal_apparatus.md)

---

This is the heart of the apparatus. Every content in your field — a perception, a
thought, a feeling, a memory — gets measured on three separate scales. The three scales
answer three different questions about the *same* item, and the whole theory turns on the
fact that they can come apart. One thing can be loud-and-present but barely part of you;
another can be deeply part of you while utterly silent. You need three numbers, not one,
to say what any given content is doing.

> **In plain terms —** for anything floating in your experience right now, ask three
> separate questions: *Is it pressing on me?* (contact), *Does it hold up as true?*
> (truth-indistinguishability), and *Is it part of who I am?* (identity-correlation). The
> answers don't have to agree, and that disagreement is the point.

The three measurements, written symbolically, are **κ** (the contact reading), **φ** (the
truth reading), and **ρ** (the identity reading), each evaluated for a particular content
*x* at a particular time *t* for a particular mind *m*. Don't let the subscripts spook
you: `m,t` just means "for me, right now." The rest of this page unfolds the three one at
a time.

## κ — Contact

**κ (kappa, "contact")** — in plain terms, *how much a thing is actually touching you at
this moment.* The world pressing on perception, the body in current sensation, the
environment causally engaging you. High κ = live, present, happening-to-you-now; low κ =
remote, dormant, far away.

Formally, contact for a raw item in the world (something in **N**, the not-I — everything
that isn't you) is just its value on the **contact interface χ (chi)** at the present
time: χ is the theory's name for the live causal surface where the world meets your
substrate, and κ reads off how hard the world is pushing there. For a *content* (an item
already inside your field), contact traces back through the content's **source map σ
(sigma)** — the bookkeeping that says "this experience came from *that* part of the
world" — to whatever is currently touching you, and takes the strongest such touch. If a
content has no traceable source, its contact reads zero.

> **In plain terms —** don't worry about tracking N, χ, and σ by name on a first read; they just mean *the world outside you*, *the live surface where it touches you*, and *the paper trail of where an experience came from*. The worked example just below is the part that matters.

**Worked example.** You're at your desk. The mug of coffee at your elbow has high κ —
its warmth and weight are pressing on your hand right now, the world is live against your
skin. The same mug, remembered tomorrow on the train, has low κ: nothing is touching you;
you're only picturing it. The mug didn't change. *Your contact with it* did. Same item,
two readings, because κ measures the live touch, not the thing.

> **From the inside —** κ is the difference between *feeling* the rain and *thinking
> about* the rain. One is wet on your face right now; the other is a dry little picture.
> κ is how wet-on-your-face it is.

## φ — Truth-indistinguishability

**φ (phi, "truth-indistinguishability")** — in plain terms, *how impossible it is to tell
this content apart from a true one when you actually scrutinize it.* What holds up under
examination; what you can't deny without tripping over a contradiction. φ is not "how
confident I feel" — it's how well the content survives your best available testing. φ
comes in three tiers:

- **Tier 1 — intrinsic items** (logic, math, pure reason): *outside the φ-scale
  entirely.* They aren't given a score because they're the ruler everything else is
  measured against. You don't ask how true "2 + 2 = 4" is; you measure other things
  *with* it.
- **Tier 2 — the cogito** (the bare fact that you, thinking this, exist): fixed at
  **φ = 1 − δ**, the same for any mind. **δ (delta)** is the single, tiny, fixed
  "perspectival gap" — one unavoidable step between pure universal self-evidence and
  *your* particular indexed "I am." So the cogito scores as high as anything gets without
  being a Tier-1 ruler: maximal, minus that one step. See [The Cogito](the-cogito.md).
- **Tier 3 — everything else**: φ is **you-relative**, set by your current verification
  toolkit. It depends on how many reasoning steps connect the content back toward
  universal structure (each step costs another δ), and how empirically robust it is along
  the way.

The full Tier-3 form is **φ = 1 − nδ − ε**. Unpacked: **n** counts the reasoning steps
between the content and bedrock — more steps, more distance from certainty, more δ's
subtracted. **ε (epsilon)** is the empirical wobble — a small penalty gathered from
poking the content with tests (probes) and seeing where it gives. The more steps and the
more it wobbles, the lower the score.

> **In plain terms —** φ is *how much it would survive you really pushing on it.* "There's
> a wall in front of me" survives a lot of pushing. "That noise means someone's breaking
> in" survives much less. φ is the count of how far you'd have to reason, plus how shaky
> the footing is along the way.

**Worked example.** You hear a creak downstairs at night. The thought "someone is in the
house" might *feel* certain in the moment, but its φ is modest: to back it you'd need
several inference steps (creak → footstep → intruder, each a place where you could be
wrong) and the empirical support is thin (houses creak on their own all the time). Now
flip on the light and *see* the empty hallway — "no one is here" now has high φ: short
path, robust support, hard to deny. The fear didn't track truth. φ does.

**Crucially, φ only applies where you can actually construct a verification pathway from
your current tools.** For a raw feeling whose source you can't trace — a wave of dread
with no nameable cause — there's no chain of steps to count, so **φ is simply
*undefined*** — while κ and ρ still apply. Undefined φ doesn't mean the feeling is fake or
absent; it means the feeling is *real and present but you can't show your work*. (See the
four content classes in [The Two Layers](two-layers.md).)

> **From the inside —** undefined φ is the honest "I don't know why I feel this." The
> dread is fully here (it has its own κ and ρ); you just can't trace it back to anything
> you could check.

## ρ — Identity-correlation

**ρ (rho, "identity-correlation")** — in plain terms, *how much of* you *is bound up in a
thing; the stuff whose loss would actually change who you are.* Not how real it is, not
how loud it is — how *integrated into you* it is. This is the coordinate the theory is
really about, and it has the most structure.

ρ is defined as **flow through a network rooted at the cogito**. Picture your lived self
as a directed graph: the **cogito** (your bare core "I") sits at the center, and every
content you've ever integrated is wired in by **weighted edges** — connections, built up
over your whole history, each carrying a strength between 0 and 1. A content's ρ measures
how much "you-ness" can flow from the core out to it.

The specific way it measures that flow is **max-flow** — the most you-ness that can be
pushed from the center to the content through all the available wiring at once.

> **In plain terms —** imagine your sense of self as water that has to reach a content
> through a tangle of pipes. ρ is how much water can actually get there. A content wired
> to your core by many thick channels drinks deeply; one hanging off a single thin thread
> barely gets wet.

**Why max-flow, and why bottlenecks matter.** Max-flow has a particular feature: it
respects **bottlenecks.** It doesn't care how many fat pipes feed a content if everything
has to squeeze through one narrow neck to get there — the narrow neck caps the whole
flow. The theory chose max-flow precisely because *this matches how fragile self-
integration actually feels.* When a part of who-you-are hangs on a single connection,
that part feels precarious, no matter how much else is going on around it. Cut the one
thread and the whole thing goes.

**Worked example.** Think of someone whose entire sense of being-a-competent-adult runs
through one relationship, or one job, or one skill. On paper their life is rich and
well-connected. But everything that makes them feel like *themselves* has to flow through
that single channel. That's a bottleneck. Max-flow says: the ρ of "being a competent
adult" for this person is capped by that one fragile link — and that is exactly why losing
the job, or the person, doesn't just hurt, it threatens *who they are.* A theory using
"total wiring" instead of max-flow would miss this; it would see all the other
connections and call them safe. Max-flow sees the neck.

> **From the inside —** fragile integration is the feeling that one loss could unmake you
> — that you've routed too much of yourself through one door. That felt precariousness
> *is* a bottleneck in the network. ρ-by-max-flow is built to register it.

**The squash, and why only the core I reaches ρ = 1.** The raw flow to a content is some
number called **C** (capacity) — it can be tiny or large. But ρ is supposed to live on a
clean scale, with the very center pinned at the top. So the theory runs C through a
**squash**: ρ = C / (1 + C). This little formula takes *any* amount of flow, however
huge, and folds it into the range below 1 — a content with enormous flow gets close to 1
but never touches it. Only the cogito itself is set to ρ = 1 by hand, as the anchor the
whole graph is measured from.

> **In plain terms —** *everything that is part of you sits strictly below the top of the
> scale; only the bare "I" sits at the very top.* No memory, no relationship, no body
> part — however central — ever fully *becomes* the core self. They're all part of you;
> none of them *is* the you they're part of. The squash is what guarantees that.

ρ is well-defined for **both conscious and unconscious** contents — a repressed memory you
can't access at all can still have high ρ (it's deeply wired into you) with no defined φ
at all (you can't reason your way to its source). ρ doesn't need you to be looking at
something to measure how much of you it holds.

> **ρ is not valuation.** ρ measures *structural integration*, not what you'd preserve,
> value, or act to protect. The cogito's ρ = 1 is a mathematical anchor, not a claim
> that the core self is what you'd sacrifice everything else for. A parent may, without
> contradiction, hold a child higher in *value* than their own core I, even though the
> child's ρ is below 1 by construction. Integration and valuation are different
> measurements. See [The Two Prerogatives](the-two-prerogatives.md).

## Independent, but entangled

The headline claim is that the three are:

- **Formally non-reducible** — none is definable in terms of the others. In the model
  you can vary one while holding the other two fixed: change the contact interface (χ) and
  only κ moves; change the reasoning profile and only φ moves; change the integration
  graph and only ρ moves. They are *separate dials.*
- **Dynamically entangled** — in a *living* mind they constantly push on each other.
  Sustained contact tends to build integration over time (what you're around a lot tends
  to become part of you); strong integration biases what captures attention (what's part
  of you grabs your eye); high φ can reorganize ρ by making distinctions available; low φ
  can *protect* a high-ρ content from correction (you can't fix what you can't examine).
  These are contingent operating dynamics, not definitions.

> **In plain terms —** the three dials are built independently but they're wired to tug on
> each other once the mind is running. Separate at the workbench; coupled in the wild.

So "three independent coordinates" means **independent at the level of definition,
entangled at the level of dynamics**. A critique that reads the independence as
*statistical* or *causal* independence has misread the claim — the theory is not saying
the three never correlate in practice; it's saying none is *defined* out of the others.

## Why three, not one

The [dissociation cases](the-problem.md) are precisely the configurations where the
coordinates split apart — where a single number couldn't possibly describe what's going
on, because the three readings disagree:

| Case | κ (contact) | φ (truth) | ρ (identity) |
|---|---|---|---|
| Stable embodied content | high | high | high |
| Vivid hallucination | low | high | low |
| Anesthetized limb | low | low | high |
| Alien clear thought | varies | high | low |
| Phantom limb | low | varies | high |
| Repressed memory | varies | undefined | high |

Read a row as a little portrait. A **vivid hallucination** holds up to your reasoning in
the moment (high φ) and isn't really touching the world or wired into you (low κ, low ρ) —
a convincing apparition that's nonetheless not *of* you and not *on* you. An
**anesthetized limb** is deeply yours (high ρ) but you can't feel it and can't currently
verify it as yours from the inside (low κ, low φ) — it's part of you gone quiet. A
**repressed memory** is woven into who you are (high ρ) without any traceable verification
path (undefined φ) and may or may not be pressing on you. A single-scale theory can't
write this table — it would have to call all of these the same kind of thing, or rank them
on one axis that doesn't exist. TLICA's can — and the
[profile](identity-correlation-profile.md) built from these coordinates is its primary
object.

> **From the inside —** you already know these splits. The limb you can't feel but would
> never call "not mine." The thought that's airtight but somehow not *you.* The mood whose
> cause you can't name but that is unmistakably *yours.* Three coordinates is just the
> theory taking those everyday splits seriously.

---

**Applied in:** [Temporal Phenomenology](app-temporal-phenomenology.md) (κ and the felt "now"), [Differentiated Affect](app-differentiated-affect.md) (κ/φ/ρ plus Π and A as affect signatures), and [The Cold Frame](app-referent-routing.md) (the modeling-vs-routing split).

*Next: [The Identity-Correlation Profile](identity-correlation-profile.md)*
