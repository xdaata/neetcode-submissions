class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res: list[list[int]] = []
        path: list[int] = []

        def backtrack(idx: int, amount: int) -> None:
            if amount == k:
                res.append(path[:])
                return

            for i in range(idx, n + 1):
                path.append(i)
                backtrack(i + 1, amount + 1)
                path.pop()
            
        
        backtrack(1, 0)
        return res