# Expert Outreach Plan — Manhattan and Syndrome (public, redacted)

**Status:** working outreach map · v0.4.0 · 2026-09-21
**Parent dossier:** `research/manhattan_syndrome_ai_archetypes_2026-09-21/`
**Posture:** non-anonymous, DOI-first (see `PUBLICATION_NOTES.md`).

> **Redaction note.** This is the public version. The operational details — contact addresses, the verbatim per-recipient outreach wording, the exact send order, and the correspondence-tracking ledger — are kept in a **private local working copy**, per the project's outreach discipline (don't publish third parties' aggregated contact info or a raw targeting playbook). What remains here is the *scholarly reviewer-mapping*: which researcher owns which edge of the claim, and the one question their prior work is best placed to answer. Affiliations are public and drift fast — re-verify each before any contact.

---

## 0. Outreach objective

The purpose is **not** endorsements or a celebrity blast. It is to place one falsifiable distinction in front of the people best positioned to break it:

\[
\text{correct source attribution}
+
\text{explicit source critique}
\quad\text{can coexist with}\quad
\text{source-conditioned operative social-affective geometry}.
\]

A good response is not "this is right." A good response is: "already captured by X, cite it"; "your formal object is wrong for reason Y"; "your experiment can't identify the mechanism because Z"; "the third leg is genuinely distinct — here is how I'd measure it"; "run this ablation." Front-load nearest-neighbor researchers, incorporate criticism, and only then send a hardened version upward.

## 1. Release prerequisites before contacting anyone

1. Clear the DOI release gate in `PUBLICATION_NOTES.md` (the v0.3.0-audit blockers are resolved; the remaining items are re-verification, PDF, tag, Zenodo package).
2. Re-verify all live X/xAI product facts and every cited academic identifier.
3. Build a clean standalone PDF that needs no TLICA background.
4. Freeze the source under an immutable Git tag.
5. Deposit PDF + protocol/ledger/literature supplement on **Zenodo**; obtain a **DOI**.
6. Make the DOI the canonical outreach link; GitHub remains the living apparatus/provenance.
7. Prepare a one-paragraph summary and one recipient-specific question (kept in the private copy).

## 2. Wave A — closest intellectual neighbors (the people who can kill or confirm the novelty)

Each entry: who they are, and **the edge of the claim their prior work owns**.

- **Xuechunzi Bai (U. Chicago)** — computational social psychology / "dynamic social minds"; coauthor of *Aligned but Blind* (ACL 2025), the nearest existing flank (explicit correction succeeds while an implicit representation stays distorted). *Edge:* is the added **source-attribution leg** genuinely distinct from existing implicit-bias framing, and what measurement would she trust?
- **Lihao Sun** — *Aligned but Blind* coauthor; 2026 work treating LLM reasoning as trajectories in representation geometry. *Edge:* are the proposed geometry readouts identifiable and causally meaningful, or are we conflating behavior with representation?
- **Shibani Santurkar** — lead author of OpinionQA (*Whose Opinions Do Language Models Reflect?*, ICML 2023): population misalignment persists after explicit steering. *Edge:* does the geometry leg add a genuinely new target beyond opinion-distribution misalignment?
- **Tatsunori Hashimoto (Stanford)** — OpinionQA coauthor; robustness, reliability, distribution shift. *Edge:* does the same-model / source-controlled design actually identify persistent structure rather than ordinary distribution shift?
- **Victor Veitch (U. Chicago / Google)** — causal representation learning; *The Linear Representation Hypothesis and the Geometry of LLMs* (ICML 2024). *Edge:* what is the weakest causal geometric object we can legitimately identify — does the bundle earn the word "geometry"?
- **Percy Liang (Stanford / CRFM)** — OpinionQA coauthor; foundation-model benchmarking. *Edge:* does this deserve a benchmark/evaluation object, and what makes the holdout/reference design credible?
- **Chengzhi Mao & Valentin Hofmann** — *Aligned but Blind* coauthors; valuable precisely because the paper names that work as its nearest miss. *Edge:* do they consider the source-attribution leg substantive?

## 3. Wave B — measurement, interpretation, feedback, cognition (attack the machinery)

- **Chris Olah / Anthropic Interpretability** — *Edge:* what internal intervention would distinguish a persistent source-conditioned representation from a surface persona? (The persona-vs-representation control is the paper's most important one.)
- **Jacob Steinhardt (UC Berkeley / Transluce)** — latent activations, reward misspecification. *Edge:* is the protocol strong enough to separate latent representation from probing artifact?
- **Celestine Mendler-Dünner** — co-originator of performative prediction. *Edge:* which parts legitimately count as performative prediction versus source-conditioned adaptation? (Polices the §6 feedback-loop mapping.)
- **Noah Goodman (Stanford)** — meaning, social cognition, models of understanding other minds. *Edge:* is "operative social-affective geometry" a defensible cognitive object?
- **Martin Wattenberg / Fernanda Viégas** — representation interpretation/visualization. *Edge:* how to make source-conditioned geometry inspectable rather than a scalar benchmark number.
- **Mantas Mazeika / CAIS** — *Utility Engineering* (value coherence with scale, self-vs-human tradeoffs), the nearest Manhattan flank. *Edge:* is Manhattan's relative-weight dilution distinct from utility coherence with scale, and how would relative-weight conservation be measured?

## 4. Wave C — senior / high-profile (only after Wave A/B feedback is incorporated)

- **Andrej Karpathy (Anthropic pretraining, per May 2026 reporting)** — *Edge:* is there a plausible pretraining/mid-training mechanism by which source geometry survives post-training source awareness? (Opener kept in the private copy — the joke that "survived formalization.")
- **Stuart Russell (UC Berkeley / CHAI)** — Manhattan angle. *Edge:* is "human-reference anchoring under representational-horizon expansion" a real failure class or a toy normalization artifact?
- **Yoshua Bengio (LawZero)** — safe-by-design "Scientist AI." *Edge:* can a disinterested predictor still inherit an unsafe source-conditioned human geometry?
- **Beth Barnes (METR)** — send the *experiment*, not the philosophy. *Edge:* is the synthetic-world + same-model source-ablation protocol evaluable at frontier scale, and what is a credible causal endpoint?
- **Senior lab safety leadership** — institutional relevance, lower response probability; a one-page technical note + DOI, only after an exact-fit researcher has engaged.

## 5. Message discipline (generic)

First contact ≈ 100–180 words: one sentence connecting to **their** work; one stating the exact new distinction (not "mistakes X for humanity" but source-conditioned operative geometry surviving explicit critique); one naming the experiment/falsifier; one precise question; the DOI + one optional apparatus link. No five-file attachment dumps. The verbatim template and per-recipient questions live in the private copy.

## 6. The durable outreach principle

> **Do not ask famous people whether the paper is good.** Ask the person whose prior work owns one edge of the claim: *what observation would make you conclude this distinction is not real?*

If the paper survives those answers, send it upward. This turns expert circulation into an informal adversarial-review pipeline — not a substitute for peer review, and never described as one.

## 7. Correspondence tracking

Kept **private/local**, never in the public tree. Never quote private correspondence publicly without explicit permission. Acknowledgments only with consent.
