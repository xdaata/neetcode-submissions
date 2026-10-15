class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res: list[list[int]] = []
        path: list[int] = []
        n = len(nums)

        def backtrack(idx: int) -> None:
            res.append(path[:])
    
            for i in range(idx, n):
                if i > idx and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
            
            return
        
        backtrack(0)
        return res