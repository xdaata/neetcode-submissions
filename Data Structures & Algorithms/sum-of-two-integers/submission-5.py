class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        extr = 0
        for i in range(32):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1

            sum_bit = bit_a ^ bit_b ^ extr
            extr = (bit_a & bit_b) | (bit_a ^ bit_b) & extr

            res |= sum_bit << i

        return res if res <= 0x7FFFFFFF else ~(res ^ 0xFFFFFFFF)
        