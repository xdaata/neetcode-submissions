class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        count = n
        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x

        def union(a, b):
            rootA = find(a)
            rootB = find(b)
            if rootA != rootB:
                parent[rootB] = rootA
                return True
            return False

        for x, y in edges:
            if union(x, y):
                count -= 1

        return count        