class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}

        def dfs(i):
            if i in memo: return memo[i]
            if i == 1: return 1

            res = 0 if i==n else i
            for k in range(1, i):
                val = dfs(k) * dfs(i-k)
                res = max(val, res)
            
            memo[i] = res
            return memo[i]
        return dfs(n)