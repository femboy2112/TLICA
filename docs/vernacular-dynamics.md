# Vernacular Dynamics
### The Mathematics of the Sauce

[← Wiki home](README.md) · Source: [`research/vernacular_dynamics_2026-10-12/`](../research/vernacular_dynamics_2026-10-12/README.md) · **Research note · 2026-10-12 · UNVERIFIED**

> **A research-tier experiment, and honest about it.** This is a dated research bootstrap
> (**v0.1.0**), not an application paper and not a result. It asks a playful question seriously:
> when people say a room has a *vibe*, call a comforting thought *cope*, or admit they're *lost in
> the sauce*, are those words picking out real, context-sensitive structure in how someone meets,
> reads, focuses on, and acts in their world — and can TLICA make those distinctions *sharper*
> rather than just restating slang in symbols? The deliverable is **not** a dictionary that tells
> you what a person *is* from one phrase. It is a typed, source-aware list of *candidate*
> mechanisms — including the plain fact that saying the word is itself an act — plus precise
> counterexamples, honest uncertainty, and tests designed to make the pretty story fail.
>
> **The one thing this page is built never to do** is let a slang label masquerade as proof of
> someone's inner state. There is **no diagnosis here, no reading of anyone's mind, no
> person-level verdict** — and the formalism is arranged so that it *cannot* quietly become one.
> It changes **nothing** in the frozen foundation: no new coordinate, no new developmental mode,
> no registered application, no published claim. Everything past the attested-usage lists carries
> its hedge in plain sight.

---

## The seed: slang might be doing real work

The project began as exactly the kind of idea that sounds like a joke until you take it seriously.
The author's originating note (preserved verbatim in the dossier's
[author seed](../research/vernacular_dynamics_2026-10-12/AUTHOR_SEED.md), status **Observed**) proposed
taking terms from the culture — *vibe*, *cope*, *lost in the sauce* — and describing them
"characteristically/mathematically" using TLICA. The title *The Mathematics of the Sauce*, the rival
models, and the manuscript shape are the assistant's proposals, not positions put in the author's mouth.

The charitable, worth-the-effort reading: slang is *compressed*. A word survives in a community
because it reliably points, for its users, at some configuration of experience that would otherwise
take a paragraph. That compression might be tracking something genuine — a recurring shape in how
attention, rapport, belief, or immersion behave — or it might just be a vibe about vibes. The honest
version of the project is the one that can tell those two outcomes apart, and reports when it can't.

> **In plain terms —** We're not assuming slang is deep. We're asking whether some slang *happens
> to* name a real pattern in lived experience, and building the machinery to check — including the
> machinery to catch ourselves if we're just dressing up a hunch in math.

## The one rule that keeps it honest: world, then content, then utterance

Everything downstream rests on a single typing discipline, and it is the **critical safeguard** of the
whole project. Three things that ordinary talk smears together are kept rigidly distinct:

1. **The world** — what actually happened in some episode or task context: the external history, the
   people in it, who said what to whom.
2. **The content** — what a particular *observer* reconstructs from the limited cues they were exposed
   to. Exposure is a measurement; interpretation is a decoding; both are indexed to *that* observer,
   their toolkit, and their history. Two observers can decode the same smile as "warmth" and
   "courtesy."
3. **The utterance** — the act of *saying the slang word*. A label like "good vibes" or "that's cope"
   is itself another event in the world. If someone observes it, they decode *it* too — but it is a
   speech act (a report, an alignment signal, a joke, a dismissal, an **accusation**), and the person
   being labeled need not endorse the label at all.

