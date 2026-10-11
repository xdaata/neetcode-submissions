class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            adj[c].append(p)
        
        state = [0] * numCourses
        # 0 - не посещали; 1 - в текущей ветке; 2 - трогали раньше
        def has_cycle(node: int) -> bool:
            if state[node] == 1:
                return True
            elif state[node] == 2:
                return False
            
            state[node] = 1
            for neigh in adj[node]:
                if has_cycle(neigh):
                    return True
            
            state[node] = 2
            return False

        for c in range(numCourses):
            if state[c] == 0:
                if has_cycle(c):
                    return False

        return True
