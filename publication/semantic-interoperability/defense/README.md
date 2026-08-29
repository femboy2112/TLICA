# Gate H2 Defense — live state & round hub

> **⚠ STANDING META UPDATED 2026-08-29.** Under the new standing meta, this defense is an
> **optional theory-sharpening tool**, not a mandatory gate. **AI may now draft manuscript
> prose** (the "`manuscript.md` stays untouched" rule is lifted); Leah is the final **fidelity
> authority**, and the acceptance test is her fidelity review, not this viva. Hard floor
> unchanged: no falsehoods/fabrication/plagiarism, verified citations, respect reality. Run the
> rounds when they sharpen the theory; skip the ceremony when they don't.

This directory runs the Gate H2 adversarial defense for **Paper I (Semantic
Interoperability)**. The **authoritative rules** are in
[`../defense_protocol.md`](../defense_protocol.md); this file tracks **where we currently
are** and documents each round file's job.

## Purpose

Preparation for actual peer review. It establishes Leah's **command, ownership,
consistency, and ability to defend or revise** the theory by having her answer
progressively harder questions **in her own words.** It does **not** by itself establish
truth, novelty, empirical validity, literature adequacy, or publication quality.

## Live state

| Field | Value |
|---|---|
| **Protocol version** | v1 (handoff), merged to `main` (PR #4, merge commit `0c168c1`) |
| **Current round** | Round 3 — **questions posted; awaiting Leah's answers** |
| **Current phase** | Round 2 complete (both analyses + differential on `main`; ChatGPT's Round-2 analysis merged via PR #7 → `3b0ac61`). Round 3 (prior art & rivals): both examiner sets integrated in [`round-03/questions_combined.md`](round-03/questions_combined.md) (Q1–Q10; ChatGPT's Q1–Q5 merged via PR #8 → `da90429`; Claude's Q6–Q10 frozen `sha256 e300cf81…` before reading PR #8; **no exact duplicates removed**); Leah writes & commits [`round-03/answers_leah.md`](round-03/answers_leah.md). |
| **▶ Next physically executable action** | **Leah answers Round 3 in her own words** in [`round-03/answers_leah.md`](round-03/answers_leah.md) (Q1–Q10; full text in [`round-03/questions_combined.md`](round-03/questions_combined.md)) and commits it herself. Each question is a **distinguish-or-concede** against a named rival (the rivals are prior-art *pointers*, not required reading — Gate H3 is separate). Then: Leah → ChatGPT for `round-03/analysis_chatgpt.md`. **Claim-status changes remain recommendations only — none applied; ownership is Leah's explicit act.** |

## Status vocabulary (authoritative defs in `../defense_protocol.md`)

**Candidate** (proposed, unowned) · **Owned** (Leah commands it, explicit confirmation
required) · **Grounded** (evidence/literature personally checked — Gate H3) ·
**Manuscript-eligible** (owned + grounded + bounded + necessary) · **Rejected** ·
**UNVERIFIED** (needs a probe). **Answering a question never auto-marks a claim owned.**

## The handoff cycle (per round)

1. ChatGPT writes Q1–Q5 → 2. Leah → Claude → 3. Claude writes Q6–Q10 (drafted before
opening ChatGPT's set where possible) → 4. Claude prepares `round-NN/` (combined +
differential) → 5. **Leah writes & commits all answers herself** → 6. Leah → ChatGPT →
7. ChatGPT writes `analysis_chatgpt.md` → 8. Leah → Claude (answers + ChatGPT analysis) →
9. Claude writes `analysis_claude.md` (ChatGPT's report = one constraint surface, not
truth) → 10. Leah → ChatGPT (both analyses) → 11. ChatGPT generates next round's Q1–Q5
from the answers + the analysis differential → 12. repeat, escalating.

## Hard rules (operational)

- **Leah writes and commits every answer herself.** No model drafts or paraphrases her
  answers. Rough, conversational, misspelled, compressed, or unfinished is fine.
- **The defense fills these round files, not the manuscript** — but as of the 2026-08-29
  meta, `../manuscript.md` may now be drafted (AI-assisted, Leah reviews for fidelity) in
  parallel; the defense no longer blocks it.
- **The two models are not independent witnesses.** Separately prompted, partially
  orthogonal, overlapping provenance — **their agreement is not corroboration.** The value
  is the differential, not the consensus.
- **Provenance is named** on every artifact (ChatGPT / Claude / Leah / literature /
  synthesis) and every materially distinct AI session is logged in
  [`../ai_use_log.md`](../ai_use_log.md).

## Each round directory (`round-NN/`) — file jobs

| File | Job | Who authors |
|---|---|---|
| `questions_chatgpt.md` | ChatGPT's five questions **exactly as delivered** (date, model, upstream provenance, source commit, targets; **no answers**). Claude must not silently rewrite them — typographic normalization only, and noted. | ChatGPT (filed by Leah/Claude) |
| `questions_claude.md` | Claude's five questions, generated as independently as operationally possible (date, model, source commit, confirmation it was drafted before opening ChatGPT's set if true, targets; **no answers**). | Claude |
| `questions_combined.md` | All surviving questions Q1–Q10: examiner provenance, target, question, and an answer slot `[ AWAITING LEAH ]`. **No candidate answers or answer scaffolds.** | Claude |
| `answers_leah.md` | **LEAH-AUTHORED ANSWERS ONLY.** The file Leah edits and commits herself. Answer headings only, no suggested content. | **Leah** |
| `analysis_chatgpt.md` | ChatGPT's post-answer analysis (reconstruction, ambiguities, contradictions, boundaries, candidate splits/merges, unresolved objections, status-change *recommendations*, next-round targets, nonclaims). Model analysis until Leah confirms. | ChatGPT |
| `analysis_claude.md` | Claude's separate analysis — independently first, then where it agrees/disagrees with ChatGPT, what ChatGPT missed or overclaimed, shared model-family blind spots; recommends status changes, **never auto-promotes**. | Claude |
| `differential.md` | The triangulation: overlap · ChatGPT-only · Claude-only · conflicts · shared-provenance risks · what is stable enough to pressure next · what stays unverified · what would change the verdict. Diagnostic, not certification. | Claude |
| `handoff_next_round.md` | Round status · claims provisionally owned (pending Leah's confirmation) · rejected/narrowed · unresolved contradictions · missing evidence/prior-art · exact material ChatGPT should read · next round's theme/difficulty · one next physically executable action. | Claude |

New rounds are created by copying the `round-01/` structure to `round-NN/`.
