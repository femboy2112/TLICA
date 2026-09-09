# Integration and local research handoff

**Date:** 2026-09-09. **Branch:** `agent/idubbbz-hyde-paper-2026-09-09`.

## Established state

Repository: `femboy2112/TLICA`, private at inspection. Parent branch: `agent/geometry-of-actualization-2026-09-07`. Parent commit: `e6b1b33611489af4c1598f6140548e7a2700de7b`. Parent tree: `f1a58d6765a37acca329a8d257a0ad5db93c0ff1`. Main was separately observed at `0eb46646a1c18850ab5204921cb2edc76bb1e64b`; it is not this branch's assumed immediate parent.

The connector supplied repository read/write access. The container contained the user's transcript but no Git checkout. Its read-only network probe failed DNS resolution, so no authenticated complete checkout or full `make validate` was possible. The repository's root/research structure and Makefile were inspected. No AGENTS.md appeared at those ancestor directories. All additions are new files confined to this package; no foundation or application registration was changed.

The companion branch is `agent/actualization-recognition-2026-09-09`, documentation commit `997a927434c0889751e1e1ed53f876225c70369e`. It contains the broad discussion and author-correction ledger. This paper stands alone and does not require importing that branch first.

## Validation actually performed

The exact shared Python script was run locally under Python 3.13.5. Sixteen tests passed; zero failures and errors. The uploaded script blob matched the locally computed Git blob SHA `60cb92d1606bbe452074300cbe9ea22cf18fb161`. JSON output is preserved with normalized whitespace, and the text test log preserves the captured run output. No human subjects, creator-scene labels, inter-rater scores, or comparative findings were generated.

Remote commit, path inventory, parent relation, and unchanged-main checks should be read from the final session receipt rather than inferred from this prospective instruction. Full `make validate` remains a required local gate before promotion.

## Safe local workflow

```bash
git remote get-url origin
git status --short
git branch --show-current
git fetch origin agent/idubbbz-hyde-paper-2026-09-09
git worktree add ../TLICA-idubbbz-hyde-review \
  -b local/idubbbz-hyde-review \
  origin/agent/idubbbz-hyde-paper-2026-09-09
cd ../TLICA-idubbbz-hyde-review
git log -1 --oneline
git diff --stat e6b1b33611489af4c1598f6140548e7a2700de7b...HEAD
python3 research/idubbbz_hyde_paper_2026-09-09/structural_checks.py
make validate
```

If the local branch or worktree path already exists, inspect it rather than deleting or resetting it. Do not force-push. To integrate with a newer main, create a separate integration branch and cherry-pick only the new documentation commit after inspecting the range. Resolve any newer instructions and source definitions before editing.

## Research priorities

Acquire and inspect both original 2022 documentary editions before claiming a close reading. Preserve lawful source copies or fingerprints, align shared intervals, and distinguish event, camera, edit, voiceover, and audience commentary. Treat the allegation that Ian intended a takedown as an attribution requiring evidence. Search for episodes that reverse the proposed roles; do not merely accumulate confirming clips.

Keep the paper's mode distinction separate from the author-level distribution hypothesis. The former can be conceptually useful even if the latter fails. A returning title does not prove an unchanged apparatus. A public apology does not give privileged access to motives. Satire can have norms and harm; an audit can be an intervention.

Do not add a quantitative truth score, clinical labels, literal person-minus-model residual, or mathematical reflection without a declared typed construction. Preserve canonical T-modeling/R-affective uptake separately from evidence attribution. Improve the draft in Leah's voice without erasing uncertainty or making the creators representatives of the whole person.

## One-paragraph local-session prompt

```text
Work in femboy2112/TLICA on a new non-main review branch. Fetch agent/idubbbz-hyde-paper-2026-09-09 and the companion agent/actualization-recognition-2026-09-09; inspect repo instructions, branch, commit, and worktree first. Read the standalone manuscript, evidence/correction ledger, protocol, corpus manifest, and handoff completely. Preserve Leah's 'inside out and reflected' hypothesis as a testable comparison of authority allocation, not a proven duality or personality diagnosis. Both creators may audit, provoke, enforce norms, and edit evidence. Obtain full primary 2022 sources before any claimed close reading; align footage and track event families, interventions, omissions, and uncertainty. Seek counterexamples and held-out works. Keep evidence attribution distinct from canonical T/R routing, and ethical permission distinct from predictive accuracy. Run structural_checks.py and make validate; the remote session ran only the finite tests, not full repository validation or a human study. Preserve original foundation and unrelated work; do not merge or publish without Leah's authorization.
```
