from cbio_kb.ingest.seed import build_rows


def test_build_rows_splits_dedupes_and_sorts():
    studies = [
        {"studyId": "meso_tcga", "pmid": "29625048,29596782, 29625048"},
        {"studyId": "alk_msk_2026", "pmid": None},
        {"studyId": "brca_msk_2025", "pmid": "40379787"},
        {"studyId": "odd", "pmid": "PMC123;  "},
    ]
    assert build_rows(studies) == [
        ("brca_msk_2025", "40379787"),
        ("meso_tcga", "29596782"),
        ("meso_tcga", "29625048"),
    ]
