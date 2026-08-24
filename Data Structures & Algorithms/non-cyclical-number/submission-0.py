class Solution:
    def isHappy(self, n: int) -> bool:
        others = set()
        while True:
            curr = 0
            while n:
                curr += (n % 10) ** 2
                n //= 10

            if curr == 1:
                return True
            if curr in others:
                return False
            
            others.add(curr)
            n = curr