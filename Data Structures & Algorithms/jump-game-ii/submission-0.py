class Solution:
    def jump(self, nums: List[int]) -> int:
        k = 0
        l = 0
        r = 0
        best = 0
        while l < len(nums) - 1 and r < len(nums) - 1:
            for i in range(l, r + 1):
                if i < len(nums) - 1:
                    best = max(best, i + nums[i])
            l = r + 1
            r = best
            k += 1

        return k