class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1

        for n in nums:
            tmp = currMax * n

            currMax = max(n, tmp, currMin * n)
            currMin = min(n, tmp, currMin * n)

            res = max(res, currMax)

        return res