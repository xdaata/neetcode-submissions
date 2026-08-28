class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber:
            columnNumber -= 1
            rem = columnNumber % 26
            res.append(chr(ord('A') + rem))
            columnNumber //= 26
        return "".join(res[::-1])
