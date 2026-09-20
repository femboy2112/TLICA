# AI provenance and disclosure — Moreish publication v1.0

**Branch:** `moreish-publication-v1.0-2026-09`  
**Date:** 2026-09-19  
**Purpose:** tell the truth about AI participation without either laundering it into "copyediting" or surrendering human authorship/accountability.

## 1. Governing rule

The publication record must distinguish:

- **conceptual origin / autobiographical testimony**;
- **assistant-proposed synthesis or mapping**;
- **author acceptance, rejection, or revision**;
- **source discovery**;
- **source verification**;
- **formal derivation / code execution**;
- **editorial and typesetting assistance**.

AI agreement is not independent corroboration. A sentence can be author-endorsed and still be wrong. A citation can be suggested by AI and only becomes usable after source verification.

## 2. What the repository already establishes

The existing Moreish dossier records that:

- the manuscript is Leah's authorial self-application;
- the 2026-09-14 three-sensor continuation was developed with AI assistance;
- assistant-proposed readings were explicitly labeled for author review rather than silently attributed to Leah;
- conversation provenance was preserved as provenance, **not evidence**;
- the finite toy was created/checked within the AI-assisted research workflow, with raw outputs and calibration retained;
- the final application text was author-endorsed before promotion to `main`.

Relevant durable records:

- `../README.md`
- `../AUTHOR_INTENT_AND_HANDOFF.md`
- `../AUTHOR_LAYER_WORKSHEET.md`
- `../EVIDENCE_CLAIMS_AND_SOURCES.md`
- `../FORMALISM_AND_PROBES.md`
- branch `moreish-wwjd-moral-actuator-2026-09-14`:
  - `PROVIDENCE_CONVERSATION_RECORD_2026-09-14.md`
  - `PROVIDENCE_CONVERSATION_RECORD_2026-09-14_CONTINUATION.md`
  - `PROVIDENCE_METHOD_ADDENDUM_2026-09-14.md`
  - `PROVIDENCE_SYNTHESIS_2026-09-14.md`

The Providence transcript labels the model-side participant simply **Assistant**. It does not encode a trustworthy model/version identifier.

## 3. Known AI system identity

### Current publication-hardening pass — known

On 2026-09-19, this publication-hardening branch was developed with:

- **OpenAI ChatGPT — GPT-5.6 Sol**

Roles in this pass:

- repository inspection and state reconciliation;
- publication-readiness critique;
- venue/publisher policy research;
- source discovery and primary-source verification;
- drafting the shorter abstract, method/claim boundary, related-literature section, disclosure language, and publication apparatus;
- integrating Leah's explicit correction that moral intent does not imply good moral outcome;
- GitHub branch/file/commit operations at Leah's request.

### Continuation hardening pass — 2026-09-19 (Claude)

A subsequent same-day publication-hardening pass on this branch was performed with:

- **Anthropic Claude (Claude Code, Opus 4.8)**

Roles in this pass:

- fetching and analyzing the ChatGPT-seeded branch; independent verification of its citations against primary sources;
- an adversarial hostile-novelty literature search across eleven families, with every load-bearing source re-verified by real retrieval (results in `SOURCE_AND_NOVELTY_AUDIT.md`);
- rewriting the manuscript's adjacent-literature / novelty-boundary section to concede prior art and narrow the claim;
- completing the venue-style bibliography;
- repairing corrupted display-math in the source audit and correcting the toy-model `d`-vs-`|A|` language (with a clean re-run);
- committing checkpoints on this branch (no merge, no push without author authorization).

The conceptual architecture and autobiographical claims remain Leah's; both assistants operated under author direction, and all cited sources were verified against real records before entering the manuscript.

### Later revision and audit passes — 2026-09-19c to 2026-09-20

Subsequent conceptual-refinement and audit passes on this branch used:

- **OpenAI ChatGPT 6** — the slack-bootstrap/compiled-governance refinement, the costume-party/chosen-sincerity developmental precursor, and the "withhold TLICA until §11" architectural critique (each verified and integrated under author direction);
- **Anthropic Claude (Claude Code, Opus 4.8)** — verification, integration, de-branding, title-page and declarations assembly, and typesetting.

Leah confirmed this tool set (ChatGPT 6 and Claude Code Opus 4.8) on 2026-09-20.

### Earlier Moreish development — exact model identity not yet recovered

The repository proves substantive AI assistance, but the exact provider/model/version for every earlier interaction is not encoded in the durable transcript.

**Do not invent it.**

Before final journal submission, recover model/provider names from any available chat/session metadata if practical. If exact version recovery fails, disclose at the service/provider level that can actually be substantiated and state that model-version metadata was not retained.

