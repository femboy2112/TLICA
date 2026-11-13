# Validation Record — Trust and the Contact–Integration Loop

**Session date:** 2026-11-12, America/New_York.

**Baseline:** `main` at `61bcb24ed61765d23dd2595b8df4c8beb4fe0a63`.

**Working branch:** `astra/trust-kappa-rho-phi-2026-11-12`.

**Scope:** research documentation, a small finite standard-library witness, and the required rendering-observation entry in the existing compatibility ledger.

## Baseline observed

The repository was cloned into an isolated working directory. Its head matched the GitHub branch read, and the initial working tree was clean. The root agent read `AGENTS.md`, `AGENTS_MATH_PROTOCOL.md`, the GitHub math test card, and the compatibility ledger before editing.

`make validate` passed on the unchanged baseline:

- all **2,416** local Markdown links resolved across **489** Markdown files;
- self-containment and terminology pins passed;
- the GitHub-math static scan reported **0 errors**, **45 warnings**, and **153 informational findings**;
- the portable-math gate reported **0 portable findings** in its live scan;
- the existing math-guard calibration controls passed;
- the **22** calibration fallback items and **10** TLICA fallback items had **0 findings**.

These baseline warning/info counts are recorded for comparison. A passing static gate is not a browser rendering observation.

## New packet verification

The root agent executed the finite witness on its final source and captured its complete JSON output:

```bash
python3 -I research/trust_kappa_rho_phi_2026-11-12/finite_witness.py --json > research/trust_kappa_rho_phi_2026-11-12/WITNESS_RESULTS.json
python3 scripts/math_guard.py research/trust_kappa_rho_phi_2026-11-12 --strict-portable
make validate
```

**Finite result:** **26/26** named checks passed, exit code **0**. The raw report contains the declared evaluation inputs, symbolic φ signatures, fibre collisions, closed transition domain, events, holdout identities, surviving candidates, and every cell of the three factorial regimes. The script uses standard-library exact rational arithmetic and never replaces δ with a small floating-point value.

**Narrow portable-math result:** **7** new Markdown files scanned, **0 issues**, exit code **0**.

**Original packet archive result:** `make validate` passed with **2,483** local links across **496** Markdown files. Its live GitHub-math scan reported **0 errors**, **45 warnings**, and **153 informational findings**; the latter counts match the baseline. The live portable scan covered **479** files with **0 portable findings**. Self-containment, term pins, existing math-guard controls, and both mobile-fallback decks passed.

### Exact witness outcomes

| Fixture | Observed result | Scope |
| --- | --- | --- |
| TF-1 | The lossy coordinate projection has assessment/status collisions; declared evaluation inputs have none. | Synthetic current-assessment sufficiency cases. |
| TF-2 | Equal initial readouts have different successors under the same action; the full four-state domain is closed under both actions. | Deterministic distinction between present readout and transition sufficiency. |
| TF-3 | Repeating one identical constraint 32 times leaves the same two candidates; a new-context constraint leaves one. | Finite deterministic candidate set. |
| TW-1 | Selected accuracy is **1**, disjoint changed-context accuracy is **0**, and specified-population accuracy is **1/4**. | Designed selection failure; no statistical sampling claim. |
| TW-2 | Baseline four-cell gains are **0, 0, 0, 1**; interaction **1**. Duplicate-probe null and selection-dependence mutation each yield interaction **0**. | Specified access/selection mechanism; learning is not simulated. |

### Reproducibility binding

SHA-256 of `finite_witness.py`:

```text
58395b2989b04af02b773e370911ea11c8d36905de983b893e24bf7a3b85c201
```

SHA-256 of `WITNESS_RESULTS.json`:

```text
dbfa0accbb04beb5121a47df3a4e4fbffa1abb404bdca31b290dddc6324fd60e
```

The result file is captured stdout, not a hand-written summary. Changing descriptive text in the script can change its report digest even when the mathematical outputs remain the same; regenerate and rebind rather than silently leaving stale output.

### Review and correction record

The root agent inspected the proofs and the executable. A second assistant review checked them against the frozen foundation and source terminology. Two precision corrections were applied before the final capture:

1. The selection policy is **specified/model-linked**, not learned by this simulation. Developmental learning remains an open mechanism.
2. The dynamic counterexample has **two initial histories in a four-state domain**. The domain is explicit, with an additional closure check; its successors are not mislabeled as a two-state system.

The reviewers share model and conceptual provenance; their agreement is code/mathematical review, not independent empirical validation. No claim is promoted to a human-mechanism result on that basis.

## Author extension verification

The [osmotic-imprinting and social-scaffolding addendum](IMPRINTING_AND_SOCIAL_SCAFFOLDING.md) was added after the original finite run, with the author's exact new wording retained in the seed. The root agent reviewed IS-1's proof, the countable counterexample, the transport-map types, and the false-model commutation example against their stated assumptions. IS-1 is a statement about accumulated version spaces, not a general algorithmic stabilization or halting theorem.

The finite script and captured JSON are byte-identical to the digests above. The **26** existing checks remain the executed finite result; no new cultural-learning experiment or executable convergence test is claimed for the addendum. The expanded dossier's narrow portable-math scan covered **8** Markdown files with **0 issues**.

**Appended packet archive result:** `make validate` passed, exit code **0**, with **2,515** local links across **497** Markdown files. The live math scan covered **480** files with **0 errors**, **45 warnings**, and **153 informational findings**; baseline warning/info counts remain unchanged. The portable gate reported **0 portable findings**. Link, self-containment, term-pin, math-guard calibration, and the **22 + 10** mobile-fallback checks all passed.

A further read-only assistant review found no additional substantive blocker in IS-1, the countable counterexample, the Posit G attribution, or the typed transport square. The root applied the narrower version-space wording before this gate. This review shares model provenance and is not an empirical replication.

## Rendering boundary

The root agent inspected the actual GitHub repository views in desktop Chrome. The [exact observation record](RENDER_OBSERVATION.json) binds the URLs, commits, affected TeX bodies, and scope; the required [compatibility-ledger entry](../../docs/github-math/MATH_COMPATIBILITY_LEDGER.md) records the result.

At commit `37e60fdcdad620892608c7f9c705c29599b0e0c3`, the formalism's set braces disappeared in three display blocks and a thin-space escape became a literal comma in the integral. These were live rendering failures despite a passing source guard. The four TeX bodies were preserved exactly while their delimiters were changed to fenced math. At commit `7340d8c9b66e76a0b419f40e9f6d2b63e512dd7a`, all four repaired blocks were visually inspected and passed: braces were visible and differential spacing was correct. The proposed update, probe-weighting map, response derivative, and TF-1/TF-2 display equations were also seen as rendered notation during inspection; this is not a certificate for every possible surface or future edit.

The overview's Section 4 Mermaid diagram was visually inspected at the first commit, across two screenshots; its labels, arrows, and pathway-based φ node rendered. Other dossier pages and uninspected portions, mobile browsers, the native GitHub app, wiki, and PR/issue rendering remain **UNVERIFIED**. Screenshots remain in the task conversation. No PDF or wiki mirror is generated by this work.

## Research boundary

The witness checks only the declared finite models and exact arithmetic. No human experiment, neural measurement, population estimate, latent truth probability, or full generative κ–ρ-to-φ law has been run or established. The [claim ledger](CLAIM_LEDGER.md) controls downstream wording.
