from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        return sorted(count, key=lambda x: count[x], reverse=True)[:k]
        