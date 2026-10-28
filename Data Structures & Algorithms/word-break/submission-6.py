class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s) + 1):
            for w in wordDict:
                offset = len(w)
                if dp[i] and i + offset <= len(s):
                    dp[i + offset] = dp[i + offset] or (dp[i] and s[i:i + offset] == w)
        
        print(dp)
        return dp[-1]
