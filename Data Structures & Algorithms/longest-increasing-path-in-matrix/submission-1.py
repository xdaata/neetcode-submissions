from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))
        max_path = 0
        @cache
        def dfs(r, c):
            best = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[r][c] < matrix[nr][nc]:
                    best = max(best, 1 + dfs(nr, nc))
            return best

        for r in range(rows):
            for c in range(cols):
                max_path = max(max_path, 1 + dfs(r, c))
        return max_path