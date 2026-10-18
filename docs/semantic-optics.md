# Semantic Optics

[← Wiki home](README.md) · Source: [`research/semantic_optics_2026-10-01/`](../research/semantic_optics_2026-10-01/README.md) · **Research note · 2026-10-01 · UNVERIFIED · foundation untouched**

> **What this is.** A research-tier *umbrella* dossier, written up for the wiki. It takes a
> pattern the archive kept running into separately — cinema, political "vibe," reputation,
> institutions, comedy, ordinary social reading — and proposes that they are all the *same typed
> shape*: a situation gets exposed, somebody reconstructs it, they act, and the world changes.
> It then asks whether a specific piece of standing mathematics — **categorical optics**, and the
> **categorical cybernetics** built on top of them — is the right language for that shape, and
> whether TLICA adds anything the generic machinery doesn't already supply. It **composes existing
> machinery**: it introduces **no new foundation coordinate, mode, prerogative, or law**, and
> changes nothing in the frozen core.
>
> **What it is careful never to claim.** It does **not** claim a proven categorical equivalence
> between TLICA and optics. The headline "Yoneda moonshot" is a stated *target*, not a theorem —
> every TLICA-specific equivalence claim in it is **UNVERIFIED**. The computer checks that *have* run
> are finite construction-level consistency witnesses; they say **nothing** about human cognition,
> politics, or cinema. And "semantic optics" is explicitly **not** a new scalar coordinate alongside
> κ/φ/σ/ρ/μ. Everything past the surface keeps its hedge in plain sight.

---

## The loop everybody already knows

Ask "how does this look?" and you have already smuggled in several different objects. Pull them
apart and a loop appears that is the same whether you are watching a film, reading a politician, or
judging a stranger across a table:

`realized situation → exposed evidence → reconstruction → response → updated situation`

Written with the moving parts named:

- the **proper situation** `x` — what is actually the case, including the parts nobody can see;
- an **observation map** `Oⱼ` — the interface that exposes only *some* of `x` to observer `j`;
- the **available evidence** `yⱼ = Oⱼ(x)` — the quote, the camera frame, the visible action, the dashboard number;
- a **decoder** `Dⱼ` — the observer's learned reconstruction machinery, which runs on their own state;
- the **reconstructed object** `ẑⱼ = Dⱼ(yⱼ; Θⱼ)` — what the situation *becomes* for that observer;
- a **response policy** `πⱼ` turning the reconstruction into an action `aⱼ`;
- a **world-update** `F` that returns the action to the shared world, producing the next `x`.

The smallest one-way object here — call it a **semantic optic** — is just the composite
`Ωⱼ = Dⱼ ∘ Oⱼ`: situation in, reconstruction out. But the interesting object is the whole closed
loop, because the reconstruction drives an action and the action changes the next reality to be
read.

> **In plain terms —** nobody reacts to the world. They react to their *reconstruction* of the
> slice of the world they were shown. Then they act on that reconstruction, and their action is
> now part of the world the next person has to read.

This is what makes the object cross-family. The content differs wildly between a sitcom and a
parliament; the *interface pattern* is identical.

---

## Three things that must never be collapsed

The decoder runs on **observer state** `Θ` — history, conceptual toolkit, learned distinctions,
source map, current context, available probes, focus, role knowledge, identity coupling. Because of
that, three levels in the loop are genuinely different objects and the whole framework depends on
keeping them apart:

1. **Proper state** `x` — what is instantiated inside the declared decision boundary. The formalism
   does *not* assert anyone has direct access to this.
2. **Available evidence** `y = O(x)` — only what the interface exposes. Different interfaces expose
   different projections of the same `x`.
3. **Reconstructed object** `ẑ = D(y; Θ)` — what the evidence *becomes* once a particular observer
   decodes it.

Two failures of one-to-one-ness fall straight out, and they are the archive's two oldest "optics"
phenomena:

