# Moreish publication audit — 2026-09-19

**Repository:** `femboy2112/TLICA`  
**Branch audited:** `moreish-publication-v1.0-2026-09`  
**Head audited:** `4c12b6eb5af655eed90616f4f8c09c454a57132d`  
**Base:** `main` at `6708b411e5ff7481569b695f3a0df32d3c53f423`  
**Branch state at audit:** 13 commits ahead, 0 behind  
**Status:** publication candidate; nearly preprint-ready; not yet journal-submission-ready.

## Executive status

The Claude continuation materially improved the paper. The publication branch no longer reads as if it is claiming novelty for present bias, Bellman continuation value, plural control, self-evidencing, or first-person method. The strongest surviving distinctive object is now narrower and more defensible:

$$\boxed{\text{bounded first-person synthesis} + \text{scope-usurpation pathology} + \text{heterogeneous governance framing}}$$

The conceptual work is no longer the main bottleneck. Remaining work is finite and mostly concerns:

1. closing the last novelty/source flanks;
2. repairing one internal formalism contradiction;
3. normalizing the bibliography and provenance;
4. final author review;
5. generating the actual preprint and anonymous journal artifacts.

## Current manuscript state

Active publication manuscript:

`research/moreish_ontology_2026-09-13/publication_v1_0/MANUSCRIPT_v1_0_WORKING.md`

Audit measurements at the inspected head:

- approximately **7,165 words** including references;
- abstract: **191 words**;
- keywords: **6**;
- formal reference entries: **25**;
- current venue target remains *Phenomenology and the Cognitive Sciences* unless later venue review changes that decision.

The shortened method/claim-boundary section is an improvement. It preserves the load-bearing limits while reducing front-loaded methodological bulk:

- one-author first-person object;
- no population generalization;
- mathematics constrains the analogy but does not certify autobiography;
- autobiographical fit does not validate the model for others;
- the finite toy is calibration/illustration, not phenomenological evidence;
- redemptive over-coherence remains an explicit falsification hazard.

## What the Claude pass successfully improved

### 1. Novelty discipline

The hostile novelty search was directionally correct and materially narrowed the paper.

The current five-element candidate bundle is:

1. **E1 — scope compilation:** a locally valid sensor is promoted into global executive authority;
2. **E2 — epistemic ratchet:** installation and revision operate under asymmetric evidential thresholds;
3. **E3 — self-seasoning feedback:** consequences generate states that make the governing interpretation feel increasingly apt;
4. **E4 — authority architecture:** governance among heterogeneous signals rather than replacement by one global scalar;
5. **E5 — bounded first-person specimen:** the structure is developed on one autobiographical case without population generalization.

The audit result is not "all five are novel." It is:

- **E1:** currently the strongest surviving distinctive limb;
- **E2:** has close formal antecedents and is unsafe as a standalone novelty claim;
- **E3:** substantially prior art as a phenomenon;
- **E4:** substantially prior art as an architecture;
- **E5:** not novel as method.

The remaining defensible novelty hypothesis is therefore an **integration claim**, especially the pathology framing of **scope usurpation** across heterogeneous signal types.

### 2. Moral intent/outcome firewall

The §3.3 Jesus/WWJD section is now significantly stronger.

The paper explicitly separates:

$$\text{moral intent} \to \text{perceived harm model} \to \text{chosen correction} \to \text{world-state consequence}$$

with no shortcut

$$\text{good intent} \not\Rightarrow \text{good outcome}$$

This prevents the section from implying that a sincere drive toward moral error-cancellation establishes moral achievement.

The current manuscript correctly says:

- the objective describes the controller's intent;
- the perceived perturbation is itself model-mediated;
- an attempted correction can generate more real harm than less intervention or no intervention;
- the long arc being "morally better" is an authorial present evaluation, not a certificate;
- present moral adequacy remains open.

This distinction is load-bearing and should survive every later compression.

### 3. Toy-model repair

The executable toy and its test report were repaired in the right direction.

Current intended interpretation:

