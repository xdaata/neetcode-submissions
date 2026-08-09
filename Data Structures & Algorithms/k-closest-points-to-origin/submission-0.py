class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_n_point = []
        for p in points:
            dist = p[0]**2 + p[1]**2
            dist_n_point.append([dist, p[0], p[1]])
        heapq.heapify(dist_n_point)
        answ = []
        while k:
            answ.append(heapq.heappop(dist_n_point)[1:])
            k -= 1
        return answ        