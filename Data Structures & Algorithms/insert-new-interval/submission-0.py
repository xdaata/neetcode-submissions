class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answ = []
        start, end = newInterval
        i = 0
        
        # всё что точно слева
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            answ.append(intervals[i])
            i += 1

        # всё, что пересечётся
        while i < len(intervals) and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        
        answ.append([start, end])
        while i < len(intervals):
            answ.append(intervals[i])
            i += 1 

        return answ       