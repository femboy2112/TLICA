# Execution record — 2026-10-12

Environment: isolated local Python 3.13.5 working directory (not a full Git checkout). Source files were created locally and tested before drafting the research branch.

Commands executed:

~~~bash
python3 -m unittest -v test_finite_lexicon
python3 finite_lexicon.py
python3 -m py_compile finite_lexicon.py test_finite_lexicon.py
~~~

Outcome: **10/10 unit tests passed**, py_compile passed; example summary:

~~~json
{
  "vibe": {"candidate_count_from_token": 2, "probe": "independent_report", "split_and_unresolved_pairs": [1, 0]},
  "cope": {"candidate_count_from_token": 3, "probe": "speech_role", "split_and_unresolved_pairs": [2, 1]},
  "lost_in_sauce": {"candidate_count_from_token": 2, "probe": "checkpoint", "split_and_unresolved_pairs": [1, 0]}
}
~~~

A deliberate mutation makes two "sauce" candidates predict the same checkpoint result, reducing distinguishing pairs from 1 to 0; the test detects that change. An incomplete prediction does not count as a split, and constructing an equivalence class from a partial prediction raises an error.

**Limits:** all 7 candidate states and all probes are invented; no transcripts, demographics, human participants, source reliability calibrations, actual TLICA profile values, or learned parameters. Tests establish consistency of *this finite bookkeeping*, not truth of the sociological/psychological interpretation.

**Not executed:** full-repository make validate / link audit (GitHub DNS inaccessible to the isolated container); branch-level GitHub Actions; independent package checkout or verification of blob-byte equality. These must be explicitly reported until performed.
