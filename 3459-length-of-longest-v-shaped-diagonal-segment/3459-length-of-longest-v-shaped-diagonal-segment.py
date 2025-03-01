class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        
        R, C = len(grid), len(grid[0])
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        memo = {}

        def dfs(r, c, d, turn, order):
            if not (0 <= r < R and 0 <= c < C):
                return 0
            if not ((grid[r][c] == 2 and order) or (grid[r][c] == 0 and not order)):
                return 0
            
            # Use memoization key
            key = (r, c, d, turn, order)
            if key in memo:
                return memo[key]

            # Move straight
            length = 1 + dfs(r + directions[d][0], c + directions[d][1], d, turn, not order)

            # Make a single 90-degree turn if not turned already
            if not turn:
                new_d = (d + 1) % 4  # Turn 90 degrees clockwise
                length = max(length, 1 + dfs(r + directions[new_d][0], c + directions[new_d][1], new_d, 1, not order))

            memo[key] = length
            return length

        ans = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    for index in range(4):
                        nr, nc = i + directions[index][0], j + directions[index][1]
                        ans = max(ans, 1 + dfs(nr, nc, index, 0, 1))

        return ans
