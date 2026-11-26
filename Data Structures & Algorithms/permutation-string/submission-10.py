from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ch = defaultdict(int)
        for c in s1:
            ch[c] += 1
        
        l = 0
        k = len(s1)
        curr_ch = defaultdict(int)
        for r, c in enumerate(s2):
            curr_ch[c] += 1
            if r - l >= k:
                left_c = s2[l]
                curr_ch[left_c] -= 1
                if curr_ch[left_c] == 0:
                    del curr_ch[left_c]
                l += 1
            if curr_ch == ch:
                return True

        return False              
            
                

        