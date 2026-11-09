"""Phase 2 tests. Remove the skip markers when validation is implemented."""
import pytest
from motif_finder import validate_sequence, validate_motif, ValidationError


def test_valid_sequence_accepted():
    validate_sequence("ACGT")           # must not raise


def test_empty_sequence_is_valid():
    validate_sequence("")               # proposed contract: valid


@pytest.mark.parametrize("bad", ["ACXT", "acgt", "AC GT", "ACG1"])
def test_invalid_sequence_rejected(bad):
    with pytest.raises(ValidationError):
        validate_sequence(bad)


@pytest.mark.parametrize("bad", ["", "AN", "a"])
def test_invalid_motif_rejected(bad):
    with pytest.raises(ValidationError):
        validate_motif(bad)
