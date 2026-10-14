class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))
        def backtrack(r: int, c: int, word_idx: int) -> bool:
            if word_idx == len(word):
                return True

            temp = board[r][c]
            board[r][c] = "#"

            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if (
                    0 <= nr < rows 
                    and 0 <= nc < cols
                    and board[nr][nc] == word[word_idx]
                    and backtrack(nr, nc, word_idx + 1)
                    ):
                    board[r][c] = temp
                    return True
            
            board[r][c] = temp
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and backtrack(r, c, 1):
                    return True
        
        return False  
