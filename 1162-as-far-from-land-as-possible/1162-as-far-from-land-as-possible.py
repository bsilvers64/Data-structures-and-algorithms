class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        N = len(grid)

        for i in range(N):
            for j in range(N):
                if grid[i][j]: 
                    q.append([i, j, 0])

        if len(q) == 0 or len(q) == N * N:  
            return -1

        ans = -1
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while q:
            r, c, dis = q.popleft()
            ans = grid[r][c]
            for i, j in directions:
                nr, nc = r + i, c + j
                if nc < 0 or nr < 0 or nr >= N or nc >= N or grid[nr][nc] != 0:
                    continue
                q.append([nr, nc, dis+1])
                grid[nr][nc] = grid[r][c] + 1

        return ans-1 
