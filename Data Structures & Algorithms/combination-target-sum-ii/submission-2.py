class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res: list[list[int]] = []
        path: list[int] = []
        n = len(candidates)

        def backtrack(idx: int, curr_sum: int) -> None:
            if curr_sum == target:
                res.append(path[:])
                return

            for i in range(idx, n):
                if curr_sum + candidates[i] > target:
                    break

                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                backtrack(i + 1, curr_sum + candidates[i])
                path.pop()

        backtrack(0, 0)
        return res