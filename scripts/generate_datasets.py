"""Thin command-line wrapper: python scripts/generate_datasets.py [options]"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT))

from experiments.generate_data import main

if __name__ == "__main__":
    raise SystemExit(main())
