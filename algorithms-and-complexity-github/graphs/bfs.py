"""BFS for unweighted adjacency-list graphs."""
from collections import deque

def distances(g,start):
 d={start:0};q=deque([start])
 while q:
  u=q.popleft()
  for v in g.get(u,[]):
   if v not in d:d[v]=d[u]+1;q.append(v)
 return d

def shortest_path(g,start,goal):
 parent={start:None};q=deque([start])
 while q:
  u=q.popleft()
  if u==goal:
   result=[]
   while u is not None:result.append(u);u=parent[u]
   return result[::-1]
  for v in g.get(u,[]):
   if v not in parent:parent[v]=u;q.append(v)
 return None
