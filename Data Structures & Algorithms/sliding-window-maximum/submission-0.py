class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        answ = []
        for r in range(k, len(nums) + 1):
            answ.append(max(nums[l:r]))
            l += 1
        return answ        