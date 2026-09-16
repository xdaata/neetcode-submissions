class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums: return 0
        def dfs(i, sum_):
            if i == len(nums): return sum_

            return dfs(i + 1, sum_ ^ nums[i]) + dfs(i + 1, sum_)

        return dfs(0, 0)

