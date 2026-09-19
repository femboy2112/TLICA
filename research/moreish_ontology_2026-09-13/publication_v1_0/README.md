# Moreish publication-hardening v1.0

**Branch:** `moreish-publication-v1.0-2026-09`  
**Base:** current `main` on 2026-09-19  
**Canonical source being hardened:** [`applications/moreish_ontology_v0_2_9.md`](../../../applications/moreish_ontology_v0_2_9.md)  
**Status:** active publication workstream; **do not merge to `main` until author review/sign-off**.  
**Foundation impact:** none. This branch is publication packaging and manuscript hardening only.

## Objective

Turn *This Ontology Is Really Moreish* from a strong first-final application draft into a publication-ready package without sterilizing the paper's voice or silently upgrading its epistemic status.

The publication target is deliberately split:

1. **public preprint master** — citable, named, complete, provenance-rich;
2. **anonymous journal submission build** — double-blind and venue-compliant;
3. **research apparatus** — claim ledger, source/novelty audit, toy-model receipts, and AI provenance retained outside the front-door prose.

The current working venue is *Phenomenology and the Cognitive Sciences* (Springer Nature), with a low-friction public route of Zenodo DOI first and PhilArchive indexing/linking afterward. Venue policies are time-sensitive; re-check immediately before submission.

## Frozen editorial decisions

These are branch-level constraints unless Leah explicitly changes them.

- Preserve the conceptual heart: **scoped truth -> sensor; sensor != global governor**.
- Preserve the modest mathematical claim: under state coupling, maximizing present reward **need not** maximize total return. Do not regress to "greedy always fails."
- Preserve the comic machinery as conceptual compression: Underground Super Hans, Pavlov's Veruca, Jesus/WWJD without root access, "the bug was in the compiler," and "self-seasoning."
- Do not convert autobiographical structural interpretation into a clinical diagnosis, population-level result, or validated causal psychology.
- Do not use TLICA as authority for the paper's claims. The intended direction remains phenomenon -> ordinary description -> formal question -> theory.
- Do not hide or minimize substantive AI assistance. The declaration must reflect the actual workflow, with human authorship/accountability explicit.
- Do not modify the frozen TLICA foundation from this branch.
- Do not overwrite or erase v0.2.9. Publication v1.0 is a descendant with its own preserved lineage.

## Acceptance criteria for a publication candidate

A build is not "submission ready" until all of the following are true:

- [x] Canonical v0.2.9 integrated on `main`.
- [x] Greedy claim weakened to the correct "need not" form.
- [x] Irreversible-downside sign in the option-value objective repaired.
- [x] Paper carries an explicit epistemic-status firewall.
- [x] New publication branch forked from current `main`.
- [x] Abstract is 150-250 words for Springer target. (191)
- [x] 4-6 indexing keywords supplied. (6)
- [x] Explicit method/scope paragraph states what kind of first-person object this is.
- [x] Nearest-neighbor literature section prevents a reviewer from misreading the contribution as merely "present bias in control-theory language."
- [x] Every load-bearing scholarly reference is verified against a real source; no AI-generated citation debt remains. (all cited refs retrieval-verified; 3 APA DOIs left off pending publisher check)
- [x] Bellman / present-bias / viability / first-person-method literature is integrated with an explicit novelty boundary.
- [x] Character dialogue is clearly identified as author-composed unless sourced.
- [x] Toy-model language is internally consistent: the demo variable `d` is **not** literal legal-action cardinality.
- [ ] AI-use disclosure names tools/roles at the level we can actually substantiate.
- [ ] Named preprint build and anonymous double-blind build both exist.
- [ ] Title page, declarations, competing-interests statement, funding statement, contact metadata, and ORCID choice are resolved.
- [ ] Reference list uses the target venue's author-year format and full DOI links where available.
- [ ] LaTeX/PDF build passes visual inspection.
- [ ] `make validate` passes after repository links/registration are finalized.
- [ ] Final venue policy re-check performed immediately before submission.

## What has been added on this branch

Publication work lives in this directory rather than inside the canonical application path until sign-off.

- `MANUSCRIPT_v1_0_WORKING.md` — publication-facing descendant of v0.2.9. It receives real manuscript edits.
- `SOURCE_AND_NOVELTY_AUDIT.md` — verified nearest-neighbor literature, source debt, and novelty boundary.
- `VENUE_AND_SUBMISSION_PATH_2026-09-19.md` — time-stamped venue requirements and AI/preprint policy notes.
- `AI_PROVENANCE_AND_DISCLOSURE.md` — disclosure floor and provenance questions that must be resolved honestly.
- `SUBMISSION_CHECKLIST.md` — operational package checklist.
- `TITLE_PAGE.md` — journal title-page scaffold with unresolved personal metadata left explicitly blank rather than invented.
- `LOCAL_SESSION_HANDOFF.md` — bootstrap for a local TLICA/Claude/Codex session to continue without reconstructing this chat.

## Load-bearing reviewer objection to pre-empt

A competent reviewer can reasonably say:

> "This is present bias / temporal discounting plus Bellman-style continuation value, redescribed autobiographically."

Do **not** answer by denying the overlap. The publication version must concede and cite the overlap, then isolate the actual proposed contribution:

1. **scope compilation:** a locally valid truth/sensor is promoted to global executive authority;
2. **epistemic ratchet:** phenomenological resonance can install a policy more easily than downstream suffering can revise it;
3. **self-seasoning feedback:** policy consequences generate states that make the governing interpretation feel still more apt;
4. **authority architecture:** correction is framed as governance among heterogeneous sensors rather than the replacement of one scalar objective by another;
5. **first-person structural specimen:** the integration is offered as an explicitly bounded autobiographical model, not as a population generalization.

That five-part bundle is the novelty candidate. Its novelty is **CONJECTURED until the literature audit is complete**.

## Epistemic ledger for this branch

- **DISCLOSED:** the v0.2.9 text exists on `main`; the toy program and its recorded checks exist; the Springer/Zenodo/PhilArchive policy pages recorded here were fetched on 2026-09-19.
- **CORROBORATED:** the standard dynamic-programming distinction between immediate reward and continuation value; present-bias/dynamic-inconsistency literature as a genuine neighboring family.
- **OBSERVED:** the current finite toy has a coupled case where greedy underperforms full-horizon control and a decoupled calibration where they agree.
- **CONJECTURED:** the paper's sensor/governor + ratchet + self-seasoning synthesis is sufficiently novel for publication; the structural self-interpretation accurately captures more than one autobiographical episode.
- **UNVERIFIED:** journal reviewer reception; pedagogical performance as a TLICA on-ramp; generalization beyond the authorial specimen.
- **Boundary:** this branch cannot turn an autobiographical conceptual paper into an empirical population result by prose alone.

## Continue from here

Read this file first, then:

1. `MANUSCRIPT_v1_0_WORKING.md`
2. `SOURCE_AND_NOVELTY_AUDIT.md`
3. `AI_PROVENANCE_AND_DISCLOSURE.md`
4. `VENUE_AND_SUBMISSION_PATH_2026-09-19.md`
5. `SUBMISSION_CHECKLIST.md`
6. the pre-existing dossier one directory up:
   - `../README.md`
   - `../EVIDENCE_CLAIMS_AND_SOURCES.md`
   - `../FORMALISM_AND_PROBES.md`
   - `../AUTHOR_INTENT_AND_HANDOFF.md`

Do not trust stale "still owed" notes in the older dossier without checking the current bytes; several earlier math repairs have already landed.
