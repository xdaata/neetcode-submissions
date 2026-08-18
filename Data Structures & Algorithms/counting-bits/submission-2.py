class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        for i in range(n + 1):
            for j in range(32):
                output[i] += bool(i & (1 << j))
        return output      