class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        M, N = len(grid), len(grid[0])
        
        def dfs(i, j):
            if 0 <= i < M and 0 <= j < N and grid[i][j] == "1":
                grid[i][j] = "0"
                for r, c in directions:
                    dfs(i + r, j + c)
            else:
                return
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        
        return count