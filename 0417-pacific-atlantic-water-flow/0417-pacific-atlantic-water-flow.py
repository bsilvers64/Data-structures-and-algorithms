class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        ROW, COL = len(heights), len(heights[0])

        def dfs(r, c, visit, prevHeight):
            if r < 0 or c < 0 or r >= ROW or c >= COL \
                or (r, c) in visit or heights[r][c] < prevHeight:
                return 
            visit.add((r, c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
            

        for c in range(COL):
            dfs(0, c, pac, heights[0][c])
            dfs(ROW-1, c, atl, heights[ROW-1][c])
        
        for r in range(ROW):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COL-1, atl, heights[r][COL-1])

        ans = []

        for r in range(ROW):
            for c in range(COL):
                if (r, c) in atl and (r, c) in pac:
                    ans.append([r, c])

        return ans