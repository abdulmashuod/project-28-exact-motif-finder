# Project 28 - Exact Motif Finder in Synthetic DNA

| | |
|---|---|
| **Course** | CS-251 Design and Analysis of Algorithms (NUST / SINES) |
| **Instructor** | Dr. Umer Asgher |
| **Project ID** | 28 |
| **Student name** | [Abdul Mashuod] |
| **Student ID** | [530836] |
| **Group member (max 2)** | [One-man Army] |
| **Python version** | [python 3] |
| **GitHub repository** | [https://github.com/abdulmashuod/project-28-exact-motif-finder] |

> **Status: Phase 1 (skeleton).** The algorithm, validation, tracing, data
> generation and experiments are **not implemented yet**. Every unfinished
> function raises `NotImplementedError` and carries a TODO naming its phase.
> No experimental results exist yet.

## Problem statement
Given an uppercase DNA sequence (A, C, G, T only) and a non-empty motif, report
**every exact occurrence** of the motif, including overlapping ones, as
zero-based start positions. Invalid input is rejected; a motif longer than the
sequence yields no matches.

## Bioinformatics context
DNA is written in the alphabet A (adenine), C (cytosine), G (guanine),
T (thymine). Locating short patterns ("motifs") in a sequence is a basic
sequence-analysis task. This is an **educational algorithms project on
synthetic data**; it makes no biological predictions and uses no real or
personal data.

## Algorithm
Naive exact matching, implemented from scratch in `src/motif_finder/algorithm.py`:
for every start position, compare motif and DNA character by character, count
every comparison, record the start if all characters match, then continue
(so overlaps are found). No `str.find`, regex or search libraries.

## Input / output
- Input: `sequence: str`, `motif: str`
- Output: `MatchResult` with `positions`, `comparisons`, `positions_examined`,
  `sequence_length`, `motif_length` (and `matches_found`)

## Example
```
DNA:   ATATA
Motif: ATA
Output: [0, 2]
```

## Complexity (n = sequence length, m = motif length)
Worst case O(nm) time. Best case, expected behaviour and auxiliary space are to
be derived and documented in `docs/report/02_design.md`. Complexity comes from
analysis; experiments only support it.

## Repository structure
```
src/motif_finder/   core: algorithm, validation, models, oracle, tracing
experiments/        data generation, experiment runner, analysis, config.json
data/               hand_created/, generated/{random,motif_rich,motif_poor}/, expected/, metadata/
tests/              unit + edge-case tests, fixtures/expected_cases.json
results/            raw/, processed/, tables/, figures/, traces/
docs/               course_specification, report/, presentation/, development/, decisions/
ui/                 future interface boundary (not implemented)
scripts/            thin command-line wrappers
```
Layering: `UI -> core API -> data/results`. The core never imports experiments,
plotting, timing or UI code; the oracle is used only by tests/experiments.

## Installation
```bash
git clone <https://github.com/abdulmashuod/project-28-exact-motif-finder>
cd project-28-exact-motif-finder
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
pip install -r requirements.txt
```

## Running
```bash
python -m pytest -v                  # or: python scripts/run_tests.py
python scripts/generate_datasets.py  # Phase 7 (placeholder now)
python scripts/run_experiments.py    # Phase 8 (placeholder now)
python scripts/generate_results.py   # Phase 9 (placeholder now)
```
Running the algorithm from the command line: TODO (Phase 3 - small CLI/demo).

## Reproducing results
TODO (Phase 14): list exact commands, seed (`experiments/config.json`),
Python version and machine details.

## Future interactive UI
See `ui/README.md`. Planned for Phase 13; it will only use the core public API.

## Limitations
TODO (fill honestly as the project develops): synthetic data only; DNA
alphabet only; exact matching only; timing is secondary and machine-dependent.

## Academic integrity / acknowledgement
TODO: describe permitted assistance used (e.g. AI tools for scaffolding), what
you wrote and understand yourself, sources, and your individual contribution
(hand-made dataset, generated dataset, design decision, stress case, log).
You must be able to explain every line in the viva.
