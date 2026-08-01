class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        n = len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] > target and matrix[mid][n] > target:
                right = mid - 1
            
            elif matrix[mid][0] < target and matrix[mid][n] < target:
                left = mid + 1
            else:
                return target in matrix[mid]
        return False        