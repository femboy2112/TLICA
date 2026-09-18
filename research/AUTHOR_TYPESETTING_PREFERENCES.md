# Author typesetting preferences — Leah

**Recorded:** 2026-09-16  
**Scope:** polished standalone academic/philosophical/mathematical/physics-style papers prepared for Leah.  
**Status:** author preference, not a TLICA theoretical claim and not a requirement for the repository's generic Markdown reading-copy build.

## Reference grammar

Default visual target: the author's *Who Shot First: Han or Greedo? And Insights on Spacetime from the Usage of Advanced Interrogation Techniques on Sherlock Holmes* (2 August 2026), together with the accepted *Moreish* checkpoint v0.2.8.

The desired register is a **physics/preprint paper that can carry philosophical prose**, not a designed essay, web document, or presentation deck.

## Default page and typography

Unless a venue specifies otherwise:

- `article`, **10 pt**, US Letter;
- approximately **1-inch margins**;
- **Latin Modern / conventional LaTeX serif** for body, mathematics, and callouts;
- do not introduce a second display font inside callout boxes;
- centered title / subtitle / author-date architecture, compact rather than a decorative title page;
- narrow centered abstract block (about `0.82\textwidth`), with conventionally justified text inside;
- principal body remains conventionally **fully justified** within a visually centered text measure;
- `\parindent = 0pt`, modest paragraph spacing (around `0.30em`), near-single line spacing (around `1.02`);
- plain page numbers; avoid decorative running headers unless a venue or long document genuinely benefits from them.

## Section and equation structure

- use ordinary numbered **serif** section headings for paper structure;
- avoid colored section rules, dashboard styling, or ornamental heading systems;
- display equations use ordinary centered academic LaTeX treatment;
- the page should feel closer to an arXiv/theoretical-physics manuscript than to magazine/editorial design.

## Callout / dialogue / thesis boxes

Boxes are allowed and often preferred for load-bearing propositions, character dialogue, and compact plain-language translations, but they must remain subordinate to the paper:

- **thin black rectangular rule**, white interior;
- centered on the page;
- **shrink-wrap to the text** rather than spanning the full column by default;
- cap width around `0.82–0.84\linewidth` so long content wraps naturally;
- text inside the centered box is **left-aligned**;
- use the **same Latin Modern serif family as the paper**;
- emphasis comes from **bolding and/or modest size change**, not a different font family, color palette, shaded UI-card treatment, or excessive ornament;
- ordinary dialogue/callouts may be slightly smaller than body text; major thesis statements may be normal-size bold;
- group a coherent multi-turn dialogue into one box when that improves reading flow rather than creating a stack of tiny boxes;
- do not box every memorable sentence. Boxes mark hierarchy, not decoration.

A useful baseline is approximately:

```tex
\setlength{\fboxrule}{0.45pt}
\setlength{\fboxsep}{5.5pt}
```

with `varwidth` inside a centered environment for intrinsic-width wrapping.

## Reading-flow rules

Formatting should serve fluent reading rather than visually fragment the prose:

- keep headings with enough following text (`needspace` or equivalent);
- avoid orphaned one-line paragraphs, headings, equations, or boxes at page bottoms;
- keep vertical whitespace compact and consistent around boxes and displays;
- preserve natural paragraph groups; do not turn every rhetorical beat into its own visual object;
- typesetting-only passes should **not rewrite prose** unless the author explicitly asks for editorial changes.

## Anti-patterns

Avoid by default:

- full-width UI-like cards;
- colored or shaded callouts as the dominant visual language;
- sans-serif text inside otherwise serif academic boxes;
- oversized title pages for ordinary papers;
- decorative headers, rules, and palettes that make the artifact look like a report template rather than a paper;
- centering the actual prose lines. The **block** is centered in the page architecture; prose inside remains left/right justified for readability.

## Boundary

This preference can be overridden by:

1. an explicit author instruction for a specific artifact;
2. a journal/conference/template requirement;
3. a materially different artifact type (slides, manifesto, handout, poster, web page, etc.).

When none applies, use this file as the default formatting contract for polished standalone paper PDFs and LaTeX sources.
