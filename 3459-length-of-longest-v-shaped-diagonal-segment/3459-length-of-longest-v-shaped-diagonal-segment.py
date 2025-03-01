class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        
        memo = {}

        @cache
        def dfs(r, c, d, turn, order):
            length = 0
            # checks for - we are within the grid and following the sequence
            if ((0 <= r < R) and (0 <= c < C) and
                ((grid[r][c] == 2 and order) or 
                (grid[r][c] == 0 and not order))):

                # 2 choices - to go straight or to make a 90-degree turn

                length = max(length, 1 + dfs(r + directions[d][0], c + directions[d][1], d, turn, not order))

                if not turn:
                    d = (d + 1) % 4
                    length = max(length, 1 + dfs(r + directions[d][0], c + directions[d][1], d, 1, not order))


            return length
             

        R, C = len(grid), len(grid[0])
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for index, d in enumerate(directions):
                        nr, nc = i + d[0], j + d[1]
                        ans = max(ans, 1 + dfs(nr, nc, index, 0, 1))

        return ans