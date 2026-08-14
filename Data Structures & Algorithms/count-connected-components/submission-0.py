class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        comps = [{i} for i in range(n)] 
        count = n
        def find(x):
            for i in range(len(comps)):
                if x in comps[i]:
                    return comps[i]
        def union(a, b):
            comps.remove(a)
            comps.remove(b)
            a |= b
            comps.append(a)

        for x, y in edges:
            a, b = find(x), find(y)
            if a != b:
                union(a, b)
                count -= 1

        return count        