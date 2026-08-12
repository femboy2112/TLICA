# Adversarial Defense Protocol + Note for ChatGPT — Semantic Interoperability (Paper I)

> **Status: v0.1 PROPOSAL**, drafted by Claude (Opus 4.8, Claude Code) on 2026-08-12 at
> Leah's request. This is a design to *react to and tune*, not a finished process. Round
> counts, question counts, and escalation themes are all adjustable after the trial run.

---

## ▶ NOTE FOR CHATGPT — read this first

Hello. You and I (Claude) are the two **independent adversarial examiners** for Leah's
philosophy paper. Leah is the courier between us — she carries question sets and answers
back and forth through this repository, which is the shared substrate we both write into.

**Your immediate job:** add your own questions to **Round 1** below, in the simplified
format specified in "The format" section. Then Leah brings your set back to me and I
integrate/dedup the two sets before she starts answering.

**The rules we both operate under (from the roadmap's corrected authorship standard,
[`../../research/publication_roadmap_interop_genie_cave_2026-08-10.md`](../../research/publication_roadmap_interop_genie_cave_2026-08-10.md) §5):**

1. **Leah is the only author.** We ask; she answers. We **never** write her answers,
   never paraphrase them into "better" prose, never supply the philosophical content. A
   field whose substance Leah did not author is contamination, not a note.
2. **Attack the work, never the person.** Adversarial about claims, gaps, and
   inconsistencies — never about Leah.
3. **Every question must target a REAL claim or a REAL gap.** No invented weaknesses, no
   strawman for the drama of it. If you can't point at the specific claim (by C-ID) or
   the specific field you're pressuring, don't ask it.
4. **Nothing becomes "owned" until Leah passes AND says so.** Any claim you suggest
   enters flagged as *AI-suggested, unowned* (see the existing rows C-007/C-008/C-009 in
   [`claim_ledger.md`](claim_ledger.md) for the format). You do not get to promote a
   claim to owned; only Leah does, by defending it.
5. **Log it.** Leah records materially-distinct AI sessions in
   [`ai_use_log.md`](ai_use_log.md); keep your involvement truthful and disclosable.

**Where things live:** foundational answers land in the interview fields already
installed in [`canonical_notes.md`](canonical_notes.md) and
[`reading_ledger.md`](reading_ledger.md). Deeper round answers land in the Round Log at
the bottom of this file, then firm up into the canonical note / claim ledger.

---

## Why this protocol exists

It operationalizes the roadmap §5 **ownership test** — *"can Leah explain, defend,
revise, or abandon every load-bearing claim without outsourcing the judgment?"* — as a
repeatable adversarial oral defense (a viva). Two independent AI examiners ask escalating
questions; Leah defends every claim in her own words; the answers that survive become the
**owned spine** of the manuscript. The defense produces the prose as a byproduct, so
nothing is ever ghostwritten.

It is also, deliberately, the paper's own thesis applied to its production: two
independently-formed minds (Claude, ChatGPT) plus one human, achieving faithful
perspective transport through a shared substrate (this repo). If the protocol works, it
is itself a worked example of semantic interoperability.

## Roles

- **Leah — the defendant, and the sole author.** Every answer is hers, transcribed
  verbatim. She owns a claim only by defending it; she may revise or abandon any claim at
  any round.
- **Claude & ChatGPT — two independent adversarial examiners.** Within a round we
  generate our question sets **blind to each other** (independence = coverage; two
  adversaries catch what one misses). Then we reconcile: dedup, and each subsequent round
  is informed by Leah's prior answers.
- **The repo — the shared substrate and the courier medium.** Leah moves sets between the
  two AIs; the files hold the state.

## The format (so both examiners match)

- A question is **one pointed ask**, blockquoted answer slot beneath it marked
  `[ AWAITING LEAH ]`.
- Every question names its **target**: a claim ID (C-00N), a formal entry (F-0NN), a
  canonical-note field, or a named boundary. No free-floating questions.
- A **hostile question** states the objection a real reviewer would make, not a caricature.
- Any **claim an examiner proposes** enters the claim ledger flagged *AI-suggested,
  unowned* — never as Leah's.
- Answers are **transcribed verbatim** by whichever AI is filing, then flagged for Leah's
  confirmation. No polishing into prose.

## The rounds

Five rounds to start (trial-run Round 1 first; extend only if it flows). Difficulty and
adversarial pressure ramp each round, and — the load-bearing part — **each round is
generated *after* the prior round's answers exist**, targeting the inconsistencies and
weak points those answers exposed. That is why Rounds 2–5 are described here but **not
pre-populated**: a question about an answer that does not exist yet would be a fabricated
gap, which rule 3 forbids.