- **Optic collapse** — distinct proper situations become indistinguishable at the interface:
  `x₁ ≠ x₂` yet `Ωⱼ(x₁) ≡ Ωⱼ(x₂)`. Repository specimen: *Cold Frame*, where genuinely different
  inner structure can produce behaviorally identical conduct while a field holds.
- **Optic splitting** — one fixed situation becomes *different* reconstructed objects under
  different learned bases or roles: `Ωᵢ(x) ≠ Ωⱼ(x)`. Repository specimen: *Shared Reality,
  Divergent Maps*, where one public token is decoded differently across citizens.

> **In plain terms —** two different realities can look the same (collapse), and one reality can
> look like two different things to two different people (splitting). These are not the same bug,
> and a theory that blurs them loses the plot.

---

## Six things that go wrong (the basic phenomena)

The dossier catalogues six distinct behaviors of the loop, offered as **definitions / structurally
coherent descriptions**, not proven empirical mechanisms:

- **Collapse** / **Splitting** — the two one-to-many failures above.
- **Occlusion** — some load-bearing part of the causal structure lives only in the *hidden residual*
  and never reaches the exposed view. Specimen: [distributed institutional realization](distributed-institutional-realization.md),
  where local behavior looks discontinuous because its predictive support sits outside the local frame.
- **Steering** — an actor chooses an intervention partly by *predicting its reconstruction*. This
  spans benign explanation, staging, politeness, filmmaking, PR, and deception alike; the formalism
  deliberately does **not** morally equate them.
- **Recursion** — the reconstruction produces an action that changes the next state, so the audience's
  reading becomes material inside the ongoing performance. Specimen: Kaufman-style classification
  perturbation.
- **Adversariality** — an actor deliberately hunts for an `x'` that changes a favored observer's
  reconstruction *while a declared proper-state invariant stays fixed*.

That last one lets "pure optics management" be made precise. Fix a task invariant `R_τ`. An
intervention is **task-pure optic steering** when `R_τ(F(x,u)) = R_τ(x)` yet `Ωⱼ(F(x,u)) ≠ Ωⱼ(x)` —
the declared task-relevant reality is untouched while its reconstruction moves. Because this is
defined *only relative to the declared invariant*, it blocks two lazy inferences (**Disclosed as
definition**): "optics changed" does **not** imply "reality unchanged in every respect," and "reality
changed" does **not** imply "optics changed" (a real reform can be causally important and locally invisible).

---

## "Good optics" is not one number

A central negative result: there is no single scalar called *good optics*. At minimum these six
quantities move independently, so collapsing them is **Refuted as a formalization**:

| quantity | what it measures |
|---|---|
| **fidelity** | how well the reconstruction preserves a declared proper-state invariant |
| **legibility** | whether the observer can recover the structure the present task needs |
| **favorability** | whether the reconstruction elicits a desired response |
| **robustness** | whether reconstruction survives channel / context / viewer changes |
| **manipulability** | how cheaply the reconstruction can be shifted with the invariant held fixed |
| **source adequacy** | whether the observer attributes the evidence to the correct source |

So `favorable ≠ faithful ≠ legible ≠ robust ≠ correctly-sourced`. This is exactly the discipline the
rest of the theory already enforces, and the page keeps the TLICA quantities **typed and separate**:
**κ** (contact), **φ** (toolkit-relative truth-indistinguishability / pathway state), **σ** (source
map and its *separately audited* adequacy), **ρ** (identity / commitment integration), **μ** (probe
availability / weighting), plus toolkit closure, coherence, independence, and discrimination. See
[three-coordinates.md](three-coordinates.md) and the [glossary.md](glossary.md).

> **In plain terms —** "looks good," "is accurate," "is understandable," "holds up when re-shot,"
> "is easy to spin," and "is pinned to the right source" are six different dials. They are routinely
> confused, and most arguments about "optics" are really arguments about which dial someone means.

The optic is an **interface / process object**. The TLICA quantities *constrain or decorate* the
decoder occupying that interface — they are not a score the optic hands back. For that reason, adding
"semantic optics" as a new foundation coordinate is **NOT CLAIMED and currently disfavored**:

