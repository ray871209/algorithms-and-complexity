import unittest,random
from sorting.algorithms import insertion_sort,merge_sort,hybrid_sort
from searching.algorithms import binary_search,predecessor,successor,range_query,range_count
from graphs.bfs import distances,shortest_path
from dynamic_programming.lis import longest_increasing_subsequence
class Tests(unittest.TestCase):
 def test_sorts(self):
  rng=random.Random(8)
  for n in (0,1,2,25,26,100):
   a=[rng.randrange(-10,10) for _ in range(n)]
   for fn in (insertion_sort,merge_sort,hybrid_sort):self.assertEqual(fn(a),sorted(a))
 def test_threshold(self):
  with self.assertRaises(ValueError):hybrid_sort([2,1],0)
 def test_search(self):
  a=[-2,1,1,4,9]
  self.assertEqual(binary_search(a,1),1)
  self.assertEqual(binary_search(a,3),-1)
  self.assertEqual(predecessor(a,3),1)
  self.assertEqual(successor(a,3),4)
  self.assertIsNone(predecessor(a,-3))
  self.assertIsNone(successor(a,10))
 def test_range(self):
  a=[1,1,2,4,5]
  self.assertEqual(range_query(a,1,4),[1,1,2,4])
  self.assertEqual(range_count(a,1,4),4)
  with self.assertRaises(ValueError):range_query(a,4,1)
 def test_graph(self):
  g={'a':['b','c'],'b':['d'],'c':['d'],'d':[],'x':[]}
  self.assertEqual(distances(g,'a'),{'a':0,'b':1,'c':1,'d':2})
  self.assertEqual(shortest_path(g,'a','d'),['a','b','d'])
  self.assertIsNone(shortest_path(g,'a','x'))
 def test_lis(self):
  rng=random.Random(6)
  for _ in range(100):
   a=[rng.randrange(-20,20) for _ in range(rng.randrange(35))]
   dp=[1]*len(a)
   for i in range(len(a)):
    for j in range(i):
     if a[j]<a[i]:dp[i]=max(dp[i],dp[j]+1)
   seq=longest_increasing_subsequence(a)
   self.assertEqual(len(seq),max(dp,default=0))
   self.assertTrue(all(x<y for x,y in zip(seq,seq[1:])))
