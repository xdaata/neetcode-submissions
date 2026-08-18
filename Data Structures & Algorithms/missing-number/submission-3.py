class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        nums.append(-1)
        for i in range(len(nums) + 1):
            if i ^ nums[i]:
                return i
        return 0       