- (d) is an **option-richness / maneuverability resource**;
- ($d \neq |A(x)|$);
- legal-action cardinality remains nonzero;
- both policies are state-responsive feedback rules;
- the tested contrast is **myopic horizon-1 reward** versus **full-horizon continuation value**;
- the toy is an illustration/calibration of standard sequential-control structure, not evidence for the autobiographical interpretation.

The recorded run reports:

- CPython 3.12.3;
- standard library only;
- 6/6 checks passed;
- decoupled calibration: greedy = DP = brute-force = 32;
- coupled case: greedy (J=12), optimal (J=30);
- DP and brute-force agree.

### 4. AI provenance

The branch now records substantive use of:

- **OpenAI ChatGPT — GPT-5.6 Sol**;
- **Anthropic Claude — Claude Code, Opus 4.8**.

The disclosure language is appropriately stronger than "copyediting." It records substantive roles including drafting, adversarial critique, literature/source work, mathematical/code checking, typesetting, and manuscript revision.

Historical model identities remain unresolved where the provenance record only says `Assistant`. The correct rule remains: **do not invent missing model identities**.

## Independent audit findings not yet fully absorbed

### A. E2 has an even closer antecedent: Ditto & Lopez (1992)

A closer source than the current branch foregrounds is:

**Ditto, P. H., & Lopez, D. F. (1992). "Motivated Skepticism: Use of Differential Decision Criteria for Preferred and Nonpreferred Conclusions."**

This work explicitly studies **different evidential decision criteria** for preferred versus nonpreferred conclusions.

That is structurally close to the epistemic-ratchet idea because it directly concerns unequal thresholds for accepting versus resisting conclusions.

This does **not** eliminate the Moreish ratchet, because Moreish is more specific:

- installation of a governing rule;
- later policy revision under downstream consequences;
- asymmetry between what can canonize a rule and what is allowed to de-canonize the policy compiled from it.

But E2 should now be framed as:

$$\boxed{\text{novel integration/application}\quad\text{rather than}\quad\text{novel asymmetry mechanism}}$$

**Action:** add Ditto & Lopez to the hostile novelty audit and, if retained as load-bearing, to the manuscript discussion/reference list.

### B. AGM is useful vocabulary but probably not the strongest threat

The AGM belief-revision tradition distinguishes expansion, contraction, and revision formally.

That makes it relevant background for different belief-change operators, but AGM by itself does not assert the psychological Moreish asymmetry that installation and revision have different real-world evidential thresholds.

Treat AGM as:

- relevant formal vocabulary;
- not yet a direct owner of the ratchet mechanism.

### C. One real repository contradiction remains

The repaired toy code/test output and the older formalism dossier are not fully synchronized.

Current stale file:

`research/moreish_ontology_2026-09-13/FORMALISM_AND_PROBES.md`

It correctly warns near the top that ($d \neq |A(x)|$), but later still contains stale language such as:

- `d = open "doors" ... (the concrete |A(x)| proxy)`;
- greedy terminal `|A(x)| (0)` collapses while feedback stays maximal.

Those later sentences are now false under the repaired model.

The correct statement is:

- terminal **(d)** collapses to zero in the greedy run;
- legal-action cardinality stays nonzero;
- the toy demonstrates depletion of option-richness / maneuverability, not deletion of all legal moves.

Also replace "option-deleting move" where necessary with a phrase such as:

- **option-richness-depleting move**;
- **maneuverability-reducing move**.

Unless a genuinely irreversible state model is built, do not imply literal action-set deletion.

### D. Checklist/provenance drift

Some operational files still contain stale unchecked tasks.

Examples:

- `SUBMISSION_CHECKLIST.md` still leaves "determine whether Claude materially edited this manuscript" unchecked even though `AI_PROVENANCE_AND_DISCLOSURE.md` now explicitly records that it did.
- Several source/formalism items are partially completed but not reconciled with the checklist state.

**Action:** run one checklist reconciliation pass after the next source/formalism edits.

## Wording refinements recommended before freeze

### 1. Avoid universal novelty language

Current manuscript language:

> "No single neighboring literature contains all five."

That is too universal for an incomplete search.