## 4. Human contribution boundary

The publication should make clear that Leah:

- supplied the autobiographical object and its lived interpretation;
- originated or explicitly endorsed the paper's central figures and conceptual direction;
- corrected assistant misunderstandings of the acquisition methodology;
- specified the Jesus/WWJD continuation and its moral-controller meaning;
- decided the disclosure calibration of sensitive autobiographical material;
- accepted/rejected revisions;
- owns the normative judgments;
- is responsible for all final claims, references, and wording.

AI systems:

- proposed framings and decompositions;
- stress-tested claims;
- drafted and revised prose under instruction;
- helped map the phenomenology to control-theoretic language;
- found candidate literature and venue rules;
- generated/checked code or formal examples where recorded;
- assisted typesetting and repository organization.

No AI system is an author.

## 5. Source verification rule

For every citation introduced or shaped through AI assistance:

1. locate a real source;
2. prefer primary/publisher/official records;
3. verify author/title/year/venue/pages/DOI;
4. verify the source actually supports the proposition attached to it;
5. record uncertainty when a primary copy is unavailable;
6. do not cite an AI summary as evidence.

Current initial verified publication-neighbor set is tracked in `SOURCE_AND_NOVELTY_AUDIT.md`.

## 6. Disclosure draft — public preprint

Candidate language, not frozen:

> **AI-assisted research and manuscript development.** Generative AI systems were used as dialogic research and manuscript-development tools during the development of this paper, including structural exploration, adversarial critique, drafting and revision, source discovery, mathematical/code checking, and typesetting assistance. The autobiographical object, conceptual commitments, normative judgments, selection and rejection of proposed framings, and final editorial decisions are the author's. The author remains responsible for the accuracy of all claims and citations. The publication-hardening passes used OpenAI ChatGPT (GPT-5.6 Sol in the initial 2026-09-19 pass, and ChatGPT 6 in later revision and audit passes) and Anthropic Claude (Claude Code, Opus 4.8). Earlier AI-assisted development is preserved in the project's provenance record; exact historical model-version metadata was not retained in every transcript. No AI system is listed as an author.

This is intentionally stronger than "AI-assisted copyediting" because copyediting would be false.

## 7. Disclosure draft — Springer journal route

Springer Nature's current guidance requires substantive LLM use to be documented in Methods or a suitable alternative section, and its current risk framework treats author-directed outlining/drafting/structuring as an amber use requiring disclosure and human accountability.

Candidate blinded-manuscript language:

> Generative AI was used in an author-directed manuscript-development workflow for structural exploration, adversarial critique, drafting/revision, source discovery, mathematical/code checking, and typesetting assistance. The first-person data, autobiographical interpretations, conceptual commitments, and final scholarly judgments are the author's. All references and substantive claims are subject to human verification, and the author accepts responsibility for the final manuscript. Additional tool-identifying details are supplied in the separate title-page/disclosure material where necessary to preserve double-blind review.

Candidate title-page disclosure:

> The publication-hardening passes used OpenAI ChatGPT (GPT-5.6 Sol in the initial 2026-09-19 pass, and ChatGPT 6 in later revision and audit passes) and Anthropic Claude (Claude Code, Opus 4.8). Earlier stages also used generative-AI assistance as documented in the author's research provenance archive; some historical transcript records did not retain exact model-version metadata. AI systems were not treated as authors or independent evidential sources.

**Before submission:** re-check the journal's current wording and put the disclosure in exactly the location requested by the live submission system.

## 8. Double-blind constraint

The anonymous manuscript must not erase the **fact** of substantive AI use if the journal requires it, but tool/provider detail can live on the separate title page when revealing it would identify the author through a public provenance trail.

Do not link the blinded manuscript directly to:

- `femboy2112/TLICA`;
- Leah's GitHub account;
- the Zenodo author profile/DOI if that would trivially reveal identity;
- Providence transcript URLs.

The editor can receive full disclosure separately.

## 9. Open provenance tasks

- [ ] Recover any exact historical model/provider names for the 2026-09-13 to 2026-09-17 Moreish sequence that are actually available.
- [x] Record whether local Claude/Codex sessions materially edited this specific manuscript, rather than adjacent TLICA work. (yes — the 2026-09-19 Claude continuation pass above materially edited the manuscript novelty section and bibliography)
- [ ] Do not infer a model name from generic `Assistant` transcript labels.
- [ ] Freeze a final disclosure only after the manuscript stops changing.
- [ ] Record the final publication commit SHA and DOI in this file.
