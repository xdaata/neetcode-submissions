class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {char: i for i, char in enumerate(order)}
        return words == sorted(words, key=lambda word: [rank[c] for c in word])
        
      