class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1': return False
        dp = [False] * len(s)
        dp[0] = True
        reachable = 0
        for i in range(minJump, len(s)):
            if i - maxJump > 0 and dp[i - maxJump - 1]:
                reachable -= 1

            if dp[i - minJump]:
                reachable += 1
            
            if s[i] == '0' and reachable:
                dp[i] = True
        return dp[-1]
