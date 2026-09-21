class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        res = ""
        for _ in range(min(len(word1), len(word2))):
            res += word1[i] + word2[i]
            i += 1

        for j in range(i, len(word2)):
            res += word2[j]

        for j in range(i, len(word1)):
            res += word1[j]
        
        return res