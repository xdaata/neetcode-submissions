from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        res = []
        for i in range(len(nums), 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res

        