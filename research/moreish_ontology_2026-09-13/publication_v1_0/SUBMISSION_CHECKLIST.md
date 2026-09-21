# Moreish v1.0 submission checklist

**Branch:** `moreish-publication-v1.0-2026-09` (merged to `main`)  
**Target:** public preprint first; then double-blind submission to *Phenomenology and the Cognitive Sciences* unless venue fit changes after literature audit.  
**Status:** **v1.0.1 frozen** as the public preprint (2026-09-20) — v1.0 hedged and the two closest novelty flanks closed with Crossref-verified citations (Alchourrón, Gärdenfors, & Makinson 1985; Taber & Lodge 2006). Tag `moreish-v1.0.1`.

## A. Intellectual hardening

- [x] Preserve correct mathematical claim: greedy **need not** optimize total return under state coupling.
- [x] Add explicit first-person method / scope boundary.
- [x] Add nearest-neighbor literature section.
- [x] Add intent/outcome firewall to the Jesus/WWJD moral-controller section.
- [x] Explicitly state invented character dialogue is author-composed unless sourced.
- [x] Hostile novelty search across hierarchical control, cognitive control, model-based/habitual RL, active inference, self-regulation, commitment devices, and self-sealing belief literature. (2026-09-19; 5 named flanks remain — see SOURCE_AND_NOVELTY_AUDIT.md)
- [x] Narrow novelty claim wherever prior art reaches the proposed bundle. (manuscript adjacent-literature section rewritten to concede E3/E4/E5, narrow E2)
- [x] Decide whether the current related-literature section belongs before §4 or later in a conventional discussion section. (2026-09-19: moved to the back — after provenance, before References — for narrative flow, per author.)
- [x] Decide whether to include any autobiographical "receipts" inline; do not add them merely to make the paper look empirical. (2026-09-20: author decision — no inline receipts.)
- [x] Final author pass on whether "long arc morally better" wording says exactly what Leah intends without functioning as self-certification. (2026-09-20: author approved wording as-is.)

## B. Source integrity

