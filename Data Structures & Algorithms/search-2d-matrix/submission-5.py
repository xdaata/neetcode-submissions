class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        mm = 0
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][-1] < target:
                left = mid + 1
            else:
                mm = mid
                break

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[mm][m] > target:
                r = m - 1
            elif matrix[mm][m] < target:
                l = m + 1
            else:
                return True
        return False        