class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        n = min(len(word1), len(word2))
        for i in range(n):
            res.append(word1[i])
            res.append(word2[i])

        res.append(word1[n:])
        res.append(word2[n:])

        return "".join(res)

        