`Ω ≠ f(κ, φ, σ, ρ, μ)` as one universal scalar.

---

## Why a piece of pure category theory walks in here

The strongest *mathematical* clue is that someone already built the bidirectional interface shape, for
unrelated reasons. For a symmetric monoidal category `(𝒞, ⊗, I)`, Mitchell Riley's optic is the coend

$$\mathbf{Optic}_{\mathcal C}\big((S,S'),(A,A')\big)=\int^{M}\mathcal C(S,\,M\otimes A)\times\mathcal C(M\otimes A',\,S')$$

A representative is a forward map `l : S → M ⊗ A` and a backward map `r : M ⊗ A' → S'`, where `M` is
*residual scratch space* — information kept from `S` so that `S'` can be reconstructed later — and the
coend quotient stops that private residual from becoming part of the optic's public identity. (Riley,
*Categories of Optics*, arXiv:1809.00738.) The semantic reading of the type dictionary is unusually
clean, and is a **Conjectured interpretation** (not proven to hold under composition in every domain):

| categorical optic | semantic reading |
|---|---|
| `S` | current proper situation |
| `A` | exposed evidence / view |
| `M` | hidden residual causal/contextual state |
| `A'` | response returned through the interface |
| `S'` | updated proper situation |
| `l` | observation / presentation split |
| `r` | world-update using retained context + response |

> **In plain terms —** category theorists needed a tidy way to say "take a thing apart, keep a stub
> of what you removed, act on the visible part, then reassemble." That is the shape of exposing a
> situation, letting someone react, and feeding the reaction back into the world. Structural, not a pun.

The genuinely useful move is the **"hole."** Riley reads an optic diagram as having a gap you can drop
a process into. Give the optic as `ω = [M, l, r]` and a controller `c : A → A'`, and closing the hole
yields a single process `S → S'`:

$$\mathrm{cl}_c(\omega)=r\circ(\mathrm{id}_M\otimes c)\circ l$$

For semantic optics this is a clean division of labor: **the categorical optic supplies the
bidirectional world/interface shell; TLICA supplies a structured account of the process that occupies
the hole.** That is a sharper and more honest claim than "TLICA *is* an optic." Treating TLICA
observer/controller state as the hole-process is **CONJECTURED** — a strong type match, with no proof
of categorical or empirical completeness.

One small thing *is* proved. The closed behavior does not depend on which residual representation you
chose: if two representatives are related by an `f : M → N` in the standard coend way, then
`r ∘ (id ⊗ c) ∘ l = r' ∘ (id ⊗ c) ∘ l'` for every hole process `c`. **Status: Disclosed, conditional
on the standard optic/coend construction.** It matters because hidden context must not become
semantically significant merely because we picked one internal encoding over an equivalent one.

A refinement is flagged as a **Conjectured design choice**, not settled: the forward and backward
channels probably want to live in *different* categories (mixed / enriched optics, Clarke et al.,
arXiv:2001.07488) rather than being forced into `Set`.

---

## The shell is borrowed — TLICA lives in the hole, if anywhere

A primary-source pass sharpened the target and, importantly, *shrank the novelty claim*.
**Categorical cybernetics** (Capucci, Gavranović, Hedges, Rischel, arXiv:2105.06332) already combines
the `Para` and `Optic` constructions into **parametrised optics**: residuals and parameters carry
private agent state/memory, and reparametrisations carry agency dynamics. The preferred target is
therefore no longer bare optics but a TLICA-typed region of parametrised optics:

$$\mathsf{TLICAOptics}\ \stackrel{?}{\simeq}\ \mathsf{CyberOptics}^{\mathrm{TLICA}}\ \subseteq\ \mathbf{Para}(\mathbf{Optic})$$

