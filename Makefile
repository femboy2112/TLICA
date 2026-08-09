# TLICA archive -- validation harness and PDF reading copies.
#
# The archive is pure Markdown: the foundation (Files 0-5, frozen at v5.3.3),
# the application papers, and a hand-written wiki under docs/. The Markdown is
# authoritative. Two kinds of target:
#
#   validate / links / self-check  -- pure standard-library Python 3, no LaTeX,
#     no third-party packages, no network. Run these constantly.
#   pdfs / foundation-pdfs / pdf   -- render on-demand reading-copy PDFs; these
#     need pandoc + lualatex. PDFs land under output/ and are NOT tracked.
#
# Run `make validate` after any edit that adds, moves, or links a document, and
# always when registering a new application paper. Run `make help` for the list.

PYTHON ?= python3
OUT    ?= output/pdf

# Current reading version of each application paper. Curated by hand, NOT
# globbed: the archive retains superseded drafts (the earlier Cold Frame
# versions, the referent_routing skeleton, the self_applied working docs)
# beside their successors, so "latest file on disk" is not "current paper."
# Add a line here when a paper is versioned up -- it is part of registering it.
PAPERS := \
  applications/6_temporal_phenomenology.md \
  applications/differentiated_affect_v1_0_2.md \
  applications/free_will_v0_3_0.md \
  applications/agency_architecture_v0_3_0.md \
  applications/out_of_the_cave_v0_1_2.md \
  applications/cold_frame_v0_4_3.md \
  applications/self_applied_architecture_prose_draft_v0_1.md \
  applications/caves_lagrange_points_v0_1_0.md \
  applications/this_is_water_truth_respecting_choice_v0_1_0.md \
  applications/shared_reality_divergent_maps_v0_1_0.md

FOUNDATION := $(wildcard foundation/*.md)

.PHONY: validate links self-check pdfs foundation-pdfs all-pdfs pdf help

## validate: run every archive invariant (links + self-containment)
validate: links self-check
	@echo "validate: OK (links + self-containment)"

## links: verify every internal Markdown link resolves on disk
links:
	@$(PYTHON) scripts/check_links.py

## self-check: verify the archive links to nothing outside its own tree
self-check:
	@$(PYTHON) scripts/check_self_contained.py

## pdfs: render current application papers to reading-copy PDFs (needs pandoc+lualatex)
pdfs:
	@bash scripts/build_pdf.sh $(OUT) $(PAPERS)

## foundation-pdfs: render the frozen foundation (Files 0-5) to PDFs
foundation-pdfs:
	@bash scripts/build_pdf.sh $(OUT) $(FOUNDATION)

## all-pdfs: render the foundation and every current application paper
all-pdfs:
	@bash scripts/build_pdf.sh $(OUT) $(FOUNDATION) $(PAPERS)

## pdf: render one file, e.g. `make pdf FILE=applications/free_will_v0_3_0.md`
pdf:
	@test -n "$(FILE)" || { echo "usage: make pdf FILE=path/to/doc.md" >&2; exit 2; }
	@bash scripts/build_pdf.sh $(OUT) $(FILE)

## help: list the available targets
help:
	@grep -E '^## ' $(MAKEFILE_LIST) | sed 's/^## /  /'
