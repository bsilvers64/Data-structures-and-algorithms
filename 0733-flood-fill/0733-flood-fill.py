class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        M, N = len(image), len(image[0])
        directions = [[0, 1], [-1, 0], [1, 0], [0, -1]]
        og_color = image[sr][sc]

        def dfs(i, j):
            if min(i, j) < 0 or i >= M or j >= N or image[i][j] != og_color or image[i][j] == color: return
            image[i][j] = color
            for r, c in directions:
                dfs(i + r, j + c)
        
        dfs(sr, sc)
        return image
