# This Ontology Is Really Moreish — dossier (2026-09-13)

**Underground Super Hans, Pavlov's Veruca, and the Greedy Integral of the Present**

> **Status: DRAFT — author-derived, UNVERIFIED, and explicitly *unfinished*.**
> Research-tier working note. **Foundation untouched.** Captured here durably so the
> manuscript is not lost; the archive-standard finishing work (below) is still owed.

## What this is

An author-written essay on a specific self-reinforcing failure mode: the policy that
**maximizes the lived present while discounting the future's *causal* pull on the ground
that the future is only *epistemically* weak** — a category mistake between uncertainty
and irrelevance. It develops the mode through two comic figures (Underground Super Hans =
adversarial epistemic freedom promoted from *sensor* to *governor*; Pavlov's Veruca =
immediate-reward reinforcement promoted to capital allocation), names the **Greedy Integral
Problem** (maximizing the integrand locally ≠ maximizing the integral when the integrand is
dynamically coupled through state), and argues the corrective is not more planning but an
**adaptive feedback policy** with preserved invariants — corrigibility, **option value**,
and suspicion of gratuitous irreversible commitments.

- [`MANUSCRIPT.md`](MANUSCRIPT.md) — the paper, **captured verbatim** as the author wrote it.

## TLICA anchors it leans on (finishing must verify these, not assume them)

The manuscript borrows several TLICA constructs by name. Each is a **claim to be checked
against the frozen foundation and the landed papers**, not yet a verified cross-reference:

- **Mode-B projection** as the phenomenological status of Future-Me — "simulations of
  possible imprinting rather than already-imprinted actuality" (§5).
- **Slack** — the "low slack ⇒ expensive model-predictive control is unaffordable" argument
  (§5). (NB: in the differential-field working model, slack S is currently **not
  operationalized** / S=0 — so this leans on a construct that is itself open. Flag on finish.)
- **Steerable / correctable commitment** — "an endorsed destination is not itself an
  actuator" (§8), from the Geometry-of-Actualization traversability continuation.
- **Plural inhabited life with low-cost reflective transitions** (§10), same source cluster.

Thematically this sits in the **actualization / recognition** family
([`../geometry_of_actualization_2026-09-07/`](../geometry_of_actualization_2026-09-07/README.md)
and siblings) — it is a philosophy-of-agency essay in that lineage, not an empirical study.

## What "finish" means here (owed work — none of it done yet)

1. **Claim ledger** — grade every load-bearing claim (Demonstrated / Observed / Conjectured /
   Refuted / UNVERIFIED), per the archive convention. Right now the whole thing is
   author-derived and UNVERIFIED.
2. **Source ledger** — pin the borrowed figures and results: Dostoevsky's Underground Man,
   *Peep Show*'s Super Hans, Veruca Salt, Pavlovian conditioning, and the control-theory
   frame (greedy vs. optimal control, open-loop vs. feedback policy, option value).
3. **TLICA cross-reference verification** — confirm each anchor above against
   `foundation/` and the landed papers; correct any that don't actually say what the essay
   attributes to them (especially the **slack** lean — see the caveat above).
4. **Formalism repair** — the display-math blocks were pasted with LaTeX backslashes/relations
   stripped. **Two blocks are missing an operator and are ambiguous as written** and must be
   repaired by the author, not guessed:
   - §4, the greedy policy: `a_t^{G}  \arg\max_a u(x_t,a)` — the relation between LHS and
     `\arg\max` (`:=` / `=`) was dropped.
   - §9, the objective `\pi^*(x)`: the term `\lambda O(F(x,a))  \mu I(x,a)` is missing the
     sign on the irreversible-downside term — text says `I` is a downside, so it reads as
     `- \mu I(...)`, but the manuscript does not state it. **Do not silently insert; confirm.**
   The rest of the math is well-formed once the `[ … ]` display delimiters are normalized.
5. **A probe / demo**, if one is warranted — the family convention includes a small
   standard-library finite-model demonstration (e.g., a greedy-vs-option-value controller on a
   toy state machine where greedy provably shrinks the reachable action set). Optional; decide
   on finish.

## Discipline notes

- **Foundation is FROZEN (v5.3.3) and UNTOUCHED by this dossier.** No frozen file was edited.
- The manuscript is the **author's own text**; the assistant captured it verbatim and wrote
  only this status header. No claims were promoted, softened, or attributed to the freeze.
- Not yet wired into `research/README.md`, the root README, or the docs wiki — those index
  **landed** work, and this is a draft. Wire it in when it's finished.
