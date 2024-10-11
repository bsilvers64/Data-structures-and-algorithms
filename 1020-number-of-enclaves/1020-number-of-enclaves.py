class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        res = 0
        visited = set()

        def dfs(r, c):
            if min(r, c) < 0 or r >= R or c >= C: return False
            if (r in (0, R-1) or c in (0, C-1)) and grid[r][c]: return False
            if not grid[r][c]: return True
            visited.add((r, c))
           
            ans = True
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            
            for i, j in directions:
                nr, nc = r + i, c + j
                if (nr, nc) not in visited:
                    ans &= dfs(nr, nc)
                    print(nr,nc, ans)
            
            return ans



        for i in range(R):
            for j in range(C):
                if grid[i][j] and (i, j) not in visited:
                    k = len(visited)
                    if dfs(i, j): 
                        res += len(visited) - k

        return res