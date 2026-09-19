# Moreish publication audit — 2026-09-19

**Repository:** `femboy2112/TLICA`  
**Branch audited:** `moreish-publication-v1.0-2026-09`  
**Head audited:** `4c12b6eb5af655eed90616f4f8c09c454a57132d`  
**Base:** `main` at `6708b411e5ff7481569b695f3a0df32d3c53f423`  
**Branch state at audit:** 13 commits ahead, 0 behind  
**Status:** publication candidate; nearly preprint-ready; not yet journal-submission-ready.

## Executive status

The Claude continuation materially improved the paper. The publication branch no longer reads as if it is claiming novelty for present bias, Bellman continuation value, plural control, self-evidencing, or first-person method. The strongest surviving distinctive object is now narrower and more defensible:

[
oxed{
	ext{bounded first-person synthesis}
+
	ext{scope-usurpation pathology}
+
	ext{heterogeneous governance framing}
}
]

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

[
	ext{moral intent}
	o
	ext{perceived harm model}
	o
	ext{chosen correction}
	o
	ext{world-state consequence},
]

with no shortcut

[
	ext{good intent}
otRightarrow	ext{good outcome}.
]

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
- (d
eq |A(x)|);
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

[
oxed{
	ext{novel integration/application}
quad	ext{rather than}quad
	ext{novel asymmetry mechanism}
}
]

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

It correctly warns near the top that (d
eq|A(x)|), but later still contains stale language such as:

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

[
d=	ext{option-richness/maneuverability proxy},
]

not

[
d=|A(x)|.
]

And:

[
	ext{myopic feedback}
quad	ext{vs}quad
	ext{full-horizon feedback},
]

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

[
oxed{
	ext{close novelty flanks}
	o
	ext{repair formalism contradiction}
	o
	ext{normalize sources}
	o
	ext{Leah sign-off}
	o
	ext{freeze v1.0}
	o
	ext{build artifacts}
	o
	ext{deposit + submit}
}
]

At that point the paper should be treated as **v1.0 preprint-ready**.

Until then, the correct status is:

[
oxed{	extbf{strong publication candidate; nearly preprint-ready; not yet journal-submission-ready}}
]
