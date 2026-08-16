class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_len = 1

        def expand(left, right):
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                length = right - left + 1
                if length > max_len:
                    start = left
                    max_len = length

                left -= 1
                right += 1
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return s[start:start + max_len]