class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        n = len(digits)
        res: list[str] = []
        def backtrack(idx: int, path: str) -> None:
            if idx == n:
                if len(path) == n:
                    res.append(path)
                return
            
            for i in range(idx, n):
                for letter in map[digits[i]]:
                    temp = path
                    path += letter
                    backtrack(i + 1, path)
                    path = temp
            
        backtrack(0, "")
        return res