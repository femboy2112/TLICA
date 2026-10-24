# TLICA core equations — Android-app fallback 📱

[← calibration kit](README.md) · [calibration strips](MOBILE_APP_FALLBACK.md) · [compatibility ledger](MATH_COMPATIBILITY_LEDGER.md)

> **Why this page exists.** GitHub's Android app renders no live MathJax, so on the app the equations below would otherwise appear as raw `$…$` source. Each image is rendered from the **exact TeX in the source file named beneath it** — never retyped — and pinned to a SHA-256 of that source, so it cannot silently drift. On desktop or a mobile **web browser**, read the live theory instead; this is a fallback, not the canon.

> **Boundary.** A PNG appearing on screen is **not** a passing TeX-render test, and these ten equations are a reader's entry map, not the full formal apparatus — that lives in the [foundation](../../foundation/).

## The load-bearing equations

### E01 · The three coordinates: contact, truth-indistinguishability, identity

![E01 — The three coordinates: contact, truth-indistinguishability, identity](../../assets/mobile-tlica/e01.png)

*Source: [`foundation/3_formal_apparatus.md`](../../foundation/3_formal_apparatus.md).*

### E02 · Contact as max-flow from the self-node

![E02 — Contact as max-flow from the self-node](../../assets/mobile-tlica/e02.png)

*Source: [`foundation/3_formal_apparatus.md`](../../foundation/3_formal_apparatus.md).*

### E03 · Identity-correlation from a single toolkit

![E03 — Identity-correlation from a single toolkit](../../assets/mobile-tlica/e03.png)

*Source: [`foundation/3_formal_apparatus.md`](../../foundation/3_formal_apparatus.md).*

### E04 · Identity-correlation aggregated over toolkits

![E04 — Identity-correlation aggregated over toolkits](../../assets/mobile-tlica/e04.png)

*Source: [`foundation/3_formal_apparatus.md`](../../foundation/3_formal_apparatus.md).*

### E05 · The identity-correlation profile (vector-valued rho)

![E05 — The identity-correlation profile (vector-valued rho)](../../assets/mobile-tlica/e05.png)

*Source: [`foundation/3_formal_apparatus.md`](../../foundation/3_formal_apparatus.md).*

### E06 · Felt-field potential V = tau * norm of Delta

![E06 — Felt-field potential V = tau * norm of Delta](../../assets/mobile-tlica/e06.png)

*Source: [`foundation/3_formal_apparatus.md`](../../foundation/3_formal_apparatus.md).*

### E07 · The driven allostatic orbit

![E07 — The driven allostatic orbit](../../assets/mobile-tlica/e07.png)

*Source: [`foundation/3_formal_apparatus.md`](../../foundation/3_formal_apparatus.md).*

### E08 · Mismatch descent along the rho-metric gradient

![E08 — Mismatch descent along the rho-metric gradient](../../assets/mobile-tlica/e08.png)

*Source: [`foundation/3_formal_apparatus.md`](../../foundation/3_formal_apparatus.md).*

### E09 · Slack: capacity minus pressure

![E09 — Slack: capacity minus pressure](../../assets/mobile-tlica/e09.png)

*Source: [`foundation/3_formal_apparatus.md`](../../foundation/3_formal_apparatus.md).*

### E10 · Identity-correlation from max-flow (File 5 form)

![E10 — Identity-correlation from max-flow (File 5 form)](../../assets/mobile-tlica/e10.png)

*Source: [`foundation/5_translations_open_problems_conclusion.md`](../../foundation/5_translations_open_problems_conclusion.md).*

## Rebuilding

Verify committed images against their sources (standard library only):

```bash
python3 scripts/mobile_fallback.py --deck tlica
```

Regenerate after a source equation changes (needs Node + mathjax-full, CairoSVG, Pillow):

```bash
make mobile-fallback            # or: python3 scripts/mobile_fallback.py --build --deck tlica
```

The equation list is [`mobile-math.sources.json`](mobile-math.sources.json); each entry names a source file and a unique substring of the display block to project. Add an entry there, never retype an equation here.

