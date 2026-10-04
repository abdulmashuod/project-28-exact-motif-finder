"""Skeleton smoke test: the package imports and exposes its public API."""
import motif_finder


def test_public_api_importable():
    for name in ("find_motifs", "trace_search", "validate_sequence", "validate_motif"):
        assert hasattr(motif_finder, name)
