"""Sync canonical ontologies from cBioPortal + OncoTree.

Writes machine-readable JSON under schema/ontology/ that the agents and the
linter validate against. Stdlib only — no extra deps.
"""
from __future__ import annotations

import json
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

CBIO = "https://www.cbioportal.org/api"
ONCOTREE = "http://oncotree.mskcc.org/api/tumorTypes"


def _get(url: str, timeout: int = 120):
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def fetch_genes() -> list[dict]:
    return _get(f"{CBIO}/genes?pageSize=100000&projection=SUMMARY")


def fetch_studies() -> list[dict]:
    return _get(f"{CBIO}/studies?pageSize=10000&projection=SUMMARY")


def fetch_cancer_types() -> list[dict]:
    return _get(f"{CBIO}/cancer-types?pageSize=10000")


def fetch_gene_panels() -> list[dict]:
    return _get(f"{CBIO}/gene-panels?pageSize=10000&projection=SUMMARY")


def fetch_oncotree() -> list[dict]:
    return _get(ONCOTREE)


def fetch_molecular_profiles() -> list[dict]:
    return _get(f"{CBIO}/molecular-profiles?pageSize=10000")


def fetch_clinical_attributes() -> list[dict]:
    data = _get(f"{CBIO}/clinical-attributes?pageSize=100000")
    from collections import Counter
    counts = Counter(a["clinicalAttributeId"] for a in data)
    
    # Keep only IDs present in more than one study (Global/Standardized)
    global_ids = {aid for aid, count in counts.items() if count > 1}
    
    # Deduplicate: Keep only the first study's definition for each global ID
    seen = set()
    filtered = []
    for a in data:
        aid = a["clinicalAttributeId"]
        if aid in global_ids and aid not in seen:
            filtered.append(a)
            seen.add(aid)
            
    # Sort for deterministic output
    return sorted(filtered, key=lambda x: x["clinicalAttributeId"])


SOURCES = [
    ("genes", fetch_genes, "hugoGeneSymbol"),
    ("studies", fetch_studies, "studyId"),
    ("cancer_types", fetch_cancer_types, "cancerTypeId"),
    ("gene_panels", fetch_gene_panels, "genePanelId"),
    ("oncotree", fetch_oncotree, "code"),
    ("molecular_profiles", fetch_molecular_profiles, "molecularAlterationType"),
    ("clinical_attributes", fetch_clinical_attributes, "clinicalAttributeId"),
]


def run(out_dir: Path) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    log = {
        "synced_at": datetime.now(timezone.utc).isoformat(),
        "sources": {},
    }
    rc = 0
    for name, fn, key in SOURCES:
        try:
            data = fn()
            (out_dir / f"{name}.json").write_text(json.dumps(data, separators=(",", ":")))
            log["sources"][name] = {"count": len(data), "key": key, "ok": True}
            print(f"[ok] {name}: {len(data)} entries")
        except Exception as e:
            log["sources"][name] = {"ok": False, "error": str(e)}
            print(f"[fail] {name}: {e}")
            rc = 1
    (out_dir / "sync_log.json").write_text(json.dumps(log, indent=2))
    return rc
