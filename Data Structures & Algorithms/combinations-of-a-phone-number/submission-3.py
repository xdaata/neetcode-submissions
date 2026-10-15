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
        def backtrack(idx: int, path: str) -> None:
            if idx == n:
                res.append(path)
                return
            
            for letter in digit_to_char[digits[idx]]:
                temp = path
                path += letter
                backtrack(idx + 1, path)
                path = temp
        
        backtrack(0, "")
        return res