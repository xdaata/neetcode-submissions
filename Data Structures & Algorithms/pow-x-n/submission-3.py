class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x, n = 1/x, -n

        def recPow(x, n):
            if x == 0: return 0
            if n == 0: return 1
            curr = recPow(x, n // 2)
            curr *= curr
            if n % 2 != 0:
                curr *= x
            return curr

        return recPow(x, n)