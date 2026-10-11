class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for c, p in prerequisites:
            adj[p].append(c)
            in_degree[c] += 1
        
        queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
        completed_c = 0

        while queue:
            p = queue.popleft()
            completed_c += 1
            for c in adj[p]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    queue.append(c)
 
        return completed_c == numCourses
