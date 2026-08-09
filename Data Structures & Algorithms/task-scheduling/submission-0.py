class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for t in tasks:
            if t in freq: freq[t] += 1
            else: freq[t] = 1

        
        max_heap = [-val for key, val in freq.items()]
        heapq.heapify(max_heap)
        q = deque()
        time = 0
        # элемент очереди = [остаток частоты, когда достанем]
        while max_heap or q:
            time += 1

            if max_heap:
                task = heapq.heappop(max_heap)
                task += 1
                if task:
                    q.append([task, n + time])

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time      