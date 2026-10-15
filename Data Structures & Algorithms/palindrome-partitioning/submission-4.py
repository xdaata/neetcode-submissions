class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
        
        def backtrack(idx: int, path: list[str]) -> None:
            if idx == n:
                res.append(path[:])
                return

            for i in range(idx, n):
                if dp[idx][i]:
                    path.append(s[idx:i + 1])
                    backtrack(i + 1, path)
                    path.pop()


        backtrack(0, [])

        return res
