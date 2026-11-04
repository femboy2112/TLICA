#!/usr/bin/env bash
set -euo pipefail

# Fetch pinned upstreams for the Embodied Drosophila × TLICA research bootstrap.
# This script intentionally does not install CUDA, MuJoCo, conda environments,
# or Python dependencies. It only creates a reproducible source workspace.

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="${TLICA_FLY_UPSTREAM_ROOT:-${HERE}/.external}"

EON_REPO="https://github.com/eonsystemspbc/fly-brain.git"
EON_SHA="a3db62f9436074e485c0278290c2164ed6150808"

FLYGYM_REPO="https://github.com/NeLy-EPFL/flygym.git"
FLYGYM_SHA="38c8ec61034cd59bc5ba0de20688d4a3c0000d60"

mkdir -p "${ROOT}"

fetch_pinned() {
  local url="$1"
  local dest="$2"
  local sha="$3"

  if [[ ! -d "${dest}/.git" ]]; then
    git clone --filter=blob:none "${url}" "${dest}"
  fi

  git -C "${dest}" fetch --tags --prune origin
  git -C "${dest}" checkout --detach "${sha}"

  local actual
  actual="$(git -C "${dest}" rev-parse HEAD)"
  if [[ "${actual}" != "${sha}" ]]; then
    echo "ERROR: ${dest} resolved to ${actual}, expected ${sha}" >&2
    exit 1
  fi
}

fetch_pinned "${EON_REPO}" "${ROOT}/eon-fly-brain" "${EON_SHA}"
fetch_pinned "${FLYGYM_REPO}" "${ROOT}/flygym" "${FLYGYM_SHA}"

cat > "${ROOT}/UPSTREAM_LOCK.txt" <<EOF
Embodied Drosophila × TLICA upstream lock
created_by=bootstrap.sh

eonsystemspbc/fly-brain=${EON_SHA}
NeLy-EPFL/flygym=${FLYGYM_SHA}
EOF

cat <<EOF
Pinned upstreams are ready:
  brain: ${ROOT}/eon-fly-brain @ ${EON_SHA}
  body : ${ROOT}/flygym @ ${FLYGYM_SHA}
  lock : ${ROOT}/UPSTREAM_LOCK.txt

Next:
  1. Read HANDOFF.md.
  2. Reproduce an upstream brain-only Brian2 run before modifying anything.
  3. Instantiate an official FlyGym example unmodified.
  4. Run the dependency-free prototype tests in this dossier.

No heavy dependencies were installed automatically.
EOF
