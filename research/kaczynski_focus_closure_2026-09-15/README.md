# When the Map Becomes a Mandate
## Phase 1 research package — 15 September 2026

**Author:** Leah. **Drafting support:** AI-assisted research and composition; human review pending. **Version:** 0.1.0. Not peer reviewed.

This package studies reported experience, attention, self-interpretation, and moral authorization in Ted Kaczynski's writings. It is a source-critical pilot and research design, not a diagnosis, an endorsement, a validated causal biography, or a violence-risk instrument.

Read [MANUSCRIPT.md](MANUSCRIPT.md) first. It contains the substantive paper: a literature position, operational translation of TLICA, documentary pilot, rival explanations, preliminary constraints, ethics, and a prospective study design.

### What Phase 1 establishes

The particular 1983-origin story is incompatible with a campaign beginning in 1978, conditional on the dates used. Published justification is not direct evidence of developmental causation. The pilot retains revenge-first, reciprocal, audience-dependent, and knowing-harm accounts rather than declaring the attention hypothesis victorious. Numerical psychological coordinates have not been estimated.

### Package map

| File | Purpose |
|---|---|
| [MANUSCRIPT.md](MANUSCRIPT.md) | Substantive first draft |
| [SOURCES.md](SOURCES.md) | Bibliography, locators, access levels, and source families |
| [CLAIM_LEDGER.md](CLAIM_LEDGER.md) | Scoped verdicts and verdict-changing evidence |
| [PROTOCOL.md](PROTOCOL.md) | Prospective rival-discrimination and coding protocol |
| [PROVENANCE_AND_CORRECTIONS.md](PROVENANCE_AND_CORRECTIONS.md) | Initiating prompts, theory pin, and corrections to the conversational hypothesis |
| [data/evidence.json](data/evidence.json) | Ten development-set observations; not a representative corpus |
| [HANDOFF.md](HANDOFF.md) | Next research session and acceptance gates |
| [scripts/validate.py](scripts/validate.py) | Offline package-integrity checks |
| [scripts/test_validate.py](scripts/test_validate.py) | Positive, null, negative, and mutation controls |
| [checks/VALIDATION.md](checks/VALIDATION.md) | Validation scope and access limitation |
| [checks/validation.txt](checks/validation.txt) | Actual local test output |

### Reproduce the package checks

From the repository root:

```sh
python3 research/kaczynski_focus_closure_2026-09-15/scripts/validate.py
python3 -m unittest discover -s research/kaczynski_focus_closure_2026-09-15/scripts -p 'test_*.py' -v
make validate
```

The first two commands check this package. The third is the existing whole-archive gate and requires a complete checkout. Passing structural checks does not validate historical claims or TLICA.

### Repository boundary

Base commit: `e925fec1897488038e9efc20769b9bce403fd6ea`.

Base tree: `208cb557e20abb1cb924fefdf4cd7228cb0e1817`.

Branch: `research/kaczynski-focus-closure-2026-09-15`.

Theory: [TLICA v5.5.0 reading guide](../../foundation/0_reading_guide.md), including its explicitly experimental dynamical layer. Stable pre-dynamical material remains at [v5.3.3](../../foundation/previous_v5.3.3/). These relative links follow the checkout; the exact reference state is the base commit above.

Only this research directory is added. No foundation, application register, generated wiki, main branch, or publication pipeline is changed. No merge or public-release recommendation is implied by a working branch.
