class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(i, rem, els):
            if rem == 0:
                res.append(els.copy())
                return
            
            for j in range(i, len(candidates)):
                if candidates[j] > rem:
                    return

                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                els.append(candidates[j])
                backtrack(j + 1, rem - candidates[j], els)

                els.pop()
        
        backtrack(0, target, [])
        return res