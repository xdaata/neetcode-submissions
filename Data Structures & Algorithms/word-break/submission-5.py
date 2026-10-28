from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dfs(idx):
            if idx == len(s):
                return True

            result = False
            for w in wordDict:
                offset = len(w)
                if s[idx:idx + offset] == w:
                    result = result or dfs(idx + offset)
            
            return result

        return dfs(0)