Because these are separately typed, a sentence like "you're just coping" can never be silently promoted
into a fact about the target's mind. The utterance is data about the *speaker's act*; the target's
actual interpretation, commitment, and belief-updating are different objects entirely, reached — if at
all — only by their own evidence. This is the world-first typing discipline the dossier borrows as a
**proposed compatibility rule** from the draft [TLICA–EPIC](tlica-epic.md) work (see
[the compatibility promise](#what-it-borrows-and-what-it-refuses-to-borrow) below).

> **In plain terms —** What happened, what someone *thinks* happened, and what someone *says* about it
> are three different things. Keeping them apart is the entire trick that stops this from becoming a
> machine that reads minds off of catchphrases.

## Why a slang label can't be a readout of someone's mind

The refusal to read minds isn't just a promise of good manners — it's forced by an elementary argument,
stated as finite propositions in the
[formalism](../research/vernacular_dynamics_2026-10-12/FORMALISM.md). None of these are empirical
discoveries; they are standard facts about functions and finite sets, flagged **Disclosed** inside
their model and nothing more.

Collect a finite catalogue of rival explanations and a finite family of probes you could actually run.
Map each rival to the bundle of results it would predict across those probes — its **observation
fiber**. Two rivals that predict *identically* on everything you can check fall into the same
**observational equivalence class**. That quotient is legitimate, but it says *nothing* about whether
the true explanation is even in your catalogue.

- **Proposition 1 (non-identification).** If two distinct candidate states produce the *same*
  observation yet disagree on some target property, then no function of that observation alone can
  recover the property correctly for both — because equal inputs force equal outputs. In particular,
  *the same slang token can be consistent with different underlying mechanisms.* **(Disclosed.)**
- **Corollary (finite compression).** A coarse label map from many distinct inner states onto few
  words must collide (pigeonhole). The collision alone never tells you which rival was right.
- **Proposition 2 (fixed-model refinement).** Adding compatible, fixed observations can only *shrink*
  the set of surviving candidates, never grow it — *as long as* the catalogue, the source
  interpretation, and the observations are held fixed. New senses, repaired source maps, or withdrawn
  testimony legitimately break that premise, so real-world updating need not be monotone. **(Disclosed.)**
- **Proposition 3 (contextual non-invariance).** Identical exposed signals need not yield identical
  labels when the decoders differ by observer or context. This is *permitted* by the model; showing it
  actually happens in people would require data. **(Disclosed.)**

> **In plain terms —** If two different inner situations would look exactly the same from the outside,
> no amount of cleverness recovers which one you're facing from the outside view alone. A word that
> compresses many states into one is *guaranteed* to blur some of them. That's a theorem about the
> setup, and it's why the label can never be the proof. See [other-minds](other-minds.md) for the same
> discipline applied to minds in general.

## Three words, three different shapes

A key finding of the lexicon draft is that these three expressions do **not** share one structure — they
need different machinery, and conflating their senses is exactly the mistake to avoid. Each entry in
[LEXICON_V0](../research/vernacular_dynamics_2026-10-12/LEXICON_V0.md) separates attested usages, a
candidate TLICA reading, an observable discriminator, a negative control, and its claim status. The
examples are invented; none of them are corpus statistics.

### Vibe — an observer's low-dimensional snapshot

*Attested usages:* the mood or atmosphere of a person or place; getting along with someone; relaxing
into an activity. (It is also sometimes used for prejudicial exclusion — an impression can be biased
rather than perceptive.) *Candidate structure:* an observer decodes a few cues and emits a coarse,
context-indexed readout. A "good vibe" might be reciprocal rapport, polite masking, shared rhythm, or
mere personal preference — one label collapsing hidden relational differences. *Split probe:* compare
the instant global label against separately consented, task-specific signals (did they voluntarily come
back? did they independently report comfort?). *Negative control:* two people both report "good vibes"
while one is strategically polite and never seeks another interaction — equal labels, unequal warmth;
conversely, blunt talk can be respectful despite a bad first vibe. *Status:* the non-identification
result is **Disclosed** within its finite model; the specific psychological decoding channels are
**UNVERIFIED**.

### Cope — three objects wearing one word

*Attested usages:* ordinary handling of adversity; a *supposed* self-protective rationalization; and an
online dismissal or insult, often with no argument attached. *Candidate structures, kept separate:*
(A) adaptive coping that lowers distress while leaving reality-testing intact; (B) defensive
reinterpretation that preferentially keeps an identity-relevant belief *despite credible,
independently verified* disconfirmation; (C) rhetorical "cope" — a speaker's act of discrediting
someone, which is a fact about the *speaker*, not the target. *Split probe:* compare independently
recorded belief-updates before and after vetted corrective evidence versus matched low-diagnosticity
evidence; pre-register what counts as an update. *Negative control:* grieving while accurately
acknowledging the loss is coping, not self-deception; calling a sound argument "cope" demonstrates an
utterance, not a refuted rebuttal; refusing weak evidence is not defensive rationalization. *Status:*
the sense distinction is **Observed** in the source material; the proposed identity-mediated pathway is
**CONJECTURED**; the human predictions are **UNVERIFIED**. Belief preservation is not automatically
deception, and an accusation is never proof of the recipient's mind.

### Lost in the sauce — immersion is not the same as disorientation

*Attested usages:* confused and out of depth; blissful or ecstatic immersion; intoxication; or being
excessively absorbed in success, desire, or some other high-reward environment. *Candidate structures:*
in the *absorption* usage, focal resources stay committed to a narrow set of contents over time; in a
**distinct** *disorientation* usage, corrective probes toward a predeclared goal become ineffective or
delayed. Crucially, **high focus occupancy by itself is not dysfunction** — the same profile can make
creative flow possible and remain perfectly correctable. *Split probe:* in a low-stakes consenting
task, separately measure sustained engagement, response to a scheduled checkpoint, retrieval of a prior
goal, and task performance. *Negative control:* absorbed research that pauses and checks its goal on
request is not disoriented no matter how many hours passed — and someone may *jokingly* call that state
"lost in the sauce" anyway, a true pragmatic usage without the disorientation mechanism. *Status:* the
multiple senses are **Observed** in definitions; the geometric/metacognitive dynamical explanation is
**CONJECTURED**; the behavioral claims are **UNVERIFIED**.

A further queue — *based, cringe, touch grass, down bad, delulu, cooked, rent free, main character
energy* — is listed as **proposed next lexemes**, explicitly *not* validated entries. The stated
intent: keep the humor and the shifting meanings; do not build a moral sorting machine.

> **In plain terms —** "Vibe," "cope," and "lost in the sauce" don't behave alike. Treating them as one
> kind of thing is the error. Each needs its own candidate mechanism, its own way to be caught out, and
> its own list of perfectly innocent cases that look identical from outside.

## The toy instrument: ten passing tests that prove almost nothing (on purpose)

The dossier ships a small, standard-library Python program,
[`finite_lexicon.py`](../research/vernacular_dynamics_2026-10-12/finite_lexicon.py), with a test suite
that **passes 10/10** (plus `py_compile`), recorded in
[VALIDATION](../research/vernacular_dynamics_2026-10-12/VALIDATION.md). It is essential to read what that
number does and does not mean.

The program works on **invented worlds** — seven hand-authored candidate states across the three terms,
no transcripts, no demographics, no human participants, no learned classifier, no probabilities. It does
three finite-bookkeeping jobs: keep only the rivals compatible with a set of observations; count how many
*pairs* of rivals a given probe actually distinguishes (an unknown prediction never counts as a split);
and build an operational equivalence class *only* from complete predicted signatures — asking for one
from partial predictions deliberately raises an error. In miniature: a surface "vibe" label leaves two
rivals standing, a "cope" token leaves three, and in each case it is the discriminating probe that pulls
them apart.

It also carries a **mutation control**: a deliberate change makes two "sauce" candidates predict the same
checkpoint result, dropping the distinguishing pairs from 1 to 0 — and a test *detects that change*. That
is the suite proving it can tell when its own conclusion should flip.

Cite the 10/10 for exactly what it is and nothing more: a **synthetic, toy instrument** confirming the
internal consistency of *this finite bookkeeping*, from **one local execution**. It is **not** evidence
that any slang word detects a human mechanism. The full-repository `make validate`, the link audit,
branch-level CI, and independent re-runs were **not executed** (the isolated container had no DNS), and
the dossier says so out loud rather than rounding up.

> **In plain terms —** The tests pass, and that's genuinely nice, but all they check is that the math
> toy is consistent with itself on made-up examples. No real person was measured. A green checkmark here
> is a sanity check on the bookkeeping, not a discovery about people.

## How it is designed to fail

The project's seriousness lives in its [probe protocol](../research/vernacular_dynamics_2026-10-12/PROBES.md),
which is a *preregistration sketch* for later, consented, ethics-reviewed studies — **no human studies or
real-corpus evaluations have been run.** It predeclares four rival models and makes the proposed TLICA
reconstruction earn its place against all of them:

- **M0** — a lexical baseline (the surface word and local sentence).
- **M1** — a context baseline (speaker role, surrounding discourse, community, task).
- **M2** — a behavior-only baseline (observable actions, no TLICA coordinates).
- **M3** — the proposed typed TLICA reconstruction (world/source separation, observer decoder, a candidate
  identity-integration pathway, and a correction probe).

**The discriminating criterion is blunt:** if M3 does not improve held-out sense prediction, calibrated
abstention, or out-of-context transport over M1/M2 *without* unacceptable complexity or bias, the
incremental TLICA claim **fails**. "A model that simply gives every situation a new sense is not allowed
to win by redescription." Each term gets its own pass/fail/ambiguous gates and a battery of negative
controls — masked discomfort, kind-but-blunt interaction, false accusation, sincere disagreement,
absorbed-but-correctable flow — so the fun story has somewhere to die. The eventual verdict-changing
instrument is a randomized vignette set crossing label (present/absent) × known behavioral evidence
(supporting/contradicting) × context (congruent/shifted) × speaker role (self-report/accusation), with
every rival's prediction fixed in advance and no post-hoc rescue.

> **In plain terms —** Before anyone collects data, the project writes down what would prove it *wrong* —
> including the demand that the fancy TLICA version beat plain, boring baselines. If it can't, it loses.
> That's the opposite of a theory that explains everything and predicts nothing.

## What it borrows, and what it refuses to borrow

The [reconciliation note](../research/vernacular_dynamics_2026-10-12/RECONCILIATION.md) and
[source ledger](../research/vernacular_dynamics_2026-10-12/SOURCES_AND_LEDGER.md) draw the dependency
lines exactly. The genuinely new thing here is **project packaging and typed research questions** — not
any mathematical discovery. What it leans on is existing TLICA: the observer→world→exposure→decoding→
response loop (Semantic Optics), the coordinates and their meanings, source maps, probe discrimination,
and the cultural-transport discipline.

And it is scrupulous about the [coordinates](three-coordinates.md) (full definitions in the
[glossary](glossary.md)). It refuses to repurpose any of them:

- **ρ** (rho) is identity **integration** — *not* belief certainty, value, or emotional intensity.
- **κ** (kappa) is contact — *not* validation.
- **φ** (phi) is toolkit-relative truth-*indistinguishability* — *not* an accuracy probability. If there
  is no constructible verification path, φ is **undefined**, not zero.
- **σ** source correctness, **A** phenomenal availability, **μ**, and **S** slack stay separately typed;
  slack is not μ, and the "two layers" are not developmental Modes A/B.

**Neither a person's utterance nor its social reception fixes their φ or ρ values.** The proposed lexicon
is a *research-tier semantic interface* sitting over existing TLICA dynamics — not a fourth foundational
coordinate.

On [TLICA–EPIC](tlica-epic.md): that work is a **draft, not part of main**, and the dossier borrows only
its world-first typing *discipline* as a proposed compatibility rule — not its unmerged DSL or executable
reader. Nothing is declared a literal EPIC node until its world/content distinction type-checks against a
final accepted standard. The design is **compatible-by-design with, but not dependent on**, that draft.

> **In plain terms —** It reuses TLICA's existing parts and is careful not to secretly redefine any of
> them to make the story work. The borrowed symbols keep their old, strict meanings — a word about someone
> never gets to set that someone's coordinates.

## Claim-status summary

Nothing on this page outruns its evidence. Carried faithfully from the dossier's ledger:

- **Observed** — the author's seed proposed these three lexemes within TLICA; multiple meaning families
  appear in the surveyed dictionary entries (source-bounded); and the finite code's authored fixtures
  pass 10 calibration tests plus the mutation check (one local execution).
- **Disclosed** — the three elementary propositions (non-identification, fixed-model refinement,
  contextual non-invariance) and the operational-quotient definition, each true only inside its stated
  finite model.
- **Conjectured** — that *vibe* is usefully reconstructed as an observer-indexed compressed
  interpretation; that defensive *cope* involves a TLICA-specific identity-update coupling; that
  sauce-disorientation is captured by correction/reorientation latency.
- **Conjectured / UNVERIFIED** — the human-mechanism readings of *cope* and *lost in the sauce*
  specifically.
- **UNVERIFIED** — that TLICA adds explanatory or predictive power over ordinary pragmatics/behavior
  models, and that a transport/naturality contract holds across dialects. All human predictions sit here.

**Novelty audit (as stated):** no novel general theorem, no validated psychological construct, no standard
taxonomy, no causal law, and no publishable effect has been established. The potential usefulness is a
*falsifiable, source-aware design pattern* integrating existing ingredients — nothing more.

**Foundation impact: none.** No new coordinate, no new developmental mode, no application registration, no
change to the frozen foundation, the documentation wiki's claims, or any published material. This is a
dated research bootstrap, and it stays one until held-out, multi-community evidence either earns it a
promotion or refutes its supposed advantage.

---

*Source dossier: [`research/vernacular_dynamics_2026-10-12/`](../research/vernacular_dynamics_2026-10-12/README.md)
— read the [formalism](../research/vernacular_dynamics_2026-10-12/FORMALISM.md),
[lexicon](../research/vernacular_dynamics_2026-10-12/LEXICON_V0.md),
[probes](../research/vernacular_dynamics_2026-10-12/PROBES.md), and
[ledger](../research/vernacular_dynamics_2026-10-12/SOURCES_AND_LEDGER.md) for the full detail and every
hedge in its original form.*
