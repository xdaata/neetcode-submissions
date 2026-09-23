class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    p += 4

                    if c > 0 and grid[r][c - 1]:
                        p -= 2
                    
                    if r > 0 and grid[r - 1][c]:
                        p -= 2

        return p
