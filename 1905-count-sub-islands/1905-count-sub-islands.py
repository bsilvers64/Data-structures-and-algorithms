class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid2), len(grid2[0])
        visited = set()

        
        def dfs(r, c):
            if (r not in range(rows) or c not in range(cols) 
                or (r, c) in visited or grid2[r][c] == 0): return True

            visited.add((r, c))
            res = True
            if grid1[r][c] == 0: 
                res = False  

            res = dfs(r+1, c) and res
            res = dfs(r-1, c) and res
            res = dfs(r, c+1) and res
            res = dfs(r, c-1) and res

            return res



        ans = 0

        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] and (i,j) not in visited:
                    x = dfs(i, j) 
                    print(x)
                    if x: ans += 1
        

        return ans