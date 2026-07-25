class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs, n = {}, len(nums)
        for i in range(n):

            if nums[i] in diffs:
                return [diffs[nums[i]], i]
            
            diffs[target - nums[i]] = i