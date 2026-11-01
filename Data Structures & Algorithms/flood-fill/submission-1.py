class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        orig_color = image[sr][sc]
        if orig_color == color:
            return image
        
        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))
        def dfs(r, c):
            image[r][c] = color
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and image[nr][nc] == orig_color
                ):
                    dfs(nr, nc)
        dfs(sr, sc)
        return image
            