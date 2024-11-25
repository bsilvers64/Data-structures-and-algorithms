class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}
        MOD = 10**9 + 7

        def helper(n, target):
            if (n, target) in memo: return memo[(n, target)]
            if n == 0:
                return 1 if target == 0 else 0
            
            res = 0
            for val in range(1, k+1):
                res = (res + helper(n-1, target - val)) % MOD
            
            memo[(n, target)] = res
            return res
        
        return helper(n, target)