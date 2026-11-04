# TLICA — Consolidation, Editorial Repair, and Research Navigation Plan
**Date:** 2026-10-23
**Status:** EXECUTION PLAN / NOT AN IMPLEMENTED MERGE
**Repository:** https://github.com/femboy2112/TLICA
**Initial inspected main:** 4dbd0e56cea552733d11a4fb1124be5ef2301331
**Planning branch:** plan/tlica-consolidation-math-rendering-2026-10-23
**Companion specifications:** [GitHub math rendering contract](GITHUB_MATH_RENDERING_CONTRACT_2026-10-23.md) and [Claude execution instructions](CLAUDE_TLICA_MEGA_ROUND_2026-10-23.md).

> This file records an inspected baseline, not a substitute for fresh inspection. On execution, obtain a new main HEAD, branch inventory, PR statuses, actual commit ancestry, and local validation result. Never treat a historical audit as authority over current Git state.

## Mission and acceptance criteria

Consolidate genuinely unmerged TLICA research, professionally edit the human-facing archive, update its reader-facing GitHub Wiki source, provide accessible research-front snapshots, and ensure mathematical Markdown actually renders in GitHub. Preserve the source/claim/provenance system and the distinct research, application, and foundation tiers.

**Successful outcome:** coherent main; no duplicate or destructive merges; all branch dispositions recorded; accurate current foundation-version metadata; concise newcomer and researcher routes; human-readable active fronts with statuses and next probes; passing relevant tests and rendering checks; Wiki published only through the source-mirror workflow and after reviewed source is merged. Keep archived research and authorial voice intact.

**Boundaries:** no substantive frozen-foundation change, no silent claim promotions, no invented independent audits, no unreviewed sensitive transcript publication, no journal submission, no live intervention with people, no force-pushing main.

## Inspected baseline (snapshot only)

- 27 branches including main; four open draft PRs #10–#13; 571 tracked files at main, including 50 docs/ pages and 433 research/ files (counts include history and assets).
- Main foundation Files 0–5 explicitly identify **v5.5.2**. Root README, CITATION.md, and Makefile still identify the current foundation as v5.5.1. Fix references to the current line; preserve genuinely historical citations and validate actual Git tags before claiming a tag exists.
- The root README is roughly 582 lines; research/README.md is roughly 668 lines. Both are usable but overburdened as introductions and inventories.
- docs/ is authoritative for the public wiki, generated through scripts/build_wiki.py and scripts/publish_wiki.sh; the Wiki itself is a separate Git repository.
- PR #10 TLICA-EPIC: research files already exist on main; 17/18 branch research files had identical blobs; the remaining difference is in DUAL_PASS_STRUCTURED_POINTS.md (main intake-format correction). PR #11 Vernacular: all 10 research files byte-identical on main. PR #12 Salience/Frame/Provenance: all seven research files byte-identical on main. Their PR metadata still reads open/draft. Reinspect and reconcile; DO NOT casually merge old divergent heads or overwrite intake fixes.
- PR #13 KIN-1-11: 10 commits ahead / 0 behind at inspection, with three new application docs, a wiki intro, and two navigation changes; pending author review of its normative doctrine.
- Branch research/one-ring-thousand-dominoes-session-2026-10-21: 37 commits ahead / 0 behind at inspection, adding 24 research files in two dossiers: One Ring/Thousand Dominoes and TLICA-HIGGS, plus research index changes. This is the highest priority new research integration.
- Other potentially unique historical branches: paper/facts-feelings-dissonance-filter (3 new files), research/moreish-controller-mindfulness-bridge-2026-09-29 (one new research note plus changes to a working manuscript), research/differential-field-model-2026-09-12 (one new model), research/drosophila-tlica-bootstrap-2026-09-13 (10 new files), research/phenomenological-integration-2026-09-12 (contains sensitive first-person dialogue; do not auto-publish or amplify), and moreish-wwjd-moral-actuator-2026-09-14 (historical, needs provenance and priority adjudication).
- Main wiki has recently gained 15 explanatory pages; preserve and improve those assets rather than regenerating them wholesale.
- Technical mismatch to resolve: foundation/3_formal_apparatus.md explicitly calls max-flow one selected aggregation over directed historical integration, while some docs imply it is the necessary/only possible integration model. Also docs/glossary.md paraphrases φ as how "undeniable" a belief feels while docs/three-coordinates.md correctly distinguishes φ from subjective confidence.
- Makefile's curated PDF list refers to older Moreish v0.2.9 even while README calls v1.0 the current successor; inspect other curation and version/summary drift. GitHub math rendering breakage is recurring, especially observed `\operatorname` usage; see companion contract.

