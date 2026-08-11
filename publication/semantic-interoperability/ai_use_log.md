# AI-use log — Semantic Interoperability

Every AI/tool interaction touching this paper is logged here after the scaffold
freeze (roadmap §35, Gate H0). No publication branch may contain an unlogged
generative-AI interaction. This log is the factual basis for the venue disclosure
(roadmap §8); it must be complete and exact, because a disclosure is only as honest
as the log behind it.

## Taxonomy (roadmap §6, with prosthetic use made explicit)

| Code | Use | Example |
|---|---|---|
| **A0** | No AI | Reading, handwritten notes, Leah-authored outline and prose |
| **A1** | Mechanical language aid | Spellcheck, punctuation, formatting, reference-manager cleanup |
| **A2** | Search / navigation aid | Finding candidate sources or current venue policies |
| **A3** | Critical aid | Generating objections, checking clarity, suggesting missing rivals |
| **A4** | Generative intellectual aid | Producing arguments, conclusions, section structures, or prose from Leah's ideas |
| **A5** | Autonomous / deceptive use | Fabricated sources, hidden authorship, text the author cannot defend — **prohibited** |

**Prosthetic use (explicit).** Several A1–A3 uses in this program function as an
**executive-function / ADHD prosthesis** rather than intellectual ghostwriting:
preserving state across sessions, retrieving prior decisions, maintaining these
ledgers, surfacing contradictions, generating hostile questions for Leah to answer,
and handling LaTeX/build mechanics. Prosthetic use is **permitted, logged, and
disclosed where required.** It is categorically distinct from **A4 generation of
submission prose**, which does not occur for the manuscript, and from A5, which is
prohibited. The dividing line is the operative authorship test: prosthesis organizes
and interrogates Leah's judgment; it never replaces it.

## Log

| Date | Tool / model | Category | Exact purpose | Altered conceptual content? | Output used? | Independent verification | Disclosure implication |
|---|---|---|---|---|---|---|---|
| 2026-08-10 | Claude Opus 4.8 (Claude Code) | Infrastructure (prosthetic; A2-adjacent) | Created this `publication/semantic-interoperability/` workspace — README, provenance, ledgers, outline/manuscript templates, venue matrix, submission templates | **No** — no manuscript exists; templates contain no submission prose | Yes (committed to branch `pub/interop-workspace-setup-2026-08-10`) | Leah reviews the full diff via draft PR before any merge | Publication **infrastructure**, not manuscript authorship; disclosed here and in [`provenance.md`](provenance.md) |
| 2026-08-10 | Claude Opus 4.8 (Claude Code) | A4-under-specification (governance doc, **not** the manuscript) | Rewrote the roadmap §5/§6 authorship-protocol prose from Leah's supplied specification (the corrected epistemic-authorship/prosthesis standard) | **Yes**, for the *roadmap* — governance prose drafted from substance Leah supplied; **no** manuscript content | Yes (committed to branch) | Leah supplied the standard and approves via draft PR | Concerns the research-tier **roadmap**, not the Paper I submission; logged for the roadmap's own provenance |
| 2026-08-10 | Claude Opus 4.8 (Claude Code) | A2 (navigation / verification) | Located the real schematic formulas in the interop research note to seed [`formal_ledger.md`](formal_ledger.md) with honest, unvalidated status labels | **No** — pointers only; no new formula asserted | Yes | Leah verifies each formula's status before any manuscript use | Infrastructure; every seeded formula remains **unvalidated** |

## Logging rule

Add a row for **every** AI interaction that touches this paper — including ones that
turn out useless. An omitted interaction is a false disclosure. When the manuscript
drafting begins, the expected steady state is **A0**: rows should be rare, and any
A3 red-teaming must name the venue policy that permits it.
