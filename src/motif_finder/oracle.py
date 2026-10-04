"""Trusted, SIMPLE correctness oracle - used ONLY by tests and experiments.

It is deliberately independent of algorithm.py and must never be imported by
it. Its work is never counted as algorithm operations.
Allowed here (unlike the assessed algorithm): a different, obviously-correct
method, e.g. comparing sequence[i:i+m] == motif for each i.
"""


def oracle_find_all(sequence: str, motif: str) -> list[int]:
    """Return all zero-based start positions of `motif` in `sequence`
    (overlaps included) using a different, simple method.

    TODO (Phase 6): implement. Assumes inputs are already validated.
    """
    raise NotImplementedError("Phase 6: implement oracle_find_all")
