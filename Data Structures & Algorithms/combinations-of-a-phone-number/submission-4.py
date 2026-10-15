class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_char = {
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
        path: list[str] = []

        def backtrack(idx: int) -> None:
            if idx == n:
                res.append("".join(path))
                return
            
            for letter in digit_to_char[digits[idx]]:
                path.append(letter)
                backtrack(idx + 1)
                path.pop()
        
        backtrack(0)
        return res