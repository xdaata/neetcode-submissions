class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []

        def backtrack(idx: int, path: list[int]) -> None:
            res.append(path[:])

            for i in range(idx, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        res = []
        backtrack(0, [])
        return res