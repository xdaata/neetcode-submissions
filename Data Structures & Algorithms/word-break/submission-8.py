class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            if not dp[i]:
                continue

            for w in wordDict:
                offset = len(w)
                if i + offset <= len(s) and s[i:i + offset] == w:
                    dp[i + offset] = True
        
        return dp[len(s)]
