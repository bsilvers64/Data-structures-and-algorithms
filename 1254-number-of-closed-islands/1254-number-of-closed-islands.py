class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        R, C = len(grid), len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            is_closed = True

            while q:
                row, col = q.popleft()

                for i, j in directions:
                    nr, nc = row + i, col + j
                    # If the island touches the boundary, it is not closed
                    if nr < 0 or nc < 0 or nr >= R or nc >= C:
                        is_closed = False
                    elif not grid[nr][nc] and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))

            return is_closed

        res = 0
        for i in range(R):
            for j in range(C):
                if not grid[i][j] and (i, j) not in visited:
                    if bfs(i, j):
                        res += 1

        return res
