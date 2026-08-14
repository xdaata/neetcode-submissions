class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for curr, neigh  in edges:
            adj[curr].append(neigh)
            adj[neigh].append(curr)
        
        visited = set()

        def dfs(curr, prev):
            visited.add(curr)
            for neigh in adj[curr]:
                if neigh == prev:
                    continue
                if neigh in visited:
                    return False
                if not dfs(neigh, curr):
                    return False
            return True

        if not dfs(0, None):
            return False
        if len(visited) < n: return False
        return True