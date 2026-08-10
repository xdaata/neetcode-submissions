class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(start, path):
            if start == len(s):
                res.append(path.copy())
                return
            for j in range(start, len(s)):
                curr = s[start : j + 1]
                if curr == curr[::-1]:
                    path.append(curr)
                    backtrack(j + 1, path)
                    path.pop()
        
        backtrack(0, [])
        return res

        
        