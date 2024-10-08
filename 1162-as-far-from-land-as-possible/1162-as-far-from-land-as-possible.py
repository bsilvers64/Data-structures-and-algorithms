class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        visited = set()
        N = len(grid)

        for i in range(N):
            for j in range(N):
                if grid[i][j]: 
                    q.append([i, j, 0])
                    visited.add((i, j))

        if len(q) == 0 or len(q) == N * N:  
            return -1

        ans = -1
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while q:
            r, c, dis = q.popleft()
            for i, j in directions:
                nr, nc = r + i, c + j
                if nc < 0 or nr < 0 or nr >= N or nc >= N or (nr, nc) in visited or grid[nr][nc]:
                    continue
                q.append([nr, nc, dis+1])
                visited.add((nr, nc))
                ans = dis+1

        return ans
