from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, p in flights:
            adj[u].append((v, p))
        
        min_steps = [float('inf')] * n
        min_heap = [(0, src, 0)]

        while min_heap:
            cost, u, stops = heapq.heappop(min_heap)
            if u == dst:
                return cost
            
            if stops > k or stops >= min_steps[u]:
                continue
            min_steps[u] = stops

            for v, cost_v in adj[u]:
                heapq.heappush(min_heap, (cost_v + cost, v, stops + 1))
        
        return -1        
            