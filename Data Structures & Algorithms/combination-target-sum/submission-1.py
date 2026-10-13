class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start: int, path: list[int], curr_sum: int) -> None:
            if curr_sum == target:
                res.append(path[:])
                return

            for i in range(start, len(nums)):
                if curr_sum + nums[i] <= target:
                    path.append(nums[i])
                    backtrack(i, path, curr_sum + nums[i])
                    path.pop()
        
        backtrack(0, [], 0)
        return res
