class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        answ = []
        for i in range(len(nums)):
            if q and q[0] + k <= i:
                q.popleft()
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                answ.append(nums[q[0]])
        return answ
