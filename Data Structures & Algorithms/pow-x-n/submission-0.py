class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = -1 if n < 0 else 1
        n = abs(n)
        def recPow(x, n):
            if x == 0: return 0
            if n == 0: return 1
            curr = recPow(x, n // 2)
            curr *= curr
            if n % 2 != 0:
                curr *= x
            return curr
                
        answ = recPow(x, n)
        if sign == -1: answ = 1/answ
        return answ
        
