from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        ans = max_k
        l, r = 1, max_k
        while l <= r:
            m = (l + r) // 2
            total_h = 0

            for p in piles:
                total_h += ceil(p / m)

            if total_h <= h:
                ans = min(ans, m)
                r = m - 1
            else:
                l = m + 1

        return ans

        