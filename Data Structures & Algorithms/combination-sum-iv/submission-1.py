from functools import cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @cache
        def dfs(sum_):
            if sum_ == target:
                return 1

            if sum_ > target:
                return 0

            res = 0
            for n in nums:
                res += dfs(sum_ + n)
            return res

        return dfs(0)