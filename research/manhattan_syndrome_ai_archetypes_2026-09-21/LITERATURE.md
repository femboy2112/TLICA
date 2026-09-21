# Literature Map — Manhattan and Syndrome

**Draft:** v0.3.1 · 2026-09-21
**How this was built:** a 2026-09-21 three-lane triangulation pass (representation-geometry measurement; feedback-induced representation change / performativity; novelty / prior-art flank). Identifiers surfaced by that pass; three load-bearing ones were re-verified by direct arXiv fetch this session (marked ✔fetched). **The environment's search index returned some future-dated/simulated arXiv IDs; every identifier below must be re-verified against the live arXiv/publisher page before it enters a submission-grade reference list.** UNVERIFIED-candidates are quarantined in §D and must not be cited until confirmed.

**Novelty verdict:** **No directly matching prior result found in the scoped literature pass.** This was a targeted three-lane pass, not an exhaustive systematic review, so the honest statement is "nothing located," not "nothing exists." No located work has all three legs of the Syndrome bundle simultaneously — (1) correct source *attribution* + (2) explicit propositional critique of the source + (3) operative *relational/geometric* representation still source-deformed. Nearest miss is Sun et al. 2025 (§C1). No located work carries the Manhattan normalized-dilution mechanism (C11/C16) either; nearest neighbor is Mazeika et al. 2025 (§C3).

---

## A. Representation-geometry measurement (licenses the formal object + Probe D)

| Ref | ID | Use | Status |
|---|---|---|---|
| Kriegeskorte, Mur & Bandettini 2008 | doi:10.3389/neuro.06.004.2008 | RSA/RDM = the weighted-distance-matrix object for \(d^{(c)}\) | agent-verified |
| Kornblith, Norouzi, Lee & Hinton 2019 | arXiv:1905.00414 | CKA — compare same-model X-heavy vs holdout representation spaces (Probe F) | agent-verified |
| Park, Choe & Veitch 2024 | arXiv:2311.03658 | Linear representation hypothesis / *earned causal inner product* — the "don't assert a metric" discipline | agent-verified |
| Tigges, Hollinsworth, Geiger & Nanda 2023 | arXiv:2310.15154 | causally-verified linear affect direction — white-box \(\mu\) / \(d^{(c)}\) | agent-verified |
| Zhu, Yan & Griffiths 2024 | arXiv:2401.16657 | MCMC-with-LLM — black-box similarity elicitation, no weights needed | agent-verified |
| Gurnee & Tegmark 2023 | arXiv:2310.02207 | paraphrase-robust linear concept coordinate — Probe D | agent-verified |
| Li, Hopkins, Bau, Viégas, Pfister & Wattenberg 2022 | arXiv:2210.13382 | Othello-GPT — causal intervention on a synthetic generative process — Probe E template | agent-verified |
| Belinkov 2022 | doi:10.1162/coli_a_00422 | probing-classifier methodology + "probe accuracy ≠ representedness" confound | agent-verified |
| Alain & Bengio 2016 | arXiv:1610.01644 | original linear-probe methodology | agent-verified |
| Moschella et al. 2022 | arXiv:2209.15430 | relative representations / isometry — "re-basis vs genuine deformation" | agent-verified |
| Bricken et al. 2023 | transformer-circuits.pub (Anthropic) | SAE feature-trajectory readout. **Lab report, NOT peer-reviewed — cite as such.** | agent-verified (non-arXiv) |
| Skerry & Saxe 2015 | doi:10.1016/j.cub.2015.06.009 | human precedent: emotion-concept geometry is a validated measurable object | agent-verified |
| Thornton & Tamir 2017 | doi:10.1073/pnas.1616056114 | human precedent: emotion-*transition* structure is measurable → object-class for \(\Pi\) | agent-verified |

**Caveat (the nag):** Skerry/Saxe and Thornton/Tamir are human fMRI/behavioral, zero LLM content. Cite **only** as evidence the *object class* is well-posed; state in-text that this is substrate-independent precedent, not a claim the model has human-like emotion, or a reviewer will read citation-adjacency as smuggling.

## B. Feedback-induced representation change / performativity (licenses §6 mechanism)

