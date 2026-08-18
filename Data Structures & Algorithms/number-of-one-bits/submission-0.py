class Solution:
    def hammingWeight(self, n: int) -> int:
        k = 0
        for i in range(32):
            if (1 << i) & n:
                k += 1
        return k
