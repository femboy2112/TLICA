# Adversarial Defense Protocol — Semantic Interoperability (Paper I)

> **This is the canonical specification of the Gate H2 defense process.** The *live
> state* (current round, current phase, next physically executable action) and the
> per-round files live in [`defense/`](defense/README.md). When this spec and
> `defense/README.md` disagree, **this file is authoritative for the rules** and
> `defense/README.md` is authoritative for *where we currently are*.
>
> **Status: v1 (handoff protocol).** Supersedes the v0.1 draft. Round counts, question
> counts, and escalation themes remain tunable — the method serves the work, the round
> count does not control the method.

---

## What the defense is (and is not)

The defense is **preparation for actual peer review.** It establishes Leah's command,
ownership, consistency, and ability to defend or revise the theory. It does **not**
establish truth, novelty, empirical validity, literature adequacy, or publication quality
by itself.

It operationalizes the roadmap §5 ownership test — *"can Leah explain, defend, revise, or
abandon every load-bearing claim without outsourcing the judgment?"* — as a repeatable,
escalating adversarial questioning process that Leah answers **in her own words.**

> **The defense produces authorially owned conceptual raw material and a defensible paper
> architecture as byproducts. Leah writes the manuscript later.** It does *not* produce
> manuscript prose, and neither model ever ghostwrites her answers.

## The examiners are NOT independent witnesses

Claude and ChatGPT are **separately prompted, partially orthogonal model examiners with
overlapping provenance.** They are *not* independent witnesses, and **their agreement is
not independent corroboration** — two related language models can share a blind spot and
agree straight into it. Treat concordance between them as *weak* evidence, and treat each
model's analysis as **one constraint surface, not truth.**

Their legitimate role is: orthogonal coverage · differential questioning · contradiction
detection · adversarial pressure · preservation of state · organization of Leah's answers.
Nothing they agree on is certified by that agreement; the value is in the *differential*,
not the consensus.

## Status vocabulary (keep these strictly separate)

| Status | Meaning |
|---|---|
| **Candidate** | Proposed but not owned. |
| **Owned** | Leah commands it and accepts responsibility for it, in her own words. |
| **Grounded** | Relevant evidence and literature have been personally checked (Gate H3). |
| **Manuscript-eligible** | Owned **and** grounded **and** bounded **and** necessary for Paper I. |
| **Rejected** | Leah no longer endorses it. |
| **UNVERIFIED** | Requires a probe or evidence not yet supplied. |

**Ownership is never automatic.** Answering a question does **not** mark a claim owned.
A claim becomes `owned` only on Leah's **explicit confirmation.** AI-proposed distinctions
stay `Candidate` and explicitly unowned until Leah adopts or restates them.

## What passing Gate H2 means

A claim passes Gate H2 only when Leah can, **in her own words**:

1. state it clearly;
2. explain why it matters;
3. distinguish it from nearby claims;
4. provide a positive example;
5. identify its boundary or nonclaim;
6. answer at least one serious objection;
7. name a revision, narrowing, or falsification condition;
8. reconcile it with her earlier answers;
9. explicitly say she owns the claim in its current form.

**Gate H2 establishes:** authorial command · conceptual ownership · internal consistency
to the current tested depth.
**Gate H2 does NOT establish:** external truth · novelty · empirical confirmation ·
literature adequacy · expert acceptance · manuscript eligibility by itself.

## The handoff cycle (per round)

1. **ChatGPT** writes the first five questions (Q1–Q5).
2. Leah hands those to **Claude**.
3. **Claude** independently develops five additional questions (Q6–Q10) — drafted, where
   operationally possible, **before opening ChatGPT's set** (see *Partial blinding* below).
4. **Claude** prepares the round directory: combines both sets without flattening
   meaningful differences, records the differential, and makes the questions easy for Leah
   to answer on GitHub.
5. **Leah** personally writes all answers into the round file and commits them herself.
6. Leah hands her completed answers to **ChatGPT**.
7. **ChatGPT** analyzes the answers and writes a dedicated analysis document.
8. Leah hands the answers **and** ChatGPT's analysis to **Claude**.
9. **Claude** performs its own analysis — treating ChatGPT's report as **one constraint
   surface, not truth** — and writes a separate analysis document.
10. Leah hands both analyses back to **ChatGPT**.
11. **ChatGPT** uses Leah's answers **plus the differential between the two analyses** to
    generate the first five questions of the next round.
12. Repeat, with increasing difficulty, precision, adversarial pressure, and consistency
    checks.

## Partial blinding (procedural, for coverage — not proof of independence)

When Claude generates its five questions, it should where possible:

1. read the current claim ledger, formal ledger, canonical notes, prior-round answers, and
   prior-round verdict;
2. draft its five questions in a **scratch file without reading ChatGPT's new questions**;
3. **freeze** Claude's set;
4. then open ChatGPT's set;
5. compare;
6. remove **only exact duplicates**;
7. **preserve** questions that overlap in topic but apply meaningfully different pressure;
8. record the differential (both-targeted / ChatGPT-only / Claude-only).

