# Algorithm complexity reference

These are independent technical notes, not assessment solutions.

| Algorithm | Time | Space (additional) | Preconditions |
|---|---|---|---|
| Insertion sort | O(n²) worst, O(n) best | O(1) typical | None |
| Merge sort | O(n log n) | O(n) | None |
| Hybrid merge/insertion | O(n log n) worst | O(n) | Fixed cutoff |
| Binary search | O(log n) | O(1) iterative | Sorted data |
| Predecessor/successor | O(log n) | Implementation-specific | Sorted data |
| Range reporting | O(log n + k) | O(k) output | Sorted data |
| Breadth-first search | O(V + E) | O(V) | Adjacency list |
| Longest increasing subsequence | O(n log n) | O(n) | Strict version |

## Reading benchmark results
Empirical runtime depends on Python version, machine, input distribution, data copying, and timing noise. Repeat trials and disclose conditions. Timings are not a proof of Big-O complexity.

## Distinct forms of evidence
A mathematical analysis establishes a bound; unit tests check selected behaviors; benchmarks measure observed timing. Each provides different evidence.
