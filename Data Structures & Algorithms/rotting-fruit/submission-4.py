from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))
        fresh = 0
        mins = 0
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0: return 0

        while queue:
            r, c, lvl = queue.popleft()
            mins = max(mins, lvl)
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    fresh -= 1
                    grid[nr][nc] = 2
                    queue.append((nr, nc, lvl + 1))

            
        return mins if fresh == 0 else -1