"""Set wiki paper authors (and blank doi/journal/year) from PubMed.

paper-compiler infers bibliographic metadata from the extracted text. BioC
full text and some PDFs carry no byline, and in those cases the compiler has
filled author lists from memory. PubMed is authoritative, so this rewrites
``authors:`` from PubMed efetch (``ForeName LastName``, or the collective
name) and fills ``doi`` / ``journal`` / ``year`` only where they are blank.
Titles are left alone: they come from the paper text and already match.

Line-level frontmatter surgery, like scripts/stamp_corpus.py, so field order
and quoting elsewhere are preserved. Idempotent.

Usage:
    uv run python scripts/sync_pubmed_metadata.py 24030381 27169994 ...
    uv run python scripts/sync_pubmed_metadata.py --file pmids.txt --dry-run
"""
from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
WIKI_PAPERS = REPO_ROOT / "wiki" / "papers"
EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"


def fetch(pmids: list[str]) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for i in range(0, len(pmids), 100):
        q = urllib.parse.urlencode({"db": "pubmed", "id": ",".join(pmids[i:i + 100]),
                                    "retmode": "xml", "tool": "cbio-kb"})
        root = ET.fromstring(urllib.request.urlopen(f"{EFETCH}?{q}", timeout=90).read())
        for art in root.iter("PubmedArticle"):
            pmid = art.findtext("MedlineCitation/PMID")
            authors = []
            for a in art.iterfind(".//AuthorList/Author"):
                name = " ".join(filter(None, [a.findtext("ForeName"), a.findtext("LastName")]))
                name = name or a.findtext("CollectiveName") or ""
                if name.strip():
                    authors.append(name.strip())
            doi = next((e.text for e in art.iterfind(".//ArticleIdList/ArticleId")
                        if e.get("IdType") == "doi"), "") or ""
            year = art.findtext(".//JournalIssue/PubDate/Year") or \
                (art.findtext(".//JournalIssue/PubDate/MedlineDate") or "")[:4]
            out[pmid] = {"authors": authors, "doi": doi, "year": year,
                         "journal": art.findtext(".//Journal/Title") or ""}
        time.sleep(0.4)
    return out


def _yaml_item(s: str) -> str:
    return f'"{s}"' if re.search(r'[:#\[\]{}"]|^[-?!&*]', s) else s


def patch(text: str, meta: dict) -> str:
    head, sep, body = text.partition("\n---\n")
    lines = head.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r"^authors:", line) and meta["authors"]:
            i += 1
            while i < len(lines) and lines[i].startswith("  - "):
                i += 1
            out.append("authors:")
            out += [f"  - {_yaml_item(a)}" for a in meta["authors"]]
            continue
        m = re.match(r"^(doi|journal|year):\s*(.*)$", line)
        if m and not m.group(2).strip().strip("\"'") and meta.get(m.group(1)):
            line = f"{m.group(1)}: {_yaml_item(meta[m.group(1)])}"
        out.append(line)
        i += 1
    return "\n".join(out) + sep + body


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("pmids", nargs="*")
    ap.add_argument("--file", type=Path, help="File with one PMID per line")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    pmids = list(args.pmids)
    if args.file:
        pmids += [ln.strip() for ln in args.file.read_text().splitlines() if ln.strip()]
    if not pmids:
        ap.error("no PMIDs given")

    meta = fetch(pmids)
    changed = 0
    for pmid in pmids:
        page = WIKI_PAPERS / f"{pmid}.md"
        if not page.exists() or pmid not in meta:
            print(f"[skip] {pmid}: {'no wiki page' if not page.exists() else 'not in PubMed'}")
            continue
        text = page.read_text(encoding="utf-8")
        new = patch(text, meta[pmid])
        if new != text:
            changed += 1
            print(f"[{'would update' if args.dry_run else 'updated'}] {pmid}: "
                  f"{len(meta[pmid]['authors'])} authors")
            if not args.dry_run:
                page.write_text(new, encoding="utf-8")
    print(f"[done] {changed} page(s) {'would change' if args.dry_run else 'changed'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
