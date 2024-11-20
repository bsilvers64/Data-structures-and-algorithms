class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}

        s1 = s[::-1]

        def dfs(i, j):
            if (i, j) in memo: return memo[(i, j)]
            if i >= len(s) or j >= len(s1): return 0

            if s[i] == s1[j]:
                memo[(i, j)] = 1 + dfs(i+1, j+1)
            else:
                memo[(i, j)] = max(dfs(i+1, j), dfs(i, j+1))
            
            return memo[(i, j)]
        
        return dfs(0, 0)
