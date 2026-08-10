class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(start, subset):
            res.append(subset.copy())
            for j in range(start, len(nums)):
                if j > start and nums[j] == nums[j - 1]:
                    continue

                subset.append(nums[j])

                backtrack(j + 1, subset)
                subset.pop()

        backtrack(0, [])
        return res