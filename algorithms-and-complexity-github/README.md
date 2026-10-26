# Algorithms & Complexity (Python)

Portfolio adaptations of general topics studied in COMP90038 Algorithms and Complexity at the University of Melbourne (2024): sorting, search, BFS and dynamic programming. These are **new AI-assisted implementations**, not reproductions of assessed answers, institutional problem sheets or another student's solutions.

## Contents
- `sorting/algorithms.py`: insertion sort O(n²) worst-case; merge and hybrid sort O(n log n) worst-case.
- `searching/algorithms.py`: binary search, predecessor/successor, and inclusive range query. Sorted input required: O(log n) lookup, O(log n + k) for range output.
- `graphs/bfs.py`: BFS distance and shortest path for unweighted adjacency lists, O(V+E).
- `dynamic_programming/lis.py`: longest strictly increasing subsequence, O(n log n).
- `benchmarks/benchmark.py`: synthetic, reproducible sorting time comparison with CSV output.

## Run

Python 3.10+, standard library only:

```bash
python -m unittest discover -s tests -v
python benchmarks/benchmark.py
```

Run from repository root. Sorting benchmark times are machine- and input-dependent, not universal speed guarantees. Sample results are included under `benchmarks/example_results.csv`.

## Provenance and sharing

Inspired by COMP90038 topics; all demonstration code and tests were created later with AI assistance. The source course documents include assessment prompts and solutions which are **not redistributed**. No personally identifying student details are included. Before setting Public, check course sharing restrictions.
