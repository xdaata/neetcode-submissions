from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        in_degree = {c: 0 for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(words[i]), len(words[i + 1]))
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    u, v = w1[j], w2[j]
                    if v not in adj[u]:
                        adj[u].add(v)
                        in_degree[v] += 1
                    break

        solution = ""
        q = deque()
        for u in in_degree:
            if in_degree[u] == 0:
                q.append(u)

        while q:
            curr = q.popleft()
            solution += curr
            for neigh in adj[curr]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    q.append(neigh)

        return solution if len(solution) == len(in_degree) else ""
            

            
            
