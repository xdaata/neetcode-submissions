from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(rem: int) -> int:
            if rem == 0:
                return 0
            elif rem < 0:
                return float('inf')
            min_coins = float('inf')
            for c in coins:
                res = dfs(rem - c)
                if res != float('inf'):
                    min_coins = min(min_coins, res + 1)
            
            return min_coins


        ans = dfs(amount)
        return ans if ans != float('inf') else -1