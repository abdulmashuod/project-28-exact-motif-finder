"""Phase 8: run the assessed algorithm over generated data.

Per run: call find_motifs, compare positions with the oracle, record
n, m, family, seed, comparisons, positions_examined, matches, correct(bool).
Save to a NEW timestamped file in results/raw/ (never overwrite old raw data).
Timing (secondary, optional): time.perf_counter(), 1 warm-up, 5 runs, median;
record Python version + machine details. Timing code lives HERE, not in the
algorithm. Operation counts are the primary evidence.
"""
import argparse


def main(argv=None) -> int:
    argparse.ArgumentParser(description=__doc__).parse_args(argv)
    print("TODO (Phase 8): experiment runner not implemented yet.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
