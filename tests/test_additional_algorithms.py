import unittest
from graphs.dijkstra import shortest_distances
from sorting.counting_sort import counting_sort

class AdditionalAlgorithmTests(unittest.TestCase):
    def test_dijkstra(self):
        graph = {"a": [("b", 4), ("c", 1)],
                 "c": [("b", 2)], "b": [("d", 1)]}
        self.assertEqual(shortest_distances(graph, "a"), {"a":0, "c":1, "b":3, "d":4})

    def test_dijkstra_reject_negative(self):
        with self.assertRaises(ValueError):
            shortest_distances({"a":[("b",-2)]}, "a")

    def test_counting_sort(self):
        self.assertEqual(counting_sort([3,1,2,1,0]), [0,1,1,2,3])
        self.assertEqual(counting_sort([]), [])

    def test_counting_sort_validation(self):
        with self.assertRaises(ValueError):
            counting_sort([-1])
        with self.assertRaises(ValueError):
            counting_sort([1.2])

if __name__ == "__main__":
    unittest.main()
