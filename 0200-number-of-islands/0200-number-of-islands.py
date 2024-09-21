class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        visited = set()

        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))

            while q:
                r, c = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for rd, cd in directions:
                    nr, nc = r + rd, c + cd

                    if (
                        nr < 0 or nc < 0 or nr >= len(grid) or 
                        nc >= len(grid[0]) or grid[nr][nc] == "0" or
                        (nr, nc) in visited
                    ): 
                        continue

                    
                    visited.add((nr, nc))
                    q.append((nr, nc))


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited: 
                    bfs(i, j)
                    ans += 1

        return ans            