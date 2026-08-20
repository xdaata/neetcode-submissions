"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]
        starts.sort()
        ends.sort()
        n = len(intervals)
        s = 0
        e = 0
        max_count = 0
        count = 0
        while s < n and e < n:
            if starts[s] < ends[e]:
                count += 1
                max_count = max(max_count, count)
                s += 1
            else:
                count -= 1
                e += 1     

        return max_count
