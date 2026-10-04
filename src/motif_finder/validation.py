"""Input validation. Runs BEFORE matching; the algorithm never sees bad input.

Contract (proposed - confirm with instructor, see docs/course_specification.md):
  * sequence: str of uppercase A, C, G, T only. The EMPTY sequence is valid
    (it simply contains no occurrences).
  * motif: non-empty str of uppercase A, C, G, T only.
  * Lowercase is rejected (not silently converted).
"""

VALID_BASES = frozenset("ACGT")


class ValidationError(ValueError):
    """Raised when a sequence or motif violates the input contract."""


def validate_sequence(sequence: str) -> None:
    """Raise ValidationError if `sequence` contains anything but A/C/G/T.

    TODO (Phase 2): implement. Error message should name the offending
    character and its zero-based index.
    """
    raise NotImplementedError("Phase 2: implement validate_sequence")


def validate_motif(motif: str) -> None:
    """Raise ValidationError if `motif` is empty or contains non-A/C/G/T chars.

    TODO (Phase 2): implement.
    """
    raise NotImplementedError("Phase 2: implement validate_motif")
