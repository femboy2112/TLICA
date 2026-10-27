# Claude handoff — TLICA's missing first lesson
**Date:** 2026-10-27  
**Status:** Editorial/mission proposal; AUTHOR REVIEW PENDING; NOT MERGED  
**Base at authoring:** `3cdd8a16132efb3eca8d42c0f8716308b890fb42` on `main`  
**Working branch:** `docs/missing-first-lesson-human-operating-manual-2026-10-27`  

## Intent

Front-load the public purpose of TLICA with the shortest defensible description:

> TLICA is an operating manual for being human, starting with how to question the manual.

An immediate and important distinction: the project already has *The Anarchist's Cookbook for Operating a Mind*, an operational field manual. This change **does not replace it**. It supplies the short `why` and points readers to the existing `how`, formal foundation, and methodological limits. The motivating examples come from author discussion in October 2026; do not present them as independent observations of other people's psychology.

## This branch changes only

1. `README.md` — a prominent mission lead and readable navigation.
2. `docs/README.md` — a single new entry at the beginning of the wiki reading path.
3. `docs/the-missing-first-lesson.md` — the standalone plain-language mission and its disciplined boundaries.
4. This integration handoff.

No foundation, existing application manuscripts, archived research, or versions were rewritten. This is editorial positioning plus a **proposed** educational application, not a core-theory amendment.

## Integration instructions

- Reinspect the **current** `main` and all active consolidation PRs, especially [plan PR #14](https://github.com/femboy2112/TLICA/pull/14). That PR is planning-only; don't treat it as merged implementation.
- Rebase or cherry-pick this *small* editorial change onto the eventual consolidated front door instead of overwriting the rest of the README. If another editorial pass has already reorganized the landing page, preserve the mission in the first screen, then reconcile links and duplication deliberately.
- Keep the current foundation and its claim/status ledger unchanged; do not turn TLICA's κ/φ/ρ profile plus σ/μ diagnostics into a five-dimensional primitive. Undefined φ means no constructible verification path, **not** false.
- Do not rebrand TLICA as a validated theory of consciousness, clinical intervention, or established educational curriculum. It's an identity architecture plus an explicitly provisional practical/ethical mission. Historical-frame-lock remains a candidate interpretation, not a diagnosis or established law.
- Honor the author's philosophical priority: **prevent rigid frame-lock first; recognize and repair inevitable failures second**. The need for material and emotional slack is not a demand to override legitimate boundaries.
- Preserve the [Cookbook](../applications/anarchists_cookbook_operating_a_mind_v1_0.md) as the comprehensive hands-on manual, and [This Is Water](../applications/this_is_water_truth_respecting_choice_v0_1_0.md) as the transport/agency paper.
- Check `docs/` page navigation for the generated wiki. The wiki is a **separate** generated mirror; don't publish or claim to have edited it until its own generation/review process runs.
- On a clean checkout run `make validate`, relevant docs/math unit checks, `git diff --check`, a Markdown link/anchor sweep, and a GitHub-rendered spot check of the new front matter. Record exact commands and outcomes. These checks are **not claimed as executed by this branch's GitHub-only authoring**.
- Let the author review normative/educational wording. Merge to `main` only after coherently reconciling ongoing editorial work, not automatically as a side effect of creating this draft PR.

## Claim ledger

- **Observed:** The author states a lifelong aim of avoiding sealed-off beliefs while preserving revisability, and an interest in real-time semantic translation under disagreement (author report).
- **Proposed normative goal:** Dignity, agency, model literacy, and room for inquiry should be built into an operating manual.
- **Conjectured / UNVERIFIED:** Historical-frame-lock as a general psychological mechanism; the proposed educational progression; the prevalence and causal impact of institutional pressure on frame rigidity.
- **Not claimed:** empirical validation, a new theorem, five new core coordinates, diagnoses, or a verified curriculum.

## Merge gate

The mission should appear **above** the historical theory inventory, remain readable in a few seconds, preserve all established source documents, and introduce no falsely promoted claim. If an editor cannot reconcile those criteria with an incoming README overhaul, pause this PR's merge, not the rest of the repository's work.
