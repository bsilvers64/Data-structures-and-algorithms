class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        R, C = len(grid), len(grid[0])

        def dfs(r, c):
            if min(r, c) < 0 or r >= R or c >= C: return False
            if grid[r][c]: return True
            visited.add((r, c))
            ans = True 
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            
            for i, j in directions:
                nr, nc = r+i, c+j
                if (nr, nc) in visited: continue
                ans &= dfs(nr, nc)
            return ans
        
        res = 0

        for i in range(R):
            for j in range(C):
                if not grid[i][j] and (i, j) not in visited:
                    if dfs(i, j): res += 1
        return res
                    