# Semantic Interoperability — publication workspace

This directory is the controlled workspace for **Paper I** of the publication
program described in
[`research/publication_roadmap_interop_genie_cave_2026-08-10.md`](../../research/publication_roadmap_interop_genie_cave_2026-08-10.md).

It exists to carry one bounded philosophy article from research scaffold to a
policy-compliant, anonymized submission — under the authorship standard corrected
in roadmap §5: **Leah is the epistemic and final prose author; she may consult her
own verified notes, but may not outsource the judgment or the writing.**

Nothing here is a manuscript yet. The files are ledgers, templates, and
instructions.

## Current state (2026-08-12)

- **Workspace:** initialized; Gate H2 interview scaffolding installed.
- **Native one-page thesis (Gate H1):** **written** by Leah — [`human_outline.md`](human_outline.md)
  Stage 1, the paper's human seed.
- **Claim ownership (Gate H2):** **in progress.** Rounds 1 and 2 are **complete** (both
  examiners' analyses + differential on `main`; ChatGPT's Round-2 analysis merged via PR #7).
  **Round 3 questions (Q1–Q10, prior art & rival theories) are posted** in
  [`defense/round-03/`](defense/round-03/questions_combined.md) (ChatGPT Q1–Q5 merged via PR #8;
  Claude Q6–Q10 frozen before reading them) and **await Leah's answers** — each is a
  *distinguish-or-concede* against a named rival (charity, common-ground/alignment
  psycholinguistics, inferential-role, prototype, analogy-as-cognition, the LLM case).
  Candidate claims C-001–C-009 recorded, **none owned yet;** C-010–C-014 remain **unowned and
  not applied.** Gate H3 literature reading is **separate and not started.**
- **Reading / prior-art audit (Gate H3):** **not started.** No source in
  [`reading_ledger.md`](reading_ledger.md) has been read; the pre-reading holdout is
  registered as a template but not yet filled.
- **Manuscript:** **not begun.** [`manuscript.md`](manuscript.md) contains no prose.
- **Venue:** none selected; no procedural inquiry sent (see
  [`venue_matrix.md`](venue_matrix.md)).
- **Submission:** **NOT SUBMITTED** (see [`submission/receipt.md`](submission/receipt.md)).

## Program state

| State | Paper | What it receives now |
|---|---|---|
| **Active** | Semantic Interoperability (this workspace) | writing effort |
| **Warm** | Genie / The Severed Map | source collection / scenario recovery only |
| **Parked** | Out of the Cave | no expansion |

## Controlled finish line

$$
\boxed{\text{Paper I is finished when a policy-compliant, anonymized manuscript has actually been submitted.}}
$$

Not accepted. Not praised. **Submitted.** Acceptance is a later causal layer and is
not part of finishing (roadmap §15, §31).

## ▶ Next physically executable action

> **Gate H2 — defend the claims into ownership.** The native thesis (Gate H1) is written.
> The defense now runs as a **round-based handoff** (spec: [`defense_protocol.md`](defense_protocol.md);
> live hub: [`defense/README.md`](defense/README.md)): two **separately-prompted,
> partially-orthogonal** model examiners (Claude + ChatGPT — *not* independent witnesses,
> so their agreement is not corroboration) put ten escalating questions per round; **Leah
> writes and commits every answer herself** in `defense/round-NN/answers_leah.md`. The
> defense produces **owned conceptual raw material and a defensible paper architecture** —
> **not** manuscript prose.
>
> **Immediate next action:** **answer Round 3.** Round 2's analyses + differential are on
> `main`. Both examiners' Round-3 questions Q1–Q10 (theme: **prior art & rival theories**) are
> integrated in
> [`defense/round-03/questions_combined.md`](defense/round-03/questions_combined.md). Leah
> writes every answer herself in
> [`defense/round-03/answers_leah.md`](defense/round-03/answers_leah.md) and commits it, then
> hands the answers to ChatGPT for its analysis. Each question asks her to **distinguish or
> concede** against a *named* rival — the rivals are prior-art pointers, not required reading
> (Gate H3 is separate).

The prompts previously scattered through [`canonical_notes.md`](canonical_notes.md) and
[`reading_ledger.md`](reading_ledger.md) are now a **parked question bank**, not a
mandatory upfront set. The pre-reading holdout remains time-sensitive: register it
**before** acquiring *Surfaces and Essences* (roadmap §41), so the book stays a real probe
(roadmap §29).

## Workspace artifacts

| File | Job |
|---|---|
| [`provenance.md`](provenance.md) | Honest human–AI development history and idea-origin classification |
| [`canonical_notes.md`](canonical_notes.md) | Leah-authored note per major concept (template; awaiting substance) |
| [`claim_ledger.md`](claim_ledger.md) | Every candidate claim, its status, ownership, and manuscript eligibility |
| [`formal_ledger.md`](formal_ledger.md) | Every equation/notation, its status and honest non-claims |
| [`reading_ledger.md`](reading_ledger.md) | Page-indexed prior-art differential, starting with *Surfaces and Essences* |
| [`human_outline.md`](human_outline.md) | Native one-page thesis + Leah-authored academic outline (template) |
| [`defense_protocol.md`](defense_protocol.md) | Canonical spec of the Gate H2 round-based defense handoff protocol |
| [`defense/`](defense/README.md) | Live defense hub + per-round directories (`round-NN/`); **Leah writes & commits her own answers here** |
| [`manuscript.md`](manuscript.md) | **Leah-authored submission prose only** — no generated prose |
| [`ai_use_log.md`](ai_use_log.md) | Every AI/tool interaction after freeze, with disclosure implications |
| [`venue_matrix.md`](venue_matrix.md) | Venue fit and (temporally unstable) policy checks |
| [`submission/`](submission/README.md) | Anonymized package templates and the submission receipt |

## Source scaffolds (outside this directory — the quarry, not the stone)

- [`research/this_is_water_semantic_interoperability_2026-08-09.md`](../../research/this_is_water_semantic_interoperability_2026-08-09.md) — core interoperability note
- [`research/semantic_interoperability_culture_war_constraint_closed_politics_2026-08-09.md`](../../research/semantic_interoperability_culture_war_constraint_closed_politics_2026-08-09.md) — the broader political dossier (kept **out** of Paper I except as brief motivation)
- [`applications/shared_reality_divergent_maps_v0_2_0.md`](../../applications/shared_reality_divergent_maps_v0_2_0.md) — the broad political first draft (a later application, not this paper)
- [`research/publication_roadmap_interop_genie_cave_2026-08-10.md`](../../research/publication_roadmap_interop_genie_cave_2026-08-10.md) — the governing roadmap

These are AI-assisted research records. They may be **consulted**; they may not be
**pasted**. See [`provenance.md`](provenance.md).