Prefer:

> **"This audit did not identify a single source or literature family containing all five in this combination."**

This states what was actually observed.

### 2. Tighten the active-inference comparison

Avoid describing active inference as a **"formal symmetric-Bayesian confirmation account."**

That phrase is nonstandard and unnecessary.

Prefer something like:

> **"formal Bayesian model-evidence / free-energy account"**

or a similarly source-faithful formulation.

The point is comparison, not terminological ownership.

## Reference integrity status

The bibliography is substantially improved but not fully frozen.

Still live:

- verify/add DOI for Carver & Scheier (1982);
- verify/add DOI for Kunda (1990);
- verify/add DOI for Lord, Ross, & Lepper (1979);
- verify Bellman edition metadata;
- obtain/inspect a primary or authoritative copy of Varela & Shear before relying on a specific methodological proposition;
- convert claim-bearing cultural/literary/religious sources to venue-style references where needed;
- verify exact scriptural loci/wording retained in final text;
- run full in-text-citation ↔ reference-list consistency.

Candidate DOI values identified during audit but still to be confirmed against publisher/authoritative records before insertion:

- Carver & Scheier (1982): `10.1037/0033-2909.92.1.111`
- Kunda (1990): `10.1037/0033-2909.108.3.480`
- Lord, Ross, & Lepper (1979): `10.1037/0022-3514.37.11.2098`

Do not insert solely because they appear in this audit; confirm against an authoritative record first.

## What still needs doing

### Priority 1 — close the remaining hostile novelty debt

Before freezing the novelty section:

1. audit **Ditto & Lopez (1992)** for E2;
2. audit **Taber & Lodge (2006)** for motivated skepticism / asymmetric scrutiny;
3. inspect **AGM belief revision** enough to bound it accurately;
4. inspect **Powers (1973)** primary text rather than relying on secondary summaries;
5. decide whether Fodor/Minsky/modularity and self-fulfilling-prophecy lanes are still material enough to search.

Do not spend equal effort on every flank. The goal is to attack the **load-bearing novelty claim**, not to build an encyclopedic literature review.

### Priority 2 — synchronize the formal apparatus

Repair `FORMALISM_AND_PROBES.md` so that all of the following agree:

- manuscript;
- source/novelty audit;
- toy script;
- raw JSON;
- toy test report;
- formalism note.

Target invariants:

$$d = \text{option-richness/maneuverability proxy}$$

not

$$d = |A(x)|.$$

And:

$$\text{myopic feedback}\quad\text{vs}\quad\text{full-horizon feedback}$$

not open-loop vs feedback.

### Priority 3 — one author-level manuscript pass

This should be an **author review**, not another broad AI conceptual rewrite.

Decisions still belonging to Leah:

- whether "the long arc has become morally better" says exactly what she intends;
- whether any heavy autobiographical receipts belong in the public paper;
- whether the related-literature section stays before §4 or moves later;
- whether the comic/profane register is at the desired publication intensity.

Default recommendation: keep heavy receipts out unless one is required to make the structural argument intelligible.

### Priority 4 — freeze the intellectual master

Once novelty/source debt is closed:

- stop adding new conceptual machinery;
- normalize references;
- reconcile checklist/provenance;
- run final epistemic-status language scan;
- count words/headings;
- check all cross-references and math delimiters.

### Priority 5 — generate publication artifacts

Still not complete:

- named/public preprint LaTeX source;
- named/public PDF;
- anonymous double-blind LaTeX source;
- anonymous PDF;
- separate title page;
- declarations;
- funding statement;
- competing-interests statement;
- author city/country;
- active email;
- ORCID choice;
- acknowledgments decision;
- PDF metadata stripping for blind build;
- visual page-by-page inspection.

### Priority 6 — final validation and deposit

After all final edits:

- run `make validate` again;
- re-run toy checks;
- inspect `git diff main...moreish-publication-v1.0-2026-09`;
- verify live venue AI/preprint/APC/submission rules;
- freeze preprint commit SHA;
- reserve/publish Zenodo DOI;
- create/update PhilArchive entry;
- only then generate the final journal submission package.

