class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            area = r - l
            if height[l] < height[r]:
                area *= height[l]
                l += 1
            else:
                area *= height[r]
                r -= 1

            if area > max_area:
                max_area = area

        return max_area