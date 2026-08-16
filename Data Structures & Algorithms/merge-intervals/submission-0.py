class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answ = []
        intervals.sort(key=lambda x:x[0])
        start = intervals[0]
        i = 0
        while i < len(intervals):
            start, end = intervals[i]

            # всё, что начинается также
            while i < len(intervals) and intervals[i][0] == start:
                end = max(end, intervals[i][1])
                i += 1
            # всё что пересекается на текущей итерации
            while i < len(intervals) and end >= intervals[i][0]:
                end = max(end, intervals[i][1])
                i += 1

            answ.append([start, end])
        return answ
        