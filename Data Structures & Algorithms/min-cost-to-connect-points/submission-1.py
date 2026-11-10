import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        h = [(0, 0)]
        n = len(points)
        visited = set()
        total_cost = 0
        while len(visited) < n:
            cost, u = heapq.heappop(h)
            if u in visited:
                continue
            visited.add(u)
            total_cost += cost
            x1, y1 = points[u]
            for v in range(n):
                x2, y2 = points[v]
                dist = abs(x2 - x1) + abs(y2 - y1)
                heapq.heappush(h, (dist, v))
        return total_cost
