class Solution:
    def climbStairs(self, n: int) -> int:
        dp0, dp1 = 1, 2
        if n == 1: return dp0
        while n-2 > 0:
            temp = dp1 + dp0
            dp0 = dp1
            dp1 = temp
            n -= 1
        return dp1