This cuts both ways, and the dossier is blunt about it. The frameworks it leans on are
**Source-supported / established external mathematics** (categorical cybernetics; Bayesian lenses,
Smithe arXiv:2006.01631; open games, Ghani et al. arXiv:1603.04641; Structured Active Inference,
Smithe arXiv:2406.07577). And precisely because that territory is already occupied, the generic
claims are **Refuted as novelty-shaped**: "bidirectional controller/world dynamics is a new TLICA
contribution" and "system + interface + controller + feedback is a new TLICA architecture" are **not**
things TLICA gets to claim.

> **In plain terms —** the feedback-loop machinery is not ours and we don't pretend it is. The
> honest question left is narrower: once you strip out everything the generic parametrised-optic
> machinery already does, does TLICA's *semantic typing of the observer's state* buy any held-out
> prediction the generic model can't?

The surviving **CONJECTURED / UNVERIFIED** candidates for genuinely TLICA-specific structure are the
distinctions a generic parameter object leaves abstract: **probe-closure semantics** (no constructible
verification path vs available-but-low-weight probe vs source-map defect vs identity-coupled resistance);
**source-map semantics (σ)** ("correct evidence, wrong source" vs "wrong evidence, correct source");
**identity/commitment coupling (ρ)** (changes stakes and update dynamics *without* being truth evidence —
the firewall is not automatic); **toolkit-relative representation** (one interface, different learned
bases); and **restricted-Yoneda probe adequacy** (below). Whether any of these adds non-redundant
predictive value over a generic baseline is the dossier's **UNVERIFIED flagship discriminator** — no
such test has been run.

---

## The Yoneda moonshot — an aim, not a theorem

The slogan "TLICA-optics and categorical optics are *Yoneda equivalent*" is, as stated, **not yet a
mathematical claim at all** — and the dossier says so explicitly. Yoneda's lemma — that the embedding
`y : 𝒞 → [𝒞ᵒᵖ, Set]`, `X ↦ 𝒞(−, X)`, is full and faithful — is **Disclosed standard mathematics**,
but it is a statement about *one* category. It does **not** automatically compare two independently
defined categories. To do that you first need a comparison functor `F : TOpt → Optic_𝒞`, which nobody
has built. With it, the moonshot becomes a ladder of progressively stronger, and all **UNVERIFIED**,
targets:

- **Moonshot A — embedding.** `F` is full and faithful on a declared subcategory, so TLICA-optics is a
  genuine *granularized realization* of a subfamily of categorical optics. Currently the most
  plausible strong target.
- **Moonshot B — equivalence.** Additionally essentially surjective, giving `TOpt ≃ Optic_𝒞`. This is
  the literal equivalence target and is probably too strong globally.
- **Moonshot C — probe/Yoneda reconstruction.** TLICA objects are recoverable from their complete
  compositional probe profiles and the bridge preserves them — a representation *certificate*, not a
  notation match.

> **In plain terms —** "Yoneda equivalent" is being used as an *aspiration*, not a result. Nobody has
> written down the dictionary that would even make the sentence testable, let alone proved it. The
> contribution here is turning a vague hope into a precise, falsifiable program with a stated order of
> attack.

**Global equivalence between TLICA optics and ordinary categorical optics is NOT CLAIMED** and no
bridge functor or proof exists. The dossier also fences off a tempting cheat: absorbing all TLICA
state into a bespoke "category whose objects are whatever TLICA says" would make an equivalence
*by construction* — that is **Refuted as methodology** (encoding-by-definition, not explanation). And
it records a hard logical constraint: exact equivalence with an *undecorated* optic category and an
irreducible, Yoneda-*visible* extra TLICA structure **cannot both hold at the same categorical level**
(**Refuted as framing**) — they can coexist only across a coarse level and a richer one.

---

## Restricted Yoneda: probes, collisions, and lamps

The deeper and more distinctively TLICA-flavored connection is to **restricted** Yoneda. Let
`i : 𝒫 ↪ 𝒞` be a subcategory of *available probes*, and form the nerve `N_𝒫(X) = 𝒞(i−, X)`, recording
how every available probe maps into `X`. A standard theorem — **Disclosed / established mathematics** —
says `i` is *dense* exactly when this restricted nerve is full and faithful; i.e. a dense probe family
is one rich enough to reconstruct objects up to isomorphism, and a non-dense one is not.

