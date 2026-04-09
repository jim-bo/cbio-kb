"""Single console entry point: `cbio-kb <subcommand>`.

Only deterministic subcommands live here. LLM-shaped work (compile, query,
crosslink agent, theme synthesis) is performed by agents under
.claude/agents/ or .gemini/agents/, orchestrated interactively — not by this CLI.
"""
from __future__ import annotations

import argparse
from pathlib import Path


def _cmd_ingest_extract(args: argparse.Namespace) -> int:
    from cbio_kb.ingest import extract

    return extract.run(
        pdf_dir=Path(args.pdf_dir),
        out_dir=Path(args.out_dir),
        mapping_csv=Path(args.mapping),
        limit=args.limit,
    )


def _cmd_ingest_resolve(args: argparse.Namespace) -> int:
    from cbio_kb.ingest import pmid2pmcid

    return pmid2pmcid.main([])


def _cmd_ingest_pdfs(args: argparse.Namespace) -> int:
    from cbio_kb.ingest import pmc_downloader

    return pmc_downloader.main([
        "--in", args.mapping,
        "--out-dir", args.out_dir,
        "--email", args.email,
    ])


def _cmd_index_build(args: argparse.Namespace) -> int:
    from cbio_kb.index import semsearch

    return semsearch.main([
        "index",
        "--pdf-dir", args.pdf_dir,
        "--index-dir", args.index_dir,
    ])


def _cmd_index_search(args: argparse.Namespace) -> int:
    from cbio_kb.index import semsearch

    argv = [
        "search",
        "--index-dir", args.index_dir,
        "-q", args.query,
        "--top-k", str(args.top_k),
    ]
    if args.rerank:
        argv.append("--rerank")
    return semsearch.main(argv)


def _cmd_ontology_sync(args: argparse.Namespace) -> int:
    from cbio_kb.ontology import sync

    return sync.run(out_dir=Path(args.out_dir))


def _cmd_ontology_lookup(args: argparse.Namespace) -> int:
    from cbio_kb.ontology import lookup

    return lookup.run_lookup(ontology_dir=Path(args.ontology_dir), query=args.query)


def _cmd_lint(args: argparse.Namespace) -> int:
    from cbio_kb.wiki import lint

    return lint.run(wiki_dir=Path(args.wiki_dir))


def _cmd_search(args: argparse.Namespace) -> int:
    from cbio_kb.wiki import search

    return search.run(wiki_dir=Path(args.wiki_dir), query=args.query)


def _cmd_crosslink(args: argparse.Namespace) -> int:
    from cbio_kb.wiki import crosslink

    return crosslink.run(
        Path(args.wiki_dir),
        [Path(p) for p in args.paths] if args.paths else None,
        dry_run=args.dry_run,
    )


def _cmd_logs_export(args: argparse.Namespace) -> int:
    from cbio_kb.logs import export

    sid = export._latest_session() if args.latest else args.session
    export.export(sid, Path(args.out), truncate=args.truncate)
    return 0


def _cmd_serve(args: argparse.Namespace) -> int:
    from cbio_kb.server import mcp

    return mcp.main(["--host", args.host, "--port", str(args.port)])


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="cbio-kb", description="cbio-kb CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    ingest = sub.add_parser("ingest", help="Fetch and normalize raw papers")
    ingest_sub = ingest.add_subparsers(dest="subcmd", required=True)

    ext = ingest_sub.add_parser("extract", help="PDFs -> raw/papers/*.md")
    ext.add_argument("--pdf-dir", default="data/raw/pdfs")
    ext.add_argument("--out-dir", default="data/raw/papers")
    ext.add_argument("--mapping", default="data/pmid_to_pmcid.csv")
    ext.add_argument("--limit", type=int, default=None)
    ext.set_defaults(func=_cmd_ingest_extract)

    res = ingest_sub.add_parser("resolve", help="PMIDs -> PMCIDs (NCBI)")
    res.set_defaults(func=_cmd_ingest_resolve)

    pdfs = ingest_sub.add_parser("pdfs", help="Download PDFs from PMC")
    pdfs.add_argument("--mapping", default="data/pmid_to_pmcid.csv")
    pdfs.add_argument("--out-dir", default="data/raw/pdfs")
    pdfs.add_argument("--email", required=True)
    pdfs.set_defaults(func=_cmd_ingest_pdfs)

    idx = sub.add_parser("index", help="FAISS passage index")
    idx_sub = idx.add_subparsers(dest="subcmd", required=True)
    idx_b = idx_sub.add_parser("build")
    idx_b.add_argument("--pdf-dir", default="data/raw/pdfs")
    idx_b.add_argument("--index-dir", default="data/index_dir")
    idx_b.set_defaults(func=_cmd_index_build)
    idx_s = idx_sub.add_parser("search")
    idx_s.add_argument("--index-dir", default="data/index_dir")
    idx_s.add_argument("-q", "--query", required=True)
    idx_s.add_argument("--top-k", type=int, default=5)
    idx_s.add_argument("--rerank", action="store_true")
    idx_s.set_defaults(func=_cmd_index_search)

    ont = sub.add_parser("ontology", help="Canonical ontology management")
    ont_sub = ont.add_subparsers(dest="subcmd", required=True)
    ont_s = ont_sub.add_parser("sync", help="Pull canonical lists from cBioPortal + OncoTree")
    ont_s.add_argument("--out-dir", default="schema/ontology")
    ont_s.set_defaults(func=_cmd_ontology_sync)
    ont_l = ont_sub.add_parser("lookup", help="Validate a term against canonical IDs")
    ont_l.add_argument("query")
    ont_l.add_argument("--ontology-dir", default="schema/ontology")
    ont_l.set_defaults(func=_cmd_ontology_lookup)

    lnt = sub.add_parser("lint", help="Validate wiki structure")
    lnt.add_argument("--wiki-dir", default="wiki")
    lnt.set_defaults(func=_cmd_lint)

    srch = sub.add_parser("search", help="Ripgrep-backed FTS over wiki/")
    srch.add_argument("query")
    srch.add_argument("--wiki-dir", default="wiki")
    srch.set_defaults(func=_cmd_search)

    xl = sub.add_parser("crosslink", help="Deterministic crosslinker (no LLM)")
    xl.add_argument("--wiki-dir", default="wiki")
    xl.add_argument("--paths", nargs="*")
    xl.add_argument("--dry-run", action="store_true")
    xl.set_defaults(func=_cmd_crosslink)

    logs = sub.add_parser("logs", help="Session transcript tools")
    logs_sub = logs.add_subparsers(dest="subcmd", required=True)
    logs_e = logs_sub.add_parser("export", help="Stitch main + subagent JSONLs into a Markdown transcript")
    g = logs_e.add_mutually_exclusive_group(required=True)
    g.add_argument("--session", help="session UUID")
    g.add_argument("--latest", action="store_true")
    logs_e.add_argument("--out", required=True)
    logs_e.add_argument("--truncate", type=int, default=2000)
    logs_e.set_defaults(func=_cmd_logs_export)

    srv = sub.add_parser("serve", help="Start MCP server")
    srv.add_argument("--host", default="localhost")
    srv.add_argument("--port", type=int, default=8123)
    srv.set_defaults(func=_cmd_serve)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
