import math
class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}

        def backtrack(total):
            if total > n: return float('inf')
            if total == n: return 0
            if total in memo: return memo[total]

            count = float('inf')
            for i in range(1, math.ceil(math.sqrt(n))+1):
                i *= i
                count = min(count, 1 + backtrack(total + i))
            
            memo[total] = count
            return memo[total]
        
        return backtrack(0)
        