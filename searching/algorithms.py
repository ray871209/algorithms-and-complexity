"""Queries on pre-sorted sequences."""
from bisect import bisect_left,bisect_right

def binary_search(a,x):
 i=bisect_left(a,x)
 return i if i<len(a) and a[i]==x else -1

def predecessor(a,x):
 i=bisect_right(a,x)
 return a[i-1] if i else None

def successor(a,x):
 i=bisect_left(a,x)
 return a[i] if i<len(a) else None

def range_query(a,lo,hi):
 if lo>hi:raise ValueError('invalid range')
 return list(a[bisect_left(a,lo):bisect_right(a,hi)])

def range_count(a,lo,hi):
 if lo>hi:raise ValueError('invalid range')
 return bisect_right(a,hi)-bisect_left(a,lo)
