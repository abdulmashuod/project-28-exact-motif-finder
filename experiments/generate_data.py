"""Phase 7: reproducible synthetic DNA generation (NO real biological data).

For every dataset write:
  data/generated/<family>/<id>.txt   (or .json) - the sequence + motif
  data/metadata/<id>.json            - seed, family, generation parameters,
                                       motif, n, m, rule description
Use random.Random(seed) (never the global RNG) so runs are reproducible.
Refuse to overwrite existing files unless an explicit --force flag is given.
"""
import argparse


def generate_random_sequence(n: int, seed: int) -> str:
    """TODO (Phase 7): uniform random A/C/G/T of length n."""
    raise NotImplementedError


def generate_motif_rich_sequence(n: int, motif: str, seed: int, **params) -> str:
    """TODO (Phase 7): sequence with many (incl. overlapping) motif occurrences."""
    raise NotImplementedError


def generate_motif_poor_sequence(n: int, motif: str, seed: int, **params) -> str:
    """TODO (Phase 7): sequence with few/no occurrences, by a documented rule."""
    raise NotImplementedError


def main(argv=None) -> int:
    argparse.ArgumentParser(description=__doc__).parse_args(argv)
    print("TODO (Phase 7): data generation not implemented yet.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
