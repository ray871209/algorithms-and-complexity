"""Sorting robustness tests: independent portfolio examples."""
import random
import unittest
from sorting.algorithms import insertion_sort, merge_sort, hybrid_sort

class SortingEdgeTests(unittest.TestCase):
    def test_empty_and_singleton(self):
        for algorithm in (insertion_sort, merge_sort, hybrid_sort):
            self.assertEqual(algorithm([]), [])
            self.assertEqual(algorithm([3]), [3])

    def test_duplicates_and_negative_values(self):
        values = [-3, 0, 5, -3, 5, 2, 2]
        for algorithm in (insertion_sort, merge_sort, hybrid_sort):
            self.assertEqual(algorithm(values), sorted(values))

    def test_seeded_randomized_cases(self):
        rng = random.Random(2026)
        for size in (0, 1, 2, 7, 24, 25, 50):
            values = [rng.randint(-50, 50) for _ in range(size)]
            for algorithm in (insertion_sort, merge_sort, hybrid_sort):
                with self.subTest(size=size, algorithm=algorithm.__name__):
                    original = values[:]
                    self.assertEqual(algorithm(values), sorted(values))
                    self.assertEqual(values, original)

    def test_hybrid_threshold_validation(self):
        with self.assertRaises(ValueError):
            hybrid_sort([1,2], threshold=0)

if __name__ == "__main__":
    unittest.main()
