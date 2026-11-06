from collections import defaultdict, deque
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        num_pos = {}
        for i in range(len(s)):
            if s[i] not in num_pos:
                num_pos[s[i]] = [i, i]
            else:
                num_pos[s[i]][1] = i
        
        intervals = sorted(list(num_pos.values()))
        prev = intervals[0]
        res = [prev]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if res[-1][1] > curr[0]:
                res[-1][1] = max(curr[1], res[-1][1])
            else:
                res.append(curr)
        return [res[i][1] - res[i][0] + 1 for i in range(len(res))]
                
                
            

