class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res: list[list[int]] = []
        path: list[int] = []

        def backtrack(idx: int) -> None:
            if len(path) == k:
                res.append(path[:])
                return

            max_start = n - (k - len(path)) + 2
            for i in range(idx, max_start):
                path.append(i)
                backtrack(i + 1)
                path.pop()
        
        backtrack(1)
        return res