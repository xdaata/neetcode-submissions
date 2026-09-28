class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for r in range(m):
            for c in range(n):
                if c > 0:
                    dp[r][c] = min(dp[r][c], dp[r][c - 1] + grid[r][c])
                if r > 0:
                    dp[r][c] = min(dp[r][c], dp[r - 1][c] + grid[r][c])
        
        return int(dp[m - 1][n - 1])

        