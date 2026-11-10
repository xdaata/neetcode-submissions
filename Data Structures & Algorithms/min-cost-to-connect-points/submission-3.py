class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        visited = [False] * n
        total_cost = 0
        for _ in range(n):
            u = -1
            for i in range(n):
                if not visited[i] and (u == -1 or min_dist[i] < min_dist[u]):
                    u = i
            visited[u] = True
            total_cost += min_dist[u]
            x1, y1 = points[u]
            for v in range(n):
                x2, y2 = points[v]
                dist = abs(x2 - x1) + abs(y2 - y1)
                if not visited[v] and dist < min_dist[v]:
                    min_dist[v] = dist
        return total_cost
