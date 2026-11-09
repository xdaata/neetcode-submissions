class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i + 1 not in nums:
                return i + 1
        return len(nums) + 1