That gives an exact pattern for the archive's epistemic vocabulary:

- **Probe collision** — `X ≇ Y` yet `N_𝒫(X) ≅ N_𝒫(Y)`: the current probe family cannot tell two
  genuinely distinct objects apart. This is **Observed in a finite construction** (below) and is a
  *standard possibility*, not a universal claim.
- **Dark-as-collision** — a distinction that exists in the model but that *no present discriminator
  reaches* is a candidate categorical reading of a "contextually Dark" distinction. This is a
  **CONJECTURED bridge** on structural fit only — it is explicitly **not** asserted to be identical to
  the theory's "Dark" label.
- **Lamp** — an extension `𝒫 ⊂ 𝒫'` that splits a previous collision (`N_{𝒫'}(X) ≇ N_{𝒫'}(Y)`): a
  mathematically concrete version of "name the lamp."

Two boundaries are drawn hard, as **type distinctions**, to stop an over-eager identification:
`μ ≠ density` (μ is observer-relative probe availability/weighting; density is a property of a functor)
and `φ ≠ Yoneda profile`. The relationship *may* be strong enough to formalize some of TLICA's
toolkit-relative indistinguishability claims, but no such theorem exists yet — **do not identify them.**

> **In plain terms —** "I can't currently tell these two apart" is not "these two are the same." The
> probe-family picture makes that difference exact: the objects really are distinct in the full model;
> your *instruments* just don't separate them yet — and a "lamp" is precisely the new instrument that
> would.

---

## "Optic + deviation" done honestly

A motivating proposal was `TLICA optic = categorical optic + TLICA deviation`. In a general optic
category the `+` is simply **not licensed** — hom-sets need not support addition. So the
mathematically honest starting form is a *dependent / fibred pair*, **Disclosed as type discipline**:

`ω̃ = (ω, δ_ω)` — a base optic `ω` together with structured TLICA data `δ_ω` living over that
interface — with the realization `Θ ↦ c_Θ` and closure `cl_Θ(ω) = r ∘ (id_M ⊗ c_Θ) ∘ l`. A
Grothendieck/fibred total category over the optic interfaces is a **CONJECTURED** formalization; the
prior-art-adjusted first attempt is to see whether the existing `Para(Optic)` already does the work
before inventing a bespoke fibration.

The word "deviation" is then **typed into three things that must not be conflated** (a **Disclosed
taxonomy**):

1. **gauge / residual** — two presentations of the *same* optic; quotiented away by the coend, carries
   no TLICA content;
2. **fiber / decoration** — two observer states over the same base interface that *close it
   differently*; this is the primary intended meaning;
3. **model-defect** — a discrepancy from a chosen baseline (e.g. exact Bayesian inversion); empirical
   and baseline-relative.

And a firewall: **a deviation meant as a defect is undefined without a declared baseline** (there is no
canonical "neutral observer"), so no literal deviation *magnitude* exists without a declared common
basis — the same discipline the research program applies to transported phasors elsewhere.

One concrete positive result anchors all of this. For a full, bijective-on-objects functor
`Q : 𝒯 → 𝒪`, the relation `f ∼_Q g ⟺ Qf = Qg` is a congruence and `𝒯 / ker Q ≅ 𝒪` — **Disclosed /
proved**. Relative to such an operational quotient, a precise candidate for "the TLICA delta" is
exactly the *kernel structure `Q` erases* — a **conditional** interpretation still awaiting an actual
TLICA-to-cyberoptics operationalization functor. (Hefford & Comfort, arXiv:2205.09027, study an
intensional optic category versus its extensional quotient this way — **Source-supported prior art**.)

---

## What has actually been executed

Small, deterministic, standard-library scripts were run. They are **construction-level consistency
witnesses only** — they validate *nothing* about human cognition or the TLICA bridge.

