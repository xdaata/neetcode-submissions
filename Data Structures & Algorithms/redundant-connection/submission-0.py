class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        rank = [1] * (len(edges) + 1)

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        answ = edges[-1]
        for edge in edges:
            u, v = edge
            rootU, rootV = find(u), find(v)
            if rootU == rootV:
                answ = edge
            else:
                if rank[rootU] > rank[rootV]:
                    parent[rootV] = rootU
                elif rank[rootU] < rank[rootV]:
                    parent[rootU] = rootV
                else:
                    parent[rootU] = rootV
                    rank[rootV] += 1

        return answ     
        