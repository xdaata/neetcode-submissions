class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = float('-inf')
        sold = 0
        for p in prices:
            hold = max(hold, sold - p)
            sold = max(sold, hold + p)
        return sold