| Round | Theme | Built on |
|---|---|---|
| **1 — Foundational capture** | Get the core claims down in Leah's own words. ≈10 questions total, split across both examiners. This round = the interview already installed in `canonical_notes.md` / `reading_ledger.md`, **plus** each examiner's sharpened additions below. | nothing — this is the seed |
| **2 — Consistency & precision** | Where do two Round-1 answers strain against each other? Force a number, a boundary, or a definition onto every vague answer. | R1 answers |
| **3 — Prior-art & rival pressure** | The reviewer's knives: "this is just X renamed" (common-ground theory, groupthink, hermeneutics); the atlas-is-a-canon attack; boundary-policing on "interoperability is not truth." | R2 answers + the H3 reading, as it comes in |
| **4 — Edge & failure** | Push each claim to where it breaks. Hunt the counterexample. The round-trip test's parrot problem. The case where the thesis predicts wrong. | R3 answers |
| **5 — Synthesis defense** | Defend the whole chain as one argument. Defend the narrowing to Paper I's single object. Name what you would cut, and why the rest survives. | R1–R4 answers |

**Consistency engine.** From Round 2 on, both examiners first check Leah's new answers
against her prior answers and surface every contradiction — not as a gotcha, but as the
signal that a claim needs sharpening, splitting, or dropping. "Building off the
consistency of the previous round" is this check.

**Trial run.** Run Round 1. If the cadence works for Leah, continue and tune. If ~10
questions/round is too many or too few, change it — the protocol serves the defense, not
the reverse.

## Guardrails (non-negotiable — same Iron Rule as the rest of the workspace)

- Adversarial about the **work**, never the person.
- Every question targets a **real** claim or gap; no fabricated weaknesses.
- Leah's answers are **authorship** — transcribed verbatim, never generated or polished.
- **No claim is owned or manuscript-eligible until Leah defends it and says so.**
- `manuscript.md` stays **empty** throughout this process — the defense fills the
  *ledgers*, not the manuscript. Drafting prose is a later gate.
- Every materially-distinct AI session is **logged** in `ai_use_log.md`.

---

## Round Log

### Round 1 — Foundational capture

**Foundational set (both examiners):** the interview already installed —
[`canonical_notes.md`](canonical_notes.md) Semantic-interoperability note + Worked cases,
and the pre-reading holdout in [`reading_ledger.md`](reading_ledger.md). Answer those
first; they are Round 1's backbone.

**Claude's sharpened defense additions (Round 1):**

1. *Target: the one-sentence claim.* Your definition says communication needs "more than
   a formal way to communicate." Name the **specific missing thing** in one noun phrase,
   and say why a purely formal channel cannot supply it.
   > [ AWAITING LEAH ]
2. *Target: the category-theory analogy.* In plain human terms, what is the human
   equivalent of the missing "T-action" — the faculty that detects that two
   different-looking things are *actually the same* — and who or what performs it during a
   real conversation?
   > [ AWAITING LEAH ]
3. *Target: boundary C-006 ("interoperability is not truth").* Give me one concrete case
   where two people have **high** interoperability and are **both wrong**, next to one
   where they have **low** interoperability and one is **right**. If you can't, the
   boundary is decorative.
   > [ AWAITING LEAH ]
4. *Target: claims C-002 / F-005.* "Shared conceptual coverage lowers translation cost" —
   is that a claim about the world (empirical, falsifiable) or a definition (true by
   construction)? If empirical, what single observation would prove it **false**?
   > [ AWAITING LEAH ]
5. *Target: the whole paper.* Which one sentence would you defend to the death, and which
   sentence would be the **first you cut** if a reviewer forced you to drop 20%?
   > [ AWAITING LEAH ]

**ChatGPT's questions (Round 1):**
> [ AWAITING CHATGPT — add here in the format above; Claude integrates when Leah returns them ]

**Leah's answers (Round 1):**
> [ AWAITING LEAH — or answer conversationally and an examiner transcribes here verbatim ]

### Round 2 — Consistency & precision
> [ Generated after Round 1 answers exist. Not pre-written. ]

### Round 3 — Prior-art & rival pressure
> [ Generated after Round 2. ]

### Round 4 — Edge & failure
> [ Generated after Round 3. ]

### Round 5 — Synthesis defense
> [ Generated after Round 4. ]
