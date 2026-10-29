from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_q = deque()
        d_q = deque()
        n = len(senate)

        for i, s in enumerate(senate):
            if s == 'R':
                r_q.append(i)
            else:
                d_q.append(i)

        while r_q and d_q:
            r_idx = r_q.popleft()
            d_idx = d_q.popleft()

            if r_idx < d_idx:
                r_q.append(r_idx + n)
            else:
                d_q.append(d_idx + n)
        
        return "Radiant" if r_q else "Dire"
        
        
            


                