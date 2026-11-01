from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        orig_color = image[sr][sc]
        if orig_color == color:
            return image
        
        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))
        q = deque([(sr, sc)])
        while q:
            r, c = q.popleft()
            image[r][c] = color
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == orig_color:
                    q.append((nr, nc))

        return image
            