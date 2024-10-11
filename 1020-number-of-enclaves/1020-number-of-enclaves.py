class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        res, total = 0, 0
        visited = set()

        for i in range(R):
            for j in range(C):
                if grid[i][j]: total += 1
        

        def dfs(r, c):
            if min(r, c) < 0 or r >= R or c >= C or not grid[r][c]: return
            visited.add((r, c))
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for i, j in directions:
                nr, nc = r + i, c + j
                if (nr, nc) not in visited:
                    dfs(nr, nc)


        for i in range(R):
            if grid[i][0]:
                dfs(i, 0)
            if grid[i][C-1]:
                dfs(i, C-1)

        for i in range(C):
            if grid[0][i]:
                dfs(0, i)
            if grid[R-1][i]:
                dfs(R-1, i)
                

        return total - len(visited)