class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s):
            return s == s[::-1]

        if is_palindrome(s): return True
        
        l, r = 0, len(s) - 1
        while l < r:
            if (
                s[l] != s[r]
                and not is_palindrome(s[l + 1 : r + 1])
                and not is_palindrome(s[l : r])
            ):
                return False
            l += 1
            r -= 1
        return True