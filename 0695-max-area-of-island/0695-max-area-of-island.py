class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        visited = set()

        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
            visited.add((i, j))
            area = 1
            while q:
                r, c = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for rd, cd in directions:
                    nr, nc = r + rd, c + cd
                    if (nr < 0 or nr >= len(grid) or
                        nc < 0 or nc >= len(grid[0]) or (nr, nc) in visited
                        or grid[nr][nc] == 0):
                        continue
                    visited.add((nr, nc))
                    q.append((nr, nc))
                    area += 1
            return area

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    ans = max(ans, bfs(i, j))
        
        return ans