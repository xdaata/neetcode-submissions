class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        
        currSum = {0}
        for num in nums:
            currSum |= {s + num for s in currSum if s + num <= target}
            if target in currSum:
                return True
        return False              