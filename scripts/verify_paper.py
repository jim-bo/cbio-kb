"""Ad-hoc fact-verifier for compiled paper pages.

Reads `wiki/papers/{pmid}.md`, parses its YAML frontmatter, and cross-checks
the declared facts against the public cBioPortal REST API. Each check produces
zero or more `Finding`s with severity in {pass, info, warn, fail}. Findings can
be rendered to stdout for a single paper, or dumped per-paper to JSON for
corpus-wide aggregation.

Usage:
    # single paper, stdout report
    uv run python scripts/verify_paper.py --pmid 26901067

    # batch over every wiki/papers/*.md, JSON-only output
    uv run python scripts/verify_paper.py --all --out-dir eval/verify

    # explicit list + JSON dump
    uv run python scripts/verify_paper.py --pmid 26901067 --pmid 36577525 \
        --out-dir eval/verify

    # add the slow gene-cohort spot-check (POST per gene)
    uv run python scripts/verify_paper.py --pmid 26901067 --gene-limit 5

Network: hits https://www.cbioportal.org/api directly (no auth, no caching).
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
WIKI_PAPERS = REPO_ROOT / "wiki" / "papers"
ONTOLOGY_DIR = REPO_ROOT / "schema" / "ontology"
CBIO = "https://www.cbioportal.org/api"

SEVERITY = ("pass", "info", "warn", "fail")
SYMBOL = {"pass": "✓", "info": "•", "warn": "⚠", "fail": "✗"}


@dataclass
class Finding:
    severity: str        # one of SEVERITY
    code: str            # stable identifier, e.g. "study.cancer_type_mismatch"
    scope: str           # what the finding is about, e.g. "study_id:blca_..."
    message: str         # human-readable
    evidence: dict = field(default_factory=dict)


def _get(path: str, timeout: int = 30) -> Any | None:
    """GET {CBIO}{path}. Returns parsed JSON, None on 404."""
    req = urllib.request.Request(f"{CBIO}{path}",
                                  headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def _post(path: str, body: dict, timeout: int = 30) -> Any | None:
    req = urllib.request.Request(
        f"{CBIO}{path}",
        data=json.dumps(body).encode(),
        headers={"Accept": "application/json", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def load_frontmatter(pmid: str) -> dict:
    path = WIKI_PAPERS / f"{pmid}.md"
    if not path.exists():
        sys.exit(f"missing wiki page: {path}")
    text = path.read_text()
    if not text.startswith("---\n"):
        sys.exit(f"no YAML frontmatter in {path}")
    end = text.find("\n---\n", 4)
    if end < 0:
        sys.exit(f"unterminated frontmatter in {path}")
    return yaml.safe_load(text[4:end])


def load_ontology() -> dict[str, set]:
    out = {"genes": set(), "cancer_types": set(), "gene_panels": set(), "oncotree": set()}
    for name, key, dest in [
        ("genes.json", "hugoGeneSymbol", "genes"),
        ("cancer_types.json", "cancerTypeId", "cancer_types"),
        ("gene_panels.json", "genePanelId", "gene_panels"),
    ]:
        p = ONTOLOGY_DIR / name
        if p.exists():
            for row in json.loads(p.read_text()):
                out[dest].add(row[key])
    p = ONTOLOGY_DIR / "oncotree.json"
    if p.exists():
        stack = list(json.loads(p.read_text()))
        while stack:
            node = stack.pop()
            if isinstance(node, dict):
                if node.get("code"):
                    out["oncotree"].add(node["code"])
                children = node.get("children") or {}
                if isinstance(children, dict):
                    stack.extend(children.values())
                elif isinstance(children, list):
                    stack.extend(children)
    return out


def hugo_to_entrez() -> dict[str, int]:
    p = ONTOLOGY_DIR / "genes.json"
    if not p.exists():
        return {}
    return {row["hugoGeneSymbol"]: row["entrezGeneId"] for row in json.loads(p.read_text())}


# ---------- Checks ----------

def check_study(study_id: str, fm: dict, *, is_primary: bool) -> tuple[dict | None, list[Finding]]:
    """Identity + linkage checks for one study. Returns (study_record, findings).

    `is_primary` distinguishes the paper's own `study_id:` (where a PMID
    mismatch is suspicious — likely the wrong study was picked) from entries
    in `datasets:` (where a PMID mismatch is *expected* — the paper is citing
    a third-party dataset).
    """
    scope = f"{'study_id' if is_primary else 'dataset'}:{study_id}"
    findings: list[Finding] = []
    study = _get(f"/studies/{urllib.parse.quote(study_id)}")
    if study is None:
        findings.append(Finding("fail", "study.missing", scope,
                                "not found on cBioPortal"))
        return None, findings

    findings.append(Finding("pass", "study.exists", scope,
                            f"{study.get('name', '?')!r}",
                            evidence={"name": study.get("name"),
                                      "citation": study.get("citation")}))

    # cBioPortal returns a comma-separated string for studies with multiple
    # primary citations (e.g. pan-cancer atlas releases).
    api_pmid_raw = str(study.get("pmid") or "")
    api_pmids = [p.strip() for p in api_pmid_raw.split(",") if p.strip()]
    paper_pmid = str(fm.get("pmid") or "")
    if api_pmids and paper_pmid:
        if paper_pmid in api_pmids:
            findings.append(Finding("pass", "study.pmid_match", scope,
                                    f"paper pmid in API list ({len(api_pmids)} pmid(s))",
                                    evidence={"api_pmids": api_pmids, "paper_pmid": paper_pmid}))
        elif is_primary:
            findings.append(Finding("warn", "study.pmid_differs", scope,
                                    f"paper pmid {paper_pmid} not in API pmid list {api_pmids} "
                                    f"— paper-compiler may have picked the wrong primary study",
                                    evidence={"api_pmids": api_pmids, "paper_pmid": paper_pmid}))
        else:
            findings.append(Finding("info", "study.pmid_differs_cited", scope,
                                    f"cited dataset's API pmid(s) {api_pmids} "
                                    f"differ from paper (expected for non-primary datasets)",
                                    evidence={"api_pmids": api_pmids, "paper_pmid": paper_pmid}))

    api_ct = (study.get("cancerTypeId") or "").lower()
    fm_cts = [c.lower() for c in (fm.get("cancer_types") or [])]
    if api_ct:
        if api_ct in fm_cts:
            findings.append(Finding("pass", "study.cancer_type_match", scope,
                                    f"cancerTypeId {api_ct!r} matches frontmatter cancer_types",
                                    evidence={"api_cancer_type_id": api_ct, "frontmatter": fm_cts}))
        elif fm_cts:
            findings.append(Finding("warn", "study.cancer_type_mismatch", scope,
                                    f"cancerTypeId {api_ct!r} not in frontmatter {fm_cts}",
                                    evidence={"api_cancer_type_id": api_ct, "frontmatter": fm_cts}))
        else:
            findings.append(Finding("info", "study.cancer_type_only_api", scope,
                                    f"frontmatter cancer_types empty; API says {api_ct!r}",
                                    evidence={"api_cancer_type_id": api_ct}))

    findings.append(Finding("info", "study.samples", scope,
                            f"{study.get('sequencedSampleCount')} sequenced, "
                            f"{study.get('cnaSampleCount')} CNA-profiled",
                            evidence={
                                "sequencedSampleCount": study.get("sequencedSampleCount"),
                                "cnaSampleCount": study.get("cnaSampleCount"),
                                "allSampleCount": study.get("allSampleCount"),
                            }))
    return study, findings


def check_panels(study_id: str, fm_methods: list[str],
                 known_panels: set[str], *, is_primary: bool) -> list[Finding]:
    scope = f"{'study_id' if is_primary else 'dataset'}:{study_id}"
    panel_methods = [m for m in fm_methods if m in known_panels]
    if not panel_methods:
        return [Finding("info", "method.no_panels_in_frontmatter", scope,
                        f"no frontmatter methods resolve to known panel IDs "
                        f"(of {len(fm_methods)} methods)")]
    profiles = _get(f"/studies/{urllib.parse.quote(study_id)}/molecular-profiles") or []
    sample_lists = _get(f"/studies/{urllib.parse.quote(study_id)}/sample-lists") or []
    haystack = " ".join(
        (p.get("molecularProfileId", "") + " " + p.get("name", "") + " " + p.get("description", ""))
        for p in profiles
    ) + " " + " ".join(
        (s.get("sampleListId", "") + " " + s.get("name", "") + " " + s.get("description", ""))
        for s in sample_lists
    )
    haystack_lower = haystack.lower()
    findings: list[Finding] = []
    for method in panel_methods:
        if method.lower() in haystack_lower:
            findings.append(Finding("pass", "method.panel_in_study", scope,
                                    f"{method} referenced in study profiles/sample-lists",
                                    evidence={"method": method}))
        else:
            stem = "".join(c for c in method if c.isalpha()).lower()
            if stem and stem in haystack_lower:
                findings.append(Finding("warn", "method.panel_family_only", scope,
                                        f"{method}: exact id not in study, "
                                        f"but family '{stem}' is referenced",
                                        evidence={"method": method, "stem": stem}))
            else:
                findings.append(Finding("warn", "method.panel_missing", scope,
                                        f"{method}: no matching profile/sample-list in study",
                                        evidence={"method": method}))
    return findings


def check_ontology_sanity(fm: dict, ont: dict[str, set]) -> list[Finding]:
    genes = fm.get("genes") or []
    cts = fm.get("cancer_types") or []
    methods = fm.get("methods") or []
    g_hit = sum(1 for g in genes if g in ont["genes"])
    ct_hit = sum(1 for c in cts if c in ont["oncotree"] or c in ont["cancer_types"])
    m_hit = sum(1 for m in methods if m in ont["gene_panels"])
    g_miss = [g for g in genes if g not in ont["genes"]]
    ct_miss = [c for c in cts if c not in ont["oncotree"] and c not in ont["cancer_types"]]
    findings: list[Finding] = []
    sev_genes = "pass" if not g_miss else "warn"
    findings.append(Finding(sev_genes, "ontology.genes", "paper",
                            f"{g_hit}/{len(genes)} HUGO symbols resolve",
                            evidence={"total": len(genes), "hits": g_hit, "missing": g_miss}))
    sev_ct = "pass" if not ct_miss else "warn"
    findings.append(Finding(sev_ct, "ontology.cancer_types", "paper",
                            f"{ct_hit}/{len(cts)} cancer types resolve",
                            evidence={"total": len(cts), "hits": ct_hit, "missing": ct_miss}))
    findings.append(Finding("info", "ontology.methods_as_panels", "paper",
                            f"{m_hit}/{len(methods)} methods resolve as gene panels "
                            f"(rest are free-text method slugs — not necessarily wrong)",
                            evidence={"total": len(methods), "hits": m_hit}))
    return findings


# ---------- Gene-cohort spot-check (slow, behind --gene-limit) ----------

TRUNCATING = {"Nonsense_Mutation", "Frame_Shift_Del", "Frame_Shift_Ins",
              "Splice_Site", "Nonstop_Mutation", "Translation_Start_Site"}
MISSENSE = {"Missense_Mutation"}
INFRAME = {"In_Frame_Del", "In_Frame_Ins"}


def _classify(mt: str) -> str:
    if mt in TRUNCATING: return "truncating"
    if mt in MISSENSE: return "missense"
    if mt in INFRAME: return "inframe"
    return "other"


def check_genes(study_id: str, fm_genes: list[str], hugo2entrez: dict[str, int],
                limit: int, *, is_primary: bool) -> list[Finding]:
    scope_root = f"{'study_id' if is_primary else 'dataset'}:{study_id}"
    findings: list[Finding] = []
    sample_list_id = f"{study_id}_all"
    profiles = _get(f"/studies/{urllib.parse.quote(study_id)}/molecular-profiles") or []
    mut_profile_ids = [p["molecularProfileId"] for p in profiles
                       if p.get("molecularAlterationType") == "MUTATION_EXTENDED"]
    if not mut_profile_ids:
        findings.append(Finding("info", "gene.no_mutation_profile", scope_root,
                                "no MUTATION_EXTENDED profile in study — skipping gene checks"))
        return findings
    profile_id = f"{study_id}_mutations"
    if profile_id not in mut_profile_ids:
        profile_id = mut_profile_ids[0]

    for gene in fm_genes[:limit]:
        scope = f"{scope_root}/gene:{gene}"
        entrez = hugo2entrez.get(gene)
        if entrez is None:
            findings.append(Finding("warn", "gene.no_entrez", scope,
                                    f"{gene} not in synced HUGO ontology"))
            continue
        try:
            muts = _post(
                f"/molecular-profiles/{urllib.parse.quote(profile_id)}/mutations/fetch"
                f"?projection=DETAILED",
                {"entrezGeneIds": [entrez], "sampleListId": sample_list_id},
            )
        except urllib.error.HTTPError as e:
            findings.append(Finding("warn", "gene.fetch_failed", scope,
                                    f"{gene}: API error {e.code}"))
            continue
        muts = muts or []
        if not muts:
            findings.append(Finding("warn", "gene.no_mutations", scope,
                                    f"{gene}: 0 mutation records in {profile_id}",
                                    evidence={"profile_id": profile_id}))
            continue
        buckets = {"truncating": 0, "missense": 0, "inframe": 0, "other": 0}
        samples = set()
        for m in muts:
            buckets[_classify(m.get("mutationType", ""))] += 1
            samples.add(m.get("sampleId"))
        parts = [f"{n} {k}" for k, n in buckets.items() if n]
        findings.append(Finding("pass", "gene.mutations", scope,
                                f"{gene}: {len(muts)} records in {len(samples)} samples "
                                f"({', '.join(parts)})",
                                evidence={"profile_id": profile_id,
                                          "n_records": len(muts),
                                          "n_samples": len(samples),
                                          "by_class": buckets}))
    return findings


# ---------- Orchestration ----------

def verify_pmid(pmid: str, *, gene_limit: int, ont: dict,
                hugo2entrez: dict) -> dict:
    fm = load_frontmatter(pmid)
    findings: list[Finding] = []

    study_id = fm.get("study_id")
    datasets = list(fm.get("datasets") or [])
    seen: set[str] = set()
    seq: list[tuple[str, bool]] = []  # (study_id, is_primary)
    if study_id:
        seq.append((study_id, True))
        seen.add(study_id)
    for d in datasets:
        if d and d not in seen:
            seq.append((d, False))
            seen.add(d)

    if not seq:
        findings.append(Finding("info", "study.none_declared", "paper",
                                "no study_id or datasets declared — skipping API study checks"))
    else:
        for sid, is_primary in seq:
            _, study_findings = check_study(sid, fm, is_primary=is_primary)
            findings.extend(study_findings)
            if any(f.code == "study.exists" and f.scope.endswith(sid) for f in study_findings):
                findings.extend(check_panels(sid, fm.get("methods") or [],
                                              ont["gene_panels"], is_primary=is_primary))
                if gene_limit > 0:
                    findings.extend(check_genes(sid, fm.get("genes") or [],
                                                 hugo2entrez, gene_limit,
                                                 is_primary=is_primary))

    findings.extend(check_ontology_sanity(fm, ont))

    return {
        "pmid": str(pmid),
        "title": (fm.get("title") or "").strip(),
        "study_id": study_id,
        "datasets": datasets,
        "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "tallies": _tally(findings),
        "findings": [asdict(f) for f in findings],
    }


def _tally(findings: Iterable[Finding]) -> dict[str, int]:
    out = {s: 0 for s in SEVERITY}
    for f in findings:
        out[f.severity] = out.get(f.severity, 0) + 1
    return out


def render_report(report: dict) -> None:
    print(f"\n{'='*72}\nPMID {report['pmid']} — {report['title'][:60]}")
    last_scope: str | None = None
    for f in report["findings"]:
        if f["scope"] != last_scope:
            print(f"\n[{f['scope']}]")
            last_scope = f["scope"]
        print(f"  {SYMBOL[f['severity']]} {f['message']}")
    print(f"\n  tallies: " + "  ".join(f"{SYMBOL[s]} {report['tallies'][s]}"
                                        for s in SEVERITY))


def render_progress(i: int, n: int, report: dict) -> None:
    t = report["tallies"]
    print(f"[{i:>3}/{n}] {report['pmid']:>10} — "
          f"pass={t['pass']} info={t['info']} warn={t['warn']} fail={t['fail']}")


def discover_pmids() -> list[str]:
    return sorted(p.stem for p in WIKI_PAPERS.glob("*.md") if p.stem.isdigit())


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--pmid", action="append", default=[],
                   help="PMID of a wiki paper page to verify (repeatable).")
    p.add_argument("--all", action="store_true",
                   help="Verify every wiki/papers/{pmid}.md page.")
    p.add_argument("--out-dir", type=Path,
                   help="If set, write per-paper {pmid}.json into this directory.")
    p.add_argument("--gene-limit", type=int, default=0,
                   help="Spot-check this many genes per study with the mutations API "
                        "(slow, default 0).")
    p.add_argument("--corpus", default="cbioportal",
                   help="In --all mode, only verify papers whose frontmatter `corpus:` "
                        "tag matches this value. Use 'all' to disable filtering. "
                        "Default 'cbioportal'.")
    args = p.parse_args()

    if args.all and args.pmid:
        sys.exit("--all is mutually exclusive with --pmid")
    if not args.all and not args.pmid:
        sys.exit("provide --pmid PMID [--pmid PMID ...] or --all")

    pmids = discover_pmids() if args.all else args.pmid
    if args.all and args.corpus != "all":
        pmids = [pmid for pmid in pmids
                 if (load_frontmatter(pmid).get("corpus") or "cbioportal") == args.corpus]
    batch = bool(args.all) or len(pmids) > 5

    if args.out_dir:
        args.out_dir.mkdir(parents=True, exist_ok=True)

    ont = load_ontology()
    hugo2entrez = hugo_to_entrez()

    rc = 0
    n = len(pmids)
    for i, pmid in enumerate(pmids, start=1):
        try:
            report = verify_pmid(pmid, gene_limit=args.gene_limit,
                                  ont=ont, hugo2entrez=hugo2entrez)
        except urllib.error.URLError as e:
            print(f"\n{SYMBOL['fail']} network error verifying PMID {pmid}: {e}")
            rc = 2
            continue
        if args.out_dir:
            (args.out_dir / f"{pmid}.json").write_text(json.dumps(report, indent=2))
        if batch:
            render_progress(i, n, report)
        else:
            render_report(report)
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
