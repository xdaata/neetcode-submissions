class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for i in nums:
            if i in dct: dct[i] += 1
            else: dct[i] = 1
        
        srtd_pairs = sorted(dct.items(), key=lambda x: x[1], reverse=True)
        answ = []
        for i in range(k):
            answ.append(srtd_pairs[i][0])
        return answ