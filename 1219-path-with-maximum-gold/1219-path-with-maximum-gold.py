class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def dfs(r, c):
            if min(r, c) < 0 or r >= R or c >= C or not grid[r][c]: return 0
            
            res = 0
            directions = [[r, c+1], [r+1, c], [r, c-1], [r-1, c]]
        
            currVal = grid[r][c]
            
            for nr, nc in directions:
                grid[r][c] = 0
                res = max(res, currVal + dfs(nr, nc))
                grid[r][c] = currVal
            
            return res
         
        ans = 0
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] != 0:
                    ans = max(ans, dfs(i, j))
        
        return ans