class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            new = 0
            while n:
                new += (n % 10) ** 2
                n //= 10
            return new
        slow = n
        fast = get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        
        return fast == 1