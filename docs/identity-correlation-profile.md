# The Identity-Correlation Profile

[← Wiki home](README.md) · Source: [File 3, §7.6](../foundation/3_formal_apparatus.md)

---

The architecture's **single most important object** is not any one coordinate value. It
is the **identity-correlation profile**: the complete map of ρ-values across your entire
field at a moment in time.

**ρ (identity-correlation)** — in plain terms, how much of *you* is bound up in a given
thing; the degree to which some content (your hand, a belief, a friend, a passing sound)
has been woven into the network you live as "me." A thing with high ρ is one whose loss
would actually change who you are; a thing with ρ near zero is part of the world but not
part of you.

> **P** = { (content, its ρ-value) : for every content in your field }

In the source this is written more compactly as

> `P_{m,t} = { (x, ρ_{m,t}(x)) : x ∈ A_{m,t} }`

which reads: for a given mind **m** at a given time **t**, list every content **x** in
your field (your **asymptotic field** `A_{m,t}` — the whole reach of what's
available to you, near and far) paired with how deeply that content is woven into you.
Equivalently it's a single function `ρ_{m,t}` that hands back a number in the range
`[0, 1)` for everything — strictly *below* 1 for everything that isn't the bare cogito,
and exactly 1 only at `Î`, the cogito-I itself (the "I am" at the dead center).

> **In plain terms —** the profile is a snapshot of your whole self at once: not "how
> integrated is my job," but the entire terrain of everything you're touching right now,
> each thing tagged with how much it is *you*. The "I am" is the one point that scores a
> perfect 1; nothing else in the world ever quite reaches it.

Read it as a landscape. There's a single peak at the cogito (ρ = 1), high ground for the
contents most deeply woven into you (your body, central commitments, defining
relationships and projects), gentle slopes for peripheral integrations, and a vast
lowland approaching zero — the strict not-I, the world that doesn't touch you.

### A worked profile

It helps to picture one concrete person at one ordinary moment. Suppose you're sitting at
your kitchen table on a Tuesday morning. Your profile right then might look like this:

- **The peak (ρ = 1):** the bare fact that you *are* — the "I am" you can't get behind.
  This is the only true summit; everything else is foothills.
- **High ground (ρ very high, but still under 1):** your own body and its felt
  ongoingness; your child, asleep upstairs; your sense of yourself as honest; the work
  you've staked years on. These are the contents whose loss would not just hurt — it
  would *rearrange who you are*.
- **Mid-slopes (moderate ρ):** the friend you text most weeks; your morning routine; the
  city you've lived in long enough to feel partly made of. Real, but you'd survive their
  loss as recognizably the same person.
- **Gentle foothills (low ρ):** a podcast you half-follow; an acquaintance's name; the
  novel on the shelf you keep meaning to finish.
- **The lowland (ρ → 0):** the coffee mug, the traffic outside, a stranger three streets
  over. Present in your field, but not woven into you at all — the **strict not-I**.

> **From the inside —** stand in your kitchen and ask, thing by thing: *if this vanished,
> would it change who I am, or just what I'm doing?* The honest answers, laid side by
> side across everything at once, are your profile. It isn't a list of what you like — a
> mug you love can still be lowland, a relationship you resent can still be high ground.

## Why the *profile*, not single values

A single ρ-value is a projection — one content's height on the landscape. The theory's
actual predictions are about the **shape of the whole map**, because:

