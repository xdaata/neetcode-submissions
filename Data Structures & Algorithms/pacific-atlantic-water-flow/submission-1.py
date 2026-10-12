class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))


        def dfs(r, c, visited_set):
            visited_set.add((r, c))
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited_set and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited_set)
                    
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)

        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)

        return [list(i) for i in pacific & atlantic]
        


       