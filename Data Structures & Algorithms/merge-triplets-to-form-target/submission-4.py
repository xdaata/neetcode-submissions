class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        f1 = f2 = f3 = False
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue

            if a == target[0]: f1 = True
            if b == target[1]: f2 = True
            if c == target[2]: f3 = True

        return f1 and f2 and f3

        