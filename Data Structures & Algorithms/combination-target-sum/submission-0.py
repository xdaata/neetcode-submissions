class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, s, els):
            if s > target:
                return

            if s == target:
                res.append(els.copy())
                return

            if i >= len(nums):
                return
            
            els.append(nums[i])
            s += nums[i]
            dfs(i, s, els)

            els.pop()
            s -= nums[i]
            dfs(i + 1, s, els)
        
        dfs(0, 0, [])
        return res

        