This is **partial procedural blinding for coverage, not proof of epistemic independence.**

## Question design

Each round = **ten questions**: Q1–Q5 ChatGPT, Q6–Q10 Claude. Every question must:

- target a **real** claim ID, formal entry, canonical-note field, prior answer,
  contradiction, missing boundary, or unresolved gap;
- be **one pointed ask**, not a disguised essay assignment;
- increase in difficulty appropriately for the round;
- preserve the distinction between **eliciting Leah's view** and **proposing an AI answer**;
- during foundational capture, **avoid putting the preferred answer into the question**;
- clearly label any AI-proposed distinction as an **unowned candidate**;
- attack the **claim, never Leah**;
- permit Leah to answer **naturally**, not require academic prose.

**Round 1 = open elicitation** wherever possible. Prefer *"When communication succeeds,
what exactly survives?"* over *"Does the proposition, analogy, causal structure,
confidence, source, and nonclaims survive?"* — candidate distinctions are introduced in
**Round 2**, after Leah's natural answer exists.

Later rounds explicitly build on Leah's prior answers and pressure: vague terms · internal
contradictions · shifted definitions · unearned universal claims · hidden assumptions ·
rival explanations · counterexamples · source-map defects · places her preferred frame may
be wrong · claims that do not belong in Paper I.

## The round arc (five to start; tunable)

| Round | Theme |
|---|---|
| **1** | Foundational capture (open elicitation) |
| **2** | Consistency and precision |
| **3** | Prior art and rival theories |
| **4** | Counterexamples, failure modes, and transfer tests |
| **5** | Synthesis defense, narrowing, and paper architecture |

Rounds may be shortened, extended, split, or repeated if the answers reveal that would
produce a cleaner discriminator.

## Repository structure

The defense runs in a durable directory, **one subdirectory per round**:

```text
publication/semantic-interoperability/defense/
├── README.md               ← live state + per-file templates (see defense/README.md)
├── round-01/
│   ├── questions_chatgpt.md
│   ├── questions_claude.md
│   ├── questions_combined.md
│   ├── answers_leah.md      ← Leah writes & commits this herself
│   ├── analysis_chatgpt.md
│   ├── analysis_claude.md
│   ├── differential.md
│   └── handoff_next_round.md
├── round-02/ …
└── …
```

The purpose and required provenance of each file are documented in
[`defense/README.md`](defense/README.md).

## Main-branch workflow

- **Infrastructure or protocol changes** (like this file): a **separate non-main branch +
  draft PR**, merged only on Leah's explicit `merge` instruction.
- Once this protocol is merged, **routine round preparation** may be committed directly to
  `main` **when Leah explicitly instructs** Claude to prepare a round.
- **Leah personally commits her own answers** (`answers_leah.md`) to `main`.
- **Claude may commit its own analysis documents** to `main` when Leah explicitly hands off
  the completed answers.
- **ChatGPT does not directly edit `main`.** It returns a document for Claude to integrate
  with exact provenance, or uses a separate branch and instructs Claude to merge only after
  Leah's approval.
- **Never merge a branch or PR without Leah's explicit "merge" instruction.**

## Authorship and provenance (unchanged boundary)

- **Leah is the epistemic and final prose author.**
- The defense produces **authorially owned conceptual raw material**, not manuscript prose.
- Neither model may rewrite Leah's answers into polished philosophical language, or silently
  fill gaps in her view.
- **Candidate AI formulations stay explicitly unowned** until Leah adopts or restates them.
- Leah's **exact answers remain durably accessible**, even after later summaries exist.
- Every materially distinct AI session/task is logged in [`ai_use_log.md`](ai_use_log.md).
- **Model provenance must name** whether content originated with ChatGPT, Claude, Leah, the
  literature, or a synthesis. **Shared model agreement is not independence.**
- [`manuscript.md`](manuscript.md) **remains untouched** during Gate H2.
- Reading and prior-art grounding remain **Gate H3**. Peer review is the external test this
  process prepares for.

## Question bank (the previously-seeded prompts are NOT the mandatory Round 1)

The prompts already scattered through [`canonical_notes.md`](canonical_notes.md) (the
Semantic-interoperability note and Worked cases) and [`reading_ledger.md`](reading_ledger.md)
(the pre-reading holdout) are a **parked question bank**, not a mandatory set Leah must
answer all at once. Draw from them; do not treat them as the round. This avoids recreating
a forms-and-ledgers burden.

**Actual Round 1** runs as the handoff cycle above: ChatGPT's five first, then Claude's
five, integrated into `defense/round-01/`, answered by Leah. Unused bank prompts stay parked
for future rounds.

After each round, `canonical_notes.md`, `claim_ledger.md`, and `formal_ledger.md` are updated
**only** by: linking to Leah's exact answer; recording a model-generated **candidate**
summary; then waiting for Leah to confirm, edit, or reject that summary — **never** replacing
her answer with the summary.
