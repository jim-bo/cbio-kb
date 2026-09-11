#!/usr/bin/env bash
# Package the passage index (data/paper_index: FAISS + BM25) for deployment.
#
# The index is gitignored and too large for git, so it ships as a versioned
# tarball plus a sha256 file. Where it goes from there is up to you:
#   - attach both files to a GitHub Release (or any HTTPS file host), then set
#     the repository variables PAPER_INDEX_URL / PAPER_INDEX_SHA256 so CI
#     bakes the index into the MCP and chat images;
#   - or unpack it on the host / a PersistentVolume and mount the
#     paper_index/ directory at /app/data/paper_index.
# docs/hosting.md ("Passage index") has the details.
#
# Usage:
#   scripts/package_index.sh [INDEX_DIR] [OUT_DIR]
#     INDEX_DIR  default data/paper_index
#     OUT_DIR    default dist
#
# Produces OUT_DIR/paper-index-YYYYMMDD.tar.gz (one top-level paper_index/
# directory) and OUT_DIR/paper-index-YYYYMMDD.tar.gz.sha256.

set -euo pipefail

INDEX_DIR="${1:-data/paper_index}"
OUT_DIR="${2:-dist}"

for f in meta.jsonl bm25.pkl index_config.json; do
    if [[ ! -f "${INDEX_DIR}/${f}" ]]; then
        echo "error: ${INDEX_DIR}/${f} not found. Build the index first:" >&2
        echo "  uv run cbio-kb index build-papers && uv run cbio-kb index build-bm25" >&2
        exit 1
    fi
done

STAMP="$(date -u +%Y%m%d)"
NAME="paper-index-${STAMP}.tar.gz"
mkdir -p "${OUT_DIR}"
OUT="$(cd "${OUT_DIR}" && pwd)/${NAME}"

# Stage through a symlink so the archive's top-level directory is always
# paper_index/, whatever INDEX_DIR is called (-h follows it; works with both
# GNU and BSD tar).
STAGE="$(mktemp -d)"
trap 'rm -rf "${STAGE}"' EXIT
ln -s "$(cd "${INDEX_DIR}" && pwd)" "${STAGE}/paper_index"
# COPYFILE_DISABLE keeps macOS tar from adding ._* AppleDouble files.
COPYFILE_DISABLE=1 tar -C "${STAGE}" -czhf "${OUT}" --exclude '.DS_Store' paper_index

if command -v sha256sum >/dev/null 2>&1; then
    (cd "$(dirname "${OUT}")" && sha256sum "${NAME}" > "${NAME}.sha256")
else
    (cd "$(dirname "${OUT}")" && shasum -a 256 "${NAME}" > "${NAME}.sha256")
fi
SHA="$(cut -d' ' -f1 < "${OUT}.sha256")"

MODEL="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1])).get("embed_model", "?"))' \
    "${INDEX_DIR}/index_config.json" 2>/dev/null || echo "?")"

cat <<EOF
Wrote ${OUT} ($(du -h "${OUT}" | cut -f1))
      ${OUT}.sha256
sha256:      ${SHA}
embed_model: ${MODEL}   (build the images with EMBED_MODEL=${MODEL})

To publish it as a GitHub Release asset (run these yourself):
  gh release create index-${STAMP} --latest=false --title "Passage index ${STAMP}" --notes "embed_model: ${MODEL}"
  gh release upload index-${STAMP} "${OUT}" "${OUT}.sha256"
Then set repository variables:
  PAPER_INDEX_URL=https://github.com/<owner>/<repo>/releases/download/index-${STAMP}/${NAME}
  PAPER_INDEX_SHA256=${SHA}
EOF
