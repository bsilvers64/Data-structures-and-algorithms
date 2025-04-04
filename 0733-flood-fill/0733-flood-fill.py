class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        M, N = len(image), len(image[0])
        og_color = image[sr][sc]
        if color == og_color: return image

        def dfs(r, c):
            if 0 <= r < M and 0 <= c < N and image[r][c] == og_color:
                image[r][c] = color
                dfs(r + 1, c)
                dfs(r, c + 1)
                dfs(r - 1, c)
                dfs(r, c - 1)
        
        dfs(sr, sc)
        return image