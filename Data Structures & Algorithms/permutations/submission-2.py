class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)
        def backtrack(idx: int, path: list[int], visited: list[bool]) -> None:
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if visited[i] == False:
                    path.append(nums[i])
                    visited[i] = True
                    backtrack(i + 1, path, visited)
                    path.pop()
                    visited[i] = False


        backtrack(0, [], visited)
        return res


        