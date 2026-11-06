class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {c: i for i, c in enumerate(s)}
        start = end = 0
        res = []

        for i in range(len(s)):
            end = max(end, last_idx[s[i]])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res
        
                
            

