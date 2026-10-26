"""Dijkstra shortest paths for directed, non-negative weighted adjacency lists."""
from heapq import heappop, heappush
from math import inf

def shortest_distances(graph, source):
    for edges in graph.values():
        for neighbor, weight in edges:
            if not isinstance(weight, (int, float)) or weight < 0 or weight == inf or weight != weight:
                raise ValueError("Edge weights must be finite and non-negative")
    best = {source: 0}
    queue = [(0, source)]
    while queue:
        distance, node = heappop(queue)
        if distance != best[node]:
            continue
        for neighbor, weight in graph.get(node, ()):
            candidate = distance + weight
            if candidate < best.get(neighbor, inf):
                best[neighbor] = candidate
                heappush(queue, (candidate, neighbor))
    return best