## Claim ledger after this audit

| Claim | Status |
|---|---|
| Greedy need not optimize total return under state coupling | **DISCLOSED / standard** |
| Toy reproduces one coupled failure + decoupled calibration | **OBSERVED in recorded run** |
| Present bias / dynamic inconsistency are established neighbors | **CORROBORATED / standard literature** |
| E3 self-seasoning as a general phenomenon is novel | **REFUTED as novelty claim** |
| E4 plural/non-scalar authority architecture is novel | **REFUTED as broad novelty claim** |
| E5 bounded first-person method is novel | **REFUTED as method novelty claim** |
| E2 asymmetric epistemic ratchet is novel in isolation | **WEAKENED; close antecedents exist** |
| E1 scope-usurpation pathology survives current search | **CONJECTURED-surviving** |
| Five-part integration is novel | **CONJECTURED / not yet saturated** |
| Autobiographical mapping is accurate | **CONJECTURED / authorial structural interpretation** |
| Architecture generalizes beyond Leah | **UNVERIFIED** |
| Long arc is morally better | **AUTHORIAL EVALUATION**, not empirical result |
| Present moral adequacy | **UNVERIFIED** |

## Bottom line

The Claude pass was substantively successful because it did not merely polish the paper; it **reduced its truth debt**.

The paper no longer needs a new theory pass.

Its remaining route is:

$$\boxed{\text{close novelty flanks} \to \text{repair formalism contradiction} \to \text{normalize sources} \to \text{Leah sign-off} \to \text{freeze v1.0} \to \text{build artifacts} \to \text{deposit + submit}}$$

At that point the paper should be treated as **v1.0 preprint-ready**.

Until then, the correct status is:

$$\boxed{\textbf{strong publication candidate; nearly preprint-ready; not yet journal-submission-ready}}$$


---

# 2026-09-19 current-head refinement — slack, autopilot, and compiled governance

