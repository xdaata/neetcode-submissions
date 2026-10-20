class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def base_rob(houses: list[int]) -> int:
            prev1 = 0
            prev2 = 0
            for h in houses:
                curr = max(prev1, prev2 + h)
                prev2 = prev1
                prev1 = curr
            return prev1
        
        return max(base_rob(nums[1:]), base_rob(nums[:-1]))
