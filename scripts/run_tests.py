"""Run the whole test suite: python scripts/run_tests.py [pytest args]"""
import sys
import pytest

if __name__ == "__main__":
    raise SystemExit(pytest.main(sys.argv[1:] or ["-v"]))
