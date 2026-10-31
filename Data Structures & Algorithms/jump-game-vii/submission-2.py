class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1': return False

        dp = [False] * len(s)
        dp[0] = True
        reachable = 0

        for i in range(minJump, len(s)):
            reachable += dp[i - minJump]

            if i > maxJump:
                reachable -= dp[i - maxJump - 1]
            
            if s[i] == '0' and reachable > 0:
                dp[i] = True
        
        return dp[-1]