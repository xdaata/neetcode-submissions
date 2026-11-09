class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                trgt = nums[i] - 1
                nums[trgt], nums[i] = nums[i], nums[trgt]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1