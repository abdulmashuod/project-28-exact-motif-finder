"""Phases 3-6: ordinary + personally constructed cases from expected_cases.json.

Expected outputs come from the JSON fixture (hand-derived) - NOT from running
the implementation. Remove the skip marker once find_motifs exists.
"""
import pytest
from motif_finder import find_motifs

PHASE6 = pytest.mark.skip(reason="TODO Phase 6: oracle not implemented yet")



def test_fixture_cases_match_expected(expected_cases):
    for case in expected_cases["cases"]:
        if case["sequence"] is None:      # unfilled personal placeholder
            continue
        result = find_motifs(case["sequence"], case["motif"])
        assert result.positions == case["expected_positions"], case["name"]


def test_operation_counters_consistent():
    # (sequence, motif, positions, comparisons, positions_examined)
    cases = [
        ("ATATA", "ATA", [0, 2], 7, 3),
        ("ACGT", "TT", [], 3, 3),
        ("AAAA", "AA", [0, 1, 2], 6, 3),
    ]
    for sequence, motif, positions, comparisons, examined in cases:
        result = find_motifs(sequence, motif)
        assert result.positions == positions
        assert result.comparisons == comparisons
        assert result.positions_examined == examined
        assert result.positions_examined == len(sequence) - len(motif) + 1


def test_motif_longer_than_sequence_has_zero_counts():
    result = find_motifs("ACG", "ACGT")
    assert result.positions == []
    assert result.comparisons == 0
    assert result.positions_examined == 0


@PHASE6
def test_matches_agree_with_oracle():
    """TODO Phase 6: compare against oracle_find_all on many small inputs."""
