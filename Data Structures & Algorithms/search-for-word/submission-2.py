class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtrack(r: int, c: int, idx: int) -> bool:
            if idx == len(word):
                return True

            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[idx]:
                    return False

            board[r][c] = "#"

            found = (
                backtrack(r + 1, c, idx + 1)
                or backtrack(r, c + 1, idx + 1)
                or backtrack(r - 1, c, idx + 1)
                or backtrack(r, c - 1, idx + 1)
            )

            board[r][c] = word[idx]
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and backtrack(r, c, 0):
                    return True
        
        return False  
