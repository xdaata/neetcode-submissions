class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {char: i for i, char in enumerate(order)}
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if rank[c1] > rank[c2]:
                        return False
                    break
            else:
                if len(w1) > len(w2):
                    return False   
        return True     