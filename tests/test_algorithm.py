"""Phases 3-6: ordinary + personally constructed cases from expected_cases.json.

Expected outputs come from the JSON fixture (hand-derived) - NOT from running
the implementation. Remove the skip marker once find_motifs exists.
"""
import pytest
from motif_finder import find_motifs

PHASE3 = pytest.mark.skip(reason="TODO Phase 3: find_motifs not implemented yet")


@PHASE3
def test_fixture_cases_match_expected(expected_cases):
    for case in expected_cases["cases"]:
        if case["sequence"] is None:      # unfilled personal placeholder
            continue
        result = find_motifs(case["sequence"], case["motif"])
        assert result.positions == case["expected_positions"], case["name"]


@PHASE3
def test_operation_counters_consistent():
    """TODO Phase 4: hand-derive expected comparisons for 2-3 tiny inputs
    (e.g. ATATA / ATA) and assert them here; also positions_examined == n-m+1."""


@PHASE3
def test_matches_agree_with_oracle():
    """TODO Phase 6: compare against oracle_find_all on many small inputs."""
