class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res: list[list[int]] = []
        path: list[int] = []
        n = len(nums)
        used = [False] * n

        def backtrack() -> None:
            if len(path) == n:
                res.append(path[:])
                return

            for i in range(n):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                

                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False
        
        backtrack()
        return res
        