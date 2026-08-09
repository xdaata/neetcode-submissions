class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_n_point = []
        for p in points:
            dist = p[0]**2 + p[1]**2
            dist_n_point.append((dist, p))

        heapq.heapify(dist_n_point)
        
        answ = []
        for _ in range(k):
            _, p = heapq.heappop(dist_n_point)
            answ.append(p)
        return answ        