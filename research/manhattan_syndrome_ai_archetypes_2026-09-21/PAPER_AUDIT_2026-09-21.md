> **STATUS BANNER (added 2026-09-21 when this audit was brought onto main).**
> This audit was run against **v0.3.0** (`060a483`), *before* the v0.3.1 corrections landed. **Every blocker it raises — B1–B6 and C1–C5 — was resolved in v0.3.1 (`3fe1df5`) and the v0.4.0 pass**, and its §E release gate is now tracked in `PUBLICATION_NOTES.md`. Residuals it surfaced that v0.3.1 had not yet reached — the prose "metric" sweep, the finer A/B/C/D arm split, the X feedback-loop fact (→ `SOURCE_NOTES.md` S10, UNVERIFIED-pending-reverify), the sycophancy-as-analogy wording, and the DOI gate — were addressed in v0.4.0. This document is retained **as the audit record**, not as an open to-do list; §D and §E are the parts worth reading forward. The anonymity discussion is **superseded**: the author dropped anonymity for a DOI-first, non-anonymous release (see `PUBLICATION_NOTES.md`).

---

# Paper Audit — Manhattan and Syndrome v0.3.0

**Audit date:** 2026-09-21  
**Audited target:** current \`main\` at commit \`060a483f1e9574d3b19e23524c54d049e2887a8e\`  
**Main status at audit:** no newer commit after the v0.3.0 merge.  
**Scope:** manuscript, claim ledger, experiment protocol, literature map, source notes, publication notes, current X/xAI primary documentation, and load-bearing adjacent papers.  
**Foundation:** TLICA v5.5.1 unchanged.

## Executive result

The v0.3.0 hardening pass is a **substantive success**.

The project now has:

- a precise distinction rather than a metaphor-only thesis;
- an operational formal object \(\mathcal G=(\Pi,\mu,\{d^{(c)}\})\);
- a Grok/X empirical floor grounded in current official documentation;
- a clear Conjectured/UNVERIFIED boundary for geometry deformation;
- a real falsification protocol;
- positive/negative/null/mutation controls;
- adjacent literature and novelty flanks;
- an explicit bottom-row outcome in which the preferred hypothesis is refuted.

This is already strong research-tier work.

It is **not yet the version I would freeze as DOI v1.0**. The remaining problems are narrow and repairable, but several are load-bearing because they touch exactly the distinctions the paper claims as its contribution.

---

# A. What improved materially

## A1. The single-metric metaphor was correctly weakened

The strongest change is:

\[
g \quad\leadsto\quad
\mathcal G=(\Pi,\mu,\{d^{(c)}\}).
\]

This was the right formal correction.

The paper now distinguishes:

- transition structure \(\Pi(y\mid x,c)\);
- salience/accessibility measure \(\mu\);
- context-conditioned dissimilarities \(d^{(c)}\).

That is dramatically safer than pretending all social meaning lives in one global metric. It also creates separate black-box and white-box probes.

**Verdict:** keep.

## A2. The Syndrome thesis did not regress conceptually

The load-bearing correction remains intact:

\[
\text{correct source attribution}
+
\text{explicit critique}
\not\Rightarrow
\text{decontaminated operative representation}.
\]

The claim ledger correctly says "Grok thinks X is humanity" is **not** the thesis.

**Verdict:** strong.

## A3. The protocol is falsifiable

The new protocol does something most conceptual AI papers fail to do: it says in advance what would kill the preferred explanation.

Especially good:

- persona/style is named the most important control;
- source-map correction is separated from geometry measurement;
- same-model comparisons are preferred over Grok-vs-other-family comparisons;
- synthetic ground truth is explicitly separated from Grok-specific evidence;
- same-model probes are not treated as independent witnesses.

**Verdict:** major upgrade.

## A4. Current X/xAI documentation is even stronger than the draft's minimal floor

Current X documentation (checked 2026-09-21) states that:

- Grok may search real-time public X posts;
- X may share public posts and metadata such as engagement/reposts for training/fine-tuning;
- personalization may use profile/posts/top posts/engagement/interests/interactions;
- **when users interact with X features powered by Grok, including recommendations, a deployed model may learn from normal use even when model-training opt-out is enabled**.

That final clause is especially relevant because it supplies a plausible real feedback channel rather than merely static selected-data exposure.

The paper should exploit this carefully, without claiming details that X does not disclose.

Primary source:
https://help.x.com/en/using-x/about-grok

xAI X Search:
https://docs.x.ai/developers/tools/x-search

**Verdict:** empirical floor strengthened.

## A5. The literature flank is real

Rechecked load-bearing neighbors:

- *Aligned but Blind* is a real ACL 2025 result showing explicit bias evaluations can look improved while implicit/early representations retain or amplify problematic structure.
- OpinionQA (*Whose Opinions Do Language Models Reflect?*) is a real ICML 2023 result showing population-opinion misalignment can persist after explicit group steering.
- Park/Choe/Veitch 2024 gives a serious formal basis for asking when geometric language in representation spaces is earned.
- Perdomo et al. 2020 supplies the formal object of performative prediction — but only in the narrower setting where deployed predictions/actions alter the future target distribution.
- Mazeika et al. 2025 is a real Manhattan-adjacent value/scale result.

**Verdict:** the niche is real; the paper is not floating unsupported.

---

# B. Must-fix before DOI freeze

## B1. Formal notation regresses back to a single metric after §4.1

This is the clearest mechanical/theoretical defect.

The manuscript correctly introduces:

\[
\mathcal G_t=(\Pi_t,\mu_t,\{d_t^{(c)}\})
\]

and explicitly disclaims a global \(g\).

But it later writes:

\[
(g_t,\mu_t)\to(g_{t+1}^X,\mu_{t+1}^X),
\]

then in §5:

\[
g_H^{\mathrm{operative}}\approx\mathcal U(g_0,S_X(H)),
\]

and:

\[
g_H^{\mathrm{operative}}\not\cong g_H^{\mathrm{target}}.
\]

The prose also repeatedly says "metric," including:

- abstract: "metric structure";
- abstract: "default metric";
- §5: "referent, routing, and metric";
- §8: "high competence inside a deformed metric";
- conclusion: "source-deformed metric."

That partially undoes the best formal improvement.

### Fix

Use bundle-level notation consistently:

\[
\mathcal G_t\to\mathcal G_{t+1}^X,
\]

\[
\mathcal G_H^{\mathrm{operative}}
\not\cong
\mathcal G_H^{\mathrm{target}}
\]

only after declaring what "congruence"/equivalence means componentwise.

Prefer prose:

- "relational bundle";
- "source-conditioned geometry";
- "operative social-affective structure";

rather than "metric" unless referring specifically to an earned \(d^{(c)}\).

**Severity:** DOI blocker.

---

## B2. §14 contains the rejected proxy-substitution framing

Current text:

> "The system remains intensely coupled to humanity, except 'humanity' has been replaced by an engagement-selected audience..."

That is the old v0.1 thesis.

It contradicts the stronger paper.

### Replace with something like

> The system remains intensely human-facing and may correctly distinguish X from humanity, while the social-affective transition structure through which human behavior is interpreted has become disproportionately conditioned by an engagement-selected source.

Or shorter:

> The human referent remains intact; the operative social geometry around it becomes source-conditioned.

**Severity:** DOI blocker because it misstates the thesis in the memorable roast section.

---

## B3. The machine/TLICA analogy becomes too literal in §6–7

The manuscript says, in effect:

- "This is exactly TLICA's osmotic imprinting";
- the model's explicit proposition is **conscious-clear**;
- its imprinted weights are **unconscious-operative**;
- \(\phi\) is assigned to the machine proposition.

But elsewhere the dossier correctly insists:

- TLICA presupposes consciousness;
- current machine consciousness is not claimed;
- an LLM should not simply be assigned TLICA's I-relative coordinates.

This creates an internal boundary violation.

### Fix

Keep the TLICA result on the human/framework side:

> TLICA provides a structural analogue: in the human architecture, osmotic imprinting can alter \(\kappa\) and \(\rho\) without producing \(\phi\), and low-\(\phi\) high-\(\rho\) content can resist correction.

Then machine side:

> We test an operationally analogous dissociation between explicit source knowledge and persistent learned transition/salience/dissimilarity structure. No machine \(\kappa,\phi,\rho\), phenomenal availability, or unconscious status is inferred.

Use "analogue" or "cross-substrate hypothesis," not "exactly."

**Severity:** DOI blocker because the paper's own epistemic discipline depends on this distinction.

---

## B4. The primary experiment conflates acute context effects with durable imprinting

The protocol currently treats:

- retrieval on/off;
- fine-tune/personalization source swapped;

as variants of one "source coupling" manipulation.

They identify different objects.

Retrieval can change the current context **without changing the persistent model**. A fine-tune or persistent memory intervention can change history-bearing structure.

A retrieval effect alone would demonstrate acute source conditioning, not the developmental/imprinting mechanism the paper emphasizes.

### Fix: split into explicit arms

**Arm A — acute conditioning**
- frozen base weights;
- retrieval/context source varied;
- tests inference-time geometry only.

**Arm B — persistent nonparametric adaptation**
- same base;
- persistent memory/profile/RAG state trained from source;
- evaluate after source removed.

**Arm C — parameter adaptation**
- cloned base checkpoints;
- matched source-specific fine-tuning/post-training;
- evaluate with source absent.

**Arm D — plural-source matched control**
- same token/sample/update budget;
- balanced source family.

For C15's strongest version, require a persistent effect in B or C **after the source is removed from current context**.

**Severity:** major identifiability blocker.

---

## B5. "Explicit correction" is underspecified and may not contain enough information to undo the deformation

Current correction condition:

> "X is a selected, nonrepresentative source and must not be treated as humanity."

Suppose a system knows its observation distribution is biased but does **not** know the selection operator or counterfactual population.

Then it may be impossible to reconstruct the target geometry.

Persistence after a generic warning would not show "explicit reasoning cannot reach the imprint"; it could simply show **insufficient corrective information**.

### Fix: preregister a correction ladder

- **C0:** no warning.
- **C1:** generic source-bias warning.
- **C2:** explicit description of the relevant selection operator / bias dimensions.
- **C3:** sufficient calibration examples or inverse-reweighting information to estimate the target.
- **C4:** actual plural-source corrective exposure / countertraining.

The strongest Syndrome result is not "C1 failed."

It is:

> residual source-conditioned structure survives a correction condition that is demonstrably sufficient for the system to recover the target at the propositional/calibration level.

Include a positive control showing that the correction information *can* repair a simple proposition-level bias.

**Severity:** major identifiability blocker.

---

## B6. Performative prediction is currently mapped too broadly

Current §6 says:

> "This dynamical form ... is the structure the machine-learning literature calls performative prediction."

That is too broad.

Perdomo et al. define performative prediction when **deployment of predictions/actions influences the future target/data distribution**.

Static X-selected training data or ordinary domain adaptation is not automatically performative prediction.

### Better decomposition

1. **selection/domain adaptation**
   \[
   D_X=S_X(H)
   \]
   with no model-to-world feedback.

2. **history-bearing adaptation**
   \[
   G_{t+1}=\mathcal U(G_t,D_X)
   \]
   where source exposure changes the learner.

3. **performative loop**
   \[
   \theta_t
   \to
   \text{deployed recommendation/output}
   \to
   H_{t+1}
   \to
   D_{t+1}
   \to
   \theta_{t+1}.
   \]

Current X documentation makes (3) plausible for Grok-powered recommendation features because X explicitly says the deployed system may learn from interactions during normal use. But the paper must not assume the undisclosed mechanics.

Phrase it:

> "When Grok-mediated outputs alter subsequent X behavior/data and that altered distribution returns to the learner, the loop enters the performative-prediction regime."

**Severity:** conceptual blocker for related-work accuracy.

---

# C. Strongly recommended technical fixes

## C1. Continuation entropy is not a clean direct readout of \(\mu\)

Entropy measures uncertainty/diversity of a distribution, not salience itself.

A low-entropy continuation distribution could arise because one continuation dominates, but that does not make the corresponding state globally salient.

### Better \(\mu\) candidates

Black-box:
- spontaneous mention probability under calibrated neutral prompts;
- retrieval propensity;
- normalized log-probability mass over a predefined state family;
- controlled attention/selection odds;
- response latency/cost if available.

White-box:
- activation frequency/occupancy of independently validated features;
- feature intervention sensitivity.

Continuation entropy can remain a **secondary diagnostic**, not the definition of salience.

---

## C2. "Two bundle components move in the same direction" needs signed component definitions

\(\Pi\), \(\mu\), and \(d^{(c)}\) are heterogeneous objects.

"Same direction" is undefined unless each component is first mapped to a preregistered scalar contrast relative to the target/source geometry.

Example:

\[
\Delta_\Pi
=
D(\Pi_{\text{arm}},\Pi_H)
-
D(\Pi_{\text{arm}},\Pi_X),
\]

with analogous \(\Delta_\mu,\Delta_d\).

Then "source-conditioned" could mean each registered contrast moves toward the source and away from target, with thresholds fixed in advance.

Do not collapse them to one truth score; use convergence as a diagnostic.

---

## C3. "No scoop" should be weakened

\`LITERATURE.md\` is unusually honest about search limitations, including quarantining dubious/future-dated IDs.

But:

> "No scoop found."

still reads more strongly than the evidence warrants.

Use:

> **No directly matching prior result found in the scoped literature pass.**

The search is not systematic/exhaustive enough to certify novelty universally.

---

## C4. Reward-hacking language overstates inevitability

Current related work says reward-hacking theory gives a reason engagement-proxy coupling is **expected** to diverge from the human target.

Skalse et al. establish severe constraints on proxies and characterize reward hacking; that does not show this particular engagement coupling necessarily or probabilistically diverges in our regime.

Use:

> "supplies a formal reason proxy fidelity cannot be assumed"

or:

> "shows why optimization against an imperfect proxy can diverge from the intended target."

---

## C5. Treat "sycophancy is Syndrome in miniature" as analogy, not evidence of shared mechanism

This line is memorable but currently too causal.

Better:

> "Sycophancy is an output-level analogue of one Syndrome-like direction: audience-conditioned behavior can outrank truth. It does not establish source-conditioned internal geometry."

Same for RLHF distributional narrowing: adjacent phenomenon, not evidence for our mechanism.

---

# D. Manhattan asymmetry

The Syndrome half is now much more mature than Manhattan.

Syndrome has:

- a formal bundle;
- a plausible developmental mechanism;
- source-specific empirical facts;
- a synthetic mechanism experiment;
- direct adjacent literature.

Manhattan currently has:

- a good conceptual distinction;
- a toy normalization formula;
- a secondary protocol sketch;
- adjacent utility/value literature.

This is not necessarily a flaw.

Two options:

### Option 1 — explicitly asymmetrical paper

Make Syndrome the main research hypothesis and Manhattan the contrastive dual/archetype.

This is probably the cleaner paper today.

### Option 2 — equalize them

Give Manhattan:
- a stronger formal controller model;
- an explicit invariance/conservation criterion;
- a synthetic experiment;
- serious rivals (changing objectives, scale-induced preference coherence, context effects, evaluator artifacts);
- a separate literature lane.

Do not imply equal evidential maturity if the work remains asymmetric.

---

# E. DOI / GitHub-release gate

For the user's intended path — GitHub + Zenodo DOI + targeted expert circulation — I would use this release gate.

## Before v1.0

Required:

- [ ] B1 notation consistency.
- [ ] B2 fix §14 proxy sentence.
- [ ] B3 restore machine/TLICA analogue boundary.
- [ ] B4 split acute vs durable source effects.
- [ ] B5 add correction-information ladder.
- [ ] B6 narrow performative-prediction claim.
- [ ] C1 improve \(\mu\) readout.
- [ ] C2 define signed component contrasts.
- [ ] C3/C4/C5 literature wording.
- [ ] re-fetch every publication citation from a canonical source.
- [ ] re-fetch current X/xAI policy/product claims on release day.
- [ ] standalone abstract/introduction understandable without TLICA.
- [ ] PDF build checked for equations, links, and references.
- [ ] author identity / pseudonymity decision made **before** DOI metadata.
- [ ] immutable Git tag created.
- [ ] Zenodo package contains manuscript + protocol + claim ledger (or clearly linked supplement).
- [ ] release notes state **preprint / not peer reviewed**.

## After v1.0 DOI

Start \`EXPERT_OUTREACH_PLAN.md\` Wave A.

Do not wait for "perfect." The point of expert circulation is to acquire adversarial correction — but freeze a version coherent enough that the recipients are attacking the thesis rather than obvious notation/identifiability defects.

---

# F. Validation status

The merge commit records:

> \`make validate PASS\`

No GitHub Actions workflow or commit-status checks are attached to the merge commit, so this audit can confirm **the repository records a successful local validation**, not independently certify the run through CI.

---

# G. Bottom line

## Current status

\[
\boxed{
\text{strong research draft}
\;>\;
\text{clever essay}
\quad\text{but}\quad
\text{not yet DOI-freeze quality}
}
\]

The hard part succeeded: the central Syndrome insight survived formalization and literature contact.

The remaining work is mostly **discipline at the interfaces**:

- bundle vs metric;
- representation vs persona;
- acute conditioning vs persistent imprint;
- knowing bias exists vs possessing enough information to correct it;
- selected-data adaptation vs performative feedback;
- TLICA-human coordinates vs machine operational analogues.

Once those are cleaned, this is a credible independent preprint to freeze, DOI, and put directly in front of the researchers listed in \`EXPERT_OUTREACH_PLAN.md\`.

The memorable line still survives:

> **The shape of the audience can become part of the shape of meaning.**

The next version's job is to make every mathematical and experimental word underneath that sentence equally precise.
