class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        M, N = len(image), len(image[0])
        directions = [[0, 1], [-1, 0], [1, 0], [0, -1]]
        og_color = image[sr][sc]
        queue = collections.deque()
        def bfs(i, j):
            queue.append((sr, sc))
            image[sr][sc] = color
            while queue:
                i, j = queue.popleft()
                for r, c in directions:
                    nr, nc = i + r, j + c
                    if min(nr, nc) < 0 or nr >= M or nc >= N or image[nr][nc] != og_color or image[nr][nc] == color: continue
                    image[nr][nc] = color
                    queue.append((nr, nc))
        bfs(sr, sc)
        return image
