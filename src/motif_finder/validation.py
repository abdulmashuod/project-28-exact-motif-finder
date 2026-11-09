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
    """Raise ValidationError if `sequence` contains anything but A/C/G/T."""
    for index, char in enumerate(sequence):
        if char not in VALID_BASES:
            raise ValidationError(f"character {char!r} at position {index} is invalid")


def validate_motif(motif: str) -> None:
    """Raise ValidationError if `motif` is empty or contains non-A/C/G/T chars."""
    if len(motif) == 0:
        raise ValidationError("motif must not be empty")
    for index, char in enumerate(motif):
        if char not in VALID_BASES:
            raise ValidationError(f"character {char!r} at position {index} is invalid")