## Work packages, in dependency order

### Wave 0 — Frozen baseline, inventory, and reproducibility

1. Inspect AGENTS.md / CLAUDE.md / repository-local instructions, actual worktree, origin, current branch, main SHA, active/untracked modifications, branch heads, PR review state, tag/release state, and existing validation scripts. Do not trash or reset another session's worktree.
2. Run baseline `make validate` and targeted unit tests in a clean local checkout/worktree. Record commands and exact outcomes; no fabricated green checkmarks. If a dependency is missing, name it and provide an alternative or explicit UNVERIFIED status.
3. Create an exhaustive branch disposition ledger, with branch, SHA, merge base, ahead/behind, changed paths, byte-equivalent paths already on main, unique value, sensitivity, risk, suggested action, author gate, and final disposition. Distinguish commit ancestry from effective content integration.
4. Record current claim/status and source-map invariants; prevent accidental changes to foundation/*.md and retained prior-version snapshots.

### Wave 1 — New intellectual material, integrated without damaging main

**Research integration first:** take One Ring and TLICA-HIGGS onto fresh current main. Preserve their author seeds, corrections, formal propositions, caveats, witness scripts, SVGs, and provenance. Ensure all indexed links point to the final location. Re-run the new scripts in a clean checkout, including controls, not just published result files.

**Application integration second:** prepare KIN-1-11 as a separate reviewable change. Preserve v0.1 and v0.2 independently and the author's distinctive prose. Clearly label draft / normative / nonviolent / voluntary and author review pending. Do not silently convert doctrine into a mathematical foundation claim or interpret draft prose as author-adopted.

**Historical research, selective third:** triage Facts/Feelings, Mindfulness Controller, Drosophila, Differential Field, Moreish WWJD, and other live unique branches. Reconcile revised understanding and old superseded claims. Integrate useful non-sensitive research notes selectively, behind clear status labels; do not import every historical README/version from an outdated branch. Keep sensitive source dialogues off main pending explicit scope review.

**Old PR cleanup:** after blob/content equivalence and editorial corrections are confirmed, record why PR #10/#11/#12 were superseded by main integration and close them administratively if correct. Leave no ambiguous "not merged" language on docs now on main.

### Wave 2 — Canonical status and editing pass

1. Create one authoritative current-state/status registry (e.g. docs/PROJECT_STATUS.md or a small machine-readable source with generated views). Keep version, current applications, active research fronts, draft and superseded states distinct. Never change historical notes by automated search-and-replace.
2. Repair root README.md, CITATION.md, Makefile, docs/README.md, research/README.md for honest current versions, current files, and working reader paths. Verify actual Git tags before referencing them as existing tags.
3. Refactor root README toward: one-paragraph orientation, the three-coordinate distinction, assumptions and limits, quick reader map, current status, links. Move exhaustive version inventories to dedicated indices rather than deleting useful context.
4. Professionally edit *current* material for paragraph flow, heading hierarchy, argument ordering, consistent notation, citations, equation presentation, grammatical quality, and skimmable summaries. Preserve original archived manuscripts, voice, citations, and precise qualifiers; distinguish pure copyedits from semantic amendments with labeled diffs.
5. Formal glossary pins must prevent confusion between κ/contact; φ/toolkit-relative truth-indistinguishability; σ/source-map adequacy; μ/probe availability; ρ/identity-correlation; Cl(Tools); coherence; independence; discrimination; phenomenal availability A; preservation ranking Π; modeled world versus internal representation.
6. Explain max-flow as the currently implemented integration functional, not automatically a universally forced primitive. If an alternative integration law changes mathematics, draft a separate foundation-extension proposal; do not silently redefine ρ on main.
7. Preserve the explicit difference between conditional derivation, finite model success, empirical validation, proposed mechanism, normative recommendation, and subjective example.

### Wave 3 — Human-readable wiki and research-front dashboard

Retain docs/ as the source of truth. Introduce beginner, intermediate/formal, and research reading paths. Use progressive disclosure on each major page: **in one sentence → plain explanation → carefully typed formulation → what does not follow → evidence/status → related concepts → exact source/probes**. Ensure examples remain examples, not measurements. Do not turn all 50 wiki pages into duplicates of full manuscripts; link to primary artifacts.

Provide accessible introductions for the newly merged research and KIN, while preserving direct links to derivations and primary source documents. Improve the concept→application→research cross-link graph, anchors, sidebar groupings, glossary, and "where next" recommendations.

Create research/FRONTIER_STATUS.md (and optional focused front summaries) with date and link for each active front: question, strongest verified result, biggest obstruction, nearest live rivals, best discriminator, next concrete action, source/implementation link, last reproducible check. Group by conceptual program rather than only chronological filename. Make historical/dormant states explicit. Reserve machine-readable ledgers and exhaustive session handoffs as lower-level sources.

### Wave 4 — GitHub math compatibility and regression

Read companion contract. Read the [GitHub official math documentation](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions). Treat GitHub Markdown as the target, not a LaTeX PDF compiler. Calibrate good/bad controls, build a context-aware detector, correct current-facing broken expressions without altering mathematical meaning or indiscriminately rewriting history, then verify representative pages **on rendered GitHub**, including the generated Wiki. Pay special attention to `\operatorname`, `\operatorname*`, `\( ... \)` / `\[ ... \]`, dollar parsing, inline-code collisions, tables, and multiline math. Rerun after any global editorial formatting.

Make a stable low-cost `make check-github-math` target (or comparable) that supports a strict current-facing mode and advisory archive mode. A passing static parser check alone is not proof of rendered success. Preserve exact observed screenshots/HTML/links or explicit "render visually UNVERIFIED" when inspection is unavailable.

### Wave 5 — Test, release, and mirror

Minimum evidence: `make validate`; relevant deterministic Python unit tests; explicit Markdown link/heading-anchor audit; math fixture tests and GitHub-rendered spot checks; wiki build-to-temp and navigation/relative-to-absolute URL verification; representative PDF smoke renders if pandoc/LaTeX is available (these do not replace GitHub checks); `git diff --check`, current-vs-archival semantics diff, privacy review, no contradictory statuses, and current versions verified.

Merge **small, independently validated** work packages into main via PRs if safe and authorized by this request (routine research-tier + editorial docs); do not batch all changes in one risky PR. Major foundation rewrites, authorial normative approvals, any external submission, and sensitive content exposure remain separately gated for Leah. Recheck main and PR heads immediately before any merge. Publish GitHub Wiki only after the authoritative docs PRs are merged, with an explicit source-SHA and generated diff review; no blind wiki push.

## Execution governance and compute discipline

- One orchestrator coordinates parallel read-only audits/experiments; partition writers by non-overlapping paths. Never let multiple child sessions edit README, docs/README, research/README, Makefile, or math-policy infrastructure concurrently.
- Worktrees per child or explicit no-write research children; commits on dedicated branches, clean fast-forward/cherry-pick handoffs. Do not use destructive resets, global search/replace, force-push, or unexamined broad merges.
- Prefer 3–5 bounded concurrent specialists per wave, with concise results, exact files, checks, SHA, risks, and handoff to the sole integrator. Fan out independent probes, not overlapping edits.
- Run local incremental tests during work; run full validation at meaningful integration gates. Minimize CI-triggering pushes; batch validated commits before pushing; do not repeatedly push formatting tweaks merely to trigger CI. Re-run only failed jobs when appropriate.
- Commit and push coherent work, use informative PR titles and checklists, and keep an auditable release/merge ledger. No fictitious runs, reviewers, or independent witnesses.
- Complete as much work as fits the current session; preserve uncompleted tasks and exact resume state instead of implying that future work has already happened.

## Completion report required from Claude

Report: main and branch SHAs before/after; inventory of branch dispositions and PR outcomes; integration commits/PR URLs; version drift resolved; edited files and plain-language improvements; newly accessible front-page links; math warnings before/after and actual GitHub render evidence; tests and exact commands; privacy/author-approval holds; unresolved mathematical or conceptual conflicts; final recommended next probe/work item.

**Priority:** truth and reversibility > formal and provenance invariants > content preservation > navigability > polished prose > cosmetics.
