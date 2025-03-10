class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        color_to_change = image[sr][sc]
        M, N = len(image), len(image[0])

        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        queue = deque()
        queue.appendleft((sr, sc))
        visited.add((sr, sc))

        while queue:
            for _ in range(len(queue)):
                r, c = queue.pop() 
                image[r][c] = color

                for d1, d2 in directions:
                    nr, nc = r + d1, c + d2

                    if (0 <= nr < M and 0 <= nc < N and 
                        (nr, nc) not in visited and 
                        image[nr][nc] == color_to_change):

                        queue.appendleft((nr, nc))
                        visited.add((nr, nc))


        return image