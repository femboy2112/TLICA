# Bootstrap validation record

Session date: 2026-09-22. Python 3.13.5. Base main commit: `471c28566dbf08b54bbc64d2c83089806a772e9f`.

## Executed

`python3 run_checks.py`: exit 0, **38 tests passed**, zero failures/errors. This includes an exhaustive three-valued conjunction check over 1,093 input tuples (lengths 0–6), 150 deterministic configuration-holdout catalogs checked against a separately expressed set oracle, the eight fixtures, and input/transport/provenance/consent controls.

`python3 mutation_checks.py`: exit 0, **3/3 deliberate semantic mutants killed by assertion failures** in the otherwise unchanged suite. The mutated versions treat unknown as true, erase consent, or bypass source availability. Each mutant's unittest process exited 1 as expected; syntax errors were excluded as successful kills.

`python3 -m py_compile interop.py fixtures.py test_interop.py run_checks.py mutation_checks.py`: exit 0.

The final hardening pass added explicit rejection of a case missing its reality gate or any participant's acceptability floor. Standing/third-party gates and complete option-consent records are also required. This prevents schema omissions from silently becoming universal acceptance. It cannot prove that the supplied real-world model would be complete or accurate.

## Results, not just test counts

| Invented case | Recorded result |
|---|---|
| Shared workshop | Three supported schedules; two non-dominated alternatives; no arbitrarily selected winner |
| Attractive but unsafe windfall | Rejected despite both participants' high stipulated preference ranks |
| Unmeasured insulation | UNRESOLVED; missing physical evidence is not turned into agreement or impossibility |
| Shared causal map, conflicting floors | No permissible option in the supplied catalog; two-floor minimal blocking set |
| Withheld consent | Rejected even though all modeled benefit gates pass |
| Burden exported to an outsider | Rejected by the declared standing gate |
| Music/shared listening | A separate-use option passes; music is one of eight cases, not the program boundary |
| Three-party compatibility | Each pair has an acceptable option; all three have none in this catalog |
| Empty candidate catalog | Explicit pathway gap, not a no-solution theorem |

The windfall is an option inside the workshop case, not a ninth independent fixture. All sources in the base fixtures are authored stipulations, except a deliberately unverified measurement entry. Removing the authored source family removes supported agreement; it does not manufacture new evidence. A known consent refusal remains a rejection even when other support is removed.

## Preserved records and rerun instructions

[results.json](results.json) contains the machine report, full gate matrices, input/source SHA-256 hashes, source-family ablations, and probe split counts. [tests.txt](tests.txt) preserves the final unittest output. [mutations.json](mutations.json) preserves the final mutation-run readout. The mutation script regenerates the detailed failure traces as `checks/mutation_*.txt`; the session's full raw traces are also retained in the accompanying local audit archive.

Re-run from the dossier directory:

```bash
python3 run_checks.py
python3 mutation_checks.py
python3 -m py_compile interop.py fixtures.py test_interop.py run_checks.py mutation_checks.py
```

Expected tracked source Git blob hashes (same bytes tested locally):

```
744104e46d6870d95708b1e847097605fa31cc6e  interop.py
0e8d562fcc9bf419d485635c4ff795212cd6b0ba  fixtures.py
65a766e02a6be437a2d4df02d8ca726f979d65e9  test_interop.py
9b203fe74278fa336fb7b2d875982a5c3ee12c5d  run_checks.py
23cb22eb6696983a3d5e09ccfab5de5d88ec5dc6  mutation_checks.py
```

JSON formatting, unittest duration, Python version, and temporary mutation-directory paths can differ on rerun. Compare input/source hashes and substantive results, not those incidental strings.

## Repository-wide gate: NOT RUN

An attempted container clone failed with `Could not resolve host: github.com`. The GitHub connector remained available for reads and branch writes. A complete archive could not be downloaded either. The full `make validate` therefore was **NOT RUN**; do not confuse this package PASS with the repository's link, self-containment, and term-pin gates. The Makefile and the term checker were inspected. Run the full gate in the local complete checkout before merging.

No existing foundation/application/index file is changed by this dossier. Add the research index entry and changelog note during reviewed integration. No main update, pull request, wiki publication, or DOI release is performed here.

## Scientific boundary

All outcomes above concern a finite, hand-encoded synthetic instrument. The two code expressions share authoring provenance; no independent agent, blinded assessor, real listener, negotiated human outcome, or validated cultural mechanism is claimed. The cultural atlas, natural-language interpretation, dynamic learning, candidate-generation capability, and practical efficacy remain unimplemented or UNVERIFIED as documented in HANDOFF.md and CLAIM_LEDGER.md.