**Current branch head considered for this refinement:** \`4ba85e20f7f40d76d795a0116784510a0cd3b895\`

This refinement responds to the Gemini-identified **executive-depletion / slack-bootstrap problem** between manuscript §5 and §10, and to Leah's clarification of the phenomenology.

## The qualification

TLICA does **not** entail

\[
S\le 0
\Longrightarrow
\text{greedy or degenerate behavior}.
\]

Foundation §8.11 explicitly says that when slack is nonpositive the pressured/contact-driven response dominates and active Mode-B reweighting is unavailable, but it also explicitly warns:

> automatic is not the same as myopic, and an automatic policy may preserve future room.

The Moreish claim is narrower and autobiographically conditional:

\[
\boxed{
\text{low slack}
+
\text{already-degenerate internalization}
\Longrightarrow
\text{likely degenerate local move}
}
\]

The degeneracy is therefore not *caused by* low slack. Low slack removes or sharply reduces the ability to reflexively override/reweight the **already-imprinted** policy.

## Hans and Veruca are not runtime homunculi

The current prose risks making Hans and Veruca sound like internal agents who deliberate in real time and then choose the action.

That is not the strongest architectural reading.

Under low slack, the causal order is closer to:

\[
G_{\mathrm{degenerate}}
+
S\le0
\longrightarrow
\pi_{\mathrm{auto}}(x;G_{\mathrm{degenerate}})
\longrightarrow
a_t
\longrightarrow
\text{Hans/Veruca-shaped interpretation}.
\]

In words:

1. slow lived-I structure \(G\) already carries the learned policy geometry;
2. low slack removes effective active Mode-B reweighting;
3. the current automatic/contact-driven frame produces a locally coherent response;
4. Hans/Veruca-style reasoning appears phenomenologically as an explanation or rationalization of what already feels obvious in that frame.

So the low-slack process is **not** primarily:

\[
\text{Hans argues}
\to
\text{Hans wins}
\to
\text{action}.
\]

By that point, the argument has largely already occurred historically through internalization and imprinting.

Hans and Veruca are better treated as **personified readouts of policy structure**.

## Why this feels like “business as usual”

Because the current frame is already active, its interpretation is self-resonant.

The local move can feel:

- obvious;
- appropriate to the present situation;
- identity-consistent;
- descriptively accurate from inside the active frame;
- easily rationalized after the fact.

The system does not phenomenologically announce:

> maladaptive global policy currently executing.

It announces something more like:

> given *this* situation, obviously this is what makes sense.

Hence the load-bearing distinction:

\[
\boxed{
\text{locally coherent}
\neq
\text{globally adequate}.
}
\]

The failure becomes visible across the coupled trajectory, not necessarily inside any one local state.

This is the Greedy Integral Problem applied to **self-interpretation** as well as action.

## Three roles for each comic figure

The publication version should distinguish at least three architectural roles.

### Hans

**Hans-as-sensor**

> representations may be wrong.

This is locally useful adversarial epistemics.

**Hans-as-degenerate compiled frame**

> because projected futures are uncertain, they deserve weak practical authority.

This is the scope-compilation error.

**Hans-as-low-slack narrator**

> obviously we are not ruining Tuesday for a speculative spreadsheet future.

At this stage the voice is largely a phenomenological caption on the already-active policy.

### Veruca

**Veruca-as-sensor**

> this life must contain actual experienced reward.

This is useful reward telemetry.

**Veruca-as-degenerate compiled frame**

> present resonance is sufficient evidence for policy.

This is the scope-compilation error.

**Veruca-as-low-slack narrator**

> obviously take the thing that makes the current situation livable.

Again, the narration is downstream of the already-active frame more than an independent deliberative cause.

This distinction prevents the character construction from becoming an implicit homunculus model.

## The council is a training-time model, not the low-slack runtime

Gemini's objection is correct if manuscript §10 is read literally as the mechanism required at every pressured choice:

\[
\text{low slack in §5}
\quad\text{vs}\quad
\text{multi-agent deliberative council in §10}.
\]

A system that lacks slack cannot be expected to fund expensive real-time parliament.

The stronger interpretation is:

\[
\boxed{
\text{the council is an explicit high-slack model of the controller.}
}
\]

When slack is available, the system can separate signals that ordinarily arrive fused:

- Hans is reporting model uncertainty;
- Veruca is reporting present-reward starvation;
- the moral channel is reporting possible externalized cost;
- no one signal is automatically entitled to determine action.

That decomposition is computationally expensive at first.

Its purpose is not to remain expensive forever.

## Slack first, imprinting later

The foundation already supplies the transition mechanism.

Mode B is self-directed writing into the slow lived-I structure \(G\). Osmotic/contact-driven imprinting and self-directed imprinting operate on the same substrate family from different sides.

So the corrected architecture can be written schematically as:

\[
G_{\mathrm{old}}
\xrightarrow[\;S>0\;]{\text{repeated explicit correction}}
G_{\mathrm{new}}.
\]

Early in correction:

\[
S\le0
\Longrightarrow
\pi_{\mathrm{auto}}(\cdot;G_{\mathrm{old}})
\approx
\text{degenerate Moreish default}.
\]

When positive slack exists:

\[
S>0
\Longrightarrow
\text{Mode-B correction/reweighting becomes available}.
\]

Repeated corrected operation can then alter \(G\).

Later:

\[
S\le0
\Longrightarrow
\pi_{\mathrm{auto}}(\cdot;G_{\mathrm{new}})
\]

need not reproduce the old degenerate response.

The key claim is therefore:

\[
\boxed{
\text{use slack to change the controller}
\neq
\text{require slack forever to run the changed controller}.
}
\]

## The three-phase corrective

The paper's practical architecture is best understood in three phases.

| Phase | Slack condition | Mechanism | Functional role |
|---|---:|---|---|
| **Old default** | low | already-imprinted automatic policy | Hans/Veruca rationalize a locally coherent but globally degenerate frame |
| **Retraining** | positive | explicit Mode-B decomposition / council | separate sensors from governors; practice corrected responses |
| **Compiled governance** | low again | newly imprinted automatic response | better scope discipline survives without reconstructing the council |

This resolves the apparent contradiction between §5 and §10.

## Cheap tripwires are the transition layer

Imprinting takes repetition. During the interval between recognizing the problem and having the corrected policy become cheap/default, low-slack episodes remain dangerous.

The bridge should therefore include **low-cost precommitted tripwires** that protect option value without demanding full deliberation.

Examples:

- if the action is hard to reverse, delay it;
- if pressure is high, do not make the irreversible move;
- if a decision deletes a major option, require a pause or external check;
- if the current relief is financed by future obligation, flag it before action.

Schematically, a cheap gate can be something like:

\[
q(x,a)\in\{0,1\},
\]

where \(q=1\) marks a predeclared high-risk transition.

This is deliberately cheaper than solving the full long-horizon control problem online.

The tripwire is not the ultimate corrective. It protects the system **while the new controller is being compiled**.

## The deeper recursion

The same machinery that made the original Moreish frame self-reinforcing can be recruited in reverse.

Repeated degenerate operation can train:

\[
G_{\mathrm{degenerate}}.
\]

Repeated corrected operation can train:

\[
G_{\mathrm{better}}.
\]

So the long-run target is not merely:

> govern Hans and Veruca better.

It is:

\[
\boxed{
\text{train a system whose default Hans and Veruca already know their scope.}
}
\]

Hans need not disappear. The better-imprinted Hans can become:

> uncertainty is a reason to audit the forecast, not a license to erase future causal structure.

Veruca need not disappear. The better-imprinted Veruca can become:

> current life must contain reward, but present resonance alone does not get capital-allocation authority.

The corrected architecture therefore changes not only the executive decision but eventually **what arrives as the obvious local response**.

## Stronger formulation of the paper's corrective

The paper should not end with only:

\[
\text{better governance}.
\]

The fuller dynamical arc is:

\[
\boxed{
\begin{aligned}
\text{scoped truths compiled globally}
&\to G_{\mathrm{degenerate}}\\
&\to \text{degenerate autopilot}\\
&\to \text{locally coherent Hans/Veruca rationalization}\\
\text{positive slack}
&\to \text{explicit decomposition/council}\\
&\to \text{corrected repeated responses}\\
&\to G_{\mathrm{better}}\\
&\to \text{better low-slack autopilot}.
\end{aligned}
}
\]

This yields a stronger concluding principle:

\[
\boxed{
\textbf{Governance should eventually alter what needs governing.}
}
\]

Or, in the paper's compiler register:

> **The council is training-time interpretation. Imprinting compiles the result into the runtime.**

## Epistemic boundary

This interpretation is strongly aligned with the current TLICA machinery but must not be overstated.

**Supported by the current architecture:**

- slack gates effective active Mode-B reweighting;
- low slack favors contact-driven/automatic response;
- Mode B is self-directed writing into slow lived-I structure \(G\);
- imprinting and activation are distinct;
- repeated patterning can alter later substrate-level response dispositions.

**Not yet empirically established by TLICA itself:**

- that this exact Moreish retraining process occurs with the proposed time course;
- that Hans/Veruca-specific defaults are measurably rewritten in the way described;
- that the \(S=0\) gate is the correct empirical threshold;
- that a particular tripwire accelerates imprinting or improves long-run outcomes.

So the manuscript should present this as the **best current mechanistic continuation**, not as an experimentally established treatment model.

## Publication impact

This is now the most important unresolved conceptual addition before freezing v1.0.

The required manuscript change is modest in size but load-bearing in function:

1. add the slack-bootstrap clarification to §9;
2. reframe §10 explicitly as a high-slack training-time council rather than mandatory runtime parliament;
3. add cheap tripwires as the transition layer;
4. use §11 to map the ordinary-language mechanism onto TLICA slack + self-directed imprinting;
5. preserve the qualification that low slack reveals the currently compiled automatic policy — it does not intrinsically imply greed or degeneracy.

Once this is integrated, the paper's sections §5, §9, §10, and §11 should form one coherent dynamical arc rather than a diagnosis followed by a computationally expensive corrective.
