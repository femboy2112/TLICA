#!/usr/bin/env bash
# Render Markdown documents to reading-copy PDFs via pandoc + lualatex.
#
# The Markdown files are authoritative; the PDFs are an on-demand artifact.
# Font choice is deliberate: DejaVu Serif (body) + DejaVu Sans Mono (code) give
# full coverage of TLICA's actual content -- text-mode Greek (kappa/phi/rho/eta/
# mu/sigma), subscripts (the Lagrange points L1..L5), and math punctuation. The
# default Latin Modern silently drops text-mode Greek; TeX Gyre Pagella drops the
# subscript digits; only the DejaVu pair renders it all. The one residue is color
# emoji (no serif font has them), which are decorative, not content. Any dropped
# glyph is surfaced loudly per file (grepped from the lualatex log), because
# pandoc exits 0 even when it drops a character: a missing symbol must never hide
# behind a clean exit code.
#
# A per-file build failure does not abort the run; the script exits nonzero only
# if some file failed to produce a PDF. Glyph drops are reported but do not fail
# the build (a dropped decorative emoji should not block a paper).
#
# Usage:
#   scripts/build_pdf.sh <out_dir> <file.md> [<file.md> ...]
set -u

MAINFONT="DejaVu Serif"
MONOFONT="DejaVu Sans Mono"

if [ "$#" -lt 2 ]; then
  echo "usage: scripts/build_pdf.sh <out_dir> <file.md> [<file.md> ...]" >&2
  exit 2
fi

out_dir="$1"; shift
mkdir -p "$out_dir"
tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT

built=0
failed=0
fail_names=()
drop_report=()

printf '%-46s %-6s %6s  %s\n' "DOCUMENT" "RESULT" "PAGES" "DROPPED GLYPHS"
printf '%s\n' "-------------------------------------------------------------------------"
for f in "$@"; do
  base="$(basename "$f" .md)"
  out="$out_dir/$base.pdf"
  err="$tmp_dir/$base.err"

  if [ ! -f "$f" ]; then
    printf '%-46s %-6s %6s  %s\n' "$base" "FAIL" "-" "(no such file: $f)"
    failed=$((failed + 1)); fail_names+=("$base"); continue
  fi

  if pandoc "$f" -o "$out" --pdf-engine=lualatex -V geometry:margin=1in \
        -V mainfont="$MAINFONT" -V monofont="$MONOFONT" >/dev/null 2>"$err"; then
    pages="$(pdfinfo "$out" 2>/dev/null | awk '/^Pages:/{print $2}')"
    drops="$(grep -c 'Missing character' "$err")"
    if [ "$drops" -gt 0 ]; then
      codes="$(grep -h 'Missing character' "$err" | grep -oE 'U\+[0-9A-Fa-f]+' \
               | sort | uniq -c | awk '{printf "%sx%s ", $2, $1}')"
      printf '%-46s %-6s %6s  %s\n' "$base" "OK" "${pages:-?}" "! $drops : $codes"
      drop_report+=("$base -> $codes")
    else
      printf '%-46s %-6s %6s  %s\n' "$base" "OK" "${pages:-?}" "-"
    fi
    built=$((built + 1))
  else
    printf '%-46s %-6s %6s  %s\n' "$base" "FAIL" "-" "(build error)"
    tail -4 "$err" | sed 's/^/      | /'
    failed=$((failed + 1)); fail_names+=("$base")
  fi
done

printf '%s\n' "-------------------------------------------------------------------------"
printf 'SUMMARY: %d built, %d failed  ->  %s/\n' "$built" "$failed" "$out_dir"

if [ "${#drop_report[@]}" -gt 0 ]; then
  printf '\n! GLYPH DROPS -- verify none are load-bearing symbols (kappa/phi/rho...):\n'
  for d in "${drop_report[@]}"; do printf '    %s\n' "$d"; done
fi

if [ "$failed" -ne 0 ]; then
  printf 'FAILED: %s\n' "${fail_names[*]}"
  exit 1
fi
exit 0
