class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        k_max = 0
        for i in nums:
            curr = i
            curr_k = 1

            while(curr + 1 in nums):
                curr += 1
                curr_k += 1

            k_max = max(k_max, curr_k)


        return k_max
