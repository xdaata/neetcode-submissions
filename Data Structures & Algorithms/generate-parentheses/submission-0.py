class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(open_, close, path):
            if len(path) == 2*n:
                res.append("".join(path))
            if open_ < n:
                path.append("(")
                backtrack(open_ + 1, close, path)
                path.pop()
            if close < open_:
                path.append(")")
                backtrack(open_, close + 1, path)
                path.pop()

        backtrack(0, 0, [])
        return res
            
            


            


