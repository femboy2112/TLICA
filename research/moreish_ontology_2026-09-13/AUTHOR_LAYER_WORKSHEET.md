# Moreish — Author-Layer Worksheet

**Paper:** [This Ontology Is Really Moreish](MANUSCRIPT.md). **Status:** DRAFT, author review
pending. **Foundation untouched** (research-tier). This is the interactive companion to the
[handoff](AUTHOR_INTENT_AND_HANDOFF.md): it pulls every open author-review decision into one
place so you can answer them inline, at your own pace.

## How to use this

- Each item has a short **Context** (why I'm asking / what I already know), the **Question**,
  and one or more `> **Leah:**` blocks. **Edit your answer directly into the blank after the
  colon.** Add as much or as little as you want.
- A blank block = "not decided yet"; I won't touch that item until it's filled.
- Shorthand is fine: `keep` / `change to …` / `accept` / `refine: …` / `reject` / `defer` /
  `reference Self-Applied instead` / `leave to reference`.
- **Nothing here is pre-filled with invented content.** The receipt slots (§3) are empty *by
  design* — life-details are yours to supply; I will not fabricate one.
- When you're done (or done with a batch), tell me. Then I: apply the confirmed math repairs
  and any accepted edits to the manuscript (**verbatim — I edit your text only where you
  direct**), add whatever receipt material you chose to bring inline, tag slack's sense if you
  asked for it, and re-run `make validate`. Anything that would touch the **frozen foundation**
  stays gated: drafted → adversarially verified → validated → **shown to you for sign-off**
  before it lands.

---

## 1. Math repairs (each needs a one-word confirm)

The manuscript is captured verbatim; these two display blocks were pasted missing a symbol.
Neither has been written into your text. Details in
[`FORMALISM_AND_PROBES.md`](FORMALISM_AND_PROBES.md) §1.

### 1a. §9 objective — the sign on the `I` term  *(confidence: high on semantics; confirm before I typeset)*

**Context.** §9 names `I` the "irreversible downside" and lists it as a **cost**, so the
missing operator reads as a subtraction. The intended objective would then be

`π*(x) = argmax_a [ R_present(x,a) + λ·O(F(x,a)) − μ·I(x,a) ]`,  with `λ, μ ≥ 0`.

I will **not** insert the sign silently — you confirm it.

**Question.** Is the `I` term subtracted (`− μ·I`)?

> **Leah:** _______  *(yes / no — if no, the intended relation: _______)*

### 1b. §4 greedy policy — the definitional symbol

**Context.** The line *introduces* the greedy action, so only a definitional relation fits;
no semantic ambiguity, just your preferred symbol: `a_t^G := argmax_a u(x_t,a)` or
`a_t^G = argmax_a u(x_t,a)`.

**Question.** `:=` or plain `=`?

> **Leah:** _______

---

## 2. The Hans / Veruca ↔ substrate-roots mapping  *(accept / refine / reject)*

**Context.** The [handoff](AUTHOR_INTENT_AND_HANDOFF.md) §3 proposes reading the two comic
figures onto the roots you declared in
[The Self-Applied Architecture](../../applications/self_applied_architecture_prose_draft_v0_1.md).
This is **an assistant-proposed reading for your review**, not a claim attributed to you and
not a TLICA primitive. In brief:

- **Pavlov's Veruca ↔ the reward channel under Root I + Root II** — "present resonance ⇒ good
  policy" as steep temporal discounting (Root I, execution/focus constraint) *amplified by* a
  high-gain reward parameter (Root II). Degenerate as head of capital allocation; load-bearing
  as the sensor asking "is this life actually receiving reward, or only training on deferred
  symbols?"
- **Underground Super Hans ↔ the adversarial-epistemic channel** — "I can see the whole
  arrangement is ridiculous" as the same shape as the Self-Applied paper's genius-spike
  self-attribution (M3) and cold-frame Underground (M1). Degenerate when promoted to govern
  the discounting function; load-bearing as the auditor that detects fraud and overconfident
  forecasts.
- **"Sensor, not a governor" (§11) ↔ the Self-Applied paper's core** — roots as generative
  substrate invariants, not scalar deficits or moral verdicts; promoting a sensor to governor
  is the category error the firewall guards against.

**Question.** Accept as-is, refine, or reject? If refine, edit the mapping in the second block.

> **Leah — verdict:** _______  *(accept / refine / reject)*
>
> **Leah — edits to the mapping (if refining):** _______

---

## 3. Receipts / self-exhibit layer  *(yours to supply — blank by design)*

**Context.** Your stated intent: roast yourself *with receipts*, a philosophical autobiography
that **explains your structure and failure modes** (not narrates your story). The heavy
receipts already exist, author-declared, in the Self-Applied paper — so *Moreish* can borrow
that grounding rather than re-earn it. Below I name the **kind** of receipt each cell wants;
you decide the instance and the disclosure calibration.

**Firewall active (handoff §4).** §7's "tragedy → delayed punchline" arc is exactly the
Self-Applied paper's **O1 redemptive over-coherence** hazard: the funny, well-integrated
retrospective can quietly become the flattering-necessity story. A receipt is only honest if
the discriminators bite — self-correction *toward* the less flattering version, accurate
content separated from disproportionate affective charge, comedy that does **not** certify the
arc was meaningful. Recovery is the vantage reconstruction is possible *from*, not proof the
trajectory was good.

### 3a. Veruca receipt — present-resonance / high-gain reward
**Kind wanted:** an episode where immediate resonance was taken and the *coupled* state
degraded — the greedy-integral trajectory lived, not just modeled.

> **Leah:** _______  *(instance, or: reference Self-Applied / leave to reference)*

### 3b. Hans receipt — adversarial epistemics promoted to governor
**Kind wanted:** an episode where a *true* skeptical observation ("that's just a model") was
used to discount a *causally real* future — Hans doing real damage precisely by being formally
correct.

> **Leah:** _______

### 3c. Corrective receipt — the §9–§11 fix
**Kind wanted:** a case where an option-preserving move (money, mobility, skills, sleep, not
deleting a route) paid off *without* worshipping a predicted future.

> **Leah:** _______

### 3d. Disclosure calibration
**Question.** Bring the heavy receipts **inline**, or keep the manuscript comic and light and
**reference** the Self-Applied paper for the heavy grounding?

> **Leah:** _______  *(inline / reference / mix — say which per receipt)*

---

## 4. Slack scope-tag  *(optional)*

**Context.** Slack is now a **foundational** construct — seated into the frozen files at v5.4.0
(§8.11, `S = M − Pressure`); §5's *use* of it is faithful. The term-discipline asks which
*sense* §5 means, since the archive tracks the scope: **will-room** (the room to push against
the current) vs. **load / planning-budget** (capacity consumed by the situation). The
foundation seats the will-room gate; §5's "low slack ⇒ expensive model-predictive control is
unaffordable" leans on the load/planning sense.

**Question.** Tag §5's slack as **will-room**, **load/planning-budget**, or **both** (with the
scope marked)? Or leave it untagged?

