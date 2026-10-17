class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res: list[list[int]] = []
        path: list[int] = []

        def backtrack(idx: int) -> None:
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(idx, n + 1):
                path.append(i)
                backtrack(i + 1)
                path.pop()
        
        backtrack(1)
        return res