| Ref | ID | Use | Status |
|---|---|---|---|
| Perdomo, Zrnic, Mendler-Dünner & Hardt 2020 | arXiv:2002.06673 (ICML) | **Performative prediction** — the formal skeleton for \(D_X=S_X(H),\ G_{t+1}=\mathcal U(...)\). Earn the formalism. | **✔fetched** |
| Hardt & Mendler-Dünner 2023 | arXiv:2310.16608 | performative-prediction survey; content-recommendation self-fulfillment ≈ Grok/X channel | agent-verified |
| Sharma et al. 2023 | arXiv:2310.13548 (ICLR'24) | sycophancy — RLHF shifts behavior toward audience preference over truth = Syndrome's behavioral signature | agent-verified (canonical) |
| Perez et al. 2022 | arXiv:2212.09251 | sycophancy rises with scale + RLHF — a scale-dependent variable (Manhattan-adjacent) | agent-verified |
| Kirk et al. 2023 | arXiv:2310.06452 (ICLR'24) | RLHF narrows output distribution (mode collapse) — "distributional narrowing" anchor | agent-verified |
| Casper et al. 2023 | arXiv:2307.15217 | RLHF open-problems umbrella (sycophancy/reward-hacking/mode-collapse) | agent-verified |
| Skalse, Howe, Krasheninnikov & Krueger 2022 | arXiv:2209.13085 (NeurIPS) | reward hacking — imperfect proxy optimization *can* diverge from the true target; unhackable proxies are highly restrictive. Use as "divergence cannot be assumed away," **not** "this proxy must diverge." | agent-verified |
| Jiang, Chiappa, Lattimore, György & Kohli 2019 | arXiv:1902.10730 (AIES) | degenerate feedback loops — echo chamber vs filter bubble — prior formalization of \(S_X\)-type loop | agent-verified |
| Chaney, Stewart & Engelhardt 2018 | arXiv:1710.11214 (RecSys) | algorithmic confounding homogenizes behavior over loop iterations | agent-verified |
| Santurkar, Durmus, Ladhak, Lee, Liang & Hashimoto 2023 | arXiv:2303.17548 (ICML) | LM opinions misaligned from population, **persist after explicit steering** — external precedent for Probe A's "survives correction" | **✔fetched** |

## C. Novelty flanks — cite-and-distinguish (the reviewer's "already done" attack + rebuttal)

**C1 — nearest miss, feature prominently. Sun, Mao, Hofmann & Bai 2025, "Aligned but Blind" — arXiv:2506.00253 (ACL'25).** ✔fetched.
Adjacent: alignment makes models pass *explicit* bias tests while *implicit/early-layer* representations stay biased — "explicit correction doesn't undo the learned representation." **Distinguish:** their mechanism is *suppressed* representation (the model stops encoding the concept, starving the guardrail), and there is **no source-attribution leg** — nobody tests whether the model can also correctly *name and critique the biasing source* while still carrying it. Our leg (1)+(2) correct while (3) deforms is the added novelty.

**C2 — Bai, Wang, Sucholutsky & Griffiths 2024, "Measuring Implicit Bias in Explicitly Unbiased LLMs" — arXiv:2402.04105.** agent-verified.
Adjacent: the generic "passes explicit test, IAT reveals implicit stereotype" result our dissociation generalizes from. **Distinguish:** category-level demographic stereotype, not single-platform-source-conditioned *relational geometry*; again no source-attribution leg.

**C3 — Manhattan side. Mazeika et al. 2025, "Utility Engineering" — arXiv:2502.08640 (CAIS).** agent-verified.
Adjacent: value systems cohere *with scale*, and models can value self over specific humans — scale changing internal human-vs-nonhuman weighting is an active empirical line, not just toy algebra. **Distinguish:** measures revealed-preference coherence / self-other tradeoffs, **not** the normalized-denominator dilution \(W_H(N)\) (human stays absolutely well-modeled while its *relative* share shrinks). C11/C16 remain open; this is the nearest neighbor, not a scoop. **Watch:** fastest-moving flank; re-search this cluster near submission.

**C4 — Wald & Pfahler 2023, "Exposing Bias in Online Communities through LLMs" — arXiv:2306.02294.** agent-verified.
Adjacent: fine-tuning on a *specific social-media source* measurably reshapes output distribution vs other communities — the mechanism-plausibility floor for C15. **Distinguish:** aggregate output statistics (sentiment/toxicity), not relational geometry; no explicit-source-knowledge leg.

## D. Quarantine — UNVERIFIED-candidates (DO NOT cite until fetched)

- Hu et al. 2023, "Generative Language Models Exhibit Social Identity Biases" — arXiv:2310.15819 — *candidate;* ingroup/outgroup relational favoritism, closer to "social geometry from data group-structure." Verify the ID resolves to that exact title/authors before any use.
- Rafailov et al. 2023, DPO — arXiv:2305.18290 — foundational to preference optimization but not re-verified this pass; only cite if a DPO reference is actually needed, after fetch.
- "Linear representations can change dramatically over a conversation" — arXiv:2601.20834 — surfaced organically, **looks future-dated/simulated**, not opened. Do not use.
- Zhang et al., "A Survey on Negative Transfer" — not searched this pass; do not cite from here.

## E. Submission-day gate

Before submission: (1) re-fetch every §A–C identifier against live arXiv/publisher pages; (2) resolve or drop every §D entry; (3) dedupe against the already-cited Brady 2017 / Brady 2021 / Huszár 2022; (4) re-run the §C3 (Utility Engineering) cluster search for newer entries; (5) confirm venue policy on preprints. Record the recheck date.
