class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1: return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0]) 
        dp = [0]*n
        dp[0] = 1
        for row in obstacleGrid:
            for c in range(n):
                if row[c] == 1:
                    dp[c] = 0
                elif c > 0:
                    dp[c] += dp[c - 1]
                    
        return dp[-1]
