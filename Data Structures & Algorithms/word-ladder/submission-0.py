class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        patterns = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                patterns[w[:i] + "*" + w[i + 1:]].append(w)
        q = deque([(beginWord, 1)])
        visited = {beginWord}
        while q:
            w, l = q.popleft()
            
            if w == endWord: return l

            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i + 1:]
                if pattern in patterns:
                    for neigh in patterns[pattern]:
                        if neigh not in visited:
                            visited.add(neigh)
                            q.append((neigh, l + 1))
        return 0