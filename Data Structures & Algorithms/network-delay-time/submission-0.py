import heapq 
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w))
        min_heap = [(0, k)]
        visited = {}
        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited[node] = time
            for neigh, w in adj_list[node]:
                if neigh not in visited:
                    heapq.heappush(min_heap, (time + w, neigh))
        
        if len(visited) == n:
            return max(visited.values())
        return -1


        