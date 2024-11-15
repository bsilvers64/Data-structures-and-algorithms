class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        M, N = len(nums1), len(nums2)
        dp = [[0]*(N+1) for i in range(M+1)]

        for i in range(1, M+1):
            for j in range(1, N+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[M][N]

"""         def dfs(i, j):
            if i >= M or j >= N: return 0
            if memo[i][j] != -1: return memo[i][j]

            if nums1[i] == nums2[j]:
                memo[i][j] = 1 + dfs(i+1, j+1)
            else:
                memo[i][j] = max(dfs(i+1, j), dfs(i, j+1))

            return memo[i][j]

        return dfs(0, 0) """