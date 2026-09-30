class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        f1, f2, f3 = False, False, False
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            if triplet[0] == target[0]: f1 = True
            if triplet[1] == target[1]: f2 = True
            if triplet[2] == target[2]: f3 = True

        
        if f1 and f2 and f3:
            return True
        
        return False

        