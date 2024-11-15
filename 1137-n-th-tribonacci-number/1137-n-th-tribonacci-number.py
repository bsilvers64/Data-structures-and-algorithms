class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def dfs(i):
            if i in memo: return memo[i]
            if i == 0: return 0
            if i < 3: return 1
            memo[i] = dfs(i-1) + dfs(i-2) + dfs(i-3)
            return memo[i]
        
        return dfs(n)