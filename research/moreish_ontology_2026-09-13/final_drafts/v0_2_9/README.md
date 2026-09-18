# *This Ontology Is Really Moreish* — synthesis draft v0.2.9

**Date preserved:** 2026-09-16
**Branch:** `moreish-final-draft-v0.2.8-2026-09-16`
**Base main commit:** `057422b0e39e510c522bd18fff1a2190b464e861`
**Parent draft:** [`../v0_2_8/`](../v0_2_8/README.md) (candidate-final v0.2.8)
**Status:** author-directed editorial + typesetting revision, originally on a non-main branch; **promoted to `main` on 2026-09-17** as the application paper `applications/moreish_ontology_v0_2_9.md` (superseding v0.1.0). Not a foundation change and not a new empirical-status claim.

This directory preserves the next revision after v0.2.8. It is a deliberate **synthesis**: v0.2.8 is the structural base (its cleaner section skeleton, plain-language "in plain terms" rungs, expanded theology, council-meeting set piece, quarantined TLICA bridge, and source/epistemic-status appendices are all kept), with the sharper voice and concrete receipts of the on-`main` application paper (`applications/moreish_ontology_v0_1_0.md`) restored where v0.2.8 had sanded them down.

The Markdown carries the prose; the LaTeX is the reproducible formatting authority for the polished paper.

## Files

- `moreish_final_draft_v0_2_9.md` — manuscript source.
- `moreish_final_draft_v0_2_9.tex` — polished standalone-paper typesetting source.

## What changed from v0.2.8

**Prose (restored bite / receipts; identical edits mirrored in `.md` and `.tex`):**

- §1 — restored the on-`main` opening premise (*"reality is not completely knowable from inside itself"* with the boxed `model ≠ world`), replacing v0.2.8's borrowed *"the map is not the territory"* framing; the plain inequality carries the point without an analogy.
- §1 — restored the "excellent philosophy for accidentally ruining your credit score" beat (with the "faintly ascetic" setup) feeding Underground Super Hans's entrance.
- §3.3 — folded the concrete autobiographical receipt back in ("Christian-coded rather than doctrinally raised: baptized, Sunday school early, grandparents"), grounding the *stronger* v0.2.8 theology ("I bet my money on atheism. I bet my soul on there being something.").
- §4 — restored the integral framing that earns the title: opens with the schematic `J = ∫₀ᵀ u(t) dt` and the "maximize the integrand at every instant" temptation, then hands off to v0.2.8's cleaner discrete dynamic-programming formalization.
- §6 — replaced the flat "Not necessarily. / Correct." beat with a single sharper line.

Net prose delta vs v0.2.8: +173 words (bite and receipts, not padding).

**Formatting / typesetting (LaTeX only, no prose change):**

- Removed the unused `helvet` (sans-serif) package — it was loaded but never invoked, and a second/sans display family is an explicit anti-pattern in the author typesetting contract.
- **Body set in a centered, justified column matching the abstract.** The `paperbody` environment now insets the body symmetrically (`adjustwidth`, ±0.08\textwidth) into one consistent centered measure, so prose, statement boxes, and displayed equations share a single column width. Previously the full-width prose fought the narrower centered boxes/equations and the text measure appeared to expand and contract down the page. Prose remains fully justified (the *block* is centered, not the individual lines), per the author typesetting contract.
- Stacked the two long §2 "pipeline" display equations (`encounter candidate insight → … → internalize`; `I repeatedly encounter this pattern ⇏ …`) as left-arrow-hanging `aligned` blocks so they fit the narrower measure and read as steps. Same stacking mirrored in the `.md` (it also reduces GitHub-mobile horizontal clipping of prose-in-display-math).

## Render check

Compiled with `pdflatex` (2 passes), exit 0: **15 pages, US Letter (612 × 792 pt)**, title `This Ontology Is Really Moreish`, author `Leah`. No `!` errors; the largest remaining overfull `\hbox` is **1.74 pt** (below the visible threshold — no clipping, no content past the margin). Pages inspected visually across the box-dense and equation-bearing sections; the body renders as one consistent centered column. The binary is not tracked (the exact `.tex` source is the reproducible authority; see the repository PDF convention).

## Integrity

SHA-256 of the preserved sources and the reviewed PDF:

- Markdown: `976cd0644ad2d10876ea1d05c2b1a59f42e2d9f4a46ba4e76807965952ae1661`
- LaTeX: `36a580782a32149f54e683de7954ad9a0ce756f2fe45667a9e4c02fa5e700975`
- reviewed PDF: `887abf45be2ca72b90ea4326c8079b592b388e0a7112a00a688ce9628a87653d`

## Status boundary

> **Update 2026-09-17 — PROMOTED.** On author direction, v0.2.9 was promoted to `main` as the
> application paper `applications/moreish_ontology_v0_2_9.md`, superseding the earlier v0.1.0 draft.
> The promotion re-attached the application-paper front-matter block (status / foundation-impact /
> epistemic-status / authorship) and updated the registration surfaces (README, `docs/applications.md`,
> `docs/README.md`, and the wiki page), while keeping the body — the TLICA bridge quarantined to §11 —
> as authored here. The paragraph below is the original draft-time boundary, retained as history.

This is a preserved draft revision, not a promotion. v0.2.9 remains a **standalone** paper draft: v0.2.8 severed the on-`main` application-paper framing (moving TLICA to a quarantined §11), so this draft carries no application-paper front-matter block and touches no registration surface. Promoting it to replace `applications/moreish_ontology_v0_1_0.md` on `main` is a separate, author-gated decision that would require re-attaching the application-paper labels (status / foundation-impact / epistemic-status / authorship) and the registration surfaces. The frozen foundation (v5.5.0) is untouched. No version number here canonizes conduct or supersedes v0.1.0 on `main`.
