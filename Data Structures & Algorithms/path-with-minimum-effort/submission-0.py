class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0
        min_heap = [(0, 0, 0)]
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while min_heap:
            effort, r, c = heapq.heappop(min_heap)
            if effort > efforts[r][c]:
                continue
            
            if r == rows - 1 and c == cols - 1:
                return effort

            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols:
                    diff = abs(heights[r][c] - heights[nr][nc])
                    next_effort = max(effort, diff)
                    if next_effort < efforts[nr][nc]:
                        efforts[nr][nc] = next_effort
                        heapq.heappush(min_heap, (next_effort, nr, nc))
        
        return 0
