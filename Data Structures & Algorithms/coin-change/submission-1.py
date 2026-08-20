from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dfs(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')
            
            min_coins = float('inf')
            for coin in coins:
                min_coins = min(min_coins, 1 + dfs(rem - coin))

            return min_coins

        res = dfs(amount)
        return res if res != float('inf') else -1

        
        