class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answ = []
        intervals.sort(key=lambda x:x[0])
        for start, end in intervals:
            if not answ or answ[-1][1] < start:
                answ.append([start, end])
            else:
                answ[-1][1] = max(end, answ[-1][1])
        return answ