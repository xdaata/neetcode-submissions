class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        els = set()
        max_len = 0
        l = 0

        for r in range(len(s)):
            while s[r] in els:
                els.remove(s[l])
                l += 1
            
            els.add(s[r])
            max_len = max(max_len, len(els))

        return max_len