- The main finite witness builds one base optic-shaped interface; two observer decorations over it
  producing different closed-loop updates; a restricted probe family that *collapses* two distinct
  objects; an added probe that *splits* them; and full representable profiles separating every object.
  Executed result: **8/8 checks pass** (**Observed, finite construction**).
- A separate *hostile* witness asks whether internally distinct TLICA-style source/probe states can be
  forgotten if they induce the same extensional controller. Under the explicit assumption that the two
  states are non-isomorphic, mapping both to one controller object makes the forgetful functor fail
  fullness (`|Hom_𝒯(A,B)| = 0` but `|Hom_𝒪(UA, UB)| = 1`). Executed result: **6/6 checks pass**
  (**Observed, finite construction**). This does **not** prove the distinction must be retained; it
  proves a clean **theorem fork — quotient the distinction as redundant, or represent it in the target.**

A further battery of finite witnesses runs in the same spirit, each labeled **Observed (finite
construction)**: a history-sensitive reparametrisation monoid (**17/17**), a local-realizability /
scale-locality square (**8/8**), Yoneda transport forms (**14/14**), and a finite context atlas with all
adjunction hom-bijection cells (**16/16**). The dossier also notes, as **Corroborated structurally**,
that its two "defect axes" (hom-defect and coverage-defect) are *independently* realized by standard
mathematics. None of this validates human semantic optics — that claim is explicitly **Refuted / NOT
CLAIMED**.

---

## Where this sits

**Claim-status summary (verbatim labels preserved):**

- **Disclosed / established mathematics** — the categorical loop as a typed schematic; Riley's optic
  coend; hole-closure `cl_c(ω) = r ∘ (id ⊗ c) ∘ l`; closure invariance under the coend relation
  (conditional on the construction); the density ⇔ fully-faithful-nerve theorem; the operational-quotient
  congruence `𝒯/ker Q ≅ 𝒪`; the deviation taxonomy and the no-baseline-no-magnitude firewall.
- **Source-supported external prior art** — categorical cybernetics / `Para(Optic)`, Bayesian lenses,
  open games, Structured Active Inference, Hefford–Comfort intensional-vs-extensional optics.
- **Observed (finite construction)** — the 8/8 main witness and the 6/6 hostile-bridge obstruction;
  plus the further 17/17, 8/8, 14/14, 16/16 witnesses.
- **Corroborated (structurally)** — hom-defect and coverage-defect independently realized in standard
  mathematics.
- **Conjectured** — the semantic reading of the optic types; TLICA state as the hole-process; the
  `Para(Optic)` placement; the fibred/Grothendieck decomposition; "Dark" as a restricted-nerve collision.
- **UNVERIFIED** — any equivalence between TLICA optics and an optic category; density of any real
  TLICA probe family; whether TLICA's typed observer semantics beats a generic baseline on held-out
  prediction; and the whole Yoneda moonshot ladder (A/B/C). *The moonshot is a target, not a theorem.*
- **Refuted / NOT CLAIMED** — "good optics" as one scalar; generic feedback / system+interface+controller+feedback
  as TLICA *novelty*; absorbing all TLICA state into a bespoke base category as an *explanation*; exact
  undecorated-optic equivalence coexisting with Yoneda-visible extra structure at one level; the finite
  demos establishing human cognition; semantic optics as a new foundation coordinate.
- **Dark** — *why* this cross-family pattern recurs as cleanly as it does is flagged, not answered.

**Foundation impact: none.** No TLICA coordinate, mode, prerogative, or law is added or changed. This
page composes existing machinery and existing research; it is a candidate *lens*, not a new primitive.
Its originating sibling is the cinema/acting work in [cinema-self-coupled-meaning.md](cinema-self-coupled-meaning.md),
where the general cross-family object first surfaced.

Full dossier, finite-witness scripts, claim ledger, and 71-item probe program:
[`research/semantic_optics_2026-10-01/`](../research/semantic_optics_2026-10-01/README.md).
