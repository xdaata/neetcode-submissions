import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        min_heap = [(grid[0][0], 0, 0)]
        rows, cols = len(grid), len(grid[0])
        visited = {(0, 0)}
        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))

        while min_heap:
            cost, r, c = heapq.heappop(min_heap)

            if r == rows - 1 and c == cols - 1:
                return cost

            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(min_heap, (max(cost, grid[nr][nc]), nr, nc))
        
                    
