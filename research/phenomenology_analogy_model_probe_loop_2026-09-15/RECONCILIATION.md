# Reconciliation against `main`

**Branch:** `phenomenology-analogy-model-probe-loop-2026-09-15`  
**Base commit:** `33d449424dd909bab5dfe8e80f302df733bd2770`  
**Base state:** foundation v5.5.0 line; developmental-substrate internalization already present  
**Date:** 2026-09-15  
**Verdict:** **research-methodology synthesis; no foundation mutation required**

---

# 1. Question

Does the Phenomenology–Analogy–Model–Probe Loop require new TLICA ontology, or is it better understood as an explicit reconstruction of a method already distributed across the repository?

**Finding:** the latter.

The new material is primarily the **explicit meta-level synthesis**:

\[
\text{phenomenology}
\to
\text{analogy}
\to
\text{bridge}
\to
\text{formal model}
\to
\text{novel implication}
\to
\text{probe}
\to
\text{revision}.
\]

Current `main` contains multiple pieces of this discipline but does not presently name the complete loop as a reusable author-level research protocol.

---

# 2. What is already on `main`

## 2.1 First-hand origin followed by formalization

The root README describes TLICA as developed first-hand and then formalized. This already supplies the broad direction

\[
\text{lived/observed structure} \to \text{formal structure}.
\]

The present dossier makes the intermediate analogy/bridge stage and the later out-of-fit/probe/revision stages explicit.

**Change needed to foundation:** none.

---

## 2.2 Application discipline: phenomena should fall out of existing apparatus

The root README states that application papers are expected to make the target phenomenon **fall out of the existing apparatus**, without casually adding new architectural commitments.

That is already compatible with the loop's central anti-retrofit rule:

> a model should generate a consequence from prior structure rather than acquire bespoke machinery after seeing every target case.

The new dossier generalizes that discipline into a reusable workflow.

**Change needed to foundation:** none.

---

## 2.3 Analogy with explicit limits

`applications/caves_lagrange_points_v0_1_0.md` is an existing specimen of careful analogy use. Its physical source is a guide, not an ontological identity claim, and its predictions remain explicitly UNVERIFIED.

The present dossier names the missing general rule as a **bridge contract** with explicit non-transports.

**Change needed to application paper:** none required for the research branch. A future mainline integration could optionally cross-link it as an exemplar.

---

## 2.4 Literal-math versus metaphor audit

The dynamical-substrate program already asks whether TLICA's borrowed motion words are earned mathematically rather than merely evocative:

- `research/dynamical_substrate_axioms_2026-09-08.md`
- `research/substrate_round1_reachability_momentum_2026-09-08.md`

The program's willingness to preserve a weaker structure while refuting an over-strong literal claim is exactly the revision behavior required by the new methodology.

The new dossier does not replace this program. It explains why such a program is a canonical **analogy-to-formalization audit**.

---

## 2.5 Claim-ledger and probe discipline

Current research packages already use status labels, source/claim ledgers, explicit UNVERIFIED states, holdout distinctions, and falsification/probe plans.

The present dossier consolidates those practices around a specific model-generation loop.

**Change needed to foundation:** none.

---

## 2.6 Residual-driven revision already occurs in research practice

Two current examples are particularly relevant:

### Distributed institutional realization

The v0.1 realization-map formalization risked merely renaming its inputs. v0.2 replaced the object with a task-relative quotient macrostate and kept the empirical usefulness claim UNVERIFIED.

This is a clean example of:

\[
\text{formal residual} \to \text{model revision}.
\]

### Developmental substrate nonstationarity

The originating intuition "new blank neurons → noise" was not protected. It was marked Refuted as stated and replaced by the narrower moving-substrate/nonstationarity claim while preserving live co-causes.

This is a clean example of:

\[
\text{bad mechanism story} \to \text{retained phenomenon} + \text{revised model}.
\]

Neither example independently validates the new method; both share project provenance. They show compatibility with existing research behavior.

---

# 3. What is genuinely new in this dossier

The following objects are not merely copied from current main.

## 3.1 The method as an explicit first-class object

The repository previously contained the pieces. The dossier names the whole procedure and gives it a stable stage structure.

## 3.2 The bridge contract

The explicit tuple

\[
B=(b_O,b_R,b_I,b_D,b_{\neg})
\]

forces the author to state:

- what maps;
- which relations map;
- what is proposed invariant;
- which dynamics map;
- what explicitly does **not** map.

This is methodology, not foundation ontology.

