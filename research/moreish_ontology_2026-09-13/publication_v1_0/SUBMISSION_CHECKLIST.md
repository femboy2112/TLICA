# Moreish v1.0 submission checklist

**Branch:** `moreish-publication-v1.0-2026-09`  
**Target:** public preprint first; then double-blind submission to *Phenomenology and the Cognitive Sciences* unless venue fit changes after literature audit.

## A. Intellectual hardening

- [x] Preserve correct mathematical claim: greedy **need not** optimize total return under state coupling.
- [x] Add explicit first-person method / scope boundary.
- [x] Add nearest-neighbor literature section.
- [x] Add intent/outcome firewall to the Jesus/WWJD moral-controller section.
- [x] Explicitly state invented character dialogue is author-composed unless sourced.
- [x] Hostile novelty search across hierarchical control, cognitive control, model-based/habitual RL, active inference, self-regulation, commitment devices, and self-sealing belief literature. (2026-09-19; 5 named flanks remain — see SOURCE_AND_NOVELTY_AUDIT.md)
- [x] Narrow novelty claim wherever prior art reaches the proposed bundle. (manuscript adjacent-literature section rewritten to concede E3/E4/E5, narrow E2)
- [ ] Decide whether the current related-literature section belongs before §4 or later in a conventional discussion section.
- [ ] Decide whether to include any autobiographical "receipts" inline; do not add them merely to make the paper look empirical.
- [ ] Final author pass on whether "long arc morally better" wording says exactly what Leah intends without functioning as self-certification.

## B. Source integrity

- [x] Verify Laibson 1997 bibliographic data/DOI.
- [x] Verify O'Donoghue & Rabin 1999 bibliographic data/DOI.
- [x] Verify Frederick, Loewenstein & O'Donoghue 2002 bibliographic data/DOI.
- [x] Verify Aubin 1991 book identity.
- [x] Verify Prentner 2025 Springer article/DOI.
- [x] Corroborate Varela/Shear 1999 bibliographic record.
- [ ] Obtain/inspect a primary or authoritative copy of Varela/Shear before depending on a specific methodological claim.
- [ ] Verify Bellman edition metadata.
- [ ] Convert Sutton & Barto and any retained learning-theory references to complete entries.
- [ ] Verify Dostoevsky attribution at the level actually used.
- [ ] If Wallace/Hitchens/Buddhist claims become more specific than provenance statements, add exact source loci.
- [ ] Verify scriptural quotations/attributions in the final text.
- [ ] Run a complete reference-to-in-text-citation consistency check.
- [ ] Ensure every DOI is a full DOI link where available.

## C. Formalism / supplement

- [x] Re-run `greedy_vs_option_demo.py` in a clean environment. (CPython 3.12.3, 6/6)
- [x] Preserve raw output and Python/environment version. (raw in `_tests.txt`/`_results.json`; CPython 3.12.3, standard library only)
- [x] Re-check DP and brute-force agreement. (coupled DP=V_root=brute=30)
- [x] Re-check decoupled calibration. (decoupled greedy=DP=brute=32)
- [x] Correct stale language that equates demo variable `d` with literal legal-action cardinality `|A(x)|`.
- [x] State clearly that both toy policies are feedback/state-responsive; tested axis is myopic vs full-horizon.
- [ ] Decide whether toy code/results ship as journal Supplementary Information or only as public repository/Zenodo material.
- [ ] If viability theory becomes more than an analogy, build a declared formal mapping and try to break it.

## D. AI provenance

- [x] State substantive AI assistance rather than laundering it as copyediting.
- [x] Record current hardening model: OpenAI ChatGPT / GPT-5.6 Sol.
- [x] Preserve human accountability and author/assistant distinction.
- [ ] Recover exact historical model/provider identities where the record genuinely contains them.
- [x] Determine whether any local Claude/Codex session materially edited this specific Moreish text. (yes — recorded in `AI_PROVENANCE_AND_DISCLOSURE.md` §3, the 2026-09-19 Claude continuation pass)
- [ ] Freeze final disclosure after text stabilizes.
- [ ] Re-check live journal/publisher AI policy on submission day.

## E. Journal-format gates

- [x] Abstract currently within 150-250 words.
- [x] Six keywords supplied.
- [ ] Count final manuscript including references; stay below 10,000 words unless strongly justified.
- [ ] Convert citations/references to final Springer/APA-compatible author-year form.
- [ ] No more than three displayed heading levels.
- [ ] Produce editable LaTeX source using a Springer-compatible template or confirm current accepted template.
- [ ] Produce separate title page.
- [ ] Produce anonymous manuscript with identifying text/metadata removed.
- [ ] Strip author from PDF metadata in blind build.
- [ ] Check self-citation/TLICA language for identity leakage.
- [ ] Add Statements and Declarations.
- [ ] Add competing-interests statement.
- [ ] Add funding statement.
- [ ] Resolve author city/country and active email for title page.
- [ ] Resolve ORCID choice.
- [ ] Decide acknowledgment text.

## F. Preprint package

- [ ] Freeze public preprint master.
- [ ] Compile publication-quality PDF.
- [ ] Visual page-by-page inspection.
- [ ] Reserve Zenodo DOI before final PDF if DOI should appear inside artifact.
- [ ] Add DOI to source/PDF metadata.
- [ ] Record exact Git commit SHA.
- [ ] Choose license intentionally.
- [ ] Upload preprint/source/supplement as desired.
- [ ] Publish Zenodo record.
- [ ] Record version DOI + concept DOI as appropriate.
- [ ] Create/update PhilArchive entry pointing to canonical DOI.
- [ ] Supply abstract, keywords, and categories in PhilArchive.

## G. Repository integration

- [x] Publication work isolated on non-main branch.
- [x] Canonical `applications/moreish_ontology_v0_2_9.md` left untouched.
- [x] Foundation untouched.
- [ ] Run `make validate` locally after final repository edits.
- [ ] Review `git diff main...moreish-publication-v1.0-2026-09`.
- [ ] Do not merge or open a PR until Leah explicitly authorizes it.
- [ ] Before eventual merge, decide what belongs on `main` versus what remains publication-branch provenance.

## Submission-day policy recheck

Re-open, do not trust cached notes:

- journal submission guidelines;
- Springer Nature AI manuscript policy;
- Springer Nature preprint policy;
- APC/subscription route;
- Zenodo deposit/licensing terms;
- PhilArchive submission/self-archiving rules.

Record the date of that final recheck.
