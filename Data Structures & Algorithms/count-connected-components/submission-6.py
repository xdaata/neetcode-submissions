class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [1] * n
        count = n
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        for a, b in edges:
            rootA = find(a)
            rootB = find(b)
            if rootA != rootB:
                if rank[rootA] > rank[rootB]:
                    parent[rootB] = rootA
                elif rank[rootA] < rank[rootB]:
                    parent[rootA] = rootB
                else:
                    parent[rootB] = rootA
                    rank[rootA] += 1
                
                count -= 1

            if count == 1:
                break

        return count        