class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = 0
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                res = m + 1
                l = m + 1
            elif nums[m] > target:
                res = m
                r = m - 1
            else:
                return m
        return res      