- [x] Verify Laibson 1997 bibliographic data/DOI.
- [x] Verify O'Donoghue & Rabin 1999 bibliographic data/DOI.
- [x] Verify Frederick, Loewenstein & O'Donoghue 2002 bibliographic data/DOI.
- [x] Verify Aubin 1991 book identity.
- [x] Verify Prentner 2025 Springer article/DOI.
- [x] Corroborate Varela/Shear 1999 bibliographic record.
- [ ] Obtain/inspect a primary or authoritative copy of Varela/Shear before depending on a specific methodological claim. (2026-09-20: bibliographic record independently corroborated across ≥4 secondary sources; the primary JCS PDF is paywalled and was not inspected. The manuscript's method sentence was tightened so its reliance is limited to the essay's general methodological thrust — no longer load-bearing on a specific claim.)
- [x] Verify Bellman edition metadata. (1957 Princeton University Press first edition is the canonical citation; the original carries no registered DOI — confirmed 2026-09-19.)
- [x] Convert Sutton & Barto and any retained learning-theory references to complete entries. (Sutton & Barto 2018, 2nd ed., MIT Press — complete entry present in References; no other learning-theory works cited formally.)
- [x] Verify Dostoevsky attribution at the level actually used. (2026-09-20: work-level thematic use; Part-level locus added — *Notes from Underground*, Part I — no specific passage quoted; dialogue is author-composed per the manuscript's dialogue note.)
- [ ] If Wallace/Hitchens/Buddhist claims become more specific than provenance statements, add exact source loci.
- [x] Verify scriptural quotations/attributions in the final text. (Matthew 7:12, Luke 6:31, Galatians 6:2 confirmed; added the missing locus for “love your neighbor as yourself” → Matthew 22:39, cf. Leviticus 19:18; 2026-09-19.)
- [x] Run a complete reference-to-in-text-citation consistency check. (2026-09-19: no orphan references — the previously-uncited Lakatos 1970 attached to its falsification-risk content home; every in-text citation resolves to a reference entry.)
- [ ] Ensure every DOI is a full DOI link where available. (2026-09-19: the three held-back APA journal DOIs — Carver & Scheier 1982, Kunda 1990, Lord/Ross/Lepper 1979 — added as full links and Crossref-verified; book/chapter/pre-DOI-proceedings entries not yet exhaustively rechecked. 2026-09-20: the two flank DOIs — Alchourrón–Gärdenfors–Makinson 1985 = `10.2307/2274239`; Taber & Lodge 2006 = `10.1111/j.1540-5907.2006.00214.x` — added as full links and Crossref-verified field-by-field.)

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
- [x] Freeze final disclosure after text stabilizes. (2026-09-20: text FROZEN at v1.0; AI disclosure names OpenAI ChatGPT — GPT-5.6 Sol / ChatGPT 6 — and Anthropic Claude Code, Opus 4.8.)
- [ ] Re-check live journal/publisher AI policy on submission day.

## E. Journal-format gates

- [x] Abstract currently within 150-250 words.
- [x] Six keywords supplied.
- [x] Count final manuscript including references; stay below 10,000 words unless strongly justified. (2026-09-20: 8,538 words incl. references + declarations — under 10,000; journal average ~9,000.)
- [x] Convert citations/references to final Springer/APA-compatible author-year form. (Already APA author-year throughout; Springer-compatible. Final template pass belongs to the blind journal build.)
- [x] No more than three displayed heading levels. (2026-09-20: 2 displayed levels — # and ##; zero level-3+.)
- [ ] Produce editable LaTeX source using a Springer-compatible template or confirm current accepted template. (Journal-build artifact; still owed.)
- [x] Produce separate title page. (`TITLE_PAGE.md` filled 2026-09-20; city-vs-state is the one open venue-format item.)
- [x] Produce anonymous manuscript with identifying text/metadata removed. (`MANUSCRIPT_v1_0_BLIND.md`, with a neutralized working title.)
- [x] Strip author from PDF metadata in blind build. (Blind PDF built with empty Author/Title metadata.)
- [x] Check self-citation/TLICA language for identity leakage. (2026-09-20: TLICA name AND branded vocabulary — Mode-B / slack / imprinting / identity-correlation — neutralized in the blind cut; the blind build's identity guard now fails loudly on any regression.)
- [x] Add Statements and Declarations. (2026-09-20: added before References — Funding, Competing interests, Ethics, Data/code, Author contributions, Acknowledgments, License.)
- [x] Add competing-interests statement. (2026-09-20: none declared.)
- [x] Add funding statement. (2026-09-20: no external funding; independent researcher.)
- [x] Resolve author city/country and active email for title page. (2026-09-20: Independent researcher, NY, USA — state not city, per author; l.vandetta.research@gmail.com.)
- [x] Resolve ORCID choice. (2026-09-20: ORCID 0009-0000-0531-6766, public, registered to Leah VanDetta.)
- [x] Decide acknowledgment text. (2026-09-20: author-supplied — the "sincere apology / path to hell paved in good intentions" statement, verbatim wording.)

## F. Preprint package

- [x] Freeze public preprint master. (2026-09-20: v1.0 FROZEN, tagged `moreish-v1.0`, brought to `main`.)
- [x] Compile publication-quality PDF. (2026-09-20: v1.0.1 preprint PDF built via `scripts/build_pdf.sh` — 22 pages, 0 dropped glyphs.)
- [ ] Visual page-by-page inspection.
- [ ] Reserve Zenodo DOI before final PDF if DOI should appear inside artifact.
- [ ] Add DOI to source/PDF metadata.
- [x] Record exact Git commit SHA. (2026-09-20: frozen commit recorded by the annotated tag `moreish-v1.0`.)
- [x] Choose license intentionally. (2026-09-20: CC BY 4.0 for the preprint; journal license follows the eventual publishing agreement.)
- [ ] Upload preprint/source/supplement as desired.
- [ ] Publish Zenodo record.
- [ ] Record version DOI + concept DOI as appropriate.
- [ ] Create/update PhilArchive entry pointing to canonical DOI.
- [ ] Supply abstract, keywords, and categories in PhilArchive.

## G. Repository integration

- [x] Publication work isolated on non-main branch.
- [x] Canonical `applications/moreish_ontology_v0_2_9.md` left untouched.
- [x] Foundation untouched.
- [x] Run `make validate` locally after final repository edits. (2026-09-20: PASS — links + self-containment + term pins.)
- [x] Review `git diff main...moreish-publication-v1.0-2026-09`. (Reviewed before the v1.0 merge; zero conflicts, foundation untouched.)
- [x] Do not merge or open a PR until Leah explicitly authorizes it. (Author authorized 2026-09-20; merged `--no-ff` to `main`.)
- [x] Before eventual merge, decide what belongs on `main` versus what remains publication-branch provenance. (v1.0/v1.0.1 master, blind cut, apparatus, and demo landed on `main`; canonical promoted to `applications/`.)

## Register / explicit-language policy verify

- [x] Confirm no target venue prohibits the paper's comic / mild-profane register (2026-09-20, author-requested pre-check). **Zenodo:** bans only illegal/malicious/military content — no language clause. **PhilArchive/PhilPapers:** no manuscript-language rule; "professional quality" plus a platform code of conduct governing user conduct, not manuscript diction. **P&CS / Springer Nature:** no profanity or tone rule in the submission guidelines or the COPE-based ethics policy; the offensive-content policy targets discrimination, hate speech, and harassment, which the paper's mild comic profanity does not engage. Residual risk is individual editor/reviewer taste at the journal — at worst a revise-and-resubmit. Re-verify live on submission day.

## Submission-day policy recheck

Re-open, do not trust cached notes:

- journal submission guidelines;
- Springer Nature AI manuscript policy;
- Springer Nature preprint policy;
- APC/subscription route;
- Zenodo deposit/licensing terms;
- PhilArchive submission/self-archiving rules.

Record the date of that final recheck.
