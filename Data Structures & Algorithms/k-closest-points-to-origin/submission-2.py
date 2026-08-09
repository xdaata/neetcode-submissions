class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for p in points:
            dist = p[0]**2 + p[1]**2
            heapq.heappush(max_heap, (-dist, p))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [p for d, p in max_heap]    