## 3.3 Fit-provenance separation

The dossier explicitly names \(D_{\mathrm{fit}}\) and disqualifies materially used construction evidence from serving as clean validation.

This makes the author's existing truth-debt practice operational for analogy-built models.

## 3.4 Out-of-fit mathematical drive

The dossier identifies the load-bearing generative move:

\[
u^* \notin D_{\mathrm{fit}},
\qquad
\hat y^*=\mathcal O(M(u^*)).
\]

This is the clearest formalization of the author's phrase:

> "Drive the math with inputs not yet phenomenologically experienced and see what drops out."

## 3.5 Failure localization

A bad outcome can now be assigned provisionally to one or more of:

- analogy selection;
- bridge transport;
- formalization;
- parameters;
- observation map;
- probe;
- domain boundary;
- source/provenance.

This prevents undifferentiated updates and gives future research a reusable debugging grammar.

## 3.6 Bridge mutation and analogy competition

The dossier proposes two stronger methods:

- compare multiple candidate analogies by designing a probe that separates their downstream predictions;
- mutate the bridge itself to determine whether a transported relation is actually load-bearing.

These are research extensions, not established empirical results.

---

# 4. Why this should not enter the frozen foundation as-is

The frozen foundation describes the architecture TLICA claims for selfhood and its dynamics.

This dossier describes **how the author constructs and audits models**.

Those are different object levels.

Promoting this methodology into the foundation would create several avoidable risks:

1. **category error** — confusing a research workflow with a structure of selfhood;
2. **circularity** — making TLICA's truth depend on a method defined as TLICA machinery;
3. **premature universality** — turning an author-reported practice into a universal cognitive law;
4. **foundation bloat** — adding no coordinate or dynamical primitive while increasing core surface area.

Therefore the current recommendation is:

> **Keep the full object research-tier; internalize only a concise research-methodology surface into mainline documentation if desired.**

---

# 5. Candidate mainline integration routes

These are recommendations for the local Claude session, not changes made on this branch.

## Route A — minimal research-tier internalization (lowest risk)

- merge/copy this dossier into `research/`;
- add one entry to `research/README.md`;
- add a changelog entry;
- foundation untouched;
- no user-facing wiki page yet.

**Use when:** the method should accumulate examples before being promoted.

## Route B — research-tier + public methodology page (recommended if prose is stable)

Route A plus:

- add `docs/research-method.md` or equivalent;
- summarize the loop, bridge contract, holdout rule, and warrant firewall;
- link it from `docs/README.md` under research/methodology rather than theory primitives;
- optionally add a short root README sentence describing the research method.

**Use when:** the repo should make its epistemic workflow legible to outside readers.

## Route C — foundation insertion

**Not recommended at present.**

A future foundation insertion would require a separate argument that the method is itself part of TLICA's architecture of cognition rather than merely the author's research practice. That argument does not presently exist.

---

# 6. Acceptance criteria for internalization

A correct mainline integration should satisfy all of the following:

- [ ] Preserve the exact author seed as provenance.
- [ ] Keep the full method research-tier unless a separate promotion argument is written.
- [ ] State that analogy is candidate generation, not evidence.
- [ ] Preserve the bridge contract including explicit non-transports.
- [ ] Preserve the \(D_{\mathrm{fit}}\) / holdout distinction.
- [ ] Preserve the out-of-fit mathematical drive as the generative hinge.
- [ ] Preserve pass/fail/ambiguous probe declarations.
- [ ] Preserve failure localization.
- [ ] Preserve Refuted as an acceptable terminal status.
- [ ] Mark internal repository examples as common-provenance specimens, not independent corroboration.
- [ ] Add no TLICA coordinate, mode, prerogative, or foundation law.
- [ ] Do not reinterpret phenomenological report as mechanism evidence.
- [ ] Do not claim the workflow is generally superior; that remains UNVERIFIED.
- [ ] Keep identity coupling as a reason for stronger controls, never evidence for the model.
- [ ] Keep mathematical disclosure distinct from empirical corroboration.

---

# 7. Current reconciliation verdict

\[
\boxed{
\text{NEW META-METHOD SYNTHESIS}
\;\land\;
\text{NO NEW FOUNDATION PRIMITIVE}
}
\]

The branch should be treated as a **research-methodology dossier** that reconstructs an author-reported practice already visible in fragments across current TLICA work.

The correct internalization target is therefore the repository's **research practice and documentation surface**, not the frozen ontology.
