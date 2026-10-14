class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)
        def backtrack(path: list[int], visited: list[bool]) -> None:
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if not visited[i]:
                    path.append(nums[i])
                    visited[i] = True
                    backtrack(path, visited)
                    path.pop()
                    visited[i] = False


        backtrack([], visited)
        return res


        