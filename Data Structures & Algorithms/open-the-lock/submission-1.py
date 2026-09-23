from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set(deadends)
        if "0000" in dead_set: return -1
        
        q = deque([("0000", 0)])
        visited = {"0000"}
        while q:
            state, steps = q.popleft()

            if state == target:
                return steps

            for i in range(4):
                d = int(state[i])
                for j in (-1, 1):
                    new_d = (d + j) % 10
                    new_s = state[:i] + str(new_d) + state[i + 1 :]
                    if not new_s in visited and not new_s in dead_set:
                        visited.add(new_s)
                        q.append([new_s, steps + 1])
        
        return -1



        