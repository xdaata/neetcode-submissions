class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k_max = k = 0
        for n in nums:
            if n == 1:
                k += 1
                k_max = max(k, k_max)
            else:
                k = 0
        return k_max
