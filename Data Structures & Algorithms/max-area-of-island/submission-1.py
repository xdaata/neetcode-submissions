class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(s_r, s_c):
            k = 1
            stack = [(s_r, s_c)]
            grid[s_r][s_c] = 0
            while stack:
                r, c = stack.pop()
                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        stack.append((nr, nc))
                        grid[nr][nc] = 0
                        k += 1
            return k
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area



        