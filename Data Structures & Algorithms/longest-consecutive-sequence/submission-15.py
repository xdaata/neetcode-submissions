class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        k_max = 0
        nums_s = set(nums)
        for i in nums_s:
            if i - 1 not in nums_s:
                curr = i
                curr_k = 1

                while curr + 1 in nums_s:
                    curr += 1
                    curr_k += 1

                k_max = max(k_max, curr_k)


        return k_max
