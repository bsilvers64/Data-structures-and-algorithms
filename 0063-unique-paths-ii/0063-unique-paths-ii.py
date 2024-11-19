class Solution:
    def uniquePathsWithObstacles(self, obs: List[List[int]]) -> int:
        if obs[0][0] == 1 or obs[-1][-1] == 1:
            return 0
        
        m, n = len(obs), len(obs[0])

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        dp[0][1] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if not obs[i-1][j-1]: 
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]
        