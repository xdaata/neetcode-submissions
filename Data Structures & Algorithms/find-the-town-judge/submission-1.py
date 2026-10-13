from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        t_map = defaultdict(set)
        visited = set()

        for p1, p2 in trust:
            t_map[p2].add(p1)
            visited.add(p1)

        judge = -1
        for j in t_map:
            if j not in visited and len(t_map[j]) == len(visited):
                judge = j
        
        return judge
                