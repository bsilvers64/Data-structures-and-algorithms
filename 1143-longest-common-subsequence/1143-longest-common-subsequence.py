class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        M, N = len(text1), len(text2)
        memo =  [[-1] * N for _ in range(M)]

        def dfs(i, j):
            if i >= M or j >= N:
                return 0
            if memo[i][j] != -1: return memo[i][j]

            if text1[i] == text2[j]: 
                memo[i][j] =  1 + dfs(i+1, j+1)
            else:
                memo[i][j] = max(dfs(i+1, j), dfs(i, j+1))

            return memo[i][j]

        return dfs(0, 0)
        