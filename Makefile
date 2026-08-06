# TLICA archive -- validation harness.
#
# The archive is pure Markdown: the foundation (Files 0-5, frozen at v5.3.3),
# the application papers, and a hand-written wiki under docs/. There is nothing
# to compile and nothing numerical to calibrate -- the only things that can
# silently break are cross-links and the self-containment invariant. Both gates
# below are pure standard-library Python 3: no LaTeX, no pandoc, no third-party
# packages, no network. Run `make validate` after any edit that adds, moves, or
# links a document -- and always when registering a new application paper.

PYTHON ?= python3

.PHONY: validate links self-check help

## validate: run every archive invariant (links + self-containment)
validate: links self-check
	@echo "validate: OK (links + self-containment)"

## links: verify every internal Markdown link resolves on disk
links:
	@$(PYTHON) scripts/check_links.py

## self-check: verify the archive links to nothing outside its own tree
self-check:
	@$(PYTHON) scripts/check_self_contained.py

## help: list the available targets
help:
	@grep -E '^## ' $(MAKEFILE_LIST) | sed 's/^## /  /'
