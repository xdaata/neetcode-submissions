class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1: return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0]) 
        dp = [[0]*n for i in range(m)]
        dp[0][0] = 1
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c]:
                    dp[r][c] = 0
                    continue
                if r > 0:
                    dp[r][c] += dp[r - 1][c]
                if c > 0:
                    dp[r][c] += dp[r][c - 1]

        
        return dp[m - 1][n - 1]
