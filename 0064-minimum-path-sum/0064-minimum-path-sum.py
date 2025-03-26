class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [[float(inf) for _ in range(N+1)] for _ in range(M+1)]

        dp[0][1] = dp[1][0] = 0

        for i in range(M):
            for j in range(N):
                dp[i+1][j+1] = grid[i][j] + min(dp[i][j+1], dp[i+1][j])


        return dp[-1][-1]