- **Two minds with similar substrates and histories tend to have similarly-*shaped*
  profiles** — even though the specific values differ. (This is "form-invariance
  conditional on existence": the structure generalizes; the numbers are personal.)
- **Disturbances are shape changes, not magnitude changes.** Two very different
  conditions can share the same average ρ. What distinguishes them is *where* ρ is high
  and low, how integration is distributed, how it lines up with **κ** and **φ**. See
  [Profile-Shape Disturbances](profile-shape-disturbances.md).
- **Development is the profile filling in.** The newborn's profile is nearly empty
  (everything undifferentiated or near zero); the mature profile is richly populated with
  characteristic structure. See [Modes of Development](modes-of-development.md).

A note on the two companion coordinates just named: **κ (salience-correlation)** — in
plain terms, how *present* a content is to you right now, how much it's lit up in
attention and contact (the loud noise that just grabbed you has high κ; the friend you
haven't thought of all day has low κ even though their ρ stays high). **φ
(verification-access)** — in plain terms, how well you can trace a content back to its
source or check it (a worked sum has clear φ; a wave of dread you can't account for has
undefined φ). The profile is about ρ, but its *shape* only makes sense alongside how
present and how checkable each region is.

> **In plain terms —** don't ask "what's my ρ?" as if it were one number, like a weight.
> Ask "what does my whole map look like?" Two people can carry the same total amount of
> self-investment and live utterly different lives — what matters is *where* the
> investment sits, and how that lines up with what's lit up (κ) and what's source-clear
> (φ). The pattern is the person.

### Form-invariance conditional on existence

This is the load-bearing reason the theory works on *shapes* rather than *numbers*. The
claim is: any two minds that ran on similar hardware and lived broadly similar histories
will end up with profiles built to the same general *pattern* — a peak at the cogito,
high ground around body and core attachments, a long lowland of not-I — even though no
two people share the same exact ρ-values anywhere. "Conditional on existence" is the
crucial hedge: the shared structure only holds *given that* such a mind exists and got
built at all. The form is common property; the contents and their precise heights are
yours alone.

> **In plain terms —** the general layout of a self is the same for everyone, the way
> every human face has two eyes, a nose, and a mouth in roughly the same places — but no
> two faces, and no two profiles, are actually identical. The theory predicts the layout,
> not the specific face. So it can say true things about *anyone's* self without ever
> needing to know your particular numbers.

## Shells: a convenient picture, not a primitive

It's natural to draw the self as concentric **shells** around the cogito — innermost,
the contents currently lived as "me"; then the stably integrated body; then deep
commitments and memories; then peripheral interests; then contents merely in awareness;
then strict not-I at the edge. These shells are useful for visualizing, but they aren't
fundamental — they're just **contour bands of the profile**, the landscape sliced at
ρ-thresholds. The continuous profile is the real object; the shells are its contour map.

Formally, the shells are the profile coarse-grained onto threshold bands
`r_0 < r_1 < … < r_n` — you pick a few cutoff heights and group every content by which
band its ρ falls into. (One of those cutoffs has special meaning: the **lived-I network**
is just the part of the profile where ρ > 0 — everything that touches you *at all* — and
strict not-I is where ρ drops to zero.)

> **In plain terms —** shells are like the brown contour lines on a hiking map. The
> mountain is one continuous slope; the lines are just heights someone chose to draw so
> you can read it at a glance. Talking about "my inner circle" versus "my outer circle"
> is convenient, but the truth underneath is a smooth gradient with no real walls between
> the rings. Don't mistake the contour lines for cliffs.

## The vector underneath

ρ is actually computed across several **integration modes** at once (different ways a
content can be bound in), so the fullest form of the profile keeps a *vector* of ρ-values
per content, not a single scalar. The scalar profile is a weighted projection of that
vector. The vector form is what carries the finest structural detail.

In the source the full version is written

> `P_vec_{m,t} = { (x, ρ_vec_{m,t}(x)) : x ∈ A_{m,t} }`, with
> `ρ_vec_{m,t}(x) = ( ρ^{m,k}_t(x) )` for each mode k in K

— meaning each content **x** doesn't get one ρ-number but a little tuple of them, one per
integration mode **k** (the arrow over ρ just marks that it's a vector, a list of values
rather than a single value). The familiar single-number profile is what you get when you
blend that tuple down into one weighted average.

> **In plain terms —** something can be part of you in more than one way at once — woven
> in through your body, through your beliefs, through your habits and feelings. The honest
> bookkeeping keeps each of those threads separate per thing, then sums them into the one
> headline number you usually see. Two people can land on the same headline ρ for "my
> father" while the threads underneath — bodily, cognitive, emotional — are braided
> completely differently. The braid is where the real detail lives.

## What the profile is — and isn't

The profile encodes **structural integration**. It is **not** a valuation map and **not**
a preservation-priority ranking. The peak at the cogito is the anchoring root of the
flow network, not a statement about what you'd protect first. What you'd *act* to
preserve under pressure depends on separate dynamics — see
[The Two Prerogatives](the-two-prerogatives.md).

> **In plain terms —** "deeply part of me" is not the same as "what I'd save from the
> fire." The profile measures how the self is *built*, not what it would *fight for*. The
> peak sits at the cogito for a mathematical reason — it's the root the whole flow gets
> measured from — not because the bare "I am" is the thing you value most. People
> routinely sacrifice themselves for someone with high ρ who isn't at the peak; that
> behavior lives in a different part of the theory, not in this map.

---

*Next: [Access to Intrinsic Structure](access-to-intrinsic-structure.md) · [Modes of Development](modes-of-development.md)*
