"""Regression tests for the PMID → PMCID elink resolver.

`elink_pubmed_to_pmc` must request the `pubmed_pmc` linkname (the PMC record
of the paper) rather than default behaviour, which also returns
`pubmed_pmc_refs` (PMC records citing the paper). Selecting the wrong block
causes the resolver to return a citing paper's PMCID for PMIDs not in PMC.
"""
from __future__ import annotations

from unittest.mock import MagicMock, patch

from cbio_kb.ingest import pmid2pmcid


def _biopython_payload(pubmed_pmc_id, include_refs=True):
    """Shape mirrors Bio.Entrez.read() output for elink XML."""
    linksetdbs = []
    if pubmed_pmc_id is not None:
        linksetdbs.append({
            "DbTo": "pmc",
            "LinkName": "pubmed_pmc",
            "Link": [{"Id": pubmed_pmc_id}] if pubmed_pmc_id else [],
        })
    if include_refs:
        linksetdbs.append({
            "DbTo": "pmc",
            "LinkName": "pubmed_pmc_refs",
            "Link": [{"Id": "13013432"}, {"Id": "13024878"}],
        })
    return [{"LinkSetDb": linksetdbs}]


def _fake_entrez(read_return):
    fake = MagicMock()
    fake.elink.return_value = MagicMock()
    fake.read.return_value = read_return
    return fake


def test_picks_pubmed_pmc_over_refs(monkeypatch):
    fake = _fake_entrez(_biopython_payload("5059467", include_refs=True))
    monkeypatch.setattr(pmid2pmcid, "Entrez", fake)

    assert pmid2pmcid.elink_pubmed_to_pmc(
        "27698471", email="t@example.org", api_key=None,
    ) == "PMC5059467"

    kwargs = fake.elink.call_args.kwargs
    assert kwargs.get("linkname") == "pubmed_pmc"


def test_returns_empty_when_only_refs_present(monkeypatch):
    # PMID 32946775 pattern: paper not in PMC; only citing papers returned.
    fake = _fake_entrez(_biopython_payload(None, include_refs=True))
    monkeypatch.setattr(pmid2pmcid, "Entrez", fake)

    assert pmid2pmcid.elink_pubmed_to_pmc(
        "32946775", email="t@example.org", api_key=None,
    ) == ""


def test_returns_empty_when_pubmed_pmc_block_empty(monkeypatch):
    fake = _fake_entrez(_biopython_payload("", include_refs=True))
    monkeypatch.setattr(pmid2pmcid, "Entrez", fake)

    assert pmid2pmcid.elink_pubmed_to_pmc(
        "99999999", email="t@example.org", api_key=None,
    ) == ""


def test_requests_fallback_filters_by_linkname(monkeypatch):
    # Biopython absent → fallback path. Put pubmed_pmc_refs FIRST to prove
    # filtering (not ordering) is what selects the right block.
    monkeypatch.setattr(pmid2pmcid, "Entrez", None)

    fake_resp = MagicMock()
    fake_resp.raise_for_status.return_value = None
    fake_resp.json.return_value = {
        "linksets": [{
            "linksetdbs": [
                {"linkname": "pubmed_pmc_refs", "links": [13013432]},
                {"linkname": "pubmed_pmc", "links": [5059467]},
            ],
        }],
    }
    with patch("cbio_kb.ingest.pmid2pmcid.requests.get",
               return_value=fake_resp) as fake_get:
        out = pmid2pmcid.elink_pubmed_to_pmc(
            "27698471", email="t@example.org", api_key="k",
        )

    assert out == "PMC5059467"
    params = fake_get.call_args.kwargs["params"]
    assert params["linkname"] == "pubmed_pmc"
    assert params["api_key"] == "k"