> **Leah:** _______

---

## 5. Title & subtitle  *(editable)*

**Current.** *This Ontology Is Really Moreish* — "Underground Super Hans, Pavlov's Veruca, and
the Greedy Integral of the Present."

**Question.** Keep, or change either line?

> **Leah — title:** _______
>
> **Leah — subtitle:** _______

---

## 6. On-ramp positioning  *(separate author call)*

**Context.** You judged this a candidate **light / accessible on-ramp to TLICA** — teaching the
apparatus (Mode-B projection, the greedy integral, option value, feedback-vs-open-loop policy)
through one vivid specimen rather than the frozen formalism. Positioning it as an *official*
on-ramp means promotion beyond the research index — into the root README's front-door list,
the docs wiki, and the Makefile's curated application-paper list — each a registration +
validation step, not automatic.

**Question.** Register this as the/an official light intro to TLICA — now, later, or no?

> **Leah:** _______  *(now / later / no — and where: README §9 / docs wiki / both)*

---

## 7. Any further foundation upgrade  *(gated — slack already seated)*

**Context.** Slack and the dynamical/differential apparatus were seated in the frozen files
(v5.3.3 → v5.4.4; §§8.9–8.11, §2.10), so the old "slack is developed-but-unseated" worry is
resolved. What remains is whether any **other** developed construct this paper leans on still
merits a frozen-file seat. Any such edit is **gated**: drafted → adversarially verified →
`make validate`'d → **shown to you for sign-off on exact wording** before it lands.

**Question.** Open a foundation-upgrade pass for any remaining construct? If so, name which; if
not, defer.

> **Leah:** _______  *(name the construct(s), or: defer / none)*

---

## What happens after you fill it

1. Confirmed math repairs (§1) applied to the manuscript; cosmetic LaTeX-delimiter normalizing
   done in the same pass.
2. §3 mapping applied per your verdict (accepted / your refinements / dropped).
3. Receipt material (§3a–d) added at your chosen calibration, firewall active; nothing invented.
4. Slack sense tagged in §5 if you asked (§4).
5. Title/subtitle set (§5); on-ramp promotion done only on an explicit "now" (§6), with its own
   registration + `make validate`.
6. Any foundation work (§7) goes through the full gated path and **back to you** before landing.
7. `make validate` after every edit that adds, moves, or links a document.

*I edit your manuscript text only where you direct it here. Everything else in the paper stays
verbatim.*
