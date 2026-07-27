class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_am = 0
        while l < r:
            max_am = max(max_am, min(heights[l], heights[r]) * (r - l))
            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            else:
                l += 1
        return max_am