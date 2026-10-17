class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res: list[list[int]] = []
        n = len(nums)

        def backtrack(idx: int) -> None:
            if idx == n:
                res.append(nums[:])
                return

            seen: set[int] = set()
            for i in range(idx, n):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])

                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]
        
        backtrack(0)
        return res
        