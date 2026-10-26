"""Reconstruct one strictly increasing subsequence, O(n log n)."""
from bisect import bisect_left

def longest_increasing_subsequence(a):
 tails=[];values=[];prev=[-1]*len(a)
 for i,x in enumerate(a):
  j=bisect_left(values,x)
  if j:prev[i]=tails[j-1]
  if j==len(tails):tails.append(i);values.append(x)
  else:tails[j]=i;values[j]=x
 if not tails:return []
 out=[];i=tails[-1]
 while i>=0:out.append(a[i]);i=prev[i]
 return out[::-1]
