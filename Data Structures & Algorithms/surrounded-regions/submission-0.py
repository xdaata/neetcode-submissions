class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c):
            if (
                r < 0 or r >= ROWS
                or c < 0 or c >= COLS
                or board[r][c] != "O"
            ):
                return 
            
            board[r][c] = "T"
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(r + dr, c + dc)
            
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        