class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        res = []
        def backtrack(idx: int, path: list[str]) -> None:
            if idx == len(s):
                res.append(path[:])
                return

            for i in range(idx, len(s)):
                if is_palindrome(s[idx:i + 1]):
                    path.append(s[idx:i + 1])
                    backtrack(i + 1, path)
                    path.pop()


        backtrack